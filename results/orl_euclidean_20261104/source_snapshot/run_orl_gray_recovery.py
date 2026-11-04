"""Bounded exploration of unpublished ORL gray CSA11x2 -> ordinary LDA16 settings.

All candidates and ten historical splits freeze before fitting/scoring. Winners
are probe-selected exploratory results, never estimates from a new blind test.
No rank, LDA dimension, sample-count, iteration, or regularization search.
"""
import argparse
import csv
import json
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps
from scipy.linalg import eigh
from scipy.spatial.distance import cdist
from threadpoolctl import threadpool_limits

from csa import CSA, PCA, LDA, leading_vectors
from gabor import file_hash
from prepare_available_data import cv2, alignment_matrix
from run_available_reproduction import split

BASE = Path(__file__).resolve().parent
SEEDS = list(range(20, 30))
LABELS = np.repeat(np.arange(1, 41), 10)
NAMES = [f's{c}/{i}.pgm' for c in range(1, 41) for i in range(1, 11)]
STARTS = ['rectangular_identity', 'hosvd', 'full_identity', 'hosvd_centered']
CONTROLS = ['PCA30_LDA18', 'PCA22_LDA16']
POLICIES = [dict(id=f'{scale}_{origin}_{metric}', scale=scale,
                 origin=origin, metric=metric)
            for scale in ['unit', 'sw']
            for origin, metric in [('gallery', 'cosine'), ('linear', 'cosine'),
                                   ('gallery', 'euclidean')]]
SOURCES = ['run_orl_gray_recovery.py', 'verify_orl_gray_recovery.py', 'csa.py',
           'gabor.py', 'prepare_available_data.py', 'run_available_reproduction.py']


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def table(path, rows):
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


def specifications():
    common = dict(eyes='yunet', distance=20., eye_y=24., interpolation='linear',
                  border='replicate', histogram='PIL')
    changes = [('historical_shared', dict(historical=True)),
               ('d20_y24', {}), ('d18_y24', dict(distance=18.)),
               ('d22_y24', dict(distance=22.)), ('d20_y22', dict(eye_y=22.)),
               ('d20_y26', dict(eye_y=26.)), ('d16_y24', dict(distance=16.)),
               ('d20_y24_cubic', dict(interpolation='cubic')),
               ('d20_y24_lanczos', dict(interpolation='lanczos4')),
               ('d20_y24_zero', dict(border='zero')),
               ('d20_y24_cdfmin', dict(histogram='CDF_min')),
               ('haar_d20_y24', dict(eyes='haar_v2'))]
    return [dict(common, id=name, **change) for name, change in changes]


def equalize(image, method):
    if method == 'PIL':
        return np.asarray(ImageOps.equalize(Image.fromarray(image)), dtype=np.float32)
    counts = np.bincount(image.ravel(), minlength=256)
    cdf = counts.cumsum()
    minimum = cdf[np.flatnonzero(counts)[0]]
    lut = np.rint(np.clip((cdf-minimum)*255/max(1, image.size-minimum), 0, 255))
    return lut.astype(np.uint8)[image].astype(np.float32)


def prepare(root):
    root.mkdir(exist_ok=False)
    for name in ['features', 'models', 'predictions', 'source_snapshot']:
        (root/name).mkdir()
    for name in SOURCES:
        shutil.copy2(BASE/name, root/'source_snapshot'/name)
    old = {}
    for path in sorted((BASE/'results').rglob('*')):
        if root not in path.parents and path.suffix in ['.json', '.csv', '.py']:
            old[path.relative_to(BASE).as_posix()] = file_hash(path)
    dump(root/'historical_evidence_hashes.json', old)
    splits = [dict(seed=s, gallery=split(LABELS, 2, s)[0].tolist(),
                   probe=split(LABELS, 2, s)[1].tolist()) for s in SEEDS]
    dump(root/'splits.json', splits)
    specs = specifications()
    protocol = dict(date='2026-10-30', inputs=specs, seeds=SEEDS,
        CSA_ranks=[11, 2], CSA_LDA=16, PCA_controls={'PCA30_LDA18': [30, 18], 'PCA22_LDA16': [22, 16]},
        Tmax=3, epsilon=.001, starts=STARTS, policies=POLICIES,
        planned_CSA_fits=480, planned_PCA_fits=240, planned_scores=4320,
        source_sha256={name: file_hash(BASE/name) for name in SOURCES},
        input_size=[56, 46], gallery_per_class=2, probe_per_class=8,
        primary_policy=POLICIES[0]['id'], paper_CSA=84.1, paper_PCA=82.2,
        selection='Best global ten-split mean over this finite pool uses observed probes; no per-split oracle aggregation.',
        limits=['Historical splits/photos already observed; not blind or nested validation.',
                'No proof of global optimum or recovery of author settings.',
                'Full identity has larger initial mode dimensions; report separately.',
                'Centered CSA subtracts the fitting tensor mean; report separately.',
                'Fixed crop targets change field of view; do not call them author-confirmed.',
                'All methods share each input, split and scored metric convention.',
                'No shrinkage, new ranks, new LDA dimensions, extra samples, or excluded splits.',
                'Historical shared input varies by split; all other inputs are globally fixed.'])
    dump(root/'protocol.json', protocol)
    raw = np.stack([np.asarray(Image.open(BASE/'data/raw/orl'/n).convert('L')) for n in NAMES])
    eyes = {}
    for kind, filename in [('yunet', 'results/orl_protocol_audit/yunet_eye_coordinates.csv'),
                           ('haar_v2', 'data/annotations/orl_eye_coordinates.csv')]:
        source = BASE/filename
        records = rows(source)
        assert [r['file'] for r in records] == NAMES
        eyes[kind] = np.array([[[float(r['left_x']), float(r['left_y'])],
                               [float(r['right_x']), float(r['right_y'])]] for r in records])
    manifests = []
    for spec in specs:
        if spec.get('historical'):
            paths = {}
            for seed in SEEDS:
                selected = read(BASE/f'results/orl_protocol_audit/seed{seed}/selected.json')
                item = selected['shared_input']
                path = BASE/item['gray_path']
                assert file_hash(path) == item['gray_sha256']
                paths[str(seed)] = dict(path=item['gray_path'], sha256=item['gray_sha256'],
                                       shared_policy=selected['shared_policy'])
            manifests.append(dict(input=spec['id'], historical_sources=paths))
            continue
        target = np.array([[23-spec['distance']/2, spec['eye_y']],
                           [23+spec['distance']/2, spec['eye_y']]])
        data = []
        for image, eye in zip(raw, eyes[spec['eyes']]):
            matrix = alignment_matrix(eye, target)
            np.testing.assert_allclose(np.c_[eye, np.ones(2)] @ matrix.T, target, atol=1e-10)
            warped = cv2.warpAffine(image, matrix, (46, 56),
                flags={'linear': cv2.INTER_LINEAR, 'cubic': cv2.INTER_CUBIC, 'lanczos4': cv2.INTER_LANCZOS4}[spec['interpolation']],
                borderMode=cv2.BORDER_CONSTANT if spec['border']=='zero' else cv2.BORDER_REPLICATE)
            data.append(equalize(warped, spec['histogram']))
        array = np.stack(data)
        path = root/'features'/f"{spec['id']}.npy"
        np.save(path, array)
        manifests.append(dict(input=spec['id'], path=path.relative_to(BASE).as_posix(), sha256=file_hash(path)))
    anchor = BASE/'results/orl_protocol_audit/features/yunet_d20_replicate_gray.npy'
    assert file_hash(root/'features/d20_y24.npy') == file_hash(anchor)
    dump(root/'feature_manifest.json', manifests)
    dump(root/'input_freeze.json', {p.name: file_hash(p) for p in
         [root/'protocol.json', root/'splits.json', root/'feature_manifest.json']})
    print('Frozen 12 input bundles, 480 CSA and 240 PCA fits, six NN policies.', flush=True)


def load_data(root, input_id, seed):
    manifest = next(r for r in read(root/'feature_manifest.json') if r['input']==input_id)
    item = manifest['historical_sources'][str(seed)] if 'historical_sources' in manifest else manifest
    assert file_hash(BASE/item['path']) == item['sha256']
    return np.load(BASE/item['path'], mmap_mode='r')


def fit_csa(x, start):
    model = CSA((11, 2), max_iter=3, center=start=='hosvd_centered')
    model.shape = x.shape[1:]
    model.mean = x.mean(axis=0) if model.center else np.zeros(model.shape)
    z = x-model.mean
    if start == 'full_identity':
        model.bases = [np.eye(m) for m in model.shape]
    elif start.startswith('hosvd'):
        model.bases = [leading_vectors(np.einsum('nij,nkj->ik', z, z), 11),
                       leading_vectors(np.einsum('nji,njk->ik', z, z), 2)]
    else:
        model.bases = [np.eye(56, 11), np.eye(46, 2)]
    initial = [u.copy() for u in model.bases]
    history = []
    energy = float(np.sum(z*z))
    for iteration in range(3):
        for k, rank in enumerate([11, 2]):
            b = z @ model.bases[1] if k==0 else (model.bases[0].T @ z).transpose(0, 2, 1)
            cov = np.einsum('nac,nbc->ab', b, b)
            reference = sum(v @ v.T for v in b)
            np.testing.assert_allclose(cov, reference, rtol=3e-12, atol=1e-5)
            model.bases[k] = leading_vectors(cov, rank)
            u = model.bases[k]
            residual = np.linalg.norm(cov@u-u@(u.T@cov@u))/max(1., np.linalg.norm(cov))
            assert residual < 1e-10
        core = model.bases[0].T @ z @ model.bases[1]
        history.append(dict(iteration=iteration+1, sse=max(0., energy-float(np.sum(core*core)))))
    assert all(history[i+1]['sse'] <= history[i]['sse'] + 1e-5 for i in range(2))
    if start != 'full_identity':
        reference = CSA((11, 2), max_iter=3, center=model.center, initial_bases=initial).fit(x)
        for u, v in zip(reference.bases, model.bases):
            np.testing.assert_allclose(u@u.T, v@v.T, atol=2e-8, rtol=2e-8)
    return model, history


def fit(root):
    p = read(root/'protocol.json')
    for name, digest in p['source_sha256'].items():
        assert file_hash(BASE/name) == digest
    fitted = []
    for spec in p['inputs']:
        for s in read(root/'splits.json'):
            gallery = np.array(s['gallery'])
            x = np.asarray(load_data(root, spec['id'], s['seed'])[gallery], dtype=float)
            for start in STARTS+CONTROLS:
                if start in CONTROLS:
                    rank, dimension = p['PCA_controls'][start]
                    model = PCA(rank, solver='gram').fit(x)
                    saved = dict(basis=model.basis, mean=model.mean)
                    history = []
                else:
                    dimension = 16
                    model, history = fit_csa(x, start)
                    saved = dict(u0=model.bases[0], u1=model.bases[1], mean=model.mean)
                core = model.transform(x).reshape(80, -1)
                lda = LDA().fit(core, LABELS[gallery])
                assert lda.max_components >= dimension
                vals, _ = eigh(lda.sb, lda.sw)
                np.testing.assert_allclose(vals[::-1][:dimension], lda.eigenvalues[:dimension], rtol=1e-7, atol=1e-7)
                w = lda.basis[:, :dimension]
                residual = np.linalg.norm(lda.sb@w-(lda.sw@w)*lda.eigenvalues[:dimension])/max(1.,np.linalg.norm(lda.sb@w))
                assert residual < 1e-9
                saved.update(lda_basis=w, lda_mean=lda.mean, gallery_core=core, gallery=gallery,
                             eigenvalues=lda.eigenvalues[:dimension])
                path = root/'models'/f"{spec['id']}_s{s['seed']}_{start}.npz"
                np.savez(path, **saved)
                fitted.append(dict(input=spec['id'], seed=s['seed'], start=start,
                    model=path.relative_to(root).as_posix(), sha256=file_hash(path), fisher_residual=residual,
                    trajectory=json.dumps(history)))
        print('Fitted all ten splits:', spec['id'], flush=True)
    table(root/'models.csv', fitted)
    dump(root/'model_freeze.json', dict(count=len(fitted), sha256=file_hash(root/'models.csv'),
                                      all_fits_before_any_new_probe_scores=True))


def project(data, saved):
    if 'u0' in saved:
        return (saved['u0'].T @ (data-saved['mean']) @ saved['u1']).reshape(len(data), 22)
    return (data.reshape(len(data), -1)-saved['mean']) @ saved['basis']


def score(root):
    p = read(root/'protocol.json')
    assert file_hash(root/'models.csv') == read(root/'model_freeze.json')['sha256']
    splits = {r['seed']: r for r in read(root/'splits.json')}
    results = []
    for row in rows(root/'models.csv'):
        seed = int(row['seed'])
        assert file_hash(root/row['model']) == row['sha256']
        saved = np.load(root/row['model'])
        q = np.array(splits[seed]['probe']); g = saved['gallery']
        data = np.asarray(load_data(root, row['input'], seed)[q], dtype=float)
        query = project(data, saved)
        predicted, neighbors = [], []
        for policy in POLICIES:
            w = saved['lda_basis'].copy()
            if policy['scale']=='unit':
                w /= np.linalg.norm(w, axis=0)
            origin = saved['lda_mean'] if policy['origin']=='gallery' else 0.
            a, b = (query-origin)@w, (saved['gallery_core']-origin)@w
            winner = cdist(a, b, metric=policy['metric']).argmin(axis=1)
            if policy['metric']=='cosine':
                independent = ((a/np.linalg.norm(a, axis=1)[:, None]) @
                               (b/np.linalg.norm(b, axis=1)[:, None]).T).argmax(axis=1)
            else:
                independent = np.array([np.sum((b-v)**2, axis=1).argmin() for v in a])
            np.testing.assert_array_equal(winner, independent)
            pred = LABELS[g[winner]]
            correct = int(np.sum(pred==LABELS[q]))
            results.append(dict(input=row['input'], seed=seed, start=row['start'], policy=policy['id'],
                                correct=correct, probe_count=320, accuracy_percent=correct/3.2))
            predicted.append(pred); neighbors.append(g[winner])
        np.savez_compressed(root/'predictions'/Path(row['model']).name,
                            probe=q, predicted=np.array(predicted), neighbor=np.array(neighbors))
    table(root/'results.csv', results)
    summary = []
    for spec in p['inputs']:
        for start in STARTS+CONTROLS:
            for policy in POLICIES:
                matches = [r for r in results if (r['input'], r['start'], r['policy']) ==
                           (spec['id'], start, policy['id'])]
                assert sorted(r['seed'] for r in matches)==SEEDS
                values = np.array([r['accuracy_percent'] for r in matches])
                target = p['paper_CSA'] if start in STARTS else (p['paper_PCA'] if start==CONTROLS[0] else None)
                summary.append(dict(input=spec['id'], start=start, policy=policy['id'], n_splits=10,
                    mean_percent=float(values.mean()), std_pp=float(values.std(ddof=1)),
                    min_percent=float(values.min()), max_percent=float(values.max()),
                    paper_percent=target if target is not None else '',
                    mean_minus_paper_pp=float(values.mean()-target) if target is not None else ''))
    table(root/'summary.csv', summary)
    eligible = [r for r in summary if r['start'] in STARTS]
    best = max(eligible, key=lambda r:r['mean_percent'])
    rank_conforming = max([r for r in eligible if r['start'] in STARTS[:2]], key=lambda r:r['mean_percent'])
    fixed = [r for r in eligible if r['input']!='historical_shared']
    fixed_best = max(fixed, key=lambda r:r['mean_percent'])
    matched = [r for r in summary if r['input']==best['input'] and r['policy']==best['policy']]
    single = max([r for r in results if r['start'] in STARTS], key=lambda r:r['accuracy_percent'])
    historical = [r for r in results if r['input']=='historical_shared' and r['start']=='rectangular_identity']
    manifests = read(root/'feature_manifest.json')[0]['historical_sources']
    old = rows(BASE/'results/orl_protocol_audit/evaluation/fixed_results.csv')
    anchor_counts = []
    for seed in SEEDS:
        policy = manifests[str(seed)]['shared_policy']
        policy_id = ('unit' if policy['scaling']=='unit_columns' else 'sw')+'_'+('gallery' if policy['lda_center'] else 'linear')+'_'+policy['metric']
        actual = next(r for r in historical if r['seed']==seed and r['policy']==policy_id)
        previous = next(r for r in old if int(r['seed'])==seed and r['method']=='CSA-2+LDA')
        assert actual['correct']==int(previous['correct'])
        anchor_counts.append(actual['accuracy_percent'])
    dump(root/'analysis.json', dict(best_mean=best, best_globally_fixed_input=fixed_best,
        best_uncentered_rank_conforming=rank_conforming, matched_settings=matched,
        highest_single_run=single, historical_anchor_mean=float(np.mean(anchor_counts)),
        historical_anchor_std=float(np.std(anchor_counts, ddof=1)),
        selection=p['selection'], limits=p['limits']))
    dump(root/'scoring_checks.json', dict(passed=True, model_count=len(rows(root/'models.csv')),
        score_count=len(results), prediction_count=len(results)*320,
        all_ten_historical_anchor_correct_counts_match=True, independent_NN_matches=True))
    print(json.dumps(dict(best=best, best_rank_conforming=rank_conforming, max_run=single), indent=2), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='results/orl_gray_recovery_20261030')
    parser.add_argument('--stage', choices=['prepare', 'fit', 'score', 'all'], default='all')
    args = parser.parse_args()
    root = BASE/args.output
    with threadpool_limits(limits=2):
        if args.stage in ['prepare', 'all']: prepare(root)
        if args.stage in ['fit', 'all']: fit(root)
        if args.stage in ['score', 'all']: score(root)


if __name__=='__main__':
    main()
