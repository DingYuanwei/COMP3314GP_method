"""Generate report/slide figures from recorded evidence; never fit new models.

Run from the project root. The final LDA-curve panel rescales saved directions
and scores saved models (zero fits), checking its 23D endpoint against records.
All other panels read existing aggregate/per-split tables directly.
"""
from pathlib import Path
from collections import defaultdict
import csv
import hashlib
import json
import textwrap
import zipfile
from decimal import Decimal, ROUND_HALF_UP

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch
from scipy.spatial.distance import cdist
from threadpoolctl import threadpool_limits

BASE = Path(__file__).resolve().parent
DATE_STAMP = '20261104'
OUT = BASE/f'results/report_figures_{DATE_STAMP}'
PDF = BASE/f'output/pdf/CSA_figure_atlas_{DATE_STAMP}.pdf'
PAPER, BLUE, TEAL, ORANGE, PURPLE, RED = '#344254', '#326FA0', '#168078', '#CF7132', '#8363A7', '#B64F58'
METHODS = ['CSA24_LDA23', 'CSA390', 'PCA24_LDA23', 'PCA33_LDA25']
NAMES = {'CSA24_LDA23':'CSA24 + LDA23', 'CSA390':'CSA390',
         'PCA24_LDA23':'PCA24 + LDA23', 'PCA33_LDA25':'PCA33 + LDA25'}
SOURCE_HASHES, ITEMS, DATAPOINTS, FIGURES = {}, [], [], []
SOURCE_MAP = {
 'all_recognition_cases':['results/orl_protocol_audit/shared_comparison.csv','results/orl_euclidean_20261104/comparison.csv'],
 'orl_paper_comparison':['results/orl_protocol_audit/shared_comparison.csv','results/orl_euclidean_20261104/comparison.csv'],
 'mnist_paper_comparison':['results/orl_protocol_audit/shared_comparison.csv'],
 'feret_paper_comparison':['results/orl_protocol_audit/shared_comparison.csv'],
 'all_paper_gaps':['results/orl_protocol_audit/shared_comparison.csv','results/orl_euclidean_20261104/comparison.csv'],
 'orl_ten_splits':['results/orl_recovery_20261027/results.csv','results/orl_recovery_20261027/summary.csv'],
 'orl_geometry_initialization':['results/orl_recovery_20261027/summary.csv'],
 'orl_sigma_context_factorial':['results/orl_controlled/summary.csv'],
 'orl_three_fixed_inputs':['results/orl_fixed_input_extensions/comparison.csv'],
 'orl_gallery_selection_stages':['results/orl_unknown_parameters/comparison.csv'],
 'orl_crop_only_optimization':['results/orl_ta_crop_optimized/comparison.csv'],
 'orl_sample_size':['results/orl_sample_size/summary.json','results/orl_sample_size/pca_control/summary.json'],
 'mnist_selection_negative':['results/mnist_protocol_optimized/comparison.csv'],
 'feret_selection_vs_fixed':['results/feret_validation_selected_v3/fixed_results.csv'],
 'dater_matched_comparison':['results/orl_dater/summary.csv'],
 'shrinkage_ablation':['results/csa_lda_optimized/evaluation/summary.json'],
 'cost_scope':['results/orl_controlled/cost_benchmark.csv'],
 'eye_perturbation':['results/orl_controlled/robustness_summary.csv'],
 'error_tradeoffs':['results/orl_controlled/historical_error_summary.json'],
 'mean_vs_maximum':['results/orl_best_search/best_results.json','results/orl_best_search/paper_dimension_best.json','results/orl_recovery_20261027/summary.csv'],
 'orl_reconstruction':['results/available_reproduction_v2/orl_reconstruction.csv'],
 'csa_convergence':['results/available_reproduction_v2/orl_convergence.json'],
 'retained_variation':['results/csa_lda_focus/representation_statistics.csv'],
 'feret_lda_curves':['results/feret_validation_selected_v3/lda_dimension_curves.csv'],
 'orl_historical_dimension_curves':['results/available_reproduction_v2/dimension_curves.csv'],
 'method_pipeline':['csa.py','run_orl_recovery.py','results/orl_euclidean_20261104/protocol.json'],
 'orl_metric_comparison':['results/orl_euclidean_20261104/summary.csv'],
 'orl_current_lda_curves':[f'results/report_figures_{DATE_STAMP}/derived_lda_curves.csv','results/orl_recovery_20261027/models.csv','results/orl_recovery_20261027/results.csv']}
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':11,
    'axes.spines.top':False, 'axes.spines.right':False, 'axes.labelsize':11,
    'axes.titlesize':13, 'legend.fontsize':9, 'pdf.fonttype':42,
    'svg.fonttype':'none', 'axes.unicode_minus':False, 'savefig.facecolor':'white'})


def source(name):
    path = BASE/name
    SOURCE_HASHES[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return path


def read(name):
    with source(name).open(encoding='utf-8-sig') as handle:
        return list(csv.DictReader(handle))


def js(name):
    return json.loads(source(name).read_text(encoding='utf-8'))


def f(row, name='mean_percent'):
    return float(row[name])


def fmt(value, signed=False):
    value=Decimal(str(float(value))).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
    return ('+' if signed and value>=0 else '')+str(value)


def pick(rows, **conditions):
    found = [r for r in rows if all(str(r[k])==str(v) for k,v in conditions.items())]
    assert len(found)==1, conditions
    return found[0]


def one(title, subtitle='', nrows=1, ncols=1, size=(13.33,7.5)):
    fig, axes = plt.subplots(nrows,ncols,figsize=size,squeeze=False)
    fig.suptitle(title,x=.055,y=.953,ha='left',fontsize=20,fontweight='bold',color=PAPER)
    fig.text(.055,.895,subtitle,fontsize=10.5,color='#596776',va='top')
    fig.subplots_adjust(left=.12,right=.95,top=.82,bottom=.21,hspace=.5,wspace=.32)
    for ax in axes.flat:
        ax.set_axisbelow(True)
        ax.grid(axis='y',color='#E5EAF0',linewidth=.7)
    return fig, axes.ravel()


def finish(fig, slug, title, caption, rows, category='Main result', use='Slides and report'):
    number=len(ITEMS)+1
    if slug in ['orl_sigma_context_factorial','orl_three_fixed_inputs','orl_gallery_selection_stages','orl_crop_only_optimization','orl_sample_size','shrinkage_ablation','cost_scope','eye_perturbation','error_tradeoffs','mean_vs_maximum','retained_variation']:
        caption='Historical protocol study; not the current matched Euclidean headline. '+caption
    if slug in ['all_recognition_cases','orl_paper_comparison','mnist_paper_comparison','feret_paper_comparison','all_paper_gaps']:
        caption+=' Paper values: Xu et al., IEEE TCSVT (2008), Tables I/II/IV, doi:10.1109/TCSVT.2007.903317.'
    for name in SOURCE_MAP[slug]:source(name)
    fig.text(.055,.993,f'{number:02d}  |  {category.upper()}',ha='left',va='top',fontsize=8,color='#667485')
    fig.text(.055,.035,textwrap.fill(caption,145),ha='left',va='bottom',fontsize=8.5,color='#4B5866',linespacing=1.35)
    path=f'{number:02d}_{slug}'
    fig.savefig(OUT/'png'/f'{path}.png',dpi=240)
    fig.savefig(OUT/'svg'/f'{path}.svg')
    FIGURES.append(fig)
    plt.close(fig)
    record=dict(number=number,slug=slug,title=title,category=category,recommended_use=use,
                png=f'png/{path}.png',svg=f'svg/{path}.svg',pdf_page=number,caption=caption,
                source_files='; '.join(SOURCE_MAP[slug]))
    ITEMS.append(record)
    for row in rows:
        DATAPOINTS.append(dict(figure=number,slug=slug,**row))
    print(f'Generated {number:02d}: {slug}',flush=True)


def draw_pair(ax, labels, paper, ours, sd=None, colors=None, limits=(65,101)):
    y=np.arange(len(labels)); colors=colors or [BLUE]*len(labels)
    for i,(p,o) in enumerate(zip(paper,ours)):
        ax.plot([p,o],[i,i],color='#C5CED8',linewidth=3,zorder=1)
        if sd is not None and np.isfinite(sd[i]):
            ax.errorbar(o,i,xerr=sd[i],fmt='none',ecolor=colors[i],capsize=3,zorder=2)
        ax.scatter(p,i,color=PAPER,marker='D',s=44,zorder=3)
        ax.scatter(o,i,color=colors[i],s=65,zorder=4)
        ax.annotate(f'{fmt(o)}  ({fmt(o-p, signed=True)} pp)',(o,i),xytext=(0,-17),textcoords='offset points',fontsize=9,ha='center',color=colors[i])
    ax.set_yticks(y,labels);ax.set_ylim(len(labels)-.05,-.55);ax.set_xlim(*limits)
    ax.set_xlabel('Top-1 accuracy (%)');ax.grid(axis='x',color='#E5EAF0');ax.grid(axis='y',visible=False)
    ax.scatter([],[],color=PAPER,marker='D',label='Paper best-configuration value')
    ax.scatter([],[],color=BLUE,label='Our recorded result')


def current_rows():
    rows=[dict(r) for r in read('results/orl_protocol_audit/shared_comparison.csv')
          if r['profile'] in ['paper_dimensions','group_primary','cosine_control']]
    current=read('results/orl_euclidean_20261104/comparison.csv')
    for r in rows:
        r['category']='Shared-setting reference'
        if r['dataset']=='ORL':
            new=pick(current,method=r['method'])
            for key in ['mean_percent','std_pp','difference_pp','source','profile','category']:
                r[key]=new[key]
    assert len(rows)==16
    return rows


def main_comparisons():
    rows=current_rows()
    short={'PCA+LDA (Gray)':'Gray PCA + LDA','CSA-2+LDA':'Gray CSA + LDA',
           'PCA (Gabor)':'Gabor PCA','CSA-3':'Gabor CSA','PCA+LDA (Gabor)':'Gabor PCA + LDA',
           'CSA-3+LDA':'Gabor CSA24 + LDA23'}
    def method_label(r):
        if r['dataset']=='ORL':
            return {'PCA+LDA (Gray)':'Gray PCA30 + LDA18','CSA-2+LDA':'Gray CSA11x2 + LDA16',
                    'PCA (Gabor)':'Gabor PCA76','CSA-3':'Gabor CSA390',
                    'PCA+LDA (Gabor)':'Gabor PCA33 + LDA25','CSA-3+LDA':'Gabor CSA24 + LDA23'}[r['method']]
        if r['dataset'].startswith('MNIST'):
            g30='G30' in r['dataset']
            return ('PCA60' if g30 else 'PCA50') if r['method']=='PCA (Gabor)' else ('CSA810' if g30 else 'CSA975')
        q=int(r['dataset'].split('=')[1])
        return ({50:'PCA45 + LDA25',100:'PCA95 + LDA40',200:'PCA112 + LDA69'} if r['method']=='PCA+LDA (Gray)'
                else {50:'CSA10x4 + LDA35',100:'CSA11x5 + LDA44',200:'CSA13x7 + LDA62'})[q]
    title='Paper versus reproduction: all 16 recognition cases'
    fig,axes=one(title,'Updated 2026-11-04: ORL uses matched Euclidean protocols. Settings and historical controls are described below.',size=(13.33,9.3))
    ax=axes[0];ax.axis('off')
    cells=[]
    for r in rows:
        score=f"{fmt(f(r))}"+(f" +/- {fmt(f(r,'std_pp'))}" if r['std_pp'] else '')
        cells.append([r['dataset'].replace(' G30/P470',' G30').replace(' G40/P460',' G40'),method_label(r),score,
                      f"{fmt(f(r,'paper_percent'))}",f"{fmt(f(r,'difference_pp'), signed=True)}"])
    table=ax.table(cellText=cells,colLabels=['Dataset / setting','Method','Our accuracy (%)','Paper (%)','Difference (pp)'],
                   cellLoc='left',colLoc='left',colWidths=[.19,.29,.22,.14,.16],bbox=[0,-.02,1,1.02])
    table.auto_set_font_size(False);table.set_fontsize(10)
    for (i,j),cell in table.get_celld().items():
        cell.set_edgecolor('#DDE4EB');cell.set_linewidth(.5)
        if i==0:cell.set_facecolor(PAPER);cell.set_text_props(color='white',weight='bold')
        else:cell.set_facecolor('#FFF0E4' if i in [2,6] else ('#F2F6FA' if i%2 else 'white'))
    finish(fig,'all_recognition_cases',title,'ORL: same ten splits and Euclidean NN; one shared gray input and one shared Gabor input across methods. LDA columns have unit norm. Inputs were previously explored on probes; context/HOSVD details are in REPORT. MNIST/FERET retain their recorded protocols. +/- is sample SD; paper aggregation is unknown.',rows,use='Report or backup slide')
    for ds,slug,title in [('ORL','orl_paper_comparison','ORL: six paper-dimension recognition cases'),
                           ('MNIST','mnist_paper_comparison','MNIST: both gallery sizes, both representations')]:
        selected=[r for r in rows if r['dataset'].startswith(ds)]
        fig,axes=one(title,'Diamonds: paper values. Circles: our means. Horizontal whiskers: sample SD.')
        labels=[method_label(r)+('\n'+r['dataset'] if ds=='MNIST' else '') for r in selected]
        colors=[ORANGE if r['dataset']=='ORL' and r['method'].startswith('CSA') else BLUE for r in selected]
        draw_pair(axes[0],labels,[f(r,'paper_percent') for r in selected],[f(r) for r in selected],
                  [f(r,'std_pp') for r in selected],colors,limits=(65,101) if ds=='ORL' else (84,96))
        axes[0].legend(loc='upper right');fig.subplots_adjust(left=.27)
        caption=('All gray methods share d15/y24 input; all Gabor methods share d20/y24 pi-context input. All use seeds20-29, G2/P8 and Euclidean NN; LDA columns have unit norm. Inputs retain prior probe exploration. See REPORT for settings and historical cosine comparisons; author aggregation is unknown.' if ds=='ORL' else
                 'MNIST uses the original three-seed references. Best paper configurations and our repeated means have different reporting conventions.')
        finish(fig,slug,title,caption,selected)
    fer=[r for r in rows if r['dataset'].startswith('FERET')]
    title='FERET: three training sizes, PCA and CSA controls'
    fig,axes=one(title,'Official grayscale Fa/Fb pairs; first q identities learn the representation; remaining identities are tested.')
    ax=axes[0]
    for method,color,label in [('PCA+LDA (Gray)',BLUE,'PCA + LDA'),('CSA-2+LDA',TEAL,'CSA + LDA')]:
        selected=[r for r in fer if r['method']==method];x=[50,100,200]
        ax.plot(x,[f(r) for r in selected],'-o',color=color,lw=2.3,label='Our fixed cosine: '+label)
        ax.plot(x,[f(r,'paper_percent') for r in selected],'--D',color=color,alpha=.65,label='Paper: '+label)
        for xx,r in zip(x,selected):ax.annotate(f'{fmt(f(r))}',(xx,f(r)),xytext=(5,5 if color==TEAL else -17),textcoords='offset points',fontsize=10,color=color)
    ax.set_xticks([50,100,200]);ax.set_xlabel('Training identities q');ax.set_ylabel('Top-1 accuracy (%)');ax.set_ylim(81,99);ax.legend(ncol=2,loc='lower right')
    finish(fig,'feret_paper_comparison',title,'These are fixed shared-cosine controls, not validation-selected winners. One fixed identity partition per q; no repeated-identity SD or significance claim. CSA does not beat the reproduced PCA at q=50.',fer)
    title='Numerical gaps from the paper across all 16 cases'
    fig,axes=one(title,'Positive differences mean a higher recorded number; they do not prove a matched-protocol improvement.',size=(13.33,9.3))
    ax=axes[0];y=np.arange(16);vals=[f(r,'difference_pp') for r in rows]
    ax.barh(y,vals,color=[ORANGE if r['dataset']=='ORL' and r['method'].startswith('CSA') else (TEAL if v>=0 else BLUE) for r,v in zip(rows,vals)])
    ax.set_yticks(y,[r['dataset']+' | '+method_label(r) for r in rows],fontsize=9);ax.invert_yaxis();ax.axvline(0,color=PAPER,lw=1)
    ax.set_xlim(-8.5,7);ax.set_xlabel('Our value minus paper value (percentage points)')
    for i,v in enumerate(vals):ax.text(v+(.13 if v>=0 else -.13),i,f'{fmt(v, signed=True)}',ha='left' if v>=0 else 'right',va='center',fontsize=9)
    fig.subplots_adjust(left=.34);finish(fig,'all_paper_gaps',title,'ORL uses matched Euclidean comparisons: gray CSA81.72 and Gabor CSA24 87.53. Inputs/splits/metric are shared within each representation. Other datasets retain their recorded protocols. Old cosine numbers are historical; original author metric/aggregation remains unspecified.',rows,use='Report / backup slide')


def recovery():
    raw=read('results/orl_recovery_20261027/results.csv');summary=read('results/orl_recovery_20261027/summary.csv')
    policy='unit_gallery_euclidean_g0';colors=[ORANGE,PURPLE,'#73899D',BLUE]
    starts=['hosvd','full_identity','rectangular_identity','PCA24'];names=['HOSVD (representative)','Full-square identity variant','Rectangular identity','Matched PCA24 + LDA23']
    selected=[r for r in raw if r['input']=='d20_y24' and r['policy']==policy]
    title='Gabor ORL Euclidean: every one of the ten splits'
    fig,axes=one(title,'Same input, G2/P8, output 24->23; Euclidean NN and unit-column LDA. All ten splits retained.',ncols=2)
    for start,color,label in zip(starts,colors,names):
        rr=sorted([r for r in selected if r['start']==start],key=lambda r:int(r['seed']))
        axes[0].plot([int(r['seed']) for r in rr],[f(r,'accuracy_percent') for r in rr],'-o',color=color,label=label,lw=1.7,ms=4)
    axes[0].axhline(90.9,color=PAPER,ls='--',label='Paper CSA reference');axes[0].set_xticks(range(20,30));axes[0].set_ylim(80,98);axes[0].set_xlabel('Split seed');axes[0].set_ylabel('Accuracy (%)');axes[0].legend(fontsize=8,loc='lower left')
    rr=[pick(summary,input='d20_y24',start=x,policy=policy) for x in starts]
    axes[1].barh(np.arange(4),[f(r) for r in rr],xerr=[f(r,'std_pp') for r in rr],color=colors,capsize=4)
    axes[1].set_yticks(range(4),['HOSVD','Full identity','Rectangular','PCA24']);axes[1].invert_yaxis();axes[1].set_xlim(80,97);axes[1].set_xlabel('Ten-split mean +/- sample SD (%)');axes[1].axvline(90.9,color=PAPER,ls='--')
    for i,r in enumerate(rr):axes[1].text(f(r)+.2,i+.22,f'{fmt(f(r))} +/- {fmt(f(r,"std_pp"))}',fontsize=9)
    finish(fig,'orl_ten_splits',title,'Current Euclidean CSA representative: HOSVD/context87.53 +/- 2.91%; matched PCA24 85.72 +/- 2.61%. Other starts are separately labeled variants. The dashed line is the CSA paper reference. Previously explored inputs; no new parameter selection.',selected,category='Context extension')
    title='Gabor ORL Euclidean: geometry and initialization'
    fig,axes=one(title,'All nine cells: fixed sigma=pi, context, magnitude power1 and Euclidean NN.')
    ss=['rectangular_identity','hosvd','full_identity'];gg=['d20_y24','d18_y25','d22_y22']
    z=np.array([[f(pick(summary,input=g,start=start,policy=policy)) for start in ss] for g in gg])
    ax=axes[0];im=ax.imshow(z,cmap='YlOrBr',vmin=85,vmax=91,aspect='auto');ax.grid(False)
    ax.set_xticks(range(3),['Rectangular identity','HOSVD','Full-square identity']);ax.set_yticks(range(3),['Eye distance20 / y24','Eye distance18 / y25','Eye distance22 / y22'])
    for i,g in enumerate(gg):
        for j,start in enumerate(ss):
            r=pick(summary,input=g,start=start,policy=policy);ax.text(j,i,f'{fmt(f(r))}%\nSD {fmt(f(r,"std_pp"))}',ha='center',va='center',fontsize=15)
    fig.colorbar(im,ax=ax,label='Ten-split mean accuracy (%)');fig.subplots_adjust(left=.23)
    finish(fig,'orl_geometry_initialization',title,'Geometry bundles change eye distance and height together; their individual effects are not isolated. Full-square initialization begins with larger mode dimensions than the final ranks. None of these means reaches 90.9%.',summary,category='Context / start variants')


def controlled_studies():
    data=read('results/orl_controlled/summary.csv')
    title='ORL fixed factorial study: sigma by context'
    fig,axes=one(title,'Four methods, twenty predeclared splits, 320 fitted models; fixed settings within each method.',nrows=2,ncols=2)
    for ax,method in zip(axes,METHODS):
        for context,color in [('crop',BLUE),('context',ORANGE)]:
            rr=[pick(data,input=spec+'_'+context,method=method) for spec in ['2pi','pi']]
            ax.errorbar([0,1],[f(r) for r in rr],yerr=[f(r,'std_pp') for r in rr],color=color,fmt='-o',capsize=3,label=context)
            for i,r in enumerate(rr):ax.annotate(f'{fmt(f(r))}',(i,f(r)),xytext=(6,5),textcoords='offset points',fontsize=9)
        ax.set_title(NAMES[method]);ax.set_xticks([0,1],[r'$2\pi$',r'$\pi$']);ax.set_ylim(74,100);ax.set_ylabel('Accuracy (%)');ax.legend(loc='lower right',fontsize=8)
    finish(fig,'orl_sigma_context_factorial',title,'Whiskers are split SD. The effects are descriptive on repeated images. Context improves CSA24, but reducing sigma under context lowers CSA390; the settings are not jointly optimal for every method.',data,category='Fixed input extension')
    data=read('results/orl_fixed_input_extensions/comparison.csv')
    title='ORL three fixed inputs: improvements and regressions'
    fig,axes=one(title,'Ten matched splits; baseline, Tan-Triggs plus equalization, and context are tested separately.',nrows=2,ncols=2)
    for ax,method in zip(axes,METHODS):
        rr=[pick(data,variant=v,method=method) for v in ['baseline','tt_hist','crop_context']]
        ax.bar(range(3),[f(r) for r in rr],yerr=[f(r,'std_pp') for r in rr],capsize=3,color=[BLUE,PURPLE,ORANGE])
        ax.set_title(NAMES[method]);ax.set_xticks(range(3),['Baseline','TT + HE','Context']);ax.set_ylim(70,101);ax.set_ylabel('Accuracy (%)')
        for i,r in enumerate(rr):ax.text(i,f(r)+f(r,'std_pp')+.6,f'{fmt(f(r))}',ha='center',fontsize=9)
    finish(fig,'orl_three_fixed_inputs',title,'120 outer fits; all negative branches retained. Context is a field-of-view extension and TT+HE is a photometric extension. This ten-split batch differs from the twenty-split factorial study.',data,category='Fixed input extension')
    data=read('results/orl_unknown_parameters/comparison.csv')
    title='Gallery-only staged selection: most gain comes early'
    fig,axes=one(title,'Own-gallery validation; fixed original output dimensions. All ten outer splits are retained.',nrows=2,ncols=2)
    stages=['legacy_baseline','stage0_context','stage_A','stage_B','stage_C']
    for ax,method in zip(axes,METHODS):
        rr=[pick(data,stage=v,method=method) for v in stages]
        ax.errorbar(range(5),[f(r) for r in rr],yerr=[f(r,'std_pp') for r in rr],fmt='-o',color=TEAL,capsize=3)
        ax.set_title(NAMES[method]);ax.set_xticks(range(5),['Crop','Context','A: input','B: power','C: start/NN'],fontsize=8);ax.set_ylim(73,100);ax.set_ylabel('Accuracy (%)')
        for i,r in enumerate(rr):ax.annotate(f'{fmt(f(r))}',(i,f(r)),xytext=(0,11),textcoords='offset points',ha='center',fontsize=8)
    finish(fig,'orl_gallery_selection_stages',title,'Inputs include context/power extensions. CSA24 stages A->C add only about 0.03pp, and other controls can decline. Inner validation improvement does not guarantee outer improvement; this is not a blind new dataset.',data,category='Gallery-only selection')
    data=read('results/orl_ta_crop_optimized/comparison.csv')
    title='Crop-only bounded optimization: small gain, negative controls'
    fig,axes=one(title,'No context, magnitude powers, shrinkage or new ranks; ten paired splits.')
    ax=axes[0]
    for i,method in enumerate(METHODS):
        a=pick(data,method=method,stage='baseline');b=pick(data,method=method,stage='final_B')
        ax.plot([f(a),f(b)],[i,i],color='#BECBD6',lw=3);ax.scatter(f(a),i,color=PAPER,s=60);ax.scatter(f(b),i,color=ORANGE,s=70)
        ax.annotate(f'{fmt(f(a))} -> {fmt(f(b))}  ({fmt(f(b)-f(a), signed=True)} pp)',(f(b),i),xytext=(0,-20),textcoords='offset points',ha='center',fontsize=10)
    ax.set_yticks(range(4),[NAMES[x] for x in METHODS]);ax.set_ylim(3.95,-.55);ax.set_xlim(76,98);ax.set_xlabel('Mean accuracy (%)');fig.subplots_adjust(left=.22)
    finish(fig,'orl_crop_only_optimization',title,'Dark: matched baseline; orange: validation-selected final setting. CSA24 improves only 0.16pp, while CSA390 and both PCA controls decline. Do not substitute this result for the context extension.',data,category='Gallery-only selection')


def sample_selection_dater():
    rows=js('results/orl_sample_size/summary.json')+js('results/orl_sample_size/pca_control/summary.json')
    rows=[r for r in rows if r['context']=='fixed_P5']
    title='ORL sample-size extension with the same five probes'
    fig,axes=one(title,'Nested G2 subset G3 subset G5; the held-out P5 images stay fixed within each split.',ncols=2)
    for method,color,label in [('CSA24',TEAL,'CSA24 direct'),('PCA24',BLUE,'PCA24 direct'),
                                ('CSA24_LDA23',ORANGE,'CSA24 + LDA23'),('PCA24_LDA23',PURPLE,'PCA24 + LDA23')]:
        rr=[pick(rows,method=method,gallery_per_class=g) for g in [2,3,5]]
        ax=axes[0 if method.endswith('24') else 1]
        ax.errorbar([2,3,5],[f(r) for r in rr],yerr=[f(r,'std_pp') for r in rr],fmt='-o',color=color,capsize=3,label=label)
    for ax in axes:ax.set_xticks([2,3,5]);ax.set_xlabel('Gallery / fitting images per identity');ax.set_ylabel('Accuracy (%)');ax.set_ylim(68,101);ax.legend(loc='lower right')
    axes[0].set_title('Matched 24-dimensional representations');axes[1].set_title('Matched 24 -> 23 dimensional pipelines')
    finish(fig,'orl_sample_size',title,'Ten splits; sample SD whiskers. More fitting/gallery images change both representation estimation and NN coverage. G5/P5 is an extension, not the original G2/P8 experiment; no original-paper threshold is drawn.',rows,category='Sample-size extension')
    data=read('results/mnist_protocol_optimized/comparison.csv');data=[r for r in data if r['profile'] in ['baseline','selected']]
    title='MNIST bounded selection: preserve the negative result'
    fig,axes=one(title,'Ten matching splits per gallery size; PCA and CSA use their original output dimensions.',ncols=2)
    for ax,g in zip(axes,[30,40]):
        for alg,color in [('pca',BLUE),('csa',TEAL)]:
            rr=[pick(data,gallery_count=g,algorithm=alg,profile=p) for p in ['baseline','selected']]
            ax.errorbar([0,1],[f(r) for r in rr],yerr=[f(r,'std_pp') for r in rr],fmt='-o',color=color,capsize=3,label=alg.upper())
            for i,r in enumerate(rr):ax.annotate(f'{fmt(f(r))}',(i,f(r)),xytext=(7,5),textcoords='offset points',color=color,fontsize=10)
        ax.set_title(f'G{g} / P{500-g}');ax.set_xticks([0,1],['Fixed baseline','Gallery-selected']);ax.set_ylim(84,94);ax.set_ylabel('Accuracy (%)');ax.legend()
    finish(fig,'mnist_selection_negative',title,'CSA declines by 0.77pp at G30 and 0.32pp at G40. These are ten-seed paired results, not changes from the three-seed main-reference means. All failed stages remain archived.',data,category='Gallery-only selection')
    data=read('results/feret_validation_selected_v3/fixed_results.csv')
    data=[r for r in data if r['profile'] in ['cosine_control','validation_selected']]
    title='FERET: validation winners and fixed controls differ'
    fig,axes=one(title,'Do not relabel the fixed shared-cosine scores as validation-selected winners.',ncols=2)
    for ax,method in zip(axes,['PCA+LDA (Gray)','CSA-2+LDA']):
        for profile,color,label in [('cosine_control',BLUE,'Fixed shared cosine'),('validation_selected',ORANGE,'Training-identity validation winner')]:
            rr=[pick(data,q=q,method=method,profile=profile) for q in [50,100,200]]
            ax.plot([50,100,200],[f(r,'accuracy_percent') for r in rr],'-o',color=color,label=label)
        ax.set_title(method);ax.set_xticks([50,100,200]);ax.set_xlabel('Training identities q');ax.set_ylabel('Accuracy (%)');ax.set_ylim(83,98);ax.legend(loc='lower right',fontsize=8)
    finish(fig,'feret_selection_vs_fixed',title,'One fixed identity partition per q; no split SD. For q200 CSA, the fixed-cosine 95.38% is higher than the actual validation-selected 93.77%; both are retained.',data,category='Selection protocol comparison')
    data=read('results/orl_dater/summary.csv')
    title='DATER supervised tensor extension: a negative result'
    fig,axes=one(title,'Matched 2pi-crop input, twenty splits, 24D representation; ordinary LDA output23.',ncols=2)
    for ax,branch in zip(axes,['direct24','LDA23']):
        rr=[pick(data,method=m,branch=branch) for m in ['PCA24','CSA24','DATER24']]
        ax.bar(range(3),[f(r) for r in rr],yerr=[f(r,'std_pp') for r in rr],color=[BLUE,TEAL,PURPLE],capsize=4)
        for i,r in enumerate(rr):ax.text(i,f(r)+f(r,'std_pp')+.6,f'{fmt(f(r))}',ha='center',fontsize=12)
        ax.set_xticks(range(3),['PCA24','CSA24','DATER24']);ax.set_ylim(55,98);ax.set_ylabel('Accuracy (%)');ax.set_title('Direct 1-NN' if branch=='direct24' else 'After ordinary LDA23')
    finish(fig,'dater_matched_comparison',title,'DATER: 20 new models; CSA/PCA controls reused. 19/20 DATER runs hit the20-iteration cap. Strict free-trajectory failure and numerical sensitivity are recorded; this result does not establish that DATER is generally ineffective.',data,category='New-method extension')
    data=js('results/csa_lda_optimized/evaluation/summary.json')
    title='Shrinkage ablation: compare both selected and matched variants'
    fig,axes=one(title,'Ordinary and shrinkage pipelines are selected separately; alpha0 removes shrinkage from the selected winner.',ncols=2)
    rr=[]
    for ax,method in zip(axes,['CSA-2+LDA','CSA-3+LDA']):
        row=[pick(data,method=method,profile=p) for p in ['optimized_ordinary_LDA','optimized_shrinkage_LDA','shrinkage_ablation_alpha0']];rr+=row
        ax.bar(range(3),[f(r) for r in row],yerr=[f(r,'std_pp') for r in row],capsize=3,color=[TEAL,PURPLE,'#A3B0BD'])
        ax.set_xticks(range(3),['Ordinary\nselected','Shrinkage\nselected','Same winner\nalpha = 0']);ax.set_ylim(65,96);ax.set_title(method);ax.set_ylabel('Accuracy (%)')
        for i,r in enumerate(row):ax.text(i,f(r)+f(r,'std_pp')+.4,f'{fmt(f(r))}',ha='center')
    finish(fig,'shrinkage_ablation',title,'Ten splits; SD whiskers. Ranks/input settings may differ between independently selected ordinary and shrinkage pipelines. Only the same-winner alpha0 comparison isolates removal of regularization in that selected configuration.',rr,category='Regularization extension')


def diagnostics():
    data=read('results/orl_controlled/cost_benchmark.csv')
    title='Representation cost: small weights, explicitly scoped timing'
    fig,axes=one(title,'Matched CSA24/PCA24 + LDA23; local Core Ultra9 275HX, two BLAS threads.',ncols=3)
    for ax,key,scale,label in [(axes[0],'projection_weight_elements',1,'Projection weight elements'),
                              (axes[1],'runtime_arrays_bytes',1024,'Counted deployment arrays (KiB)')]:
        vals=[np.mean([f(r,key) for r in data if r['method']==m])/scale for m in ['CSA24_LDA23','PCA24_LDA23']]
        ax.bar(range(2),vals,color=[TEAL,BLUE]);ax.set_yscale('log');ax.set_xticks([0,1],['CSA','PCA']);ax.set_ylabel(label)
        for i,v in enumerate(vals):ax.text(i,v*1.15,f'{v:,.0f}',ha='center',fontsize=11)
        ax.set_ylim(min(vals)/2,max(vals)*3)
    for i,m in enumerate(['CSA24_LDA23','PCA24_LDA23']):
        v=[1000*f(r,'median_320probe_projection_LDA_NN_seconds') for r in data if r['method']==m]
        axes[2].scatter(np.full(3,i)+[-.05,0,.05],v,color=[TEAL,BLUE][i],s=65)
        axes[2].hlines(np.mean(v),i-.18,i+.18,color=PAPER,lw=2)
    axes[2].set_xticks([0,1],['CSA','PCA']);axes[2].set_ylabel('320-probe projection + LDA + NN (ms)');axes[2].set_ylim(0,100)
    finish(fig,'cost_scope',title,'Weight counts830 vs618792; arrays228272 vs5171968 bytes. Timing points are per-seed medians, not an uncertainty estimate. Excludes alignment, Gabor, training and I/O; counted arrays are not peak system memory.',data,category='Cost analysis')
    data=read('results/orl_controlled/robustness_summary.csv')
    title='Probe-eye perturbations: local robustness with no refitting'
    fig,axes=one(title,'Both eye coordinates translated together by one source-image pixel; models/gallery remain fixed.',ncols=2)
    inputs=['2pi_crop','2pi_context','pi_crop','pi_context'];shifts=['x_minus1','x_plus1','y_minus1','y_plus1']
    bound=max(abs(f(r,'mean_change_pp')) for r in data if r['method'] in ['CSA24_LDA23','PCA24_LDA23'])
    for ax,m in zip(axes,['CSA24_LDA23','PCA24_LDA23']):
        z=np.array([[f(pick(data,input=i,method=m,shift=j),'mean_change_pp') for j in shifts] for i in inputs])
        im=ax.imshow(z,vmin=-bound,vmax=bound,cmap='RdBu',aspect='auto');ax.grid(False)
        ax.set_xticks(range(4),['x - 1','x + 1','y - 1','y + 1']);ax.set_yticks(range(4),['2pi crop','2pi context','pi crop','pi context']);ax.set_title(NAMES[m])
        for (i,j),v in np.ndenumerate(z):ax.text(j,i,f'{fmt(v, signed=True)}',ha='center',va='center',color='white' if abs(v)>.65*bound else PAPER,fontsize=12)
    fig.colorbar(im,ax=list(axes),label='Mean perturbed-minus-clean accuracy (pp)',fraction=.025,pad=.04)
    finish(fig,'eye_perturbation',title,'Twenty overlapping splits. The full robustness batch has1280 scores and409600 repeated predictions, zero new fits. This does not cover single-eye errors, rotation or large offsets; no universal robustness claim.',data,category='Robustness extension')
    data=js('results/orl_controlled/historical_error_summary.json');c=data['counts']
    title='Error analysis: corrections coexist with new failures'
    fig,axes=one(title,'Different panels answer different comparisons; counts are repeated probe records, not independent photos.',ncols=2)
    axes[0].bar([0,1],[c['corrected'],c['new_error']],color=[TEAL,RED]);axes[0].set_xticks([0,1],['Old error\ncorrected','New error\nintroduced']);axes[0].set_ylabel('Repeated probe records');axes[0].set_title('Gallery-selected update versus context baseline')
    for i,v in enumerate([c['corrected'],c['new_error']]):axes[0].text(i,v+5,str(v),ha='center',fontsize=16)
    z=np.array([[c['both_correct'],c['CSA_only']],[c['PCA_only'],c['both_wrong']]])
    ax=axes[1];ax.imshow(z,cmap='Blues',vmin=0,vmax=z.max());ax.grid(False);ax.set_xticks([0,1],['PCA correct','PCA wrong']);ax.set_yticks([0,1],['CSA correct','CSA wrong']);ax.set_title('Equal-budget CSA versus PCA')
    for (i,j),v in np.ndenumerate(z):ax.text(j,i,str(v),ha='center',va='center',fontsize=20,color='white' if v>1000 else PAPER)
    finish(fig,'error_tradeoffs',title,'3200 repeated probe records cover400 distinct photos. Input update:224 corrected and111 introduced errors. Same-budget comparison: CSA-only158, PCA-only249. Examples do not establish one causal explanation.',[dict(comparison='error analysis',**c)],category='Error analysis')
    data=js('results/orl_best_search/best_results.json')['best']+js('results/orl_best_search/paper_dimension_best.json')
    recovery=read('results/orl_recovery_20261027/summary.csv');new=pick(recovery,input='d20_y24',start='hosvd',policy='unit_gallery_cosine_g0')
    data+=[dict(new,paper_target=90.9,label='Historical cosine HOSVD/context\n24 -> 23, ten splits')]
    labels=['Probe-selected CSA32 + LDA24\n200 splits','Probe-selected CSA560\n200 splits','Paper-dimension CSA390\n200 splits','Historical CSA24 + LDA23\n200 splits','Historical cosine HOSVD/context\n24 -> 23, ten splits']
    title='Selected configurations: mean versus observed maximum'
    fig,axes=one(title,'A high single run and the mean of its configuration are different quantities.')
    ax=axes[0]
    for i,r in enumerate(data):
        mean=f(r);maximum=f(r,'max_percent');sd=f(r,'std_pp')
        ax.plot([mean,maximum],[i,i],color='#CBD4DE',lw=3);ax.errorbar(mean,i,xerr=sd,fmt='o',color=BLUE,capsize=3);ax.scatter(maximum,i,marker='*',s=180,color=ORANGE,zorder=4)
        ax.text(mean-.3,i+.23,f'mean {fmt(mean)}',ha='right',fontsize=9);ax.text(maximum+.3,i,f'max {fmt(maximum)}',va='center',fontsize=9)
    ax.set_yticks(range(5),labels,fontsize=10);ax.set_ylim(4.95,-.55);ax.set_xlim(72,103);ax.set_xlabel('Accuracy (%)');fig.subplots_adjust(left=.31)
    finish(fig,'mean_vs_maximum',title,'Historical winning configurations were selected using probe scores across configurations and splits. Their means are also post-selection summaries. Different dimensions, inputs and split counts prevent a common-protocol ranking; maxima are not stable test estimates.',data,category='Exploration / selection bias')


def reconstruction_and_energy():
    data=read('results/available_reproduction_v2/orl_reconstruction.csv')
    title='ORL tensor reconstruction: error and representation storage'
    fig,axes=one(title,'Forty fitting images; 56x46x40 Gabor tensors; original RMSE definition sqrt(SSE/N).',ncols=2)
    for method,color in [('PCA',BLUE),('CSA-3',TEAL)]:
        rr=[r for r in data if r['method']==method]
        assert rr,method
        axes[0].plot([f(r,'coefficients_per_image') for r in rr],[f(r,'paper_rmse') for r in rr],'-o',ms=2.8,color=color,label=method)
        rr=sorted(rr,key=lambda r:f(r,'compression_ratio'))
        axes[1].plot([f(r,'compression_ratio') for r in rr],[f(r,'paper_rmse') for r in rr],'-',color=color,lw=2,label=method)
    axes[0].set_xscale('log');axes[0].set_xlabel('Core coefficients per image (log scale)');axes[1].set_xscale('log');axes[1].set_xlabel('Compression ratio, including bases (log scale)')
    for ax in axes:ax.set_ylabel('RMSE = sqrt(SSE / N)');ax.legend();ax.set_ylim(0,4500)
    finish(fig,'orl_reconstruction',title,'Historical Gabor/alignment version; not the new HOSVD/context recognition input. Learning-sample tensor reconstruction, not Gabor inversion or unseen-face generalization. Original absolute Gabor scale/pointwise curve values are unavailable; compare qualitative trends.',data)
    data=js('results/available_reproduction_v2/orl_convergence.json');h=data['history']
    title='CSA convergence: rapid stabilization in the recorded input'
    fig,axes=one(title,'One image per identity; ten diagnostic iterations with early stopping disabled for plotting.',ncols=2)
    for k,color in enumerate([BLUE,TEAL,ORANGE]):axes[0].plot([r['iteration'] for r in h],[r['basis_similarity'][k] for r in h],'-o',color=color,label=f'Mode {k+1}')
    axes[0].axhline(.999,color=PAPER,ls='--',label='1 - epsilon = 0.999');axes[0].set_ylim(0,1.04);axes[0].set_ylabel('Successive basis similarity');axes[0].legend(fontsize=8)
    axes[1].plot([0]+[r['iteration'] for r in h],[data['initial_sse']]+[r['sse'] for r in h],'-o',color=TEAL);axes[1].set_yscale('log');axes[1].set_ylabel('Reconstruction SSE (log scale)')
    for ax in axes:ax.set_xlabel('Iteration');ax.set_xticks(range(0,11,2))
    finish(fig,'csa_convergence',title,'This diagnostic does not replace the recognition limitTmax3. Rapid SSE/basis stabilization does not prove a global optimum or optimal classification. Exact paper ordinates and author input scaling are not recovered.',h)
    data=read('results/csa_lda_focus/representation_statistics.csv')
    data=[r for r in data if r['normalization']=='baseline' and r['kind']=='gabor' and r['model'] in ['PCA-equal-budget','CSA-paper']]
    title='Equal dimension does not imply equal retained variation'
    fig,axes=one(title,'Historical matched-input Gabor24-dimensional representations; fitting-data diagnostics.')
    ax=axes[0];keys=['total_variance_retained','between_variance_retained','within_variance_retained']
    for j,(method,color) in enumerate([('PCA-equal-budget',BLUE),('CSA-paper',TEAL)]):
        rr=[r for r in data if r['model']==method];v=[100*np.mean([f(r,k) for r in rr]) for k in keys]
        ax.bar(np.arange(3)+(j-.5)*.3,v,width=.28,color=color,label='PCA24' if j==0 else 'CSA24')
        for i,value in enumerate(v):ax.text(i+(j-.5)*.3,value+1,f'{fmt(value)}',ha='center',fontsize=11)
    ax.set_xticks(range(3),['Total variation','Between-class variation','Within-class variation']);ax.set_ylabel('Fitting projection energy retained (%)');ax.set_ylim(0,105);ax.legend()
    finish(fig,'retained_variation',title,'These are projected-energy ratios, not percentages of identity information or accuracy. PCA and CSA have different structural constraints and centering conventions. This diagnostic alone does not identify the cause of the recognition gap.',data,category='Representation diagnosis')


def curves_and_pipeline():
    data=read('results/feret_validation_selected_v3/lda_dimension_curves.csv');data=[r for r in data if r['profile']=='cosine_control']
    title='FERET main experiment: recognition versus LDA dimension'
    fig,axes=one(title,'Fixed shared-cosine controls; original pre-LDA dimensions for each training size.',ncols=3)
    for ax,q in zip(axes,[50,100,200]):
        for method,color,label in [('PCA+LDA (Gray)',BLUE,'PCA + LDA'),('CSA-2+LDA',TEAL,'CSA + LDA')]:
            rr=sorted([r for r in data if int(r['q'])==q and r['method']==method],key=lambda r:int(r['lda_dim']))
            ax.plot([int(r['lda_dim']) for r in rr],[f(r,'accuracy_percent') for r in rr],color=color,label=label)
        ax.set_title(f'q = {q}');ax.set_ylim(0,101);ax.set_xlabel('LDA dimension');ax.set_ylabel('Accuracy (%)');ax.legend(loc='lower right',fontsize=8)
    finish(fig,'feret_lda_curves',title,'One fixed identity partition. These curves are descriptive evaluations across dimensions; do not reselect the winner using the held-out curve. They correspond to our fixed control, not pointwise recovery of original Fig.6.',data)
    data=read('results/available_reproduction_v2/dimension_curves.csv');data=[r for r in data if r['profile']=='group_primary']
    title='ORL historical dimension curves: three representation settings'
    fig,axes=one(title,'Early input version and three split seeds; kept as historical recognition-curve evidence.',ncols=3)
    settings=[(['PCA+LDA (Gray)','CSA-2+LDA'],'Grayscale + LDA'),(['PCA (Gabor)','CSA-3'],'Gabor direct NN'),(['PCA+LDA (Gabor)','CSA-3+LDA'],'Gabor + LDA')]
    for ax,(methods,label) in zip(axes,settings):
        for method,color in zip(methods,[BLUE,TEAL]):
            groups=defaultdict(list)
            for r in data:
                if r['method']==method:groups[int(r['feature_dim'])].append(f(r,'accuracy_percent'))
            xs=sorted(groups);ax.plot(xs,[np.mean(groups[x]) for x in xs],color=color,label=method)
        ax.set_title(label);ax.set_ylim(0,101);ax.set_xlabel('Output features');ax.set_ylabel('Mean accuracy (%)');ax.legend(fontsize=7,loc='lower right')
    finish(fig,'orl_historical_dimension_curves',title,'Historical alignment/Gabor/classification settings differ from the current matched Euclidean protocol. Do not splice current endpoints into these early curves or label all curves as one final pipeline.',data,category='Historical main experiment')
    title='CSA pipeline and the full reproduction scope'
    fig,axes=one(title,'Group22 | ORL, MNIST and grayscale FERET; original PIE omitted with instructor permission.')
    ax=axes[0];ax.axis('off');fig.subplots_adjust(left=.055,right=.95)
    blocks=[('Inputs / preprocessing','Two-eye alignment + HE\nGabor: 5 scales x 8 orientations',BLUE),
            ('CSA representation','ORL object: 28 x 23 x 40\nCore: 4 x 2 x 3 = 24',TEAL),
            ('Ordinary Fisher LDA','80 fitting images, 40 identities\n24 <= N - Nc = 40; output23',PURPLE),
            ('Nearest neighbor','Euclidean1-NN;80 gallery /320 probe\nReport all ten observed splits',ORANGE)]
    for i,(heading,body,color) in enumerate(blocks):
        x=.015+i*.245
        ax.add_patch(FancyBboxPatch((x,.49),.22,.32,boxstyle='round,pad=0.009',facecolor='#F3F6F9',edgecolor=color,lw=2,transform=ax.transAxes))
        ax.text(x+.11,.735,heading,ha='center',va='center',fontsize=12,color=color,weight='bold',transform=ax.transAxes)
        ax.text(x+.11,.61,body,ha='center',va='center',fontsize=9.4,linespacing=1.7,transform=ax.transAxes)
        if i<3:ax.annotate('',xy=(x+.237,.65),xytext=(x+.226,.65),xycoords=ax.transAxes,arrowprops=dict(arrowstyle='->',color=PAPER,lw=2))
    ax.text(.02,.30,'Fitting/gallery only: CSA bases, HOSVD initialization, means and LDA.\nThe sample axis is never compressed. Probe images do not fit the representation.',fontsize=12,transform=ax.transAxes,color=PAPER)
    ax.text(.02,.12,'Report categories separately: shared references | gallery selections | fixed extensions\ninitialization variants | probe-selected extrema',fontsize=10,transform=ax.transAxes,color='#596776')
    finish(fig,'method_pipeline',title,'Independent implementation of the paper method within the approved scope. Current Gabor ORL representative uses Euclidean NN with HOSVD/context; full-square initialization is separate. Numerical agreement, implementation coverage and author-identical protocol are distinct claims.',[dict(scope='ORL / MNIST / grayscale FERET',ORL_core='4x2x3',LDA=23)],use='Introductory slide')


def saved_model_curves():
    """Zero new fits; expose dimension curves of the existing recovery models."""
    root=BASE/'results/orl_recovery_20261027';models=read('results/orl_recovery_20261027/models.csv')
    expected=read('results/orl_recovery_20261027/results.csv')
    selected=[r for r in models if r['input']=='d20_y24']
    features=np.load(source('results/orl_recovery_20261027/features/d20_y24.npy'),mmap_mode='r')
    splits={int(r['seed']):r for r in js('results/orl_recovery_20261027/splits.json')}
    result=[]
    with threadpool_limits(limits=2):
        for row in selected:
            path=root/row['model'];assert hashlib.sha256(path.read_bytes()).hexdigest()==row['model_sha256']
            saved=np.load(path);g=saved['gallery'];q=np.array(splits[int(row['seed'])]['probe'])
            z=np.asarray(features[q],dtype=float)
            if row['start']=='PCA24':z=(z.reshape(320,-1)-saved['mean'])@saved['basis']
            else:
                for k in range(3):
                    z=np.moveaxis(np.tensordot(z,saved[f'u{k}'].T,axes=(k+1,1)),-1,k+1)
                z=z.reshape(320,24)
            w=saved['lda_basis']/np.linalg.norm(saved['lda_basis'],axis=0)
            a=(saved['gallery_core']-saved['lda_mean'])@w;b=(z-saved['lda_mean'])@w
            for d in range(1,24):
                distances=cdist(b[:,:d],a[:,:d],metric='euclidean');neighbor=distances.argmin(1)
                labels=(g[neighbor]//10)+1;truth=(q//10)+1
                score=100*float(np.mean(labels==truth))
                result.append(dict(seed=int(row['seed']),start=row['start'],lda_dimension=d,metric='euclidean',accuracy_percent=score,extra_fits=0))
                if d==23:
                    reference=pick(expected,input='d20_y24',seed=row['seed'],start=row['start'],policy='unit_gallery_euclidean_g0')
                    assert abs(score-f(reference,'accuracy_percent'))<1e-10
    path=OUT/'derived_lda_curves.csv';write_table(path,result)
    title='ORL current input: LDA dimension curves from saved models'
    fig,axes=one(title,'Zero new fits. Ten existing splits20-29; d20/y24, pi-context, 24D core, Euclidean1-NN with unit-column LDA.')
    for start,color,label in [('hosvd',ORANGE,'CSA24 HOSVD (representative)'),('full_identity',PURPLE,'CSA24 full identity variant'),('rectangular_identity',TEAL,'CSA24 rectangular identity'),('PCA24',BLUE,'Matched PCA24')]:
        rr=[r for r in result if r['start']==start];dims=range(1,24)
        means=[np.mean([r['accuracy_percent'] for r in rr if r['lda_dimension']==d]) for d in dims]
        axes[0].plot(list(dims),means,label=label,color=color,lw=2)
    axes[0].axvline(23,color=PAPER,ls=':',label='Reported LDA dimension23');axes[0].set_xlabel('Number of retained LDA directions');axes[0].set_ylabel('Ten-split mean accuracy (%)');axes[0].set_ylim(0,101);axes[0].legend(loc='lower right')
    finish(fig,'orl_current_lda_curves',title,'Descriptive scoring of saved directions1-23; no re-fitting or new parameter selection. Every23D endpoint matches the archived results. The fixed23D representative is retained even if a different curve point happens to score higher. Already-observed probes, context extension.',result,category='Zero-fit supplementary analysis')


def write_table(path, rows):
    fields=list(dict.fromkeys(k for row in rows for k in row))
    with path.open('w',newline='',encoding='utf-8') as handle:
        w=csv.DictWriter(handle,fieldnames=fields);w.writeheader();w.writerows(rows)


def metric_comparison():
    data=read('results/orl_euclidean_20261104/summary.csv')
    title='ORL: metric choice changes the method ranking'
    fig,axes=one(title,'Same inputs, ten splits, fixed dimensions and unit-column LDA. Only the NN distance changes.',ncols=2)
    groups=[('Grayscale: d15/y24',[('gray_CSA22_LDA16','CSA22 + LDA16'),('gray_PCA30_LDA18','PCA30 + LDA18'),('gray_PCA22_LDA16','PCA22 + LDA16')]),
            ('Gabor: d20/y24 pi-context',[('gabor_CSA24_LDA23','CSA24 + LDA23'),('gabor_PCA33_LDA25','PCA33 + LDA25'),('gabor_PCA24_LDA23','PCA24 + LDA23')])]
    selected=[]
    for ax,(heading,methods) in zip(axes,groups):
        ax.set_title(heading)
        for i,(id,label) in enumerate(methods):
            e=pick(data,id=id,metric='euclidean');c=pick(data,id=id,metric='cosine');selected.extend([e,c])
            ax.plot([f(e),f(c)],[i,i],color='#CAD3DC',lw=3)
            for r,color,marker,offset in [(e,ORANGE,'o',-.1),(c,BLUE,'D',.1)]:
                ax.errorbar(f(r),i+offset,xerr=f(r,'std_pp'),fmt=marker,color=color,capsize=3)
                ax.annotate(fmt(f(r)),(f(r),i+offset),xytext=(0,9 if offset<0 else -17),textcoords='offset points',ha='center',color=color,fontsize=10)
        ax.set_yticks(range(3),[label for _,label in methods]);ax.invert_yaxis();ax.set_ylim(2.6,-.6)
        ax.set_xlim(70,99);ax.set_xlabel('Ten-split accuracy (%)');ax.grid(axis='y',visible=False);ax.grid(axis='x',color='#E5EAF0')
    axes[0].plot([],[],'o',color=ORANGE,label='Current Euclidean');axes[0].plot([],[],'D',color=BLUE,label='Historical cosine control')
    axes[0].legend(loc='lower right');fig.subplots_adjust(left=.18,wspace=.55)
    finish(fig,'orl_metric_comparison',title,'CSA exceeds PCA30 in the gray Euclidean comparison and PCA24 in the Gabor equal-budget Euclidean comparison, but remains below Gabor PCA33. Cosine favors PCA more strongly. These metric controls share current inputs; they differ from earlier mixed-input published headline tables. Previously observed probes; no general superiority claim.',selected,category='Matched metric sensitivity')


def main():
    for folder in ['png','svg']:(OUT/folder).mkdir(parents=True,exist_ok=True)
    PDF.parent.mkdir(parents=True,exist_ok=True)
    main_comparisons();recovery();controlled_studies();sample_selection_dater()
    diagnostics();reconstruction_and_energy();curves_and_pipeline();saved_model_curves();metric_comparison()
    with PdfPages(PDF,metadata={'Title':'CSA full reproduction: figure atlas','Author':'HKU COMP3314 Group22','Subject':'Recorded results, scope labels and limitations'}) as atlas:
        for fig in FIGURES:atlas.savefig(fig)
    for fig in FIGURES:plt.close(fig)
    write_table(OUT/'figure_catalog.csv',ITEMS);write_table(OUT/'plot_data.csv',DATAPOINTS)
    manifest=dict(created='2026-11-04',figure_count=len(ITEMS),project_classification='Full reproduction within the instructor-approved three-dataset scope',
        generator_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),source_sha256=SOURCE_HASHES,
        provenance='All figures use saved evidence. The last curve panel newly scores saved models, zero new fits; endpoints independently match archived23D scores.',
        paper_values='Recorded Tables I/II/IV references; author split aggregation unknown.',
        current_ORL='Matched Euclidean: gray CSA11x2+LDA16:81.72+/-2.06; Gabor HOSVD/context CSA24+LDA23:87.53+/-2.91; matched PCA controls use identical inputs/splits/metric',
        historical_edition='results/report_figures_20261027 and report_figures_20261030 remain unchanged historical editions.',
        statistics='Sample SD across specified splits, not CI. FERET uses one fixed identity split. Repeated predictions are not independent photos.',
        excluded='No face images, dataset labels/arrays, model caches or private letters included.',
        atlas=PDF.relative_to(BASE).as_posix(),figures=ITEMS)
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    snippets=['% Vector PDF atlas: choose a page, or use the per-figure SVG/PNG exports.']
    for item in ITEMS:
        snippets+=['',f'% Figure {item["number"]}: {item["title"]}',r'\begin{figure}[t]',r'\centering',
                   r'\includegraphics[page='+str(item['number'])+r',width=\linewidth]{'+PDF.name+'}',
                   r'\caption{'+item['caption'].replace('%',r'\%').replace('_',r'\_').replace('&',r'\&')+'}',
                   r'\label{fig:'+item['slug']+'}',r'\end{figure}']
    (OUT/'latex_figures.tex').write_text('\n'.join(snippets)+'\n',encoding='utf-8')
    package=OUT/f'CSA_report_slide_figures_{DATE_STAMP}.zip'
    with zipfile.ZipFile(package,'w',compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(PDF,PDF.name)
        for path in sorted(OUT.rglob('*')):
            if path.is_file() and path!=package:archive.write(path,path.relative_to(OUT).as_posix())
    print(json.dumps(dict(figures=len(ITEMS),atlas=str(PDF),package=str(package)),indent=2))


if __name__=='__main__':
    main()
