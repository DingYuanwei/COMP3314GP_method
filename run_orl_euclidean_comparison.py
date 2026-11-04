"""Freeze and verify matched ORL Euclidean comparisons; no parameter search.

Reuse 50 saved models and fit 30 missing Gabor controls on exactly the same
features/splits. Also score cosine on these same models as a historical metric
control. Prior publications and their frozen evidence remain unchanged.
"""
import argparse
import json
import shutil
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
from scipy.spatial.distance import cdist
from threadpoolctl import threadpool_limits

from csa import CSA,PCA,LDA,mode_product,unfold
from gabor import file_hash
import run_orl_gray_recovery as R

BASE=Path(__file__).resolve().parent
CASES=[('gray_PCA30_LDA18','gray','PCA+LDA (Gray)',30,18,82.2),
       ('gray_CSA22_LDA16','gray','CSA-2+LDA',(11,2),16,84.1),
       ('gabor_PCA76','gabor','PCA (Gabor)',76,None,86.6),
       ('gabor_CSA390','gabor','CSA-3',(15,1,26),None,94.4),
       ('gabor_PCA33_LDA25','gabor','PCA+LDA (Gabor)',33,25,87.2),
       ('gabor_CSA24_LDA23','gabor','CSA-3+LDA',(4,2,3),23,90.9),
       ('gray_PCA22_LDA16','gray','PCA22+LDA16 equal budget',22,16,None),
       ('gabor_PCA24_LDA23','gabor','PCA24+LDA23 equal budget',24,23,None)]


def project(data,saved):
    if 'basis' in saved:
        return (data.reshape(len(data),-1)-saved['mean'])@saved['basis']
    z=data-saved['mean']
    for k in range(data.ndim-1):z=mode_product(z,saved[f'u{k}'].T,k)
    return z.reshape(len(data),-1)


def independent_core(data,saved):
    if 'basis' in saved:return (data.reshape(len(data),-1)-saved['mean'])@saved['basis']
    if data.ndim==3:
        return np.einsum('ha,nhw,wb->nab',saved['u0'],data-saved['mean'],saved['u1']).reshape(len(data),-1)
    return np.einsum('ha,nhwc,wb,cd->nabd',saved['u0'],data-saved['mean'],saved['u1'],saved['u2'],optimize=True).reshape(len(data),-1)


def check_CSA390(x,saved):
    bases=[np.eye(m,r) for m,r in zip(x.shape[1:],(15,1,26))]
    for _ in range(3):
        for k,rank in enumerate((15,1,26)):
            z=x
            for j,u in enumerate(bases):
                if j!=k:z=mode_product(z,u.T,j)
            b=unfold(z,k)
            covariance=sum(a@a.T for a in b)
            _,v=eigh(covariance);bases[k]=v[:,-rank:]
    errors=[float(np.linalg.norm(u@u.T-saved[f'u{k}']@saved[f'u{k}'].T)) for k,u in enumerate(bases)]
    assert max(errors)<2e-7,errors
    return max(errors)


def run(root):
    root.mkdir(exist_ok=False)
    for name in ['models','predictions','source_snapshot']:(root/name).mkdir()
    sources=['run_orl_euclidean_comparison.py','csa.py','gabor.py','run_orl_gray_recovery.py']
    for name in sources:shutil.copy2(BASE/name,root/'source_snapshot'/name)
    history={p.relative_to(BASE).as_posix():file_hash(p) for p in sorted((BASE/'results').rglob('*'))
             if root not in p.parents and p.suffix in ['.csv','.json','.py']}
    R.dump(root/'historical_evidence_hashes.json',history)
    gr=BASE/'results/orl_gray_recovery_20261030/refinement'
    ga=BASE/'results/orl_recovery_20261027'
    splits=R.read(gr/'splits.json');assert splits==R.read(ga/'splits.json')
    R.dump(root/'splits.json',splits)
    manifest={
        'gray':next(x for x in R.read(gr/'feature_manifest.json') if x['input']=='d15_y24'),
        'gabor':dict(path='results/orl_recovery_20261027/features/d20_y24.npy',
                     sha256=R.read(ga/'input_freeze.json')['features/d20_y24.npy'])}
    for item in manifest.values():assert file_hash(BASE/item['path'])==item['sha256']
    R.dump(root/'feature_manifest.json',manifest)
    protocol=dict(date='2026-11-04',seeds=R.SEEDS,G=2,P=8,input_size=dict(gray=[56,46],gabor=[28,23,40]),
        gray_input='d15/y24, YuNet, linear/replicate/PIL HE',
        gabor_input='d20/y24, pi-context, lambda0=4,39x39 Gabor, magnitude1; frozen recovery features',
        cases=[dict(id=i,kind=k,method=m,pre_dims=d,LDA=l,paper_percent=p) for i,k,m,d,l,p in CASES],
        default_metric='euclidean',historical_metric_control='cosine',LDA_scale='unit columns',
        NN_origin='own gallery mean; common translation has no effect on Euclidean distance',
        CSA=dict(center=False,Tmax=3,gray_start='rectangular identity',Gabor24_start='HOSVD',Gabor390_start='rectangular identity'),
        PCA=dict(center=True,solver='gram'),LDA='ordinary unregularized Fisher; fixed paper dimensions',
        planned_new_fits=30,planned_reused_models=50,planned_scores=160,
        sources_sha256={n:file_hash(BASE/n) for n in sources},
        selection='No new input/start/rank/distance search. Apply the user-selected Euclidean rule to fixed previously explored inputs.',
        limitations=['Current inputs were selected/explored on historical probes; not blind.',
          'The Euclidean default is a group decision, not author/TA confirmation.',
          'Two representation-specific inputs; all gray methods share one array and all Gabor methods share one array.',
          'Paper best-configuration aggregation is unspecified.',
          'MNIST/FERET keep their recorded internally shared protocols.',
          'Historical published cosine table mixed earlier references; the matched cosine controls here use the same current inputs.'])
    R.dump(root/'protocol.json',protocol)
    R.dump(root/'input_freeze.json',{n:file_hash(root/n) for n in ['protocol.json','splits.json','feature_manifest.json']})
    gray_models=R.rows(gr/'models.csv');gabor_models=R.rows(ga/'models.csv')
    records=[];new_count=0
    for split in splits:
        seed=split['seed'];g=np.array(split['gallery'])
        for id,kind,method,rank,dimension,paper in CASES:
            reused=None
            if kind=='gray':
                start={'gray_PCA30_LDA18':'PCA30_LDA18','gray_CSA22_LDA16':'rectangular_identity','gray_PCA22_LDA16':'PCA22_LDA16'}[id]
                reused=next(r for r in gray_models if r['input']=='d15_y24' and int(r['seed'])==seed and r['start']==start)
                path=gr/reused['model'];digest=reused['sha256']
            elif id in ['gabor_CSA24_LDA23','gabor_PCA24_LDA23']:
                start='hosvd' if id=='gabor_CSA24_LDA23' else 'PCA24'
                reused=next(r for r in gabor_models if r['input']=='d20_y24' and int(r['seed'])==seed and r['start']==start)
                path=ga/reused['model'];digest=reused['model_sha256']
            if reused is None:
                x=np.asarray(np.load(BASE/manifest[kind]['path'],mmap_mode='r')[g],dtype=float)
                model=CSA(rank,center=False,max_iter=3).fit(x) if isinstance(rank,tuple) else PCA(rank,solver='gram').fit(x)
                saved=dict(mean=model.mean,gallery=g,gallery_core=model.transform(x).reshape(80,-1))
                if isinstance(rank,tuple):saved.update({f'u{k}':u for k,u in enumerate(model.bases)})
                else:saved['basis']=model.basis
                if dimension:
                    lda=LDA().fit(saved['gallery_core'],R.LABELS[g])
                    saved.update(lda_basis=lda.basis[:,:dimension],lda_mean=lda.mean,eigenvalues=lda.eigenvalues[:dimension])
                path=root/'models'/f'{id}_s{seed}.npz';np.savez(path,**saved);digest=file_hash(path);new_count+=1
            assert file_hash(path)==digest
            records.append(dict(id=id,kind=kind,method=method,seed=seed,model=path.relative_to(BASE).as_posix(),
                sha256=digest,new_fit=reused is None,feature_sha256=manifest[kind]['sha256']))
        print('Prepared models for split',seed,flush=True)
    assert new_count==30 and len(records)==80
    R.table(root/'models.csv',records)
    R.dump(root/'model_freeze.json',dict(new_fits=30,reused_models=50,sha256=file_hash(root/'models.csv'),all_models_before_new_scoring=True))
    scores=[];checks=[];reference_error=0.
    for row in records:
        split=next(s for s in splits if s['seed']==row['seed']);g,q=np.array(split['gallery']),np.array(split['probe'])
        assert not set(g)&set(q) and sorted(np.r_[g,q])==list(range(400))
        np.testing.assert_array_equal(np.bincount(R.LABELS[g])[1:],np.full(40,2))
        np.testing.assert_array_equal(np.bincount(R.LABELS[q])[1:],np.full(40,8))
        model=np.load(BASE/row['model']);assert file_hash(BASE/row['model'])==row['sha256']
        np.testing.assert_array_equal(model['gallery'],g)
        data=np.asarray(np.load(BASE/manifest[row['kind']]['path'],mmap_mode='r'),dtype=float)
        core=project(data[g],model);query=project(data[q],model)
        np.testing.assert_allclose(core,model['gallery_core'],rtol=1e-10,atol=1e-8)
        np.testing.assert_allclose(core,independent_core(data[g],model),rtol=1e-10,atol=1e-8)
        np.testing.assert_allclose(query,independent_core(data[q],model),rtol=1e-10,atol=1e-8)
        residual=0.
        if 'lda_basis' in model:
            sw=np.zeros((core.shape[1],core.shape[1]));sb=sw.copy();mean=core.mean(axis=0)
            for label in range(1,41):
                x=core[R.LABELS[g]==label];delta=x-x.mean(axis=0);sw+=delta.T@delta
                delta=x.mean(axis=0)-mean;sb+=len(x)*np.outer(delta,delta)
            w=model['lda_basis'];residual=float(np.linalg.norm(sb@w-(sw@w)*model['eigenvalues'])/max(1.,np.linalg.norm(sb@w)))
            assert residual<1e-8
            w=w/np.linalg.norm(w,axis=0);core=(core-mean)@w;query=(query-mean)@w
        else:
            mean=core.mean(axis=0);core=core-mean;query=query-mean
        if row['id']=='gabor_CSA390':reference_error=max(reference_error,check_CSA390(data[g],model))
        if row['new_fit'] and 'basis' in model:
            x=data[g].reshape(80,-1)-model['mean'];w=model['basis']
            values=np.linalg.eigvalsh(x@x.T)[::-1][:w.shape[1]]
            err=np.linalg.norm(x.T@(x@w)-w*values)/max(1.,np.linalg.norm(w*values));assert err<1e-9
        predicted=[];neighbors=[]
        for metric in ['euclidean','cosine']:
            chosen=cdist(query,core,metric=metric).argmin(axis=1)
            if metric=='euclidean':other=np.array([np.sum((core-x)**2,axis=1).argmin() for x in query])
            else:other=((query/np.linalg.norm(query,axis=1)[:,None])@(core/np.linalg.norm(core,axis=1)[:,None]).T).argmax(axis=1)
            np.testing.assert_array_equal(chosen,other)
            pred=R.LABELS[g[chosen]];correct=int(np.sum(pred==R.LABELS[q]))
            scores.append(dict(id=row['id'],kind=row['kind'],method=row['method'],seed=row['seed'],metric=metric,
                correct=correct,probe_count=320,accuracy_percent=correct/3.2,feature_sha256=row['feature_sha256']))
            predicted.append(pred);neighbors.append(g[chosen])
        path=root/'predictions'/f"{row['id']}_s{row['seed']}.npz"
        np.savez_compressed(path,probe=q,predicted=predicted,neighbor=neighbors)
        with np.load(path) as saved:np.testing.assert_array_equal(saved['predicted'],predicted)
        checks.append(dict(id=row['id'],seed=row['seed'],Fisher_residual=residual,model_sha256=row['sha256']))
    R.table(root/'results.csv',scores);R.table(root/'model_checks.csv',checks)
    summaries=[]
    for id,kind,method,rank,dimension,paper in CASES:
        for metric in ['euclidean','cosine']:
            a=[r for r in scores if r['id']==id and r['metric']==metric];assert sorted(r['seed'] for r in a)==R.SEEDS
            v=np.array([r['accuracy_percent'] for r in a])
            summaries.append(dict(dataset='ORL',profile='matched_'+metric,method=method,id=id,kind=kind,metric=metric,n_splits=10,
                mean_percent=float(v.mean()),std_pp=float(v.std(ddof=1)),min_percent=float(v.min()),max_percent=float(v.max()),
                paper_percent=paper if paper is not None else '',difference_pp=float(v.mean()-paper) if paper is not None else '',
                source='results/orl_euclidean_20261104/summary.csv',category='Matched '+metric+' ORL'))
    R.table(root/'summary.csv',summaries)
    current=[r for r in summaries if r['metric']=='euclidean' and r['paper_percent']!='']
    R.table(root/'comparison.csv',current)
    R.table(root/'matched_cosine_history.csv',[r for r in summaries if r['metric']=='cosine'])
    # Independently recover the four earlier fixed-input metric scores.
    for filename,input_id,policy,ids,starts in [
        (gr/'results.csv','d15_y24','unit_gallery_euclidean',['gray_CSA22_LDA16','gray_PCA30_LDA18','gray_PCA22_LDA16'],['rectangular_identity','PCA30_LDA18','PCA22_LDA16']),
        (ga/'results.csv','d20_y24','unit_gallery_euclidean_g0',['gabor_CSA24_LDA23','gabor_PCA24_LDA23'],['hosvd','PCA24'])]:
        old=R.rows(filename)
        for id,start in zip(ids,starts):
            for seed in R.SEEDS:
                previous=next(r for r in old if r['input']==input_id and r['policy']==policy and r['start']==start and int(r['seed'])==seed)
                actual=next(r for r in scores if r['id']==id and r['seed']==seed and r['metric']=='euclidean')
                assert int(previous['correct'])==actual['correct']
    for name,digest in history.items():assert file_hash(BASE/name)==digest,name
    for name,digest in protocol['sources_sha256'].items():assert file_hash(BASE/name)==digest
    assert file_hash(root/'models.csv')==R.read(root/'model_freeze.json')['sha256']
    R.dump(root/'verification.json',dict(passed=True,models=80,new_fits=30,reused_models=50,scores=160,predictions=51200,
        same_feature_hash_within_each_representation=True,same_ten_splits=True,same_distance_and_LDA_scale=True,
        old_correct_counts_recovered=50,independent_projection_and_NN_checks=True,independent_CSA390_replays=10,
        max_CSA_projector_error=reference_error,max_independent_Fisher_residual=max(r['Fisher_residual'] for r in checks),
        old_evidence_unchanged=len(history),source_and_model_hashes_match=True,parameter_search=False,
        independent_blind_test=False,author_metric_confirmed=False))
    print(json.dumps(current,indent=2),flush=True)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='results/orl_euclidean_20261104')
    args=parser.parse_args()
    with threadpool_limits(limits=2):run(BASE/args.output)


if __name__=='__main__':main()
