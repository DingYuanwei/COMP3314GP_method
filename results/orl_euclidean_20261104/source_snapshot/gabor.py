"""自写 Wiskott 风格 DC-free 复 Gabor；FFT 只用于计算卷积。

本组约定：波长 4*sqrt(2)**s，sigma=2*pi，theta=o*pi/8，
3 个包络标准差截断，有限核再减均值，reflect 边界，复响应幅值。
不做通道/逐图特征归一化；强度保持 [0,255]。
"""

import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.fft import fftn, ifftn, next_fast_len


CONFIG = {"wavelengths": [float(4 * np.sqrt(2)**s) for s in range(5)],
          "orientations": [float(o * np.pi / 8) for o in range(8)],
          "sigma": float(2*np.pi), "truncate_sigma": 3,
          "finite_kernel_zero_mean": True, "boundary": "reflect",
          "response": "complex_magnitude", "channel_order": "scale_then_orientation",
          "feature_normalization": "none", "cache_dtype": "float32",
          "downsample": "response[::step,::step]"}


def kernel(wavelength, orientation):
    k, sigma = 2*np.pi/wavelength, CONFIG["sigma"]
    radius = int(np.ceil(CONFIG["truncate_sigma"] * sigma/k))
    y, x = np.mgrid[-radius:radius+1, -radius:radius+1]
    envelope = np.exp(-k*k*(x*x+y*y)/(2*sigma*sigma))
    wave = np.exp(1j*k*(x*np.cos(orientation)+y*np.sin(orientation)))
    values = (k*k/sigma**2) * envelope * (wave - np.exp(-sigma*sigma/2))
    values -= values.mean()  # 有限截断核的常量输入响应也为零。
    return values


def features(images, step=1, batch_size=32):
    """[N,H,W] -> [N,ceil(H/step),ceil(W/step),40]；先滤波后采样。"""
    images = np.asarray(images)
    if images.ndim != 3 or not np.isfinite(images).all() or step < 1:
        raise ValueError("Expected finite grayscale batch and positive step")
    n, h, w = images.shape
    result = np.empty((n, len(range(0,h,step)), len(range(0,w,step)), 40), dtype=np.float32)
    for scale, wavelength in enumerate(CONFIG["wavelengths"]):
        kernels = [kernel(wavelength, theta).astype(np.complex64) for theta in CONFIG["orientations"]]
        radius = kernels[0].shape[0]//2
        fft_shape = (next_fast_len(h+4*radius), next_fast_len(w+4*radius))
        transforms = [fftn(k, s=fft_shape) for k in kernels]
        for start in range(0,n,batch_size):
            padded = np.pad(images[start:start+batch_size].astype(np.float32),
                            ((0,0),(radius,radius),(radius,radius)), mode="reflect")
            spectrum = fftn(padded, s=fft_shape, axes=(-2,-1))
            for orientation, transformed in enumerate(transforms):
                convolution = ifftn(spectrum * transformed, axes=(-2,-1))
                response = convolution[:, 2*radius:2*radius+h, 2*radius:2*radius+w]
                result[start:start+len(padded), :, :, 8*scale+orientation] = np.abs(response[:,::step,::step])
    return result


def cached_features(images, destination, step):
    destination = Path(destination)
    metadata = destination.with_suffix(".json")
    specification = {"input_sha256": hashlib.sha256(np.ascontiguousarray(images).tobytes()).hexdigest(),
                     "input_shape": list(images.shape), "step": step, "gabor": CONFIG,
                     "implementation_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if destination.exists() and metadata.exists():
        old = json.loads(metadata.read_text())
        if old["specification"] == specification:
            digest = file_hash(destination)
            if digest != old["file_sha256"]:
                raise ValueError("Feature cache checksum mismatch")
            return np.load(destination, mmap_mode="r")
    destination.parent.mkdir(parents=True, exist_ok=True)
    array = features(images, step=step)
    np.save(destination, array)
    metadata.write_text(json.dumps({"specification": specification,
                                   "file_sha256": file_hash(destination)},indent=2),encoding="utf-8")
    del array
    return np.load(destination, mmap_mode="r")


def file_hash(path):
    digest=hashlib.sha256()
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda:handle.read(8*1024*1024),b''):digest.update(chunk)
    return digest.hexdigest()
