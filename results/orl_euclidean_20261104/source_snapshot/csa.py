"""CSA Procedure 1 与简单基线；样本轴为 0，对象模式从 0 编号。

CSA 的 mode=0 对应数组 axis=1，不压缩样本批次。使用实数 float64。
数学依据：Xu et al., TCSVT 2008, Eq. 5–6 / Procedure 1。
NumPy/SciPy 仅提供基础矩阵运算，不调用现成 CSA/Tucker/PCA/LDA。
"""

import numpy as np
from scipy.linalg import eigh, svd
from scipy.spatial.distance import cdist


def mode_product(x, matrix, mode):
    """[N,...,mk,...] × [rk,mk] → [N,...,rk,...]。"""
    axis = mode + 1
    if not 1 <= axis < x.ndim or matrix.shape[1] != x.shape[axis]:
        raise ValueError("Mode or matrix shape does not match the object")
    # contraction 将新轴放到末尾，再将它移回原对象模式位置。
    return np.moveaxis(np.tensordot(x, matrix, axes=(axis, 1)), -1, axis)


def unfold(x, mode):
    """批量展开为 [N,mk,其它模式乘积]，保持样本不混合。"""
    moved = np.moveaxis(x, mode + 1, 1)
    return moved.reshape(x.shape[0], x.shape[mode + 1], -1)


def fold(matrix, shape, mode):
    other = [shape[k] for k in range(1, len(shape)) if k != mode + 1]
    moved = matrix.reshape(shape[0], shape[mode + 1], *other)
    return np.moveaxis(moved, 1, mode + 1)


def leading_vectors(covariance, rank):
    """实对称特征分解，返回特征值最大的 rank 个列向量。"""
    covariance = (covariance + covariance.T) / 2
    _, vectors = eigh(covariance)
    vectors = vectors[:, -rank:][:, ::-1].copy()
    # 固定符号只改善记录可读性；不改变子空间或重建。
    peaks = np.argmax(np.abs(vectors), axis=0)
    signs = np.sign(vectors[peaks, np.arange(rank)])
    vectors *= np.where(signs == 0, 1, signs)
    return vectors


class CSA:
    def __init__(self, ranks, *, center=False, init="identity", seed=0,
                 max_iter=3, epsilon=0.001, stop_on_convergence=True,
                 initial_bases=None):
        self.ranks = tuple(ranks)
        self.center, self.init, self.seed = center, init, seed
        self.max_iter, self.epsilon = max_iter, epsilon
        self.stop_on_convergence = stop_on_convergence
        self.initial_bases = initial_bases

    def fit(self, x):
        x = np.asarray(x, dtype=np.float64)
        if x.ndim < 2 or x.shape[0] == 0 or not np.isfinite(x).all():
            raise ValueError("Expected a nonempty finite batch of tensors")
        self.shape = x.shape[1:]
        if (len(self.ranks) != len(self.shape)
                or any(not 1 <= r <= m for r, m in zip(self.ranks, self.shape))
                or self.max_iter < 1):
            raise ValueError("Invalid ranks or iteration limit")
        self.mean = x.mean(axis=0) if self.center else np.zeros(self.shape)
        data = x - self.mean  # 均值只能从学习样本估计。
        rng = np.random.default_rng(self.seed)
        if self.initial_bases is not None:
            # Procedure 1 allows arbitrary column-orthogonal initialization.
            # Copy explicit training-derived bases; old calls retain their path.
            if len(self.initial_bases) != len(self.shape):
                raise ValueError("Expected one initial basis per object mode")
            self.bases = [np.asarray(u, dtype=float).copy() for u in self.initial_bases]
            for u, m, r in zip(self.bases, self.shape, self.ranks):
                if (u.shape != (m, r) or not np.isfinite(u).all()
                        or not np.allclose(u.T @ u, np.eye(r), atol=1e-10, rtol=1e-10)):
                    raise ValueError("Initial bases must have the configured shape and orthonormal columns")
        elif self.init == "identity":
            self.bases = [np.eye(m, r) for m, r in zip(self.shape, self.ranks)]
        elif self.init == "random":
            self.bases = [np.linalg.qr(rng.normal(size=(m, r)))[0]
                          for m, r in zip(self.shape, self.ranks)]
        else:
            raise ValueError("init must be identity or random")
        self.history = []
        self.stop_reason = "max_iter"
        self.initial_sse = self._sse(data)
        for iteration in range(1, self.max_iter + 1):
            old = [u.copy() for u in self.bases]
            mode_sse = []
            for k, rank in enumerate(self.ranks):
                projected = data
                for j, basis in enumerate(self.bases):
                    if j != k:
                        # 已更新的小模式直接用新基；大模式仍为上次基。
                        projected = mode_product(projected, basis.T, j)
                b = unfold(projected, k)  # [N,mk,其它模式降维后的乘积]
                covariance = np.einsum("nac,nbc->ab", b, b, optimize=True)
                self.bases[k] = leading_vectors(covariance, rank)
                mode_sse.append(self._sse(data))
            similarities = [float(np.trace(np.abs(u.T @ v)) / r)
                            for u, v, r in zip(self.bases, old, self.ranks)]
            distances = [float(np.linalg.norm(u @ u.T - v @ v.T))
                         for u, v in zip(self.bases, old)]
            self.history.append({"iteration": iteration, "sse": mode_sse[-1],
                                 "mode_sse": mode_sse,
                                 "basis_similarity": similarities,
                                 "projector_distance": distances})
            if self.stop_on_convergence and iteration > 2 and all(a > 1 - self.epsilon for a in similarities):
                self.stop_reason = "paper_basis_similarity"
                break
        return self

    def _encode(self, data):
        for k, basis in enumerate(self.bases):
            data = mode_product(data, basis.T, k)
        return data

    def _sse(self, data):
        # 正交投影的勾股关系：残差能量 = 原能量 − 核能量。
        core = self._encode(data)
        return float(max(0, np.sum(data * data) - np.sum(core * core)))

    def transform(self, x):
        x = np.asarray(x, dtype=np.float64)
        if x.shape[1:] != self.shape:
            raise ValueError("Object shape differs from training")
        return self._encode(x - self.mean)

    def inverse_transform(self, core):
        data = np.asarray(core, dtype=np.float64)
        if data.shape[1:] != self.ranks:
            raise ValueError("Core shape differs from configured ranks")
        for k, basis in enumerate(self.bases):
            data = mode_product(data, basis, k)
        return data + self.mean


class PCA:
    def __init__(self, components, *, center=True, solver="svd"):
        self.components, self.center, self.solver = components, center, solver

    def fit(self, x):
        x = np.asarray(x, dtype=np.float64)
        self.shape = x.shape[1:]
        matrix = x.reshape(len(x), -1)
        self.mean = matrix.mean(axis=0) if self.center else np.zeros(matrix.shape[1])
        data = matrix - self.mean
        if self.solver == "svd":
            _, singular, vt = svd(data, full_matrices=False)
            tolerance = max(matrix.shape) * np.finfo(float).eps * singular[0]
            self.available_rank = int(np.sum(singular > tolerance))
            if not 1 <= self.components <= self.available_rank:
                raise ValueError(f"PCA components exceed numerical rank {self.available_rank}")
            self.basis = vt[:self.components].T
        elif self.solver == "gram":
            # D 远大于 N 时求 N×N 的样本 Gram 矩阵，避免完整 N×D SVD。
            values, vectors = eigh(data @ data.T)
            values, vectors = values[::-1], vectors[:, ::-1]
            tolerance = max(data.shape) * np.finfo(float).eps * max(0, values[0])
            self.available_rank = int(np.sum(values > tolerance))
            if not 1 <= self.components <= self.available_rank:
                raise ValueError(f"Gram PCA components exceed numerical rank {self.available_rank}")
            self.basis = data.T @ (vectors[:, :self.components] / np.sqrt(values[:self.components]))
        else:
            raise ValueError("PCA solver must be svd or gram")
        return self

    def transform(self, x):
        x = np.asarray(x, dtype=np.float64)
        if x.shape[1:] != self.shape:
            raise ValueError("Object shape differs from training")
        return (x.reshape(len(x), -1) - self.mean) @ self.basis

    def inverse_transform(self, coefficients):
        matrix = np.asarray(coefficients) @ self.basis.T + self.mean
        return matrix.reshape(len(matrix), *self.shape)


class LDA:
    """Fisher 广义特征分解；只保留 Sw 的非零空间，不加入 ridge。

    投影方向按 W.T @ Sw @ W = I 归一化；这是显式本组约定，
    原论文没有说明特征向量缩放。它会影响欧氏最近邻的特征权重。
    """
    def fit(self, x, labels):
        x, labels = np.asarray(x, dtype=np.float64), np.asarray(labels)
        if x.ndim != 2 or len(x) != len(labels) or not np.isfinite(x).all():
            raise ValueError("Expected finite 2-D features and matching labels")
        classes = np.unique(labels)
        if len(classes) < 2 or x.shape[1] > len(x) - len(classes):
            raise ValueError("LDA requires at least 2 classes and p <= N - Nc")
        self.mean = x.mean(axis=0)
        sw = np.zeros((x.shape[1], x.shape[1]))
        sb = np.zeros_like(sw)
        for label in classes:
            samples = x[labels == label]
            delta = samples - samples.mean(axis=0)
            sw += delta.T @ delta
            displacement = samples.mean(axis=0) - self.mean
            sb += len(samples) * np.outer(displacement, displacement)
        values, vectors = eigh((sw + sw.T) / 2)
        tolerance = max(sw.shape) * np.finfo(float).eps * max(0, values[-1])
        positive = values > tolerance
        self.sw_rank = int(positive.sum())
        if self.sw_rank == 0:
            raise ValueError("Within-class scatter has zero rank")
        whitening = vectors[:, positive] / np.sqrt(values[positive])
        values_b, directions = eigh(whitening.T @ sb @ whitening)
        self.max_components = min(self.sw_rank, len(classes) - 1)
        self.basis = whitening @ directions[:, ::-1][:, :self.max_components]
        self.eigenvalues = values_b[::-1][:self.max_components]
        self.sw, self.sb = sw, sb
        return self

    def transform(self, x, components):
        if not 1 <= components <= self.max_components:
            raise ValueError("LDA components exceed available directions")
        return (np.asarray(x) - self.mean) @ self.basis[:, :components]


def nearest_neighbor(gallery, gallery_labels, probes, *, block_size=256):
    """平方欧氏距离与欧氏距离具有相同最近邻；不做额外归一化。"""
    predictions, indices, distances = [], [], []
    for start in range(0, len(probes), block_size):
        squared = cdist(probes[start:start + block_size], gallery, "sqeuclidean")
        index = np.argmin(squared, axis=1)
        predictions.extend(np.asarray(gallery_labels)[index].tolist())
        indices.extend(index.tolist())
        distances.extend(np.sqrt(squared[np.arange(len(index)), index]).tolist())
    return np.asarray(predictions), np.asarray(indices), np.asarray(distances)


def reconstruction_metrics(x, reconstructed, *, method, dimensions, include_mean=False):
    """论文 RMSE 分母 N；存储量同时包括共享基和每个样本的核。"""
    n, shape = len(x), x.shape[1:]
    d = int(np.prod(shape))
    sse = float(np.sum((np.asarray(x) - reconstructed) ** 2))
    if method == "pca":
        storage = int(dimensions) * (n + d)
    elif method == "csa":
        if len(dimensions) != len(shape):
            raise ValueError("CSA dimensions must match object modes")
        storage = n * int(np.prod(dimensions)) + sum(m * r for m, r in zip(shape, dimensions))
    else:
        raise ValueError("Unknown reconstruction method")
    if include_mean:
        storage += d
    return {"sse": sse, "paper_rmse": float(np.sqrt(sse / n)),
            "stored_scalars": storage, "compression_ratio": n * d / storage}
