# Concurrent Subspaces Analysis: Reproduction and Critical Analysis

HKU COMP3314 group project from Group 22. We independently implement Concurrent Subspaces Analysis (CSA), compare it with PCA and Fisher LDA, and investigate the limits of reproducing a historical tensor representation method.

**Scope: full reproduction on ORL, MNIST, and original grayscale FERET.** The original CMU PIE experiments are omitted with the instructor's permission because we could not obtain the dataset. We do not claim to recover every numerical result or every unspecified setting of the paper.

## Paper

Dong Xu, Shuicheng Yan, Lei Zhang, Stephen Lin, Hong-Jiang Zhang, and Thomas S. Huang. **Reconstruction and Recognition of Tensor-Based Objects With Concurrent Subspaces Analysis.** *IEEE Transactions on Circuits and Systems for Video Technology*, 18(1), 36–47, January 2008. [DOI: 10.1109/TCSVT.2007.903317](https://doi.org/10.1109/TCSVT.2007.903317).

CSA preserves an object's row, column, and channel modes instead of flattening it before dimensionality reduction. It alternately learns orthonormal mode bases to minimize reconstruction error. Recognition uses the flattened core tensor with nearest-neighbor classification, optionally after LDA. Reconstruction and classification optimize different objectives; improved reconstruction does not guarantee better recognition.

## Start here

| File | Purpose |
|---|---|
| [TEAM_BRIEF.md](docs/TEAM_BRIEF.md) | English teammate guide: paper study, implementation, all experiment families, comparisons, critical analysis, and report/presentation preparation |
| [DETAIL.md](DETAIL.md) | Previous detailed README, now translated into English |
| [REPORT.md](docs/REPORT.md) | Detailed experiment evidence, protocols, discrepancies, and commands; now in English |
| [HANDOFF.md](docs/HANDOFF.md) | Project provenance, instructor/TA correspondence, current status, and decisions; now in English |
| [Publication manifest](docs/publication_manifest.json) | Language exceptions, immutable source hashes, translation checks, and exclusion rules |
| [HISTORY.md](docs/HISTORY.md) | English historical archive; statements describe the status at their original dates |
| [FERET/README.md](FERET/README.md) | Authorized data acquisition, official pairing, eye-coordinate conventions, and redistribution exclusions |

The coursework emphasizes **paper understanding and critical analysis**, with reproduction as an optional bonus. The guide maps the problem, motivation, contributions, course concepts, original evidence, assumptions, limitations, and our findings to these requirements. This repository supplies experimental material; the final 3–4-page LaTeX report and 9-minute presentation with 3-minute Q&A remain separate deliverables.

## Environment

Python 3.11 is used for the recorded runs; the latest DATER run records Python 3.11.9. Install the pinned scientific dependencies in your own environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install --no-deps --target .deps -r requirements-preprocess.txt
```

The last command installs the OpenCV preprocessing dependency locally. NumPy/SciPy perform array operations, eigendecomposition, FFT, and distances; Pillow/OpenCV handle images, warps, and detection; Matplotlib produces figures; threadpoolctl controls BLAS threads. Dataset and feature preparation can take substantially more storage than the source repository.

## Data and preprocessing

| Dataset | Experimental subset and split | Representation | Availability |
|---|---|---|---|
| ORL / AT&T | 400 images, 40 identities; 2 gallery and 8 probe images per identity | Aligned/equalized 56×46 grayscale; recognition Gabor 28×23×40 | Public source: [Cambridge archive](https://www.cl.cam.ac.uk/research/dtg/attarchive/pub/data/att_faces.zip) |
| MNIST | Official test set; first 500 images of each digit, 5,000 total; G30/P470 and G40/P460 | 28×28×40 Gabor magnitudes | Public source; exact local selection and hashes are recorded |
| Grayscale FERET | Official 1,195 Fa/Fb pairs; first 50/100/200 identities train, remaining Fa gallery / Fb probe | Aligned/equalized 41×27 grayscale | Obtain authorized access from [NIST](https://www.nist.gov/itl/products-and-services/color-feret-database); raw data are excluded |
| CMU PIE | Not run | Original paper's requested subsets | Omitted with instructor permission; no substitute is presented as original PIE |

The group chose eye targets, interpolation, Gabor parameters, numerical scaling, and distance rules where the original records were unavailable. The paper and TA specify nearest-neighbor recognition, but do not confirm a recoverable Euclidean-versus-cosine rule. The paper's CSA stopping tolerance is ε=0.001; recognition uses Tmax=3. Ordinary LDA obeys the pre-reduction budget p≤N−Nc.

**None of the three datasets is distributed in this repository.** Raw images, labels, prepared data, generated `.npy`/`.npz` feature/model/embedding caches, and image-bearing data examples remain local. Installed dependencies, temporary files, and private access-request correspondence are also excluded. The acquisition/reconstruction instructions, source scripts, protocols, split indices, score tables, numerical histories, and verification reports are retained. Full cache-based verification requires obtaining the data and regenerating omitted files; this checkout is not an exact byte-for-byte backup of the local experiment workspace.

### Obtain and reconstruct the inputs

Download ORL to `data/raw/orl/` and extract the archive so that `s1/1.pgm` through `s40/10.pgm` are directly below that directory. Download the official MNIST **test** files to `data/raw/mnist/`:

| File | Source | Recorded checksum |
|---|---|---|
| `att_faces.zip` | [Cambridge ORL archive](https://www.cl.cam.ac.uk/research/dtg/attarchive/pub/data/att_faces.zip) | SHA-256 `509d763bd2276aa054d260d7f1000e8be212738134f2f83d8ff13bc2adf1c8ec` |
| `t10k-images-idx3-ubyte.gz` | [MNIST test images](https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz) | MD5 `9fb629c4189551a2d022fa330f9573f3` |
| `t10k-labels-idx1-ubyte.gz` | [MNIST test labels](https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz) | MD5 `ec29112dd5afa0611ce80d1b7f02629c` |

Gunzip the two MNIST files to the same names **without `.gz`**; `prepare_available_data.py` reads the uncompressed IDX files, validates the 5,000-image balanced selection, and creates aligned images, labels, and indices under `data/processed/available/`. It regenerates automatic Haar eye candidates when local annotations are absent; historical manual corrections and later YuNet protocols are separate stages, so this step alone does not recreate every later ORL input. `run_available_reproduction.py` generates its Gabor caches from the prepared inputs.

Example acquisition commands on Windows, after checking the provider's usage terms:

```powershell
New-Item -ItemType Directory -Force data/raw/orl, data/raw/mnist | Out-Null
Invoke-WebRequest https://www.cl.cam.ac.uk/research/dtg/attarchive/pub/data/att_faces.zip -OutFile data/raw/orl/att_faces.zip
Expand-Archive -LiteralPath data/raw/orl/att_faces.zip -DestinationPath data/raw/orl
Invoke-WebRequest https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz -OutFile data/raw/mnist/t10k-images-idx3-ubyte.gz
Invoke-WebRequest https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz -OutFile data/raw/mnist/t10k-labels-idx1-ubyte.gz
python -c "import gzip,pathlib; d=pathlib.Path('data/raw/mnist'); [(p.with_suffix('').write_bytes(gzip.decompress(p.read_bytes()))) for p in d.glob('t10k-*.gz')]"
```

These commands download only the public ORL/MNIST inputs. Verify the table's checksums before preparation. The [download manifest](data/dataset_manifest.json) records the historical acquisition; its early experiment/FERET-availability status is superseded by the current results.

For FERET, obtain NIST authorization first, then run `python FERET/download_subset.py candidates`. The downloader prompts for credentials, reconstructs the permitted grayscale subset and official Fa/Fb pairing metadata, and checks byte ranges, archive version, and local hashes. Run `python prepare_feret.py` afterward. The downloader is tied to the recorded archive size/ETag and intentionally stops if the server archive changes; do not bypass that check. All downloaded files stay excluded from Git.

For the report-ready coverage, missing experiments, complete shared comparison, and extension categories, read [TEAM_BRIEF§0](docs/TEAM_BRIEF.md#reproduction-status). The latest [ORL recovery study](docs/REPORT.md#orl-recovery-20261027) preserves all historical result categories.

## Reproduction results

**Current ORL protocol,2026-11-04:** All six ORL rows use Euclidean1-NN and the same ten seeds20-29 (G2/P8). All grayscale methods share one frozen56x46 input; all Gabor methods share one frozen28x23x40 input. LDA columns are unit length. The paper/TA specify NN without confirming this metric; Euclidean is our declared convention. Full settings and historical cosine controls appear below the table.

These results retain the paper's output dimensions. +/- denotes sample SD across the stated splits; FERET has one fixed identity partition. MNIST and FERET retain their recorded internally shared protocols. Paper values are best-configuration results with unspecified repetition/aggregation, so differences are descriptive rather than proof of author-identical settings or statistical significance.

| Dataset / splits | Method | Our result | Paper | Difference, pp |
|---|---|---:|---:|---:|
| ORL / 10 | Grayscale PCA30 + LDA18 | 77.22±2.35 | 82.20 | −4.98 |
| ORL / 10 | Grayscale CSA11×2 + LDA16 | **81.72±2.06** | 84.10 | −2.38 |
| ORL / 10 | Gabor PCA76 | 86.91±1.60 | 86.60 | +0.31 |
| ORL / 10 | Gabor CSA390 | 89.66±1.92 | 94.40 | −4.74 |
| ORL / 10 | Gabor PCA33 + LDA25 | 88.41±1.96 | 87.20 | +1.21 |
| ORL / 10 | Gabor CSA24 + LDA23 (HOSVD start; context extension) | **87.53±2.91** | 90.90 | −3.37 |
| MNIST G30 / 3 | PCA60 | 87.52±0.40 | 88.50 | −0.98 |
| MNIST G30 / 3 | CSA810 | 90.34±0.15 | 92.80 | −2.46 |
| MNIST G40 / 3 | PCA50 | 88.58±0.37 | 90.50 | −1.92 |
| MNIST G40 / 3 | CSA975 | 91.04±0.25 | 92.40 | −1.36 |
| FERET q50 / one identity split | PCA45 + LDA25 | 89.08 | 84.60 | +4.48 |
| FERET q50 / one identity split | CSA10×4 + LDA35 | 88.73 | 88.20 | +0.53 |
| FERET q100 / one identity split | PCA95 + LDA40 | 90.87 | 90.60 | +0.27 |
| FERET q100 / one identity split | CSA11×5 + LDA44 | 94.25 | 92.20 | +2.05 |
| FERET q200 / one identity split | PCA112 + LDA69 | 93.87 | 93.40 | +0.47 |
| FERET q200 / one identity split | CSA13×7 + LDA62 | 95.38 | 95.20 | +0.18 |

Sources: [matched ORL Euclidean comparison](results/orl_euclidean_20261104/comparison.csv), [per-split scores](results/orl_euclidean_20261104/results.csv), [verification](results/orl_euclidean_20261104/verification.json); [shared comparison CSV](results/orl_protocol_audit/shared_comparison.csv) for MNIST/FERET. FERET remains the fixed shared cosine control, not validation-selected winners.

**Shared ORL settings:** Gray uses existing YuNet eyes, target eye distance15/y24, linear/replicate alignment and PIL equalization. Gabor uses the existing d20/y24 pi-context features; all four Gabor headline methods use that identical array. CSA24 uses HOSVD, CSA390/gray use rectangular identity; CSA remains uncentered/Tmax3, PCA is centered, and LDA is ordinary/unregularized with unit-length columns. Inputs were previously explored on probes; this is a transparent protocol change, not a new blind test or a recovered author metric. Thirty missing Gabor control fits were added and fifty models reused; there is no new parameter search.

**Matched advantages:** Gray CSA22->16 exceeds PCA30->18 by4.50pp and equal-budget PCA22->16 (77.13% +/- 2.89%) by4.59pp. Gabor CSA24->23 exceeds equal-budget PCA24->23 (85.72% +/- 2.61%) by1.81pp, but is0.88pp below paper-dimension PCA33->25. Do not claim that every CSA+LDA comparison beats PCA.

### Historical cosine comparisons

The former published headline mixed earlier reference inputs; the matched cosine column below instead applies cosine to the same current inputs/models/splits. Neither is the current Euclidean result.

| ORL method | Former published headline, % | Cosine on current matched inputs, % |
|---|---:|---:|
| Grayscale PCA30 + LDA18 | 83.22±1.76 | 83.50±2.29 |
| Grayscale CSA11×2 + LDA16 | 81.84±1.96 | 81.84±1.96 |
| Gabor PCA76 | 86.88±1.63 | 89.59±1.42 |
| Gabor CSA390 | 90.19±2.37 | 91.09±1.35 |
| Gabor PCA33 + LDA25 | 92.09±2.06 | 94.19±0.96 |
| Gabor CSA24 + LDA23 (HOSVD start; context extension) | 88.75±2.89 | 88.75±2.89 |

Historical sources: [20261030 figure edition](results/report_figures_20261030/CSA_report_slide_figures_20261030.zip), original recovery tables, and [matched cosine scores](results/orl_euclidean_20261104/matched_cosine_history.csv). Historical evidence remains unchanged.

### Controlled studies and extensions

| Study | Main result | Interpretation |
|---|---|---|
| Historical cosine grayscale follow-up, ten splits | CSA11x2 -> ordinary LDA16: **81.84 +/- 1.96**; historical shared reference77.47 | 960 CSA/PCA models verified; full design and comparison in REPORT |
| Historical cosine ORL initialization variant, 10 splits | CSA24→23: 88.81±2.97 with full-square identity initialization | Context extension and larger initial mode dimensions than the final ranks; exploratory comparison, not author-confirmed |
| ORL crop-only, gallery-selected unknown settings, 10 splits | CSA24→23: 81.25→81.41±2.41 | Only +0.16pp; does not recover 90.9% |
| ORL context/input selection extension, 10 splits | CSA24→23: 87.84±3.28 | Context and optional magnitude powers are extensions; not the original shared reference |
| ORL fixed σ×context, 20 predeclared splits | CSA24→23: 80.13±3.49 for 2π crop; 87.08±2.30 for π context | Paired +6.95pp; equal-output-budget PCA24→23 is still higher at 91.08±1.48 |
| MNIST bounded gallery-only optimization, 10 matching splits | CSA G30: 89.66→88.89; G40: 90.50→90.18 | Selection did not improve CSA; negative results retained |
| ORL fixed-probe sample-size extension | CSA24 + ordinary LDA: 81.30 / 88.10 / 94.50 for G2/G3/G5 with P5 | More fitting/gallery samples help; G5/P5 is not the original G2/P8 experiment |
| ORL shrinkage and rank extensions | Refined ordinary CSA+LDA 83.28±3.30; shrinkage 85.47±4.57 | Changed ranks/regularization, separately reported |
| DATER supervised tensor extension, 20 matching splits | Direct24: 71.64±3.18; +LDA23: 67.11±3.59 | Lower than matched CSA/PCA; 19/20 runs reach the 20-iteration cap |
| Probe-selected exploration | Maximum 95.00 for CSA32+LDA24; 97.50 for CSA560 | Parameters and splits were selected using probe scores; not independent test estimates or stable means |
| Cost and small eye-point perturbations | 830 vs 618,792 projection weights for CSA/PCA24→23; π-context CSA average −0.08pp under joint ±1-pixel shifts | Cost scope and perturbation range are limited; no universal efficiency/robustness claim |

See [all experiments and limitations](docs/TEAM_BRIEF.md), [controlled statistics](results/orl_controlled/summary.csv), [DATER statistics](results/orl_dater/summary.csv), and [MNIST comparison](results/mnist_protocol_optimized/comparison.csv). Repeated predictions reuse the same images and are not independent new samples.

## Report and slide figures

[Download the complete figure pack](results/report_figures_20261104/CSA_report_slide_figures_20261104.zip) or open the [28-page vector PDF atlas](output/pdf/CSA_figure_atlas_20261104.pdf). The28 English figures cover all16 paper-corresponding recognition cases, per-dataset comparisons, reconstruction/convergence and dimension curves, plus controlled studies and extensions. Each has a high-resolution PNG, editable SVG, caption, and traceable source data.

Use the [numbered catalogue and presentation guidance](docs/TEAM_BRIEF.md#figure-pack), [CSV source/caption index](results/report_figures_20261104/figure_catalog.csv), or [LaTeX snippets](results/report_figures_20261104/latex_figures.tex). The current ORL HOSVD/context representative and full-square initialization variant remain separately labeled. These exports contain charts only; datasets, face images and model caches remain excluded. The last dimension-curve panel scores saved models without new fitting and verifies the23D endpoints against recorded results.

The2026-11-04 edition uses matched Euclidean inputs/splits/metric for all six ORL rows; Figure28 compares matched Euclidean and cosine scores. The [2026-10-27 figure pack](results/report_figures_20261027/CSA_report_slide_figures_20261027.zip) remains an unchanged historical archive.


Historical cosine edition: [20261030 figure archive](results/report_figures_20261030/CSA_report_slide_figures_20261030.zip).

## Run and verify

Run commands from the repository root. Use **new output directories** for reruns; prepare the required data first. Some later runners also reuse earlier aligned images and source models, so they are not stand-alone download-and-run entry points. Full stage sequences and dependencies are documented in [TEAM_BRIEF](docs/TEAM_BRIEF.md#verification) and [REPORT](docs/REPORT.md#outputs).

```powershell
# Dataset-independent mathematical checks
python -c "from check_numerics import check; check()"

# Initial ORL/MNIST preprocessing and recorded baseline pipeline
python prepare_available_data.py
# Fresh checkout: establish the generated annotation file expected by the baseline verifier.
New-Item -ItemType Directory -Force data/annotations | Out-Null
Copy-Item data/processed/available/orl_eye_coordinates.csv data/annotations/orl_eye_coordinates.csv
python run_available_reproduction.py --output results/available_rerun
python verify_available_results.py --output results/available_rerun

# FERET, after authorized acquisition and official pairing preparation
python prepare_feret.py
python select_feret.py --output results/feret_rerun
python verify_feret.py --output results/feret_rerun
```

The baseline commands use freshly generated Haar annotations and therefore need not recreate later manual/YuNet scores. Later ORL drivers contain fixed dependencies on historical directories, input hashes, models, and verification files. Simply supplying a new `--output` does not redirect those dependencies. Reconstruct the preceding stages described in the guides before using them; cache-bound verifiers intentionally fail when required files are missing or hashes differ. The public checkout preserves the methods and recorded evidence, rather than promising a one-command byte-identical restoration of every archived run.

The archived numerical checks cover tensor axes/unfolding, independent CSA updates, PCA equivalence, Fisher equations, complex convolution, NN predictions, reconstruction/CR definitions, and selection/split integrity. A successful process exit alone is not treated as validation.

### DATER rerun

First regenerate the required ORL controlled inputs and CSA/PCA controls. Use the supplementary verifier and scoring adapter below: the original driver's `verify_models` and `evaluate` routes have recorded failures.

```powershell
python run_orl_dater.py --stage prepare --output results/orl_dater_rerun
python run_orl_dater.py --stage fit --output results/orl_dater_rerun
python verify_orl_dater.py --output results/orl_dater_rerun
python evaluate_orl_dater.py --output results/orl_dater_rerun
python run_orl_dater.py --stage verify --output results/orl_dater_rerun
python run_orl_dater.py --stage analyze --output results/orl_dater_rerun
```

Initial strict free-trajectory verification and the first scoring-reader failure are preserved. Exact saved-trajectory checks pass; free-reference final directions differ by up to approximately 1.01e−5. We do not claim all trajectories or probe predictions are numerically identical. See [DATER evidence](results/orl_dater/).

## Original implementation and reused components

Our group implements CSA, PCA, ordinary/shrinkage LDA, complex Gabor filtering, DATER, preprocessing, experiment selection, independent checks, and analysis scripts. The teaching team could not provide the original CSA code or hyperparameter records. This is an independent implementation, not the authors' official repository.

Scientific/image libraries, BLAS/LAPACK, the YuNet/Haar detectors, and pretrained detection assets are reused components rather than group-created algorithms. Consult [the YuNet license](data/preprocessing_models/YuNet_LICENSE), dependency licenses, and the data-provider terms. The repository does not grant redistribution rights over FERET or third-party papers. Retained source snapshots and hash-bound experiment files remain in their original language to preserve provenance; the current English guides explain them. All seven public Markdown documents are English following the2026-10-27 update; hash-bound source/protocol evidence retains its original language.

References: [CSA, Xu et al. 2008](https://doi.org/10.1109/TCSVT.2007.903317); [Gabor representation background, Wiskott et al. 1997](https://cenl.ucsd.edu/pubs/ieee-1997.pdf); [DATER, Yan et al. CVPR 2005](https://mmlab.ie.cuhk.edu.hk/archive/2005/01467312.pdf). Our TT-plus-equalization and manual covariance-shrinkage experiments are disclosed as extensions; the shrinkage grid is not an automatic Ledoit–Wolf estimator.

## Limitations and submission status

ORL has not recovered the paper's low-dimensional CSA advantage. Unknown eye/crop/filter/distance settings and best-versus-mean reporting limit exact matching. Historical probes have already been observed; later selection procedures are not new blind tests. Context changes the effective field of view, regularization changes LDA, and DATER changes the method. Negative outcomes and all result categories are retained.

This repository presents our full reproduction within the instructor-approved three-dataset scope, together with paper study and critical analysis. Full reproduction describes the experimental scope; it does not imply author-identical code, exact numerical agreement, a guaranteed mark/bonus, or completed final report/presentation deliverables.
