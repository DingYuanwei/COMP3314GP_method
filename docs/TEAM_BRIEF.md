# CSA Project: Team Handover, Report and Presentation Materials

> **ORL distance decision,2026-11-04:** The user adopts Euclidean NN as the default for subsequent ORL comparisons, shared by CSA/PCA with unit-length LDA columns. At the existing current inputs, gray CSA/PCA30 means are81.72%/77.22%, and Gabor CSA24/PCA24 means are87.53%/85.72%. These recorded scores are exploratory, not new tests. The dated cosine representatives81.84%/88.75% retain their labels. See [full default convention and sources](./REPORT.md#orl-distance-default-20261104).

Updated: 2026-10-30. This guide consolidates completed work; it does not launch new experiments. Its sources are the original papers, user-provided instructor/TA/data-author correspondence, current code, recorded protocols, and original result files.

**Conclusion: we independently implemented CSA and completed full reproduction on ORL, MNIST, and original grayscale FERET within the instructor-approved scope, and completed input, selection, sample-size, regularization, supervised tensor reduction, robustness, and cost studies.** Numerical and prediction checks support the implementation, but we have not recovered every CSA paper result or method ordering. PIE is omitted with instructor permission. The evidence supports a substantial paper study and full reproduction within that approved scope; the instructor determines grades and bonus credit.

This is a working material library for teammates, rather than the final 3–4-page report. The main text follows research questions; collapsible appendices contain historical batches and complete result entries. **Data are presented at two levels:** every experiment family, summary, before/after comparison, and paper comparison appears here; per-candidate, per-split, prediction, model, and failure records are indexed in existing CSV/JSON/NPZ files. Millions of records are not copied into Markdown. An SD or individual score omitted from one summary remains available in its linked original table.

> **Public repository edition:** All three datasets, numeric caches, and image-bearing sample/reconstruction figures remain local. Some historical links therefore require data acquisition and reconstruction. English text was translated and checked against the original Chinese guide; immutable source/protocol snapshots retain their original bytes and may contain Chinese. The earlier Chinese-document exception was superseded by the 2026-10-27 request for English versions.

<a id="reproduction-status"></a>

## 0. Report-ready reproduction status (updated 2026-10-30)

**Defensible conclusion:** We independently implemented the CSA method and completed full reproduction within the instructor-approved ORL, MNIST, and original grayscale FERET scope. We did not obtain the authors' original implementation or complete hyperparameter records. Algorithm implementation, experiment coverage, numerical agreement, and recovery of the paper's method ranking are separate claims.

**Terminology:** Full reproduction refers to the instructor-approved three-dataset experimental scope. PIE is omitted with permission; implementation choices, numerical gaps, extensions, and exploratory selection remain explicitly disclosed.

**New gray follow-up,2026-10-30:** The best tested global configuration at CSA11x2 -> ordinary LDA16 is **81.84% +/- 1.96%** over the same ten seeds20-29, versus historical shared77.47% +/- 5.41% and paper84.10%. Mean change+4.38pp, nine splits improve and one declines; the remaining paper gap is2.26pp. The winner uses fixed target eyes(15.5,24)/(30.5,24), YuNet eyes, linear warp/replicate boundary,56x46/PIL equalization, uncentered rectangular identity/Tmax3, unit-length LDA columns and gallery-centered cosine1-NN. HOSVD ties at exactly the same per-split correct counts. Matched PCA30->18 is83.50% +/- 2.29%; equal-budget PCA22->16 is81.44% +/- 2.24%. CSA exceeds the equal-budget control by0.41pp but not paper-dimension PCA. No significance claim is made.

The initial12 input bundles/four CSA variants/six NN policies were followed by one six-geometry crop neighborhood chosen after seeing initial probes. All960 models (600 CSA,360 PCA),5760 scores and1,843,200 repeated predictions are checked; each batch completed fitting before its own new probe scoring. Both verifications pass and historical evidence is unchanged. This is an **exploratory parameter winner on observed probes**, not a new blind estimate, gallery-only winner, proven global optimum, or recovered author setting. Counts, G2/P8,11x2->ordinary16 andTmax3 remain fixed; crop targets, initialization, centering and NN conventions are disclosed unknown-setting choices. No new rank, shrinkage or training sample is used.

Keep three gray categories separate: **77.47% historical shared reference**, **81.84% current original-dimension representative**, and **84.13% +/- 2.38% earlier shrinkage/rank/dimension extension**. The combined pool single maximum is**85.9375% (275/320)** atd14/y24, identity, unit-column Euclidean, seed22; it is not the81.84% mean winner. The current20261030 figure edition uses81.84% in the headline comparisons; the20261027 edition is retained as history. See [complete design, before/after and TA limits](./REPORT.md#orl-gray-recovery-20261030), [final analysis](../results/orl_gray_recovery_20261030/final_analysis.json), [all576 configuration summaries](../results/orl_gray_recovery_20261030/combined_summary.csv), and [ten paired scores](../results/orl_gray_recovery_20261030/final_paired_comparison.csv).

### 0.1 What has been reproduced

| Component | Completed work | Evidence boundary |
|---|---|---|
| CSA algorithm | General tensor mode products, sequential orthonormal covariance updates, core encoding and reconstruction | Independent formula/covariance checks support our implementation, not identity with unpublished author code |
| Comparators and recognition | Independently implemented vector PCA, ordinary Fisher LDA, and nearest-neighbor classification | Numerical libraries supply primitive operations; unknown author metric/normalization is not inferred |
| Input pipeline | Eye alignment, histogram equalization, stated image sizes, five-scale/eight-orientation complex Gabor magnitudes | Our eye targets, padding, filter support, and other missing details remain disclosed group choices |
| ORL recognition | Six paper-dimension cases; 400 images, G2/P8, ten splits | CSA numerical levels and its low-dimensional advantage over PCA are not recovered |
| MNIST recognition | Four cases: PCA/CSA at G30/P470 and G40/P460, 500 images per digit | CSA>PCA direction reproduced; absolute CSA results remain below the paper |
| FERET recognition | Six cases at q50/q100/q200, official Fa/Fb pairs | Fixed shared-cosine scores are close, but are not validation-selected winners or evidence that all method rankings match |
| Reconstruction/compression | Forty ORL fitting images, Gabor tensors, PCA/CSA dimension and storage-budget scans | Qualitative evidence; no author pointwise data or confirmed Gabor amplitude scale |
| Iterations and checks | Convergence curves, 3-to-10-iteration diagnostics, split/NN/FFT/Fisher/hash checks | Internal consistency and limited-setting convergence, not a universal optimum or author-protocol proof |

**Recognition coverage: 16 paper-corresponding cases = six ORL + four MNIST + six FERET. Coverage does not mean all 16 values match.**

### 0.2 What remains unreproduced or unconfirmed

- Original CMU PIE experiments, including Table III and the PIE parts of Fig.5/Fig.8, were not run; omission is instructor-authorized. Multi-PIE is not substituted.
- The authors' exact code, eye annotations, initialization, centering, Gabor details, NN distance, validation process, and random indices are not recovered.
- ORL low-dimensional CSA superiority and the original CSA numerical levels remain unresolved; MNIST also remains below the paper.
- Reconstruction/convergence curves are not claimed to match every original ordinate. Our reconstruction is of fitting-sample Gabor tensors, not unseen-face reconstruction or Gabor inversion.
- We cannot conclude that any single unknown setting caused the entire gap, that exact equality is necessary for course credit, or that a high exploratory maximum establishes exact numerical agreement or identical author settings.

The instructor/TA explicitly permits reasonable missing-setting choices held fixed across methods and disclosed differences. This does not individually confirm those choices as the authors' settings. Neither the supplied correspondence nor the recognition text fixes Euclidean versus cosine NN.

### 0.3 Current paper-dimension numerical comparison

Percent accuracy; differences are group minus paper in percentage points. ORL: ten-split mean±sample SD. MNIST: three-split mean±sample SD. FERET: one fixed identity partition, without repeated-partition SD. The two ORL CSA+LDA rows use the current grayscale and Gabor representatives; other rows retain shared references. Input protocols and selection procedures are not identical across rows. Grayscale crop/distance and exploratory selection are described outside the table in the follow-up above.

| Dataset | Method | Our result | Paper | Difference, pp |
|---|---|---:|---:|---:|
| ORL | PCA+LDA (Gray) | 83.22±1.76 | 82.20 | +1.02 |
| ORL | CSA-2+LDA | **81.84±1.96** | 84.10 | -2.26 |
| ORL | PCA (Gabor) | 86.88±1.63 | 86.60 | +0.28 |
| ORL | CSA-3 | 90.19±2.37 | 94.40 | -4.21 |
| ORL | PCA+LDA (Gabor) | 92.09±2.06 | 87.20 | +4.89 |
| ORL | CSA24 + LDA23 (HOSVD start; context extension) | **88.75±2.89** | 90.90 | −2.15 |
| MNIST G30/P470 | PCA (Gabor) | 87.52±0.40 | 88.50 | -0.98 |
| MNIST G30/P470 | CSA-3 | 90.34±0.15 | 92.80 | -2.46 |
| MNIST G40/P460 | PCA (Gabor) | 88.58±0.37 | 90.50 | -1.92 |
| MNIST G40/P460 | CSA-3 | 91.04±0.25 | 92.40 | -1.36 |
| FERET q=50 | PCA+LDA (Gray) | 89.08 | 84.60 | +4.48 |
| FERET q=50 | CSA-2+LDA | 88.73 | 88.20 | +0.53 |
| FERET q=100 | PCA+LDA (Gray) | 90.87 | 90.60 | +0.27 |
| FERET q=100 | CSA-2+LDA | 94.25 | 92.20 | +2.05 |
| FERET q=200 | PCA+LDA (Gray) | 93.87 | 93.40 | +0.47 |
| FERET q=200 | CSA-2+LDA | 95.38 | 95.20 | +0.18 |

Sources: [grayscale final analysis](../results/orl_gray_recovery_20261030/final_analysis.json) for gray CSA11x2->16; [HOSVD/context summary](../results/orl_recovery_20261027/summary.csv) (`d20_y24`, `hosvd`, `unit_gallery_cosine_g0`) for ORL CSA24→23; [shared CSV](../results/orl_protocol_audit/shared_comparison.csv) for the other rows. The current ORL candidate comparisons use already-observed probes and remain exploratory. FERET is numerically closest and MNIST retains CSA>PCA. ORL grayscale/Gabor CSA+LDA gaps are now2.26/2.15pp, while paper-dimension method ordering is still unrecovered. FERET does not recover every CSA-versus-PCA ordering. The paper reports best parameter configurations; its split aggregation is unspecified, so these differences are descriptive and do not establish significance or identical protocols.

### 0.4 Additional experiments and their status

| Study family | Completed evidence | Reporting category |
|---|---|---|
| Early grayscale and geometric audit | G2/V2/P6 selection; five geometric branches; six manual Haar corrections; later YuNet audit | Historical diagnostic protocols; different splits/inputs cannot be pooled into a paired gain |
| Gabor and numerical sensitivities | Kernel support, padding, wavelength, sigma, magnitude/normalization, sampling; radius rounding; 3→10 rounds | Disclosed missing-setting diagnostics; ten-round runs did not change predictions in the checked branches |
| LDA/representation analysis | Same-representation before/after LDA, scatter conditioning, output scaling and retained energy | Avoids confounding CSA390 with CSA24→23; energy is not identity information |
| Three fixed inputs | 120 outer fits; low-dimensional CSA81.25→TT78.31 / context84.31 | Illumination/context extensions, with negative results retained |
| Three-stage gallery selection | FinalCSA24→23 87.84±3.28, versus context84.31 | Own-gallery selection with context/power extensions; A→C adds only about0.03pp |
| Crop-only bounded optimization | 81.25→81.41±2.41; matched controls decline | Original dimensions and explicit TA counts retained; unknown choices are not author-confirmed |
| Fixed sigma×context | 320 outer fits, twenty fixed splits; CSA80.13/84.56/81.25/87.08 | Fixed input extension; paired improvement6.95pp for pi-context versus2pi-crop |
| Rank/shrinkage | Refined ordinary83.28±3.30 and shrinkage85.47±4.57 | Changed ranks and/or regularization; not originalCSA24→ordinaryLDA23 |
| Sample size | FixedP5, nestedG2/G3/G5:81.30/88.10/94.50 | More fitting/gallery samples; not the originalG2/P8 |
| Split sensitivity and exploration | 100 fixed splits; separate6003-configuration/200-split search; maxima95/97.5 | Probe-selected extrema; corresponding means86.42/91.43 do not become independent estimates |
| MNIST bounded selection | Ten matching splits: CSA89.66→88.89 and90.50→90.18 | Negative optimization result; do not compare old three-seed and new ten-seed means as paired gains |
| FERET validation selection | CSA87.51/94.25/93.77, distinct from fixed-cosine88.73/94.25/95.38 | Validation choices and shared fixed controls must remain separate |
| DATER supervised reduction | Direct24:71.64±3.18; LDA23:67.11±3.59; matchedCSA74.33/80.13 | New-method negative result;19/20 hit the cap; strict-path failure/sensitivity retained |
| Error, cost, and robustness |224 corrected/111 new errors;830 versus618792 projection weights;1280 zero-fit perturbation scores | Reused models/predictions; limited timing and joint±1-pixel shifts, not universal efficiency/robustness |

Full batch-level tables, failures, parameters, and source links remain in [Appendix A](#all-experiments), [Appendix B](#statistics), and the [inventory](#inventory). Counts of predictions, reused records, and files are not counts of independent experiments or new images.

### 0.5 Text teammates can adapt

**Report abstract/conclusion:** “We independently implement Concurrent Subspaces Analysis and conduct full reproduction within the instructor-approved ORL, MNIST and grayscale FERET scope, including ORL reconstruction and convergence experiments. FERET scores are numerically close to the paper, and MNIST retains the CSA-over-PCA direction. Our current ORL CSA24→23 representative uses a HOSVD start and context extension, achieving88.75%±2.89% over ten observed splits versus the paper90.90%; full-square initialization88.81%±2.97% is reported separately as a variant. Controlled preprocessing, sample-size, regularization, supervised tensor, robustness and cost studies characterize this gap without attributing it to a uniquely established cause.”

**Presentation sequence:** paper problem and tensor structure → CSA/PCA/LDA and course concepts →16-case coverage and preserved comparison → one controlled ORL improvement with its matched PCA control → failure/selection bias and representation-cost trade-off → PIE omission and unknown author settings. Use separate captions for paper results, shared references, gallery-selected results, fixed extensions, and probe-selected extrema.

**Do not write:** “identical to the authors' implementation in every detail,” “TA confirmed our cosine/Gabor/context settings,” “95% is our ten-split mean,” “more than one million independent test images,” or “DATER is generally ineffective.”

### 0.6 Current ORL representative and initialization variants (2026-10-27)

**Current reporting choice:** **88.75%±2.89%** (HOSVD start, context extension; ten splits, −2.15pp versus the paper90.90%). Report **88.81%±2.97%** (full-square identity initialization variant; −2.09pp) separately; it is not the representative README value. Historical batch tables below retain their own observed scores.

A bounded follow-up retained all ten seeds20–29, G2/P8, CSA4×2×3→ordinaryLDA23 andTmax3. Three sigma=pi/context geometry bundles and three starts produced90 CSA fits;30 matchedPCA controls were added. All120 models froze before1440 policy scores/460800 repeated predictions. No old result was overwritten.

| New fixed setting, same default centered-cosine NN | Ten-split mean±SD | Single maximum | Difference from paper90.9 |
|---|---:|---:|---:|
| d20/y24, rectangular identity |88.72±3.01|92.50|−2.18pp |
| d20/y24, HOSVD |88.75±2.89|92.19|−2.15pp |
| d20/y24, full-square identity variant |88.81±2.97|92.50|−2.09pp |
| MatchedPCA24→23, d20/y24 |90.59±1.94|94.06|No paperPCA24 counterpart |

The best single CSA run across the pool is93.125% (298/320), d18/y25, rectangular identity, seed22, default NN. This exceeds the paper as an **exploratory single best run with context**, while no tested mean reaches90.9. The best candidate mean88.81 is also selected after comparing known probes; it is not a new blind validation estimate. The original shared79.66, gallery-selected87.84, twenty-split fixed87.08, and earlier95/97.5 at different dimensions remain separate.

Full versus rectangular identity adds only0.09375pp on matched inputs. Full-square initialization starts with larger mode dimensions than the final ranks; treat it as a disclosed interpretation/variant, not an author-confirmed fix. Rank-conforming HOSVD already reaches88.75. Fisher-eigenvalue weighting is a metric extension and its best mean86.16 does not help. Gallery-SSE start selection gives88.81±2.91 at fixed d20/y24, but cannot make an input/metric selected on probes independent. PCA remains stronger in the matched control.

Teammate wording: “At fixed24→23 output dimensions, the HOSVD/context representative achieved88.75%±2.89% over ten observed splits. A full-square identity initialization variant achieved88.81%±2.97%; the pool's exploratory best single run was93.125%. No tested mean reaches90.9%, and exact author settings and CSA's relative advantage remain unrecovered.” See the [full new protocol and limits](./REPORT.md#orl-recovery-20261027), [summary](../results/orl_recovery_20261027/summary.csv), and [verification](../results/orl_recovery_20261027/verification.json).

## Reading Navigation

- [1. Correspondence between course requirements and materials](#requirements): Confirm what needs to be covered and which deliverables have not yet been completed.
- [2. Paper understanding and key theories](#paper): Problems, motivations, contributions, formulas, course connections and evidence of the paper.
- [3. Data, TA conditions and unknown protocol](#protocol): Explain whether the requirements are met and each difference.
- [4. Implementation method and experimental design](#implementation): code, shape, preprocessing, parameter selection, expansion and numerical processing.
- [5. Core results and before-and-after comparison](#results): shared anchors, latest ORL, MNIST, FERET, DATER.
- [6. Critical analysis and insights from our group](#critical): Evidence, scope, and open questions for each explanation.
- [7. Verification, reuse and rerun](#verification): There are verification, failure correction, source and correct running entries.
- [8. Report, presentation and Q&A preparation](#submission): Content and to-dos that can be directly divided into tasks.
- [Appendix A. All experimental families and data tables](#all-experiments): Complete historical summary collapsed by topic.
- [Appendix B. Precise statistical supplementary table](#statistics): mean, SD, range, difference values ​​read from existing CSV.
- [Appendix C. All results directory index](#inventory): raw scores, parameters, models and verification entries.
- [Appendix D. Available Figures and Citations](#figures): Attribution of the paper figure to our group figure.

Further tracing: [README](../README.md), [Complete status handover](./HANDOFF.md), [Detailed results and protocol explanation](./REPORT.md), [Historical explanation and reply file](./HISTORY.md). "Final," "To Do," and missing data status in older documents may belong to the then-current version and are subject to the date of this page, the current protocol, and the results file.

<a id="requirements"></a>

## 1. Correspondence between course requirements and materials

Course requirements come from user-uploaded Group Project screenshots; they are the evaluation objectives. The teacher/TA responds by explaining the acceptable range of reproduction; CSA the paper is the source of scientific methods and experiments, and the three cannot be confused with the same agreement.

| Screenshot request| Our group already has the materials| The location of this article/What the companion needs to do|
|---|---|---|
| Paper Selection: Research a paper related to the course, giving priority to major conferences/journals| selected TCSVT2008 CSA; early comparison of 12 candidate articles and retention of Chinese and English learning materials| §2; For the history of topic selection, see [History 01](./HISTORY.md#history-01). There is no need to write the ranking of the 12 articles into the final report.|
| Paper Study: Problem definition, motivation, methods, main contributions| Tensor representation, reconstruction targets, alternating eigendecomposition, recognition and compression| §2, the report should explain the formulas and shapes themselves|
| Connect with course concepts| PCA, orthogonal projection/spectral decomposition, LDA, NN, dimensionality and small samples, validation and generalization| §2.3 and §4; the relevant course has already taught the concepts, and does not make up unchecked specific courseware page numbers.|
| discusses the paper experiments and evidence supporting claims| Original Tables I/II/IV, reconstruction and convergence diagram; our group cross-dataset and same-budget comparison| §2.4, §5; indicate which are the author results and which are our group results|
| Critical Analysis: Assumptions, Strengths, Limitations, Improvements| Differences in target and classification, budget mismatch, protocol sensitivity, selection bias, costs and negative outcomes| §6; Write “Evidence→Explanation→Limitations” instead of just saying that the number was not reached|
| Experiment Reproduction: explain the approved scope, comparisons, and difficulties| Three dataset implementation, shared anchors, gaps, PIE license, independent numerical/prediction verification| §3–7; full reproduction within the instructor-approved scope|
| Implemented from scratch, distinguishing contributions and reusing code| realizes CSA/PCA/LDA/Gabor/DATER and experiments by itself; reuses scientific computing, image and detection libraries| §7.3; No the original authors code is available, which does not mean that all dependencies are implemented from scratch.|
| Reproduction code: public GitHub + README, setup/run/results, source acknowledgments | English README, pinned dependencies, run commands, protocols, and result evidence prepared for public release; all three datasets excluded | §7–8; include the public repository URL and preserve the distinction between independent implementation and reused components |
| Written Report: About 3–4 pages of LaTeX, appropriate figures and citations| The content is complete, the official LaTeX report has not yet been produced.| §8.1; Take the main line from this article, the complete data can be left in the repository appendix|
| Presentation: 9 minutes + 3 minutes Q&A, all members participate| There are available figures, explanation sequences, and Q&A materials; official slides have not yet been produced.| §8.2; division of labor determined by group|
| Demonstrates team understanding, conceptual difficulties and learning| sample axis/object-mode axis, reconstruction/discrimination target, LDA column scale, verification improvement and outer layer drop, extreme value/mean difference| §6, §8.3; members should be able to explain key judgments themselves|

Basic scoring: paper understanding 40%, critical analysis and insights 30%, report 10%, presentation and Q&A 20%; reproduction bonus up to an additional 10 percentage points, assessed individually. Workload and a certain high score cannot be automatically converted into points. The course can use GPU farm, and this project is mainly completed on the local CPU.

<a id="paper"></a>

## 2. Paper understanding and key theories

### 2.1 Paper identity, problems, motivation and contribution

Dong Xu, Shuicheng Yan, Lei Zhang, Stephen Lin, Hong-Jiang Zhang, Thomas S. Huang. *Reconstruction and Recognition of Tensor-Based Objects With Concurrent Subspaces Analysis*. IEEE TCSVT **18(1):36–47, January 2008**, DOI: [10.1109/TCSVT.2007.903317](https://doi.org/10.1109/TCSVT.2007.903317). [Local CSA paper](../Reconstruction_and_Recognition_of_Tensor-Based_Objects_With_Concurrent_Subspaces_Analysis.pdf).

Images naturally have height×width structure; Gabor images add a channel mode. Flattened PCA may require a large projection basis, and a limited fitting set restricts estimable directions. CSA learns a subspace for each object mode while jointly optimizing the reconstruction of a small core tensor. This preserves separable spatial/channel structure and reduces shared projection parameters.

The contributions should be understood in their historical context: joint multi-mode reduction, an alternating solver, reconstruction/storage analysis, and comparisons of tensor and vector representations on reconstruction and face/digit recognition. Unlike Tensorface, CSA does not require complete identity×pose×illumination combinations. Each object has internal modes. **Learning a representation with one fitting image per class does not mean recognition without a gallery.** CSA is unsupervised; labels first enter through optional downstream LDA. MNIST also tests a setting beyond small-sample face recognition.

### 2.2 Objectives, Updates and Convergence: Reports should explain formulas

An object is \(X_i\in\mathbb R^{m_1\times\cdots\times m_K}\), with mode-k basis \(U_k\in\mathbb R^{m_k\times r_k}\) and \(U_k^TU_k=I\). The sample index i is outside the object modes.

\[
G_i=X_i\times_1U_1^T\cdots\times_KU_K^T,
\qquad \widehat X_i=G_i\times_1U_1\cdots\times_KU_K.
\]

\[
\min_{U_1,\ldots,U_K}\sum_i\|X_i-\widehat X_i\|_F^2
\quad\Longleftrightarrow\quad
\max_{U_1,\ldots,U_K}\sum_i\|G_i\|_F^2.
\]

With orthogonal projection, total input energy is fixed; retaining more core energy reduces residual reconstruction error. To update mode k, project every other mode to obtain Y_i, unfold it as Y_i(k), form \(C_k=\sum_iY_i(k)Y_i(k)^T\), and take the leading r_k eigenvectors. Updates are sequential: each new basis is immediately used by later modes, rather than fitting each mode independently just once.

Procedure 1 (printed page39) specifies column-orthonormal initialization, **ε=0.001**, and a subspace-similarity stopping condition after t>2. Recognition uses Tmax=3. The default implementation starts from the first r_k columns of an identity matrix; random-QR and HOSVD initializations are separately declared. CSA ε is specified in the paper, while the authors' exact initialization is unknown.

Each conditional mode update is optimal; in exact arithmetic, reconstruction SSE is non-increasing and bounded below. The joint structured problem is non-convex: stable error proves neither a global optimum nor optimal classification. Tiny floating-point SSE fluctuations alone do not establish an algorithm error. For vector objects with matching centering, CSA reduces to PCA; different centering conventions need not produce identical values.

The core tensor is flattened for NN, optionally after Fisher LDA: \(S_bw=\lambda S_ww\). LDA seeks between-/within-class separation, while CSA retains reconstruction energy. With ORL G2, N=80 and Nc=40, the pre-LDA dimension must be ≤N−Nc=40; the output is also limited by the effective Sw rank and Nc−1. CSA390 therefore uses direct NN, whereas CSA24 can precede LDA23.

### 2.3 Connection to course concepts

| Course concept | Role in the method | Evidence and common misunderstanding |
|---|---|---|
| PCA/Feature Decomposition| Covariance leading eigenvector retains energy| Our PCA uses Gram matrix to process N≪D, and does not use huge D×D implementation as the only comparison|
| Orthogonal projection / reconstruction | Orthonormal bases justify the residual-energy equivalence | Core energy is not identity information; DATER bases need not be orthogonal, so CSA's energy identity cannot be applied to them |
| Tensors and structural constraints| Each mode is independent small base, joint alternating optimization| sample axis is not compressed; the same 24-dimensional output does not mean that the CSA and PCA expression spaces are the same|
| Dimension/small sample| The core dimension is the product of each rank; the estimation error is affected by the number of samples| High-dimensional CSA390 and low-dimensional 24→23 cannot be used to judge the quality of LDA in isolation|
| Supervised discrimination / LDA | Sw and Sb use class labels | Ordinary and shrinkage LDA are separate; unsupervised compression can discard discriminative directions before LDA |
| NN／Distance| Features nearest neighbor, scaling and normalization change geometry| Squared Euclidean, origin cosine, mean-centered cosine are different; the paper/TA only determines NN|
| Validation/Generalization| Only select candidates within your own gallery or training identity, freeze and then score| The improvement of the inner layer does not guarantee the improvement of the outer layer; the historical probe has been viewed and cannot be called a new blind test|
| Complexity/Tradeoffs| CSA basis parameters Σm_k r_k, PCA basis Dd| Small weight is not equal to complete memory/end-to-end speed, need to measure and clarify the statistical range|

### 2.4 the paper evidence and the scope of our verification

| Paper experiment / claim | Original evidence | Our corresponding work and finding |
|---|---|---|
| Reconstruction, compression, and iterations | Procedure1, Fig.2, Fig.4/5a; errors at different representation/storage budgets | 40 fitting-image reconstruction/compression curves and 10-iteration diagnostics are implemented and checked; trends are comparable, but Gabor amplitude and vertical axes are not claimed to match exactly |
| Face recognition CSA is better than PCA| FERET TableI／Fig.6，ORL TableII／Fig.7，PIE TableIII／Fig.8 | FERET Fixed control is close to the paper; ORL does not restore low-dimensional CSA advantage; PIE omitted|
| High-dimensional digital representation is valid| MNIST TableIV | The fixed process maintains the direction of CSA>PCA, but the value is lower than the paper; subsequent optimization did not improve CSA|
| Small sample representation is more suitable for tensors| paper’s parameter/sample number discussion and recognition and reconstruction results| We measured low weight cost; more galleries significantly improve the score, but it does not prove that CSA will win with a small sample size|
| LDA may overfit ORL| the paper Differences and discussion between the results of CSA390 and CSA24+LDA23| The two represent different budgets; our group is the same as CSA24 plus LDA, but it improves. It is necessary to avoid using the original comparison as evidence of causality.|

Paper IV-C gives "the best results and the optimal configuration within the brackets". The brackets are mainly dimensionality reduction. It does not specify the number of times to repeat random splits, seed, mean/SD, or whether to take the maximum value across splits. **Only the best parameter result can be confirmed, it cannot be confirmed that the author reported the mean, nor can it be confirmed that the author selected the highest based on 200 splits.** Our group mean minus the paper numbers are descriptive numerical differences, not exactly the same statistical caliber, and there is no evidence to accuse the author of seed selection.

<a id="protocol"></a>

## 3. Data, TA conditions and unknown protocol

### 3.1 Data acquisition and actual range

| data| Get/Process| main protocol and input| Notes|
|---|---|---|---|
| ORL / AT&T | Original400 images, 40 identities×10, 112×92 PGM; Cambridge archive | G2/P8; aligned/equalized56×46, recognition Gabor28×23×40, reconstruction56×46×40 | Early Haar/6-image manual review and later YuNet stages are archived separately; none supplies the original authors' eye coordinates |
| MNIST | Official test IDX10000 pictures have been verified, take the top 500 pictures of each category, a total of 5000| 28×28, G30/P470, G40/P460, 40 channels without downsampling| "First half of the test" and "500 per category" are not completely equivalent; sampling is based on the teacher's requirement of 500 per category, and the author index is unknown|
| original grayscale FERET| gray_feret in the authorized archive, 3680 TIFFs; using official 1195 Fa/Fb identity, 2390 pictures| First q=50/100/200 identity Fa+Fb learning; remaining Fa gallery/Fb probe; 41×27 grayscale| non-Color FERET turns gray; only official matches are used, no easy samples are selected from additional candidates|
| CMU PIE | Not obtained, the author replied twice to explain the distribution rights; the teacher allows omission| The original requirement is 63 people, five poses, PIE1/2, G3/P7; 64×64 grayscale/16×16×40 recognition| is not implemented, MultiPIE is not used as a replacement reproduction|

ORL/MNIST data and eye points/features are in `data/`. For FERET instructions, see [FERET README](../FERET/README.md). FERET official gallery1196 identity, Fb1195, 00989 is not matched and excluded; 317 additional candidate missing eye spots are not used for the standard 1195 pair. TIFF uses `convert('L')` to process L/P mode; the official left and right eyes of the human body are converted into the x increasing order of the picture. The status "FERET not obtained" in the history [Download List](../data/dataset_manifest.json) is outdated and cannot cover subsequent facts. The

project source, 12 topic selection evaluations, early teaching and data acquisition process can be found in [HANDOFF§1 and §5](./HANDOFF.md), [Historical Archives](./HISTORY.md). These tasks are research preparation and data collection, and do not increase the number of recognition experiments.

### 3.2 What did the teacher/TA/author each confirm?

The reply is provided by the user. This article is not connected to the email address; the document record date cannot be automatically used as the sending date. For the original sentence, see [HANDOFF§3](./HANDOFF.md), [HISTORY teacher/TA questioning](./HISTORY.md#history-14).

| Source| Confirm content| should not be expanded and interpreted as|
|---|---|---|
| Instructor | Dataset sizes, ORL two-eye alignment/normalization/HE and dimensions, 5×8 Gabor, two MNIST splits, FERET training/test identities; NN, CSA Tmax3, LDA budget | This does not specify Euclidean distance or confirm our detailed Gabor settings, eye targets, or seeds |
| Instructor | Unobtainable datasets may be omitted; unmatched settings must be disclosed, and exact numerical equality is not required | This does not confirm undisclosed author settings, guarantee full bonus credit, or waive disclosure of differences |
| TA Qiyuan | The2008 project is not maintained; original code and hyperparameter records are unavailable. Remaining ORL alignment/Gabor choices may follow public literature and standard practice, fixed across methods and disclosed | This is not individual confirmation of our σ, padding, context, NN, or DATER settings |
| Terence Sim, twice | PIE distribution rights belong to CMU; he lacks them, as does Simon Baker, who left CMU | This does not mean the data ceased to exist worldwide, were destroyed, or became inaccessible to all authors |

### 3.3 Whether it is consistent with TA and the paper: distinguish item by item

| project| clear request/the paper| our group adopt or explore| Conclusion|
|---|---|---|---|
| Data quantity, main gallery/probe| ORL400/40, G2/P8; MNIST 500 per category and G30/40; FERET1195, q50/100/200| Shared anchor points and experimental retention within recent clipping| Explicit number/split reserved; actual index/identity order still chosen by our group|
| Input size/alignment| ORL binocular processing 56×46 and 28×23×40; FERET41×27| fixed target eye point, interpolation, boundary, PIL HE| dimensions correspond to processing steps; specific author geometry and "normalization" details unknown|
| CSA Mathematics and Iteration| Column orthogonal alternating eigendecomposition, ε=.001; recognition Tmax3| identity is the default, randomQR/HOSVD is listed separately, center defaults to False| Core formula/recognition upper limit reserved; initialization and centering conditions must be disclosed with the batch|
| the paper's dimensions and ordinary LDA| ORL24→23, 390, PCA33→25, etc.; p≤N−Nc| anchor/recent the paper's dimensions are retained; PCA24→23 plus| The original row dimensions can be compared; the newly added budget rows have no corresponding paper rows|
| recognition distance| the paper and reply to confirm NN, but did not give a specific metric that can be recovered| Square Euclidean, origin/gallery mean-centered cosine, column scale ablation| are all public conventions of our group; the Euclidean norm of the paper tensor is used for reconstruction, and it does not prove that NN must use Euclidean|
| Gabor | 5 scale × 8 directions, amplitude/output size| λ, σ, core support, DC correction, sampling, padding limited control| Channel/size reserved, specific values have not been confirmed by the author one by one|
| context, TT, power, shrinkage, new rank, G3/G5| The original matching line did not acknowledge these changes.| expands independently, retaining the original anchor point| It cannot be called the restoration of the same agreement as the original CSA|
| DATER | Independently supervised tensor method, the paper has no matching ORL24-dimensional rows| our group Tmax20／ε.001／Non-orthogonal direction specification| method extension; CSA's Tmax3 cannot be directly applied to DATER requirements|
| Repeat split/best value caliber| the paper best, the number and index are unknown| three/ten/twenty/one hundred/two hundred split recorded separately| Our group has clear statistics and cannot claim that the authors have the same seed or mean/best rules.|

**Acceptable representations are: adhere to well-defined data, dimensions, CSA iterations, and LDA budgets, use fixed and transparent our group conventions for unrecoverable details, and report numerical differences.** This is consistent with some of the reproduction methods allowed by TA; it does not prove that all unknown settings are consistent. Whether the extension is valid and exactly matches the original protocol are two questions.

<a id="implementation"></a>

## 4. Implementation methods and experimental design

### 4.1 Main process, array shape and core implementation

`Original image→image-by-image alignment/intensity processing→greyscale or complex Gabor amplitude tensor→only learning set fitting CSA/PCA→gallery/probe encoding→optional LDA→shared NN→save protocol, model, index, prediction and verification `.

| module| implementation details| source code|
|---|---|---|
| object/sample axis| `[N,m1,m2,…]`; mode0 corresponds to array axis 1, sample axis 0 is not compressed; tensordot+moveaxis, unfold/fold check| [csa.py](../csa.py) |
| CSA | float64; non-finite/rank legality check; symmetric leading feature decomposition, sign specification; instant update by mode; optional learning mean; save SSE, mode SSE, base similarity/projected subspace distance| [CSA](../csa.py) |
| PCA | flatten; default subtractive learning mean; SVD or N×N Gram recovery base, eigenvalue/numeric rank threshold; do not call sklearn PCA| [PCA](../csa.py) |
| ordinary LDA| Use learning labels to construct Sw and Sb; Sw positive feature space whitening, and then solve the symmetric Fisher problem; numerical zero space truncation; ordinary branches have no ridge| [LDA](../csa.py) |
| LDA column scale| Native Sw normalization or Euclidean unit-norm columns; shared distance after normalization; different scales will change the Euclidean/cosine geometry of the features| [Optimization/NN Rules](../optimize_csa_lda.py)|
| Data and Image Processing| ORL／MNIST loading cache, eye point detection/affine, equalization, FERET official list/annotation conversion| [Data preparation](../prepare_available_data.py), [FERET preparation](../prepare_feret.py), [ORL audit](../audit_orl_protocol.py)|
| Category| Simple entry is square Euclidean cdist; each experimental wrapper also has origin cosine/mean-centered cosine; gallery mean is only estimated from gallery, query minus the same mean| [Core NN](../csa.py), [Fixed Control](../run_orl_controlled.py)|

ORL low-dimensional Gabor example: learning tensor 80×28×23×40; CSA basis 28×4, 23×2, 40×3; core 80×4×2×3, flattening 80×24, ordinary LDA output 80×23; probe320 images are encoded according to the same transformation. CSA390 uses (15,1,26). MNIST G30 is (5,9,18)=810, PCA60; G40 is (15,5,13)=975, PCA50, both are direct NN. FERET is a two-dimensional grayscale CSA: q50 is 10×4→35, q100 is 11×5→44, q200 is 13×7→62, and PCA is 45→25, 95→40, and 112→69 respectively.

ordinary LDA only solves the whitened effective Sw space, and does not truncate the value, which is called shrinkage; the output is limited by the effective rank, and the actual dimensions are stored in the result. Only use the learning set to estimate RMS, mean, HOSVD and LDA; it is forbidden to use the outer probe label for fitting. The probe label is only used for scoring and post-mortem diagnosis; the 200 split exploration explicitly uses the probe score to select maximum, so it is single column.

### 4.2 Gabor, Geometry and Fixed Input Extensions

Our group Gabor core uses Wiskott-style DC-free review: k=2π/λ, λ_s=4√2^s (s=0...4), θ_o=oπ/8 (o=0...7), and the default σ=2π.

\[
\psi(x,y)=\frac{k^2}{\sigma^2}e^{-k^2(x^2+y^2)/(2\sigma^2)}
\left[e^{ik(x\cos\theta+y\sin\theta)}-e^{-\sigma^2/2}\right].
\]

Finite kernel subtracts discrete mean; calculates complex convolution amplitude, channel scale-major. FFT is an accelerated calculation, and spatial complex convolution verification is used. The image generally retains 0...255 amplitude, feature cache float32, and model calculation float64; amplitude power and normalization are only applied to the declared branch. [gabor.py](../gabor.py) retains the original reflect version; local scripts control subsequent zero/39×39 and other versions, and it cannot be assumed that all caches are the same.

Recent fixed ORL cropping input: YuNet eye point → target (13,24)/(33,24), linear affine replicate → center 56×46 → PIL histogram equalization → λ0=4, 39×39 kernel, σ2π, zero convolution → amplitude → first filter and then `[::2,::2]` to get 28×23×40. Fixed unit LDA column, gallery mean mean-centered cosine, identity/non-centering CSA/Tmax3/ordinary LDA. **Affine padding and Gabor padding are two-layer settings.** The original shared 79.66% is different from the specific input of this fixed baseline 81.25%, and cannot be subtracted as the same round of optimization gain.

| input/change| actual implementation| Ownership and Restrictions|
|---|---|---|
| adaptive core support| Get the radius according to ceil(3σ/k); early floating point rounding and stable radius will be verified separately| core support is unknown; 25/35/49, etc. are different from the fixed 39, read by protocol|
| TT＋EQ| Grayscale/255 after γ=.2, DoGσ1/2 (nearest, truncate4), two robust equilibrium α=.1, τ=10, tanh, map uint8 and then HE| The actual measurement is this combination, non-standard TT independent branch; the overall regression does not negate all TT|
| Contextual convolution| aligns the original image to expand the surrounding 19-pixel canvas, using the HE mapping obtained from the center 56×46 histogram; complete canvas filtering, cutting the center response and then stride| The output size remains unchanged but the effective field of view is expanded and expanded independently; the canvas balance is not changed to a full-canvas histogram.|
| Power/Normalization| amplitude p=1/.75/.5; sqrt, jet L2, tensor L2, learning channel RMS and other branches| Non-linear or scaling; different single factor winners cannot be combined into an unexecuted optimal process|
| Valid area/geometry| valid hist, z-score, Lanczos, eyepoint source/target/zero or replicate| historical diagnosis; direct resize branch does not retain TA binocular processing|

Actual implementation: [Three inputs](../run_orl_fixed_inputs.py), [σ × context](../run_orl_controlled.py), [Unknown parameters](../optimize_orl_unknowns.py), [Intra-crop optimization](../optimize_orl_ta_crop.py). The public Gabor reference only supports the general form and cannot be used to determine the same numerical process of the CSA author.

### 4.3 How to distinguish various types of parameters and outer experiments

| batch| Learning/Selection Plan| Freeze and Score/Boundary|
|---|---|---|
| Early grayscale validation | Five splits with G2/V2/P6; compare equalization, interpolation, dimensions, and distances | Different from the main G2/P8; expanded candidates also include Tmax10 and new ranks |
| ORL protocol audit, targeted LDA, ordinary/shrinkage, and rank optimization | Select within each gallery; candidate sets and objectives vary by batch | Input and NN are shared within a batch; methods may have separately declared ranks/LDA dimensions. Historical probes have already been observed |
| Three-stage unknown-parameter selection | Each80-image gallery supplies16 folds:75 fitting/5 validation, every image held out once. StageA screens12 inputs and retains two; B tests three magnitude powers; C tests two initializations×six NN/scaling rules | 3520 inner models, 900 candidates, ten selections frozen before120 new outer fits; context is an extension and staged pruning is not globally optimal |
| Crop-only bounded optimization | Four inputs, σ2π/π×zero/reflect, use16-fold validation to retain two; then two initializations×six NN rules. Fixed24→23 and ordinary LDA | 960 inner models, 280 candidates;40 new outer fits plus40 historical baseline scores after freezing; no context, magnitude powers, new ranks, or shrinkage |
| Three fixed inputs| seeds20–29, baseline/TT combination/context, four methods| 120 outer layer fitting, fixed input, no parameters selected, all negative branches retained|
| 2×2 fixed control| seeds4200–4219, σ2π/π×crop/context, four methods| 320 outer layer fitting; enter all reservations, do not select author parameters with higher probe score|
| MNIST bounded optimization | Stratified5-fold validation within each G30/G40 gallery:24/32 fitting images per digit. Four inputs shortlist two, followed by three NN policies×identity/HOSVD; PCA/CSA joint validation score chooses settings | Twenty selections frozen before scoring;1000 inner-fit records and160 outer scores including baseline/stage/final profiles; paper dimensions retained |
| FERET validation | Only the first q training identities; seed3314+q. q50/100 use10/20 folds holding out five identities; q200 uses10 folds holding out20 | Inner fitting identities45/95/180. Held-out Fb is validation probe; all first-q Fa form a gallery with fitted-identity distractors, unlike the final unseen-identity-only gallery |
| 100 split diagnostics| Fixed input/model/NN, observe score distribution| is the same as 400 pictures, not 100 new data, mean is tied with the highest|
| 200-split exploration | 6003 configurations, 1,200,600 scores; configurations and seeds selected by probe accuracy, with complete scores and replay saved | Maxima95/97.5 are not independent test estimates; the score count is not the number of independently fitted new models |
| sample size expansion| fixed P5, nested G2⊂G3⊂G5, ten same split; save G2/P8 anchor point| changes the learning amount and NN reference coverage; 90 model and PCA comparison, no mixed reporting with the original G2/P8|

ORL16 folds inner p=24≤75−40=35 and outer p=24 or 33≤80−40=40. More candidates may improve validation winners but increase selection variance; screening input first may miss good configurations under other rules. The full gallery pre-screening in targeted low-rank optimization is only approximate pruning and cannot be written as an unbiased complete LOO verification. All candidates, tie-breaks, learning indexes and actual ranks are subject to the corresponding `protocol.json`/`selected_settings`.

### 4.4 shrinkage LDA and DATER: two types of independent extensions

shrinkage LDA uses \(S_w^{(\alpha)}=(1-\alpha)S_w+\alpha\,\mathrm{tr}(S_w)/p\,I\), candidate α=0/.01/.05/.15/.35/.65/1, selected in gallery. α=0 takes the ordinary LDA path; even shrinkage retains the pre-stage p budget. **This is a manual finite grid covariance shrinkage, not an automatic Ledoit–Wolf estimator.** Removing α from a shrinkage winner is a different experiment than re-independently selecting ordinary LDA.

DATER comes from Yan et al. CVPR2005 *Discriminant Analysis with Tensor Representation*, [local the paper](./sources/DATER_CVPR2005.pdf), [author PDF](https://mmlab.ie.cuhk.edu.hk/archive/2005/01467312.pdf). It uses labels to construct Sb and Sw in each mode, solves generalized feature problems and updates them alternately. The purpose is inter-class/intra-class discrimination, not CSA reconstruction energy. The paper does not have an ORL24-dimensional benchmark that matches this round.

This round of DATER is fixed within 2π clipping and seeds4200–4219, G2/P8, (4,2,3)=24 dimensions. According to Figure 3, start from the complete I28, I23, and I40, and shrink the order to 28×4, 23×2, and 40×3; the generalized direction Euclidean unit-norm columns and symbol specifications, **fitting does not do QR, no ridge/shrinkage/singular fallback**, and Sw is required to be positive definite. Tmax20 and ε=.001 are fixed conventions for our group. After t>2, the normalized basis difference of each mode reaches the threshold or stops at the upper limit; the best round is not selected according to probe or training DTC. 20 new DATER, reuse 40 CSA/PCA, direct 24-dimensional and ordinary LDA 23 branches, a total of 120 scores/38400 predictions.

19 model reached the upper limit of 20 rounds, and only 4219 met the threshold in 18 rounds; 1194 mode was updated, and 165 joint DTCs dropped. You cannot write "all converge" or "find the global discriminant optimum". DATER changes the supervision target, complete initial value, number of iterations and non-orthogonal geometry, etc. Negative results do not alone prove that supervision labels are unhelpful. Code: [dater.py](../dater.py), [Driver](../run_orl_dater.py), [Supplementary verification](../verify_orl_dater.py), [Rating Reading Entry](../evaluate_orl_dater.py).

<a id="results"></a>

## 5. Core results and before-and-after comparison

accuracy is %; the difference is pp (percentage points), ± is the sample standard deviation between splits. All tables clearly indicate categories; different seed groups do not count as matching gains, and SD is not filled in for a single FERET identity split. The figures of the paper are taken from Tables I/II/IV, and the statistical caliber of the original authors is not completely recoverable. The appendix retains all historical batches and original tables.

### 5.1 Historical shared settings at the paper's dimensions

This table is the preserved historical shared comparison. Use Section0.3 and README for the current gray81.84% and Gabor88.75% representatives; do not present the historical gray77.47% as the current result.

| data/number of times| method| our group| paper| difference pp|
|---|---|---|---|---|
| ORL／10 | PCA+LDA (Gray) | 83.22±1.76 | 82.20 | 1.02 |
| ORL／10 | CSA-2+LDA | 77.47±5.41 | 84.10 | -6.63 |
| ORL／10 | PCA (Gabor) | 86.88±1.63 | 86.60 | 0.28 |
| ORL／10 | CSA-3 | 90.19±2.37 | 94.40 | -4.21 |
| ORL／10 | PCA+LDA (Gabor) | 92.09±2.06 | 87.20 | 4.89 |
| ORL／10 | CSA-3+LDA | 79.66±2.77 | 90.90 | -11.24 |
| MNIST G30/P470／3 | PCA (Gabor) | 87.52±0.40 | 88.50 | -0.98 |
| MNIST G30/P470／3 | CSA-3 | 90.34±0.15 | 92.80 | -2.46 |
| MNIST G40/P460／3 | PCA (Gabor) | 88.58±0.37 | 90.50 | -1.92 |
| MNIST G40/P460／3 | CSA-3 | 91.04±0.25 | 92.40 | -1.36 |
| FERET q=50／1 | PCA+LDA (Gray) | 89.08 | 84.60 | 4.48 |
| FERET q=50／1 | CSA-2+LDA | 88.73 | 88.20 | 0.53 |
| FERET q=100／1 | PCA+LDA (Gray) | 90.87 | 90.60 | 0.27 |
| FERET q=100／1 | CSA-2+LDA | 94.25 | 92.20 | 2.05 |
| FERET q=200／1 | PCA+LDA (Gray) | 93.87 | 93.40 | 0.47 |
| FERET q=200／1 | CSA-2+LDA | 95.38 | 95.20 | 0.18 |

Source: [Full shared original table](../results/orl_protocol_audit/shared_comparison.csv). See §4.1 and Appendix A for method dimensions.

This table preserves the original shared results: ORL24→23 **79.66%** cannot be replaced by later87.84%,87.08%, or95%. Grayscale ORL CSA also has a gap, so the issue is not confined to Gabor. FERET is a fixed shared-cosine control, not the third-round validation winner.

### 5.2 ORL recent comparison: fixed input, optional participation extension reported separately

| Category/Input| seed | CSA24→23 | CSA390 | PCA24→23 | PCA33→25 |
|---|---|---|---|---|---|
| fixed baseline| 20–29 | 81.25±2.78 | 90.00±1.69 | 88.62±1.20 | 92.72±1.53 |
| TT＋HE | 20–29 | 78.31±2.94 | 89.56±1.24 | 87.75±2.42 | 92.34±1.10 |
| fixed context| 20–29 | 84.31±2.49 | 91.56±0.90 | 91.00±1.77 | 94.38±1.00 |
| gallery AInput| 20–29 | 87.81±3.62 | 91.06±1.24 | 90.66±1.75 | 94.06±1.06 |
| gallery B power| 20–29 | 87.78±3.10 | 90.94±1.37 | 90.72±1.69 | 94.16±1.28 |
| gallery C initialization／NN| 20–29 | 87.84±3.28 | 91.03±1.43 | 90.69±1.63 | 94.16±1.28 |
| Gallery optimization within cropping| 20–29 | 81.41±2.41 | 88.41±1.84 | 88.41±1.31 | 91.69±2.16 |
| Fixed 2π cropping| 4200–4219 | 80.12±3.49 | 88.66±2.71 | 88.81±2.47 | 92.33±2.09 |
| Fixed 2π context| 4200–4219 | 84.56±2.44 | 91.16±1.99 | 90.89±2.11 | 93.98±1.91 |
| fixed π cropping| 4200–4219 | 81.25±3.03 | 88.70±2.65 | 89.20±2.76 | 93.38±1.86 |
| Fixed π context| 4200–4219 | 87.08±2.30 | 90.09±2.46 | 91.08±1.48 | 94.14±1.69 |

The corresponding paper values are CSA24→23:90.90, CSA390:94.40, and PCA33→25:87.20. PCA24→23 has no corresponding paper row.

- ten split baseline→TT: low-dimensional CSA−2.94pp;→context+3.06pp. Context→gallery final C is +3.53pp, C is 87.84±3.28, −3.06pp from the paper; A→C is only +0.03pp. CSA390 final 91.03 is down 0.53pp from fixed context 91.56.
- Crop-only optimization gives81.25→81.41±2.41, only+0.16pp:2 wins,4 ties,4 losses; maximum85.625;0/10 splits reach90.9. All matched control methods decline. The1.75pp difference between the old79.66 and81.41 is not this round's paired improvement.
- twenty split 2π within the crop → π context 80.125 → 87.078125, the pairing +6.953125pp, 20/20 improved, still −3.82pp from the paper; the same budget PCA91.08 is still about 4.00pp higher.
- Fixed σ effect: low-dimensional CSA within clipping +1.125pp, context +2.515625pp, difference in difference +1.390625pp; only for descriptive factor evidence. The CSA390 context minus σ is −1.0625pp, so there is no common optimal input among the four methods.

### 5.3 MNIST: The original fixed process can be reported, but the limited optimization failed

| settings| old fixed three times| Original ten times| New gallery ten times| pairing changepp| paper| New-paper pp|
|---|---|---|---|---|---|---|
| G30 PCA | 87.52 | 86.67±0.74 | 86.94±0.81 | 0.27 | 88.50 | -1.56 |
| G30 CSA | 90.34 | 89.66±0.53 | 88.89±0.87 | -0.77 | 92.80 | -3.91 |
| G40 PCA | 88.58 | 88.03±0.46 | 88.26±0.86 | 0.23 | 90.50 | -2.24 |
| G40 CSA | 91.04 | 90.50±0.50 | 90.18±0.83 | -0.32 | 92.40 | -2.22 |

Under the same seed, CSA G30 dropped by 0.77pp, G40 dropped by 0.32pp, and PCA was +0.27/+0.23pp respectively; G30 CSA only input 89.44 in the stage and 88.89 in the final, and G40 only input 90.62 and final 90.18. The original 20–22 triple pairing CSA90.34→89.33, 91.04→90.34 also dropped. **You cannot calculate improvement by comparing the old mean three times to the new mean ten times.** The fixed process CSA>PCA direction is still in place; the reproduction gap is exposed and available as part of reproduction. There is no evidence that "the paper/TA requires Euclidean, so it must be changed back to Euclidean".

### 5.4 FERET: Close to the paper, but fixed control does not equal validation winner

Third-round validation selected PCA88.91/91.14/93.37 and CSA87.51/94.25/93.77. The fixed shared-cosine control gives PCA89.08/90.87/93.87 and CSA88.73/94.25/95.38. Those CSA controls exceed the paper88.20/92.20/95.20 by+0.53/+2.05/+0.18pp. This is one fixed identity split: no random-split SD or statistically significant recovery is claimed. The v1/v2 decreases, Sw-scaling/Euclidean controls, and LDA curves remain in the appendices and original files.

### 5.5 DATER: A supervised tensor extension with negative results

| Same2π crop input,20 splits | Direct24-dimensional NN | Ordinary LDA23 | Paired effect of adding LDA |
|---|---:|---:|---:|
| CSA | 74.33±3.95 | 80.13±3.49 | +5.80pp |
| PCA | 82.70±2.95 | 88.81±2.47 | +6.11pp |
| DATER | 71.64±3.18 | 67.11±3.59 | −4.53pp, dropped on 19/20|

DATER−CSA: Directly −2.69pp (4 wins, 2 draws, 14 losses), after LDA −13.02pp (20 losses); relative PCA is −11.06/−21.70pp, both 20 losses. The original CSA90.9 can only be used as a reference for different methods, not the DATER paper error. See §4.4 and §7.2 for iteration/numeric sensitivity restrictions, and all input/data/parameters of DATER cannot be negated based on this. Source: [Six groups of statistics](../results/orl_dater/summary.csv), [Pairing changes](../results/orl_dater/paired_changes.csv).

### 5.6 Expansion, Exploration and Cost: Which Numbers Cannot Enter Reproduction Master List

| work| Data/Results How| should be reported|
|---|---|---|
| shrinkage／New rank gallery selection| normal grayscale/Gabor78.56/82.47, shrinkage 84.13/84.75; subsequent Gabor normal 83.28±3.30, shrinkage 85.47±4.57| rank and regularization expansion, separated from the original 24→23 anchor point|
| fixed sample size| Same as P5, G2→G3→G5, CSA24+LDA81.30→88.10→94.50; CSA39089.80→93.95→97.45| More gallery improvements, non-original G2/P8 restoration paper|
| 100 fixed split| CSA24→23 mean 80.93, maximum 87.50; CSA32→28 mean 84.36, maximum 90.31; CSA39089.27, maximum 93.75| split sensitivity on existing photos|
| probe explores the highest| CSA32+LDA24 has a maximum of 95.00, and the same configuration has a mean of 86.42; CSA560 has a maximum of 97.50, and a mean of 91.43; CSA390 has a maximum of 97.19, and a mean of 92.00| indicates the configuration/seed selected according to probe; the original CSA24→23 has a maximum of 88.44 and a mean of 80.16|
| Rebuild/Compress| 40 fitting image, PCA d1…40, CSA r³, r1…40; RMSE and CR curves| Learning sample reconstruction, original definition √(SSE/N), non-per-pixel RMSE/unseen sample error|
| error example| stageC revised 224 items/added 111 new items; 158 unique CSA pairs and 249 unique PCA pairs within the same budget; 3200 records only 400 different photos| Explain and weigh case by case, without complete truth value, and do not identify the only cause and effect.|
| weight/deployment array| 830/618792 projected elements; counted group 228272/5171968 bytes| 745.5×/22.7× respectively, not called peak system memory|
| Local timing| Core Ultra9 275HX, two BLAS threads, 320 precomputation probe, CSA21.28–29.27ms, PCA59.67–82.14ms, pairing 2.08–3.29×| Projection + LDA + NN, exclude alignment/Gabor/training/IO/power consumption, 1 warm-up and 7 repetitions|
| probe Both eyes have a common ±1 original pixel| π context low-dimensional CSA average −0.08pp, worst direction mean −0.52, worst single split direction −1.875| 1280 items zero fitting score; does not cover monocular misalignment, rotation, and large offset|

<a id="critical"></a>

## 6. Critical analysis and insights from our group

The following materials can directly support the Critical Analysis required for screenshots; retain the degree of inference when writing, and do not write possible explanations as proven reasons.

| Analysis | Evidence | Interpretation / group contribution | Limits on the conclusion |
|---|---|---|---|
| The reconstruction target is inconsistent with the discrimination target.| Gabor24-dimensional PCA/CSA training total change energy 72.92%/20.76%, between classes 82.96%/23.62%; PCA classification with the same budget is higher| The low core with limited structure may not retain enough discriminative directions; supervised compression is proposed and DATER is measured in practice| Energy is not the amount of identity information; a negative DATER result does not prove that the target difference has been eliminated or that the label is unhelpful|
| Equal output dimension is not equal expressiveness | CSA uses separable Kronecker-style mode bases; PCA uses arbitrary vector bases; projection weights differ745.5× | Matched24→23 outputs control the representation budget and expose an accuracy/cost trade-off | Equal output dimension still differs in parameter count; original390/76 and390/24→23 comparisons also differ in budget |
| Small-sample LDA estimation | G2/Nc40; CSA24 has a relatively high Sw condition number. Removing shrinkage from selected winners lowers scores; moreG at fixedP5 helps | Shrinkage can reduce some instability; more fitting samples can help | Shrinkage is an extension, and more gallery samples also improve NN coverage; gains cannot be assigned solely to scatter estimation |
| LDA is not uniformly harmful | SameCSA24 representation77.00→79.66 with ordinary LDA; matched DATER-study controls CSA74.33→80.13 and PCA82.70→88.81 | Before/after controls on the same representation avoid the390-versus24 budget confound | DATER deteriorates after LDA; the effect depends on the preceding representation |
| Input geometry and boundaries matter | Eye-coordinate changes, Gabor support/padding, fixed context improvement, and a σ effect that changes with context | Controlled factors explain more than simply expanding a search | Context expands the effective field of view; these findings do not prove the original authors used it |
| Validation winners can lose on outer probes | MNIST CSA deteriorates; crop-only validation63.50→70.75→71.00% yields only+0.16pp externally; stagesA→C add only+0.03pp | Selection variance and differences in inner/outer sample sizes deserve analysis; failed stages are retained | Overfitting or distribution mismatch are possible explanations, not uniquely established causes |
| More iterations need not improve recognition | CSA3→10 produces zero changed predictions in two inputs and ≤3.8×10⁻¹² relative SSE improvement | Tmax3 is already stable in these specific CSA settings | This does not cover every initialization or DATER; most DATER runs reach their iteration cap |
| Repeated splits are not independent datasets | All ORL splits reuse400 photos, MNIST reuses5000, FERET uses one fixed identity grouping | Report descriptive means/SDs and paired wins/ties/losses | Millions of prediction records are not millions of new images and do not guarantee statistical significance |
| Exploratory maxima do not estimate generalization | Maxima95/97.5 accompany same-configuration means86.42/91.43;6003 candidates×200 splits | Separate maxima, configuration means, paper-dimension references, and training-only selection | A post-selected configuration mean is also not a new blind test or evidence of a global optimum |
| Original protocol details are incomplete | Best-result wording; unknown eyes/crops/Gabor/NN/splits/repetitions; TA lacks original records | Preserve uncertainty and provide auditable group choices | The gap is not proven to be solely a protocol error, and there is no basis for accusing the authors of seed selection |
| Strengths and engineering limits | Small mode bases, measured low projection cost, and some MNIST/FERET directions consistent with the paper | Useful representation-cost trade-offs for constrained settings | Timing excludes the full pipeline; counted arrays are not peak memory; small historical datasets do not establish modern SOTA |

**Reportable group insight:** Separable tensor structure trades smaller projection parameters for restricted expressiveness. Reconstruction, low output budgets, and small-sample discrimination can conflict. The fixed ORL factors show that input choices affect part of the gap, but they establish neither a unique cause nor the paper's low-dimensional CSA advantage. Failed ablations, matched-budget controls, frozen sources/selections, and independent checks make the full-reproduction study and its numerical discrepancies auditable.

**Future work, not executed:** Independent new data and manually annotated eye ground truth; external validation of a few preregistered inputs; single-factor studies of DATER convergence, scaling, and positive-definite handling; reconstruction of unseen samples; end-to-end training/inference and peak memory. Define protocols and controls before execution, and label new regularization/objectives as extensions. No additional ORL grid or MNIST/FERET tuning is launched here, and these suggestions are not counted as completed work.

<a id="verification"></a>

## 7. Verification, reuse and rerun

### 7.1 Verified content and strength of evidence

| Verification level | Work completed | Limits |
|---|---|---|
| Basic Mathematics| non-square mode product, unfold/fold, CSA conditional update/projection/inverse transformation, PCA vector equivalent, ordinary LDA/NN, RMSE/CR| supports formula implementation and non-author unknown parameter proof|
| Data/Input| Original image/index/feature hash; eye point mapping; FFT spatial convolution, the maximum absolute error in the early stage is about 1.22e−7; later float32 cache is checked according to tolerance| The target eye point mapping is correct and does not mean that the automatic eye point is a true value.|
| Select integrity| inner learning/verification isolation, candidate and tie-break recalculation, source code/data/configuration freezing, pre-probe verification| Some approximate pre-screening and small inner layer size restrictions are still there; not the full history blind test|
| ORL three inputs| 120 models, 38400 predictions, 60 CSA independent three rounds of recalculation, 30 historical baseline correct numbers| All actual branches are retained|
| ORL unknown parameter| 416 selected inner layer CSA recalculation, 72000 verified predictions, 120 new outer layer and 64000 new/historical outer layer predictions| Not refitting all 3520 inner models one by one independently|
| ORL cropped| 304 selected inner CSA recalculation, 22400 inner prediction, 20 new CSA recalculation/20 PCA equation, 40 historical replay, 25600 outer prediction| 40 new outer layer + 40 historical rating, not 80 new fitting|
| fixed 2×2 and disturbance| 320 model, 160CSA independent recalculation, 160PCA verification, 102400 clean prediction; 1280 zero fitting score, 409600 disturbance prediction and save file readback| A total of 512,000 duplicate records, non-512,000 independent photos|
| MNIST | 1000 inner fitting records, 160 outer scores, 744000 repeated predictions; save model deduplication and sampling value verification| Each candidate cannot be said to be independently refitted verification|
| DATER | 1194 actual trajectory updates, 20 LDA, 120 scores/38400 predictions; 20 free reference recalculation sensitivity| Strictly free path failed, final difference cannot be omitted|
| Exploration/Sample Size| Save full exploration score, near/exceed index and best replay; sample size 90 models/64400 predictions| explores non-all 6003×200 independent refitting verification; record reuse does not count new experiments|

Recent batches save `protocol`, `source_snapshot`, input/selection/model freeze, raw scores, predictions, verification and supplementary readback. Not all old batches have the same format. Manually supplemented readback/visual verification is not a standard stage automatic product. If complete reconstruction is required after re-running, corresponding analysis must be performed. Each verification count may include multiplexing and should not be added to the sample size for independent experiments.

### 7.2 Failure and correction records that must be kept

The first canvas-interpolation preflight failed; it was corrected before scoring and the [failure record](../results/orl_fixed_input_extensions_preflight/preflight_failure.json) is retained. A later change corrected only a verification path: see the [verifier amendment](../results/orl_fixed_input_extensions/verifier_amendment.json). It did not change fitted models or scores.

DATER Strict 1e−9 comparison of initial free path independent scatter failed in seed4200 round 8 mode1, see [initial verification failure](../results/orl_dater/initial_verification_failure.json). Keep the original model/source code/trajectory, update the verification 1194 with the actual trajectory independent scatter and Sw whitening leading direction, and do another 20 free reference recalculations. The final maximum difference in the free direction is about 1.01e−5, the projection subspace is about 1.97e−6, the gallery core is about 1.85e−5, and the stop lengths are all the same; **It is not claimed that the free round-by-round or probe predictions are completely equal.** Actual trajectory verification and sensitivity are different evidences.

DATER For the first time scoring, the control JSON is read as CSV, resulting in KeyError and failure before successful scoring. Added [evaluate_orl_dater.py](../evaluate_orl_dater.py) that only repairs reading and freeze before scoring, see [reader failure](../results/orl_dater/evaluation_reader_failure.json). The fitted model and history remain unchanged. Rerun must use supplementary verification and scoring entries, and the known failed path of the original driver cannot be used as the default.

### 7.3 our group contribution, reuse sources and environment

Our group implements CSA, PCA, ordinary/shrinkage LDA, Gabor and DATER, data flow, experiment/parameter selection, independent verification, plotting and result files from the paper; the teaching team confirms that there is no code/hyperparameter record of the original authors to provide. NumPy/SciPy provides arrays, linear algebra, FFT and distance; Pillow/OpenCV provides images, affine and detection; Matplotlib drawing, threadpoolctl controls threads, and YuNet detector/model is a reuse tool. **It cannot be said that detectors, BLAS, and library feature solving are also implemented from scratch by our group.** Public submissions must list dependencies/model sources, licenses, and disclose the use of auxiliary tools in accordance with course rules.

Dependencies see [requirements.txt](../requirements.txt): NumPy2.4.6, SciPy1.17.1, Pillow12.3.0, Matplotlib3.11.1, threadpoolctl3.6.0; [Preprocessing dependencies](../requirements-preprocess.txt)OpenCV headless4.12.0.88, press README `--no-deps --target .deps`, do not change the system settings. The current DATER records Python3.11.9; the actual environment of each historical batch is subject to execution/environment, and it is not assumed that all versions are consistent.

```powershell
# In COMP3314GP, prepare your own environment for the first time
python -m pip install -r requirements.txt
python -m pip install --no-deps --target .deps -r requirements-preprocess.txt
```

All ORL, MNIST, and FERET datasets, labels, prepared arrays, generated feature/model caches, image-bearing sample figures, credentials, and private access-request letters are omitted from the public repository. Acquisition/reconstruction methods, scripts, result tables, split indices, and verification records are retained. See the English [README](../README.md) for the public checkout's scope and reconstruction limitations.

### 7.4 When taking over, read the existing results first, and then rerun as needed.

The existing files are sufficient to write the material without having to search again for writing purposes. The verification command may rewrite the verification/analysis file and save the required existing records before execution; the commands are listed here for subsequent use, and the experiment is not run this time. The prepare/evaluate default directory of the source script should not be overwritten.

| work| Correct entry/result| Specific rerun stage|
|---|---|---|
| Original sharing/gallery protocol audit| [audit_orl_protocol.py](../audit_orl_protocol.py)，`orl_protocol_audit` | [Detailed operation instructions](./REPORT.md#outputs)|
| Normal／shrinkage／rank special| [optimize_csa_lda.py](../optimize_csa_lda.py)、[refine_orl_csa.py](../refine_orl_csa.py) | [Normal／shrinkage](./REPORT.md#csa-lda-optimization), [rank optimization](./REPORT.md#orl-csa-refinement)|
| MNIST limited optimization| [optimize_mnist_protocol.py](../optimize_mnist_protocol.py) | [prepare, select, freeze, score, verification](./REPORT.md#mnist-bounded-optimization)|
| FERET | [prepare_feret.py](../prepare_feret.py)、[select_feret.py](../select_feret.py)、[verify_feret.py](../verify_feret.py) | [FERET and command](./REPORT.md#feret), [Complete command segment](./REPORT.md#outputs)|
| Three inputs| [run_orl_fixed_inputs.py](../run_orl_fixed_inputs.py), fixed output directory, no `--output` option| [Three input instructions](./REPORT.md#orl-next-directions); do not make up new output parameters for it|
| the paper's dimensions unknown/optimized within cropping| [optimize_orl_unknowns.py](../optimize_orl_unknowns.py)、[optimize_orl_ta_crop.py](../optimize_orl_ta_crop.py) | prepare→select→verify_selection→evaluate→verify→analyze; new `--output`|
| σ × context, error, cost, disturbance| [run_orl_controlled.py](../run_orl_controlled.py) | prepare→errors→costs→evaluate→verify→analyze→robustness; new `--output`|
| sample size| [run_orl_sample_size.py](../run_orl_sample_size.py) | `--verify`/`--analyze`/`--diagnostic`, not the general `--stage`; [specific instructions](./REPORT.md#orl-sample-size)|
| probe exploration| [search_orl_best.py](../search_orl_best.py) | [Full protocol/replay](./REPORT.md#orl-best-search); currently does not automatically run the grid again|
| DATER | Supplementary entry sequence below | Requires controlled ORL inputs and reused CSA/PCA controls; read the [full protocol](./REPORT.md#orl-dater) first |

```powershell
# DATER complete rerun example: using an output directory that does not yet exist, you need to prepare the data/controlled comparison of this project
python run_orl_dater.py --stage prepare --output results/orl_dater_rerun
python run_orl_dater.py --stage fit --output results/orl_dater_rerun
python verify_orl_dater.py --output results/orl_dater_rerun
python evaluate_orl_dater.py --output results/orl_dater_rerun
python run_orl_dater.py --stage verify --output results/orl_dater_rerun
python run_orl_dater.py --stage analyze --output results/orl_dater_rerun
```

<a id="submission"></a>

## 8. Report, presentation and Q&A preparation

### 8.1 Selecting content for a 3–4-page LaTeX report

| content| Recommended length| Materials used|
|---|---|---|
| Problem, motivation, contribution and paper identity| About 0.5 pages| §2.1; Accurately cite author/journal|
| Methods, updated/reconstructed formulas, and course connections| About 1 page| §2.2–2.3, draw object → mode base → core → LDA → NN|
| reproduction scope, protocol and three original shared master tables| About 1 page| §3, §5.1; compress the table but retain clear gaps, FERET single time, MNIST three times|
| Controlled ORL, critical analysis and insights from our group| About 0.75 pages| §5.2＋§6; It is recommended to choose σ×context and equal budget/cost, and not block all old grids|
| Limitations, extensions, code, PIE license and references| remaining space| DATER negative result brief description; full table and protocol put accessible repository materials|

shared settings at the paper's dimensions and extensions are labeled with independent tables/independent rows; the figure title indicates "paper" or "our implementation", data set/input/number of dimensions/number of splits. The best number in the original paper cannot be called mean in the legend as our group mean. If 95/97.5 needs to appear, it should be placed in the exploration deviation discussion or backup page, and should not be used as a reproduction title score.

### 8.2 9 minutes presentation + 3 minutes Q&A

| period| content| Screen/Evidence|
|---|---|---|
| 0–1 minute| question, why tensor, paper contribution| An ORL picture + 40 channels/core diagram|
| 1–3 minutes| CSA target/alternative update/relationship with PCA and LDA| A formula, a flow chart and a shape without reading the source code|
| 3–4 minutes| Actual scope, TA confirmation and unknown, PIE omitted| Concise protocol sheet and data photo source|
| 4–6 minutes| Three data sets share anchor points and ORL fixed factor evidence| Main table + fixed 2×2 result chart, clear mean/SD/expansion|
| 6–8 minutes| Critical analysis, errors/costs and negative DATER results| A set of real error examples, accuracy/weighted cost, and negative results|
| 8–9 minutes| Team understanding, limitations, reviewable code and learnings| Research conclusion + real public URL/two-dimensional code, do not fill in fake links before publishing|

members should attend the presentation/Q&A. The work can be divided according to "method/protocol implementation/result analysis", but each person can at least explain the goals, data protocol and result caliber. The backup page displays the complete dimensions, Gabor settings, statistics and failure verification, and the main display does not squeeze in all history tables.

### 8.3 Q&A available answers

| Possible problem| Evidence-based answer points|
|---|---|
| Why didn’t it reach ORL90.9?| Clear sharing gap; unknown original protocol, structural constraints/low-dimensional targets and small sample estimation may be involved; controlled input improvement but no single cause confirmed|
| the paper ／TA said Euclidean?| NN has been clarified, the specific recognition distance has not been restored; the Euclidean tensor norm in the reconstruction is not equal to the recognition metric; our group shared convention and ablation transparency|
| Isn't 95%/97.5% more than the paper?| is the extreme value selected according to the probe and some dimensions are different; with the same configuration, the mean is low and cannot replace the scheduled average or independent test.|
| Why is optimization declining?| The verification target, internal and external sample size and candidate variance may cause; the actual decline is retained, the winner is not changed according to the probe, and the only reason is not separately proven Does|
| fully comply with TA?| Clear quantity/size/NN/CSA Tmax3/LDA budget reservation; unknown details our group settings, expand single column; TA allows disclosure of differences not equal to confirmed parameters Why is|
| DATER worse?| Negative results under fixed settings in this round; mostly to the iteration upper limit, numerical sensitivity, directional geometry and post-LDA adaptation; not attributed to the supervision itself and no matching original ORL rows|
| Does LDA cause poor CSA?| is the same as 24-dimensional CSA plus LDA, with budgets ranging from 390 to 24 → 23; small sample Sw may be unstable, shrinkage is effective but is an extension|
| How much faster and cheaper is CSA?| The specified weight is 745.5×, the counted group is 22.7×; the pre-computed feature local stage is 2.08–3.29×, excluding Gabor/training, and is not called end-to-end.|
| Why omit PIE?| failed to obtain and the distribution rights belong to CMU; the author has no distribution rights and the teacher allows omission; no other PIE is used to impersonate|

Suggested English scope sentence: *We independently implemented CSA and completed full reproduction within the instructor-approved ORL, MNIST, and grayscale FERET scope. Unspecified implementation choices and numerical discrepancies are reported explicitly. Extensions and probe-selected exploratory maxima are presented separately.*

PIE available sentences: *We were unable to obtain the original CMU PIE dataset within the project timeframe. We omit its experiments with the instructor's permission; our reproduction scope is ORL, MNIST, and grayscale FERET.* The details of the distribution rights reply should be supplemented at the source. Do not change "unobtainable" to "data does not exist".

### 8.4 Completion status and companion takeover list

**Completed:** Topic selection/study and reply archiving, three database data and implementation, all experiments and verification of this article, DATER expansion, result interpretation and material organization. **Not yet completed:** Formal 3–4 page LaTeX report, 9-minute slide show/rehearsal, full fresh-checkout rerun of all historical dependencies, member division of labor/final submission.

1. Check the course requirements according to §1, and master the main lines of §2–6 first; use the appendix to search for details, and do not continue reading the entire historical account.
2. Check main table values/figure titles/references; select fixed input to compare causal boundaries and equal budget costs, and retain DATER/TT/MNIST optimization failure.
3. Clarify our group's implementation, reuse tools and auxiliary sources in the final report; cite the paper, Gabor, DATER and other actually used documents.
4. Organize the public repository: only publish code, environment, legal small results/graphs, protocols and acquisition instructions; exclude restricted data/cache/credentials. The new environment runs a minimal process and verification with independent output, and then provides the real URL.
5. Write reports, make presentations, and repeat Q&A with all employees; complete data appendices are kept in the repository, and PIE is not counted as completed. This article only consolidates existing work and does not replace these final deliverables.

<a id="all-experiments"></a>

## Appendix A. All experimental families and historical data

Expand by topic; each experiment family has data, comparisons, and boundaries. The following is organized by theme from the overview of existing experiments, retaining the original values ​​and sources; Appendix B supplements the recent SD/range, and Appendix C provides complete step-by-step results. “—” in the table indicates that the abstract is not expanded, please refer to the original table for details, and the score is non-zero. Different versions, inputs or splits cannot be combined into an optimal solution.

<details>
<summary>A2. ORL all experimental batches and directions</summary>

| Experimental batch/direction What| actually does| Key results or findings| Difference/expansion boundary from the paper|
|---|---|---|---|
| Early grayscale fixation experiment and regression| Compare CSA centering and verification of different running versions| Grayscale CSA＋LDA: no centering 78.23, centering 76.67; PCA69.69／70.21| Early input and distance agreement, not the current shared master table|
| Grayscale distance/LDA column scale diagnosis| Sw normalization/unit-norm columns, Euclidean/cosine, centering/not centering| centering, unit-norm columns cosine: CSA79.38, PCA81.25| TA and the paper have not confirmed which distance is used; only for sensitivity control|
| Early grayscale verification options| 5 split, compare interpolation, equalization, dimensionality, initialization, distance, number of iterations| CSA default 79.42, fixed improvement 82.00, protocol selection 81.58, expanded selection 83.50; PCA70.92/82.25/82.58/81.50| **G2/V2/P6**, not G2/P8; expanded candidates include new dimensions and Tmax10|
| Early recognition/rebuild running v1/v2| implements recognition, curve and save predictions, and corrects the input process| ORL ordinary process: pure CSA78.23/77.40; CSA+LDA65.83/66.77| Historical input version; version differences are not directly regarded as controlled optimization gains|
| Geometry and five-branch comparison| Old alignment, eye point correction, geometric correction, combination correction, direct resize| Pure CSA77.40／77.60／71.98／71.98／85.31; CSA＋LDA66.77／65.94／56.77／54.90／78.85| The direct resize branch does not keep TA’s eyes aligned and is only used for diagnosis.|
| Manual review of eye points| Corrected 6 Haar eye spots, including glasses and accidental nose cases| Save the specific coordinates and reasons, and rerun the relevant branches| our group approximate annotation, not the original authors eye points or complete artificial ground truth|
| Gabor single factor diagnosis| padding, support, wavelength, σ, square root, normalization, sampling offset, pooling, channel RMS| input parameters will change the score, see 10.4 for details| Sensitivity analysis of undisclosed parameters; some amplitudes are processed as extended|
| CSA iteration number diagnosis| The same model is forced to continue from 3 rounds to 10 rounds| The pure CSA of the two branches is still 77.60/85.31, with a predicted change of 0; the relative SSE improvement after 3 rounds is ≤3.8×10⁻¹²| Tmax10 only diagnoses, does not replace recognition Tmax3|
| Gabor radius rounding verification| Isolate core edge length differences caused by floating point rounding| compared to pure CSA85.31→85.21, the main gap is not resolved| numerical implementation verification, not a new method|
| Effective area/intensity/resampling four-step diagnosis| whole hist、valid hist、z-score、Lanczos | Gabor CSA＋LDA65.94／66.35／66.25／68.96 | Effective area normalization and two-stage resampling are processed for our group|
| core supports × padding 2×2| adaptive／39×39 × reflect／zero | CSA＋LDA69.17／71.46／73.02／72.81; pure CSA76.56／82.60／81.04／83.23| The core and boundary are unknown; the input is different from the subsequent YuNet process|
| 10 splits and 64-dimensional comparison after four steps of freezing| Original paper configuration and PCA64/CSA64| CSA39082.97, CSA24+LDA23 is 71.69; PCA64 is 82.81, CSA64 is 79.25| 64-dimensional equal budget diagnosis; historical results before subsequent eyepoint audits|
| YuNet／Protocol re-audit| Correct the source and cropping of eye points, unify input and NN, and check the dimension of the paper| Shared anchor points CSA39090.19, CSA24+LDA23 are 79.66| Unknown setting is still our group convention|
| gallery first round selection| Verify within each gallery group, share input and rules| Grayscale CSA79.75, Pure CSA89.72, Gabor CSA＋LDA80.34| gallery-only validation selection, cannot be mixed with fixed the paper's dimensions anchor point|
| Additional balanced rank search| Expand CSA mode rank candidates| Grayscale 78.44, Pure CSA88.97, Gabor CSA＋LDA80.34| Compared with the front wheel -1.31/-0.75/about 0pp, there is no stable improvement|
| CSA＋LDA common correction ablation| centering, random initialization, z-score, L2, jet L2, channel RMS| Gabor baseline 79.66; centering 77.47, random 80.22, z-score80.47, jet L2 is 74.84, channel RMS81.59| Most of them are not enough to explain the gaps in the paper; the highest ablation is not set as the main result according to probe.|
| Change gallery to select target| Change the average of six methods to two CSA objectives to compare LDA dimension selection| Grayscale 77.47→75.19/74.56; Gabor79.66→79.31/78.69| Optimization failed, retain the old main table|
| ordinary LDA/shrinkage optimization respectively Select input, amplitude, rank, LDA dimension, α in| gallery| Normal grayscale 78.56, Gabor82.47; shrinkage grayscale 84.13, Gabor84.75| new rank must be disclosed; shrinkage is not the original ordinary LDA|
| Gabor targeted iteration| Low-dimensional CSA preliminary screening, flexible mode rank, HOSVD, amplitude normalization| Normal 83.28±3.30; shrinkage 85.47±4.57; shared pure CSA89.97| Changes such as the previous dimension/initialization, not the original 24→23 score|
| 100 split fixed diagnostics| fixed input/distance/initialization, test the impact of random split| CSA24→23 mean 80.93, maximum 87.50; CSA32→28 mean 84.36, maximum 90.31; CSA390 mean 89.27, maximum 93.75| mean is tied with the highest; same as 400 pictures, non-independent new data|
| 200 split finite grid exploration| Multiple configurations, multiple seeds, filter the highest by probe| CSA＋LDA is up to 95.00, pure CSA is up to 97.50| **probe explore extreme value**, not an independently verified estimate|
| Fixed probe sample size expansion| G2⊂G3⊂G5, share P5, leaving G2/P8 anchor points| CSA24＋LDA81.30→88.10→94.50 | Changed the number of training/gallery and test protocol, which is not the success of the original G2/P8|
| Three sets of fixed inputs| baseline, TT lighting, context; 10 split 120 fitting| CSA24＋LDA81.25／78.31／84.31 | TT and context are extended, negative results are retained|
| Three-stage optimization of unknown parameters| In the gallery, enter → power → initialization / NN, and score after freezing| CSA24＋LDA87.81→87.78→87.84 | Contains context/power expansion; the net benefit of the last two stages is small|
| Crop within the paper's dimensions Limited optimization| σ× padding, initialization, NN, do not use context/power| CSA24+LDA81.25→81.41, only +0.16pp| retains clear TA conditions, unknown parameters are not confirmed by the author|
| σ × context fixation experiment| Four inputs × 20 split × four methods, 320 fitting| CSA24＋LDA80.13／84.56／81.25／87.08 | The context is extended; fixed control, not gallery selection winner|
| Eyepoint perturbation, errors and costs| reuse model, zero new fitting| 1280 disturbance score; see 10.10 for error examples and costs.| Robustness/Interpretation/Efficiency Extension|
| DATER supervised tensor extension| input 20 new models and reuse CSA/PCA| Direct 24-dimensional 71.64, plus LDA23 is 67.11| New method; 19/20 to the upper limit of 20 rounds, no improvement|

Batch sources: [Early Grayscale Fixation/Regression](../results/orl_gray_verified/summary.json), [Distance Diagnosis](../results/orl_metric_diagnosis_verified.json), [Grayscale Verification Parameters](../results/orl_gray_improved/summary.json), [v1](../results/available_reproduction/summary.json)/[v2](../results/available_reproduction_v2/summary.json), [Five Branches](../results/orl_branches_v3/summary.json), [6 Eye point review](../results/orl_eye_review_v2/changes.json), [Compulsory 10 rounds](../results/orl_gabor_forced10/fixed_results.csv), [Radius rounding](../results/orl_gabor_radius_rounding/summary.json), [Four-step diagnosis Broken](../results/shared_protocol_final/step4/summary.json), [Protocol Audit](./REPORT.md#orl), [CSA+LDA Special](./REPORT.md#csa-lda), [General/ shrinkage optimization](./REPORT.md#csa-lda-optimization), [targeted iteration](./REPORT.md#orl-csa-refinement). Each detailed section retains the complete PCA comparison, SD, parameter range and verification boundary.

</details>

<details>
<summary>A3. Gabor single factor main data</summary>

The order of the two columns is pure CSA/CSA+LDA, three split means; the direct resize branch is only for comparison. —Indicates that this branch has not been expanded in this summary, and does not mean that it has zero points or that it has not been executed.

| Change| binocular processing branch| direct resize comparison| Extension/Difference|
|---|---:|---:|---|
| original baseline| 77.60／65.94 | 85.31／78.85 | Fixed input at that time|
| zero padding| 83.65／74.27 | 87.40／85.62 | The convolution boundary is unknown|
| fixed 39×39 core| 81.04／71.25 | 91.77／84.17 | truncation support convention|
| Basic wavelength 2| 78.44／67.40 | 90.73／81.46 | non-confirmed author parameter|
| σ=π | 83.13／75.73 | 90.52／86.88 | Envelope sensitivity|
| wrap padding| 75.42／66.15 | — | boundary diagnosis|
| square root response| 80.21／71.77 | — | Nonlinear amplitude expansion|
| jet L2 | 77.40／60.63 | — | Change the weight of each pixel channel|
| tensor L2| 77.71／66.25 | — | Amplitude normalization|
| training channel RMS| 80.21／68.85 | — | Estimated scaling only from fitting image|
| sampling offset 11| 78.02／66.46 | — | Downsampling position diagnosis|
| 2×2 mean pooling| 77.81／66.77 | — | replace stride sampling|

Source: [Full Diagnosis](../results/orl_gabor_diagnosis/summary.json). The variations cannot be combined into a set of method-by-method optimal parameters.

</details>

<details>
<summary>A4. The recent paper's dimensions ORL input/parameter results side by side</summary>

mean unit %; four methods in the same batch share input and classification rules. The two seed groups are marked separately, and pairing improvements are not calculated across groups; PCA24+LDA23 is a new equal-budget diagnosis, and there is no corresponding line in the original paper.

| Batch/Input| seed| CSA24＋LDA23 | CSA390 | PCA24＋LDA23 | PCA33＋LDA25 |
|---|---|---:|---:|---:|---:|
| fixed baseline| 20–29 | 81.25 | 90.00 | 88.63 | 92.72 |
| TT lighting + balance| 20–29 | 78.31 | 89.56 | 87.75 | 92.34 |
| fixed context| 20–29 | 84.31 | 91.56 | 91.00 | 94.38 |
| gallery option A: input| 20–29 | 87.81 | 91.06 | 90.66 | 94.06 |
| gallery selection B: power| 20–29 | 87.78 | 90.94 | 90.72 | 94.16 |
| gallery option C: initialization ／NN| 20–29 | **87.84** | 91.03 | 90.69 | 94.16 |
| Gallery optimization within cropping| 20–29 | 81.41 | 88.41 | 88.41 | 91.69 |
| Fixed 2π cropping| 4200–4219 | 80.13 | 88.66 | 88.81 | 92.33 |
| Fixed 2π context| 4200–4219 | 84.56 | **91.16** | 90.89 | 93.98 |
| fixed π cropping| 4200–4219 | 81.25 | 88.70 | 89.20 | 93.38 |
| Fixed π context| 4200–4219 | **87.08** | 90.09 | 91.08 | 94.14 |
| The corresponding number of the paper| Original paper| **90.90** | **94.40** | No corresponding line| **87.20** |

| Controlled comparison| CSA24+LDA23 changes| Paper Gap/Implications|
|---|---:|---|
| baseline → TT, 10 split| −2.94pp | Lighting combination regresses at this setting|
| baseline → context, 10 split| +3.06pp | 84.31%, still lower than the paper 6.59pp|
| Context→Final gallery selection C| +3.53pp | 87.84%, still lower than the paper 3.06pp; including extensions|
| input A→final C| about +0.03pp| There will be very little benefit from subsequent complicated selections.|
| clipping inner baseline → limited optimization| +0.16pp | 81.41%, still lower than the paper 9.49pp|
| 2π cropped inner → π context, 20 split| +6.95pp, 20/20 improvement| 87.08%, still lower than the paper 3.82pp; fixed expansion|

Source: [Three inputs](../results/orl_fixed_input_extensions/comparison.csv), [Three-stage parameter selection](../results/orl_unknown_parameters/comparison.csv), [In-crop optimization](../results/orl_ta_crop_optimized/comparison.csv), [20 split fixed control](../results/orl_controlled/summary.csv). SD and all negative phases are shown in the original table.

</details>

<details>
<summary>A5. Sample size expansion and probe exploration maximum </summary>

The sample size experiment is fixed at P5 for each split, G2⊂G3⊂G5, and the following is 10 split mean. More training images change representation learning, LDA estimation, and gallery coverage at the same time, and all gains cannot be attributed to a single link.

| method| G2/P5 | G3/P5 | G5/P5 | G2→G5pp |
|---|---:|---:|---:|---:|
| CSA390 | 89.80 | 93.95 | 97.45 | +7.65 |
| CSA24 | 76.40 | 82.95 | 90.60 | +14.20 |
| CSA24＋ordinary LDA 23| 81.30 | 88.10 | 94.50 | +13.20 |
| CSA24+ shrinkage LDA23, α=.15| 81.90 | 88.40 | 93.90 | +12.00 |
| PCA24 | 82.70 | 88.00 | 93.45 | +10.75 |
| PCA24＋ordinary LDA 23| 88.45 | 94.05 | 97.45 | +9.00 |
| PCA24+ shrinkage LDA23, α=.15| 88.20 | 93.85 | 97.25 | +9.05 |

**The high score of G5 is not the original G2/P8 reproduction success.** Source: [Sample Size Agreement and Verification](./REPORT.md#orl-sample-size), [CSA Summary](../results/orl_sample_size/summary.json), [PCA Control](../results/orl_sample_size/pca_control/summary.json).

200 split maximum independent listing of finite grid; configuration and split are both selected by probe scores, and the mean of the same configuration also comes from the configuration that has been selected, and is not an independent verification estimate.

| configuration| probe maximum| Same configuration 200 split mean ±SD| Paper Reference| maximum −paper pp|
|---|---:|---:|---|---|
| CSA32＋ordinary LDA 24| **95.00** | 86.42±2.45 | CSA24＋LDA23：90.90 | +4.10, different dimensions|
| Pure CSA560| **97.50** | 91.43±1.86 | CSA390：94.40 | +3.10, different dimensions|
| Pure CSA390| **97.19** | 92.00±1.92 | 94.40 | +2.79 |
| Original CSA24+LDA23| **88.44** | 80.16±2.90 | 90.90 | −2.46 |

Source: [Exploration Protocol/Statistical Caliber](./REPORT.md#orl-best-search), [maximum](../results/orl_best_search/best_results.json), [the paper's dimensions highest](../results/orl_best_search/paper_dimension_best.json), [All Configuration Statistics](../results/orl_best_search/configuration_summary.csv).

</details>

<details>
<summary>A6. DATER independent method extension</summary>

input within the same 2π crop, 20 splits; 20 new DATER models and 40 reused CSA/PCA models. DATER the paper does not match the ORL24-dimensional number. The CSA paper 90.9 is only used as a reference for different methods and is not called reproduction error of the DATER paper.

| method| 24-dimensional direct NN| plus ordinary LDA 23| plus LDA pairing changes|
|---|---:|---:|---|
| CSA | 74.33±3.95 | 80.13±3.49 | +5.80pp |
| PCA | 82.70±2.95 | 88.81±2.47 | +6.11pp |
| DATER | **71.64±3.18** | **67.11±3.59** | **−4.53pp, dropped on 19/20**|

DATER's direct NN is 2.69pp lower than CSA, and 13.02pp lower after adding LDA; the 19/20 model reaches the upper limit of 20 rounds, so it cannot be said that all convergence or the entire DATER is negated based on this. Tmax20, ε.001 and the direction column scale are our group convention, TA's CSA Tmax3 is not equal to DATER Tmax3; no ridge/fitting QR/singular fallback. Source: [Detailed protocol, negative results and numerical sensitivity](./REPORT.md#orl-dater), [Six sets of data](../results/orl_dater/summary.csv).

</details>

<details>
<summary>A7. All MNIST experiments and before and after data</summary>

Three types of results are separated: shared fixed process, method-by-method historical parameter selection, and subsequent limited optimization shared across methods. Historical method-by-method parameter selection allows PCA/CSA to be processed differently without replacing the shared table; cubic and decimal means cannot be mixed for gain.

| settings| shared fixed 3 split| History method-by-method parameter selection 3 split| original process 10 split| The latest shared selection 10 split| paper| latest-paper pp|
|---|---:|---:|---:|---:|---:|---:|
| G30，PCA60 | 87.52 | 90.12 | 86.67 | 86.94 | 88.50 | −1.56 |
| G30，CSA810 | 90.34 | 90.22 | 89.66 | 88.89 | 92.80 | −3.91 |
| G40，PCA50 | 88.58 | 90.75 | 88.03 | 88.26 | 90.50 | −2.24 |
| G40，CSA975 | 91.04 | 91.22 | 90.50 | 90.18 | 92.40 | −2.22 |

| Additional experiments| Actual range and results The difference/conclusion between| and the paper|
|---|---|---|
| Four-step limited optimization| data audit; adaptive／39×39 × reflect／zero; gallery 5-fold select input, NN, identity／HOSVD; score after freezing| the paper's dimensions, quantity, Tmax3 remain unchanged; input/distance is our group option|
| Staged ablation| G30 CSA89.66→Input only 89.44→Final 88.89; G40 90.50→Input only 90.62→Final 90.18| The input income is different from the final selection and cannot only be reserved for higher stages|
| Same as 20–22 three seeds read back| CSA G30 90.34→89.33；G40 91.04→90.34 | compared with the original three seeds|
| Euclidean / mean-centered cosine fixed ablation| CSA G30 89.30／89.63、G40 90.05／90.48；PCA85.43／87.53、87.33／88.60 | cosine in this ablation is higher; TA and the paper do not specify must be Euclidean|
| implementation and prediction verification| 1000 inner candidate fitting records; 160 outer scores, 744000 repeated predictions verification| supports reliable implementation, not 744,000 independent pictures|

The latest limited optimization does not improve CSA, and negative results are retained; the fixed process still supports the direction that CSA is better than PCA, but it cannot be called accurate reproduction of all values. Source: [MNIST detailed evidence](./REPORT.md#mnist), [Latest before and after table](../results/mnist_protocol_optimized/comparison.csv), [Original three matchings](../results/mnist_protocol_optimized/original_three_seed_comparison.csv), [History method-by-method selection of parameters](../results/available_tuned/summary.json).

</details>

<details>
<summary>A8. FERET verification selection participates in fixed comparison</summary>

vectors are all arranged according to q50/q100/q200; they are all fixed identity splits, and there is no repeated identity split SD. Candidates vary from round to round, you cannot just keep the higher round or replace the winner line by line.

| experiment| PCA＋LDA | CSA＋LDA | caliber and difference|
|---|---:|---:|---|
| First round of verification and selection| 88.91／91.14／91.16 | 88.03／92.97／93.47 | historical candidate collection|
| Second round of verification selection| 89.08／90.78／91.56 | 84.80／94.06／92.96 | Regressed after candidate change, retained|
| The current third round of verification selection| 88.91／91.14／93.37 | 87.51／94.25／93.77 | Actual verification of selected results|
| fixed normal Euclidean| 88.91／91.14／93.37 | 88.03／92.97／94.97 | fixed wide input, unit-norm columns direction|
| Fixed shared cosine| 89.08／90.87／93.87 | 88.73／94.25／95.38 | Fixed comparison used by shared master table|
| paper| 84.60／90.60／93.40 | 88.20／92.20／95.20 | The details of the author's processing are not completely known.|

Also save the Sw metric column scale + Euclidean control and LDA dimension curve; q200 fixed cosine CSA95.38 is higher than the verification selected 93.77, and cannot be renamed the verification winner. Source: [First round](../results/feret_validation_selected/fixed_results.csv), [Second round](../results/feret_validation_selected_v2/fixed_results.csv), [All results of the third round](../results/feret_validation_selected_v3/fixed_results.csv), [FERET detailed explanation](./REPORT.md#feret).

</details>

<details>
<summary>A9. Reconstruction, numerical verification, error cases, cost and eyepoint perturbation</summary>

| Experiment/Analysis| Data and Actual Results| relationship and limitations to the paper|
|---|---|---|
| ORL Gabor reconstruction/compression curve| Each person has a total of 40 pictures, 56×46×40; PCA d=1…40, CSA r×r×r, r=1…40| corresponds to the direction of Fig.4/5; learning sample reconstruction, non-unseen sample evaluation|
| Rebuild value range| PCA paper defines RMSE about 3733.58→0; CSA about 4084.03→10.42| RMSE=√(SSE/N), not RMSE per pixel; Gabor scale is unknown, not exact matching on vertical axis|
| storage compression rate| PCA CR is about 39.98→1.00; CSA is about 22646.15→1.61| Shared basis + scalar number of sample coefficients, not file compression ratio|
| CSA convergence curve| 10 rounds; SSE from about 2.571×10⁹, first round to about 2.040×10⁸, round 3 to about 2.034×10⁸| The current input is a fast and stable trend, the paper does not have point-by-point original data|
| 24-dimensional representation of energy diagnosis| A batch of grayscale PCA/CSA total change energy 77.55%/42.62%; Gabor72.92%/20.76%| training projection energy ratio, not identity information retention rate|
| shrinkage LDA ablation| Remove shrinkage with the same winner in the first round: Grayscale 84.13→76.84, Gabor84.75→80.22; subsequent Gabor85.47→77.00| shrinkage is effective in these selected configurations, and there is no guarantee that any configuration will improve.|
| error analysis| 3200 duplicate probe records cover 400 pictures; 224 corrections, 111 new additions; 158 correct by CSA alone, and 249 correct by PCA alone| The original image/aligned image/neighbor has been saved; there is no complete artificial eye point true value, and the only reason is not determined.|
| Projection weight cost| CSA24+LDA23 is 830 elements, PCA24+LDA23 is 618792 elements| Number of weight elements, not full system memory Array of deployments counted by|
| | CSA228272 bytes, PCA5171968 bytes| specifies arrays such as mean/gallery; excludes Python/library overhead, non-peak RSS|
| Native inference timing| 320 probe projection + LDA + NN: CSA about 21–29ms, PCA about 60–82ms, pairing about 2.08–3.29 times| Two BLAS threads, precomputed Gabor; does not include alignment/Gabor/training/power consumption|
| Early grayscale script resources| The entire script takes about 2.12 seconds, and the Windows peak working set is about 136MiB| includes the preprocessing/model/curve/output and is not directly compared with single-stage inference.|
| basic independent numerical verification| unfold/fold, non-square axis, CSA update/reconstruction, PCA equivalence, LDA characteristic equation, NN, RMSE/CR| formula implementation is consistent with independent calculation and does not prove that all unknown settings of the author are consistent|
| Gabor numerical verification| FFT and spatial complex convolution, the maximum absolute error in the early stage is about 1.22×10⁻⁷; subsequent cache will be verified separately| supports convolution to achieve reliable implementation, and does not prove that the parameters are the author's parameters.|
| DATER track verification| 1194 update, 20 LDA items; another 20 free recalculations, the maximum final direction difference is about 1.01×10⁻⁵| Initial strict path comparison fails and sensitivity is preserved, free paths are not declared equal|

Source: [Reconstruction/Basic numerical definition](./REPORT.md#validation), [Reconstruction CSV](../results/available_reproduction_v2/orl_reconstruction.csv), [Convergence trajectory](../results/available_reproduction_v2/orl_convergence.json), [Basic verification ](../results/available_numerical_checks.json), [Indicates energy](../results/csa_lda_focus/representation_statistics.csv), [Error/cost explanation](./REPORT.md#orl-controlled), [Cost timing](../results/orl_controlled/cost_benchmark.csv), [Early script resources](../results/orl_resource_profile.json).

eye point perturbation reuses the 320 model, both eyes are along the x/y ± 1 pixel of the original image, and the 1280 score is zero fitting; the following table shows the average accuracy change pp in the four directions.

| input| CSA24＋LDA23 | CSA390 | PCA24＋LDA23 | PCA33＋LDA25 |
|---|---:|---:|---:|---:|
| 2π cropped inside| −0.46 | about 0.00| −0.08 | −0.21 |
| 2π context| −0.42 | +0.02 | +0.01 | −0.01 |
| π cropped inside| −0.53 | −0.23 | −0.05 | −0.25 |
| π context| −0.08 | −0.18 | about 0.00| −0.12 |

π context low-dimensional CSA worst direction mean −0.52pp, worst single split/direction −1.875pp; **Does not cover monocular false detections, rotations or large offsets, does not prove universal robustness**. Source: [Disturbance summary](../results/orl_controlled/robustness_aggregate.csv), [verification](../results/orl_controlled/robustness_verification.json).

</details>

<details>
<summary>A10. Report attribution of various results</summary>

| Result Category How to express| | Can't express it|
|---|---|---|
| shared settings at the paper's dimensions anchor point| The known conditions correspond to the paper/TA, and the unknown details are disclosed. Reproduction| Full restoration of author agreement|
| gallery-only validation selection| Optimization results of each group of gallery selection and freezing scores| Fixed the original authors parameter|
| Fixed input/σ/distance comparison| Evidence of controlled sensitivity of current input to split| Optimal settings for all data/methods|
| context, TT, power, shrinkage, new rank, sample size, DATER| our group extension, retain the original protocol anchor for reference| Reproduction of the same experiment from the original CSA was successful|
| probe explores 95%/97.5%| Exploration with complete configuration and replay records maximum| stable mean, independent test or global optimum|
| numerical verification, error, cost, disturbance| Implementing Reliability, Critical Analysis, and Engineering Tradeoff Evidence| Eliminate all unknowns or prove the single cause of the gap|

TA Explicit data scale, dimensions, NN, CSA recognition Tmax3 and LDA budget are constraints; distance, Gabor details, eye targets and most numerical settings are still unknown. TA allows disclosure of details that cannot be matched and does not amount to itemized confirmation of our group parameters or all extensions. The existing data supports solid reproduction and critical analysis of part of the course, but it still cannot be claimed that all values ​​and conclusions of the original paper have been reproduced. The official 3–4 page LaTeX report, 9-minute presentation, and completion status for public repository release are also available in [Section 8](./REPORT.md#submission).

</details>


<a id="statistics"></a>

## Appendix B. Precise statistical supplementary table

The following complement table is read from the current CSV and retains two decimal places, and the CSV retains full precision. Contains multiplexed baselines/phases, and does not treat repeated rows as new experiments; `n` is the number of splits in the batch, not the number of independent subjects.

<details>
<summary>B1. ORL shared anchor point/first round parameter selection/additional rank </summary>

| branch| n | mean ±SD| lowest – highest| Original table difference pp*| paper| paper difference pp|
|---|---|---|---|---|---|---|
| ORL／paper_dimensions／PCA+LDA (Gray) | 10 | 83.22±1.76 | See original sequence table| 1.02 | 82.20 | 1.02 |
| ORL／paper_dimensions／CSA-2+LDA | 10 | 77.47±5.41 | See original sequence table| -6.63 | 84.10 | -6.63 |
| ORL／paper_dimensions／PCA (Gabor) | 10 | 86.88±1.63 | See original sequence table| 0.28 | 86.60 | 0.28 |
| ORL／paper_dimensions／CSA-3 | 10 | 90.19±2.37 | See original sequence table| -4.21 | 94.40 | -4.21 |
| ORL／paper_dimensions／PCA+LDA (Gabor) | 10 | 92.09±2.06 | See original sequence table| 4.89 | 87.20 | 4.89 |
| ORL／paper_dimensions／CSA-3+LDA | 10 | 79.66±2.77 | See original sequence table| -11.24 | 90.90 | -11.24 |
| ORL／training_selected／PCA+LDA (Gray) | 10 | 82.25±2.35 | See original sequence table| 0.05 | 82.20 | 0.05 |
| ORL／training_selected／CSA-2+LDA | 10 | 79.75±4.33 | See original sequence table| -4.35 | 84.10 | -4.35 |
| ORL／training_selected／PCA (Gabor) | 10 | 86.75±1.55 | See original sequence table| 0.15 | 86.60 | 0.15 |
| ORL／training_selected／CSA-3 | 10 | 89.72±2.26 | See original sequence table| -4.68 | 94.40 | -4.68 |
| ORL／training_selected／PCA+LDA (Gabor) | 10 | 91.31±1.90 | See original sequence table| 4.11 | 87.20 | 4.11 |
| ORL／training_selected／CSA-3+LDA | 10 | 80.34±3.79 | See original sequence table| -10.56 | 90.90 | -10.56 |
| ORL／balanced_rank_extension／CSA-2+LDA | 10 | 78.44±3.94 | See original sequence table| -5.66 | 84.10 | -5.66 |
| ORL／balanced_rank_extension／CSA-3 | 10 | 88.97±3.51 | See original sequence table| -5.43 | 94.40 | -5.43 |
| ORL／balanced_rank_extension／CSA-3+LDA | 10 | 80.34±4.15 | See original sequence table| -10.56 | 90.90 | -10.56 |

*The difference is according to the original table: B1 is our group − paper; B2/4/5/6 is the paired baseline; B3 is the legacy fixed baseline; B7 is the same condition CSA. Source: [shared_comparison.csv](../results/orl_protocol_audit/shared_comparison.csv). B3 split number agreement ten seeds20–29.

</details>

<details>
<summary>B2. Three fixed inputs</summary>

| branch| n | mean ±SD| lowest – highest| Original table difference pp*| paper| paper difference pp|
|---|---|---|---|---|---|---|
| baseline／CSA24_LDA23 | 10 | 81.25±2.78 | 77.19–85.94 | 0.00 | 90.90 | -9.65 |
| tt_hist／CSA24_LDA23 | 10 | 78.31±2.94 | 74.69–82.81 | -2.94 | 90.90 | -12.59 |
| crop_context／CSA24_LDA23 | 10 | 84.31±2.49 | 80.31–87.81 | 3.06 | 90.90 | -6.59 |
| baseline／CSA390 | 10 | 90.00±1.69 | 86.56–92.50 | 0.00 | 94.40 | -4.40 |
| tt_hist／CSA390 | 10 | 89.56±1.24 | 88.12–91.88 | -0.44 | 94.40 | -4.84 |
| crop_context／CSA390 | 10 | 91.56±0.90 | 90.31–93.75 | 1.56 | 94.40 | -2.84 |
| baseline／PCA24_LDA23 | 10 | 88.62±1.20 | 86.88–90.31 | 0.00 | — | — |
| tt_hist／PCA24_LDA23 | 10 | 87.75±2.42 | 84.38–92.50 | -0.88 | — | — |
| crop_context／PCA24_LDA23 | 10 | 91.00±1.77 | 87.81–92.81 | 2.38 | — | — |
| baseline／PCA33_LDA25 | 10 | 92.72±1.53 | 90.62–95.62 | 0.00 | 87.20 | 5.52 |
| tt_hist／PCA33_LDA25 | 10 | 92.34±1.10 | 90.31–93.44 | -0.38 | 87.20 | 5.14 |
| crop_context／PCA33_LDA25 | 10 | 94.38±1.00 | 92.50–96.25 | 1.66 | 87.20 | 7.17 |

*The difference is according to the original table: B1 is our group − paper; B2/4/5/6 is the paired baseline; B3 is the legacy fixed baseline; B7 is the same condition CSA. Source: [comparison.csv](../results/orl_fixed_input_extensions/comparison.csv). B3 split number agreement ten seeds20–29.

</details>

<details>
<summary>B3. Three-stage unknown parameters and reuse comparison</summary>

| branch| n | mean ±SD| lowest – highest| Original table difference pp*| paper| paper difference pp|
|---|---|---|---|---|---|---|
| legacy_baseline／CSA24_LDA23 | 10 | 81.25±2.78 | 77.19–85.94 | 0.00 | 90.90 | -9.65 |
| stage0_context／CSA24_LDA23 | 10 | 84.31±2.49 | 80.31–87.81 | 3.06 | 90.90 | -6.59 |
| stage_A／CSA24_LDA23 | 10 | 87.81±3.62 | 81.88–92.50 | 6.56 | 90.90 | -3.09 |
| stage_B／CSA24_LDA23 | 10 | 87.78±3.10 | 81.88–91.56 | 6.53 | 90.90 | -3.12 |
| stage_C／CSA24_LDA23 | 10 | 87.84±3.28 | 81.88–91.56 | 6.59 | 90.90 | -3.06 |
| legacy_baseline／CSA390 | 10 | 90.00±1.69 | 86.56–92.50 | 0.00 | 94.40 | -4.40 |
| stage0_context／CSA390 | 10 | 91.56±0.90 | 90.31–93.75 | 1.56 | 94.40 | -2.84 |
| stage_A／CSA390 | 10 | 91.06±1.24 | 88.75–92.81 | 1.06 | 94.40 | -3.34 |
| stage_B／CSA390 | 10 | 90.94±1.37 | 88.75–92.81 | 0.94 | 94.40 | -3.46 |
| stage_C／CSA390 | 10 | 91.03±1.43 | 88.75–92.81 | 1.03 | 94.40 | -3.37 |
| legacy_baseline／PCA24_LDA23 | 10 | 88.62±1.20 | 86.88–90.31 | 0.00 | — | — |
| stage0_context／PCA24_LDA23 | 10 | 91.00±1.77 | 87.81–92.81 | 2.38 | — | — |
| stage_A／PCA24_LDA23 | 10 | 90.66±1.75 | 88.12–94.06 | 2.03 | — | — |
| stage_B／PCA24_LDA23 | 10 | 90.72±1.69 | 88.12–93.75 | 2.09 | — | — |
| stage_C／PCA24_LDA23 | 10 | 90.69±1.63 | 88.12–93.44 | 2.06 | — | — |
| legacy_baseline／PCA33_LDA25 | 10 | 92.72±1.53 | 90.62–95.62 | 0.00 | 87.20 | 5.52 |
| stage0_context／PCA33_LDA25 | 10 | 94.38±1.00 | 92.50–96.25 | 1.66 | 87.20 | 7.17 |
| stage_A／PCA33_LDA25 | 10 | 94.06±1.06 | 92.81–96.25 | 1.34 | 87.20 | 6.86 |
| stage_B／PCA33_LDA25 | 10 | 94.16±1.28 | 92.81–96.25 | 1.44 | 87.20 | 6.96 |
| stage_C／PCA33_LDA25 | 10 | 94.16±1.28 | 92.81–96.25 | 1.44 | 87.20 | 6.96 |

*The difference is according to the original table: B1 is our group − paper; B2/4/5/6 is the paired baseline; B3 is the legacy fixed baseline; B7 is the same condition CSA. Source: [comparison.csv](../results/orl_unknown_parameters/comparison.csv). B3 split number agreement ten seeds20–29.

</details>

<details>
<summary>B4. Limited optimization within clipping</summary>

| branch| n | mean ±SD| lowest – highest| Original table difference pp*| paper| paper difference pp|
|---|---|---|---|---|---|---|
| baseline／CSA24_LDA23 | 10 | 81.25±2.78 | 77.19–85.94 | 0.00 | 90.90 | -9.65 |
| final_B／CSA24_LDA23 | 10 | 81.41±2.41 | 77.81–85.62 | 0.16 | 90.90 | -9.49 |
| baseline／CSA390 | 10 | 90.00±1.69 | 86.56–92.50 | 0.00 | 94.40 | -4.40 |
| final_B／CSA390 | 10 | 88.41±1.84 | 85.62–91.25 | -1.59 | 94.40 | -5.99 |
| baseline／PCA24_LDA23 | 10 | 88.62±1.20 | 86.88–90.31 | 0.00 | — | — |
| final_B／PCA24_LDA23 | 10 | 88.41±1.31 | 86.56–90.94 | -0.22 | — | — |
| baseline／PCA33_LDA25 | 10 | 92.72±1.53 | 90.62–95.62 | 0.00 | 87.20 | 5.52 |
| final_B／PCA33_LDA25 | 10 | 91.69±2.16 | 88.44–95.62 | -1.03 | 87.20 | 4.49 |

*The difference is according to the original table: B1 is our group − paper; B2/4/5/6 is the paired baseline; B3 is the legacy fixed baseline; B7 is the same condition CSA. Source: [comparison.csv](../results/orl_ta_crop_optimized/comparison.csv). B3 split number agreement ten seeds20–29.

</details>

<details>
<summary>B5. Twenty split fixed 2×2</summary>

| branch| n | mean ±SD| lowest – highest| Original table difference pp*| paper| paper difference pp|
|---|---|---|---|---|---|---|
| 2pi_crop／CSA24_LDA23 | 20 | 80.12±3.49 | 73.44–86.56 | 0.00 | 90.90 | -10.78 |
| 2pi_context／CSA24_LDA23 | 20 | 84.56±2.44 | 80.94–89.69 | 4.44 | 90.90 | -6.34 |
| pi_crop／CSA24_LDA23 | 20 | 81.25±3.03 | 74.38–85.31 | 1.12 | 90.90 | -9.65 |
| pi_context／CSA24_LDA23 | 20 | 87.08±2.30 | 82.19–90.94 | 6.95 | 90.90 | -3.82 |
| 2pi_crop／CSA390 | 20 | 88.66±2.71 | 83.75–93.75 | 0.00 | 94.40 | -5.74 |
| 2pi_context／CSA390 | 20 | 91.16±1.99 | 87.19–94.38 | 2.50 | 94.40 | -3.24 |
| pi_crop／CSA390 | 20 | 88.70±2.65 | 82.81–93.44 | 0.05 | 94.40 | -5.70 |
| pi_context／CSA390 | 20 | 90.09±2.46 | 83.44–94.06 | 1.44 | 94.40 | -4.31 |
| 2pi_crop／PCA24_LDA23 | 20 | 88.81±2.47 | 83.44–93.44 | 0.00 | — | — |
| 2pi_context／PCA24_LDA23 | 20 | 90.89±2.11 | 86.88–95.31 | 2.08 | — | — |
| pi_crop／PCA24_LDA23 | 20 | 89.20±2.76 | 81.56–92.81 | 0.39 | — | — |
| pi_context／PCA24_LDA23 | 20 | 91.08±1.48 | 89.06–94.06 | 2.27 | — | — |
| 2pi_crop／PCA33_LDA25 | 20 | 92.33±2.09 | 88.44–96.56 | 0.00 | 87.20 | 5.13 |
| 2pi_context／PCA33_LDA25 | 20 | 93.98±1.91 | 90.62–97.50 | 1.66 | 87.20 | 6.78 |
| pi_crop／PCA33_LDA25 | 20 | 93.38±1.86 | 89.06–96.56 | 1.05 | 87.20 | 6.17 |
| pi_context／PCA33_LDA25 | 20 | 94.14±1.69 | 90.62–97.19 | 1.81 | 87.20 | 6.94 |

*The difference is according to the original table: B1 is our group − paper; B2/4/5/6 is the paired baseline; B3 is the legacy fixed baseline; B7 is the same condition CSA. Source: [summary.csv](../results/orl_controlled/summary.csv). B3 split number agreement ten seeds20–29.

</details>

<details>
<summary>B6. All stages of MNIST</summary>

| branch| n | mean ±SD| lowest – highest| Original table difference pp*| paper| paper difference pp|
|---|---|---|---|---|---|---|
| 30／pca／baseline | 10 | 86.67±0.74 | 85.49–87.91 | 0.00 | 88.50 | -1.83 |
| 30／pca／input_only | 10 | 86.69±0.73 | 85.79–88.32 | 0.02 | 88.50 | -1.81 |
| 30／pca／shared_policy_identity | 10 | 86.94±0.81 | 85.79–88.57 | 0.27 | 88.50 | -1.56 |
| 30／pca／selected | 10 | 86.94±0.81 | 85.79–88.57 | 0.27 | 88.50 | -1.56 |
| 30／csa／baseline | 10 | 89.66±0.53 | 88.81–90.51 | 0.00 | 92.80 | -3.14 |
| 30／csa／input_only | 10 | 89.44±0.76 | 88.13–90.98 | -0.22 | 92.80 | -3.36 |
| 30／csa／shared_policy_identity | 10 | 88.89±0.87 | 87.55–89.91 | -0.77 | 92.80 | -3.91 |
| 30／csa／selected | 10 | 88.89±0.87 | 87.55–89.91 | -0.77 | 92.80 | -3.91 |
| 40／pca／baseline | 10 | 88.03±0.46 | 87.54–89.00 | 0.00 | 90.50 | -2.47 |
| 40／pca／input_only | 10 | 88.09±0.85 | 86.89–89.61 | 0.06 | 90.50 | -2.41 |
| 40／pca／shared_policy_identity | 10 | 88.26±0.86 | 86.89–89.61 | 0.23 | 90.50 | -2.24 |
| 40／pca／selected | 10 | 88.26±0.86 | 86.89–89.61 | 0.23 | 90.50 | -2.24 |
| 40／csa／baseline | 10 | 90.50±0.50 | 89.96–91.26 | 0.00 | 92.40 | -1.90 |
| 40／csa／input_only | 10 | 90.62±0.59 | 89.87–91.48 | 0.12 | 92.40 | -1.78 |
| 40／csa／shared_policy_identity | 10 | 90.18±0.83 | 88.39–91.48 | -0.32 | 92.40 | -2.22 |
| 40／csa／selected | 10 | 90.18±0.83 | 88.39–91.48 | -0.32 | 92.40 | -2.22 |

*The difference is according to the original table: B1 is our group − paper; B2/4/5/6 is the paired baseline; B3 is the legacy fixed baseline; B7 is the same condition CSA. Source: [comparison.csv](../results/mnist_protocol_optimized/comparison.csv). B3 split number agreement ten seeds20–29.

</details>

<details>
<summary>B7. DATER six branches</summary>

| branch| n | mean ±SD| lowest – highest| Original table difference pp*| paper| paper difference pp|
|---|---|---|---|---|---|---|
| DATER24／direct24 | 20 | 71.64±3.18 | 65.00–77.81 | -2.69 | — | — |
| CSA24／direct24 | 20 | 74.33±3.95 | 63.75–80.62 | 0.00 | — | — |
| PCA24／direct24 | 20 | 82.70±2.95 | 75.31–86.56 | 8.38 | — | — |
| DATER24／LDA23 | 20 | 67.11±3.59 | 60.31–73.12 | -13.02 | — | — |
| CSA24／LDA23 | 20 | 80.12±3.49 | 73.44–86.56 | 0.00 | — | — |
| PCA24／LDA23 | 20 | 88.81±2.47 | 83.44–93.44 | 8.69 | — | — |

*The difference is according to the original table: B1 is our group − paper; B2/4/5/6 is the paired baseline; B3 is the legacy fixed baseline; B7 is the same condition CSA. Source: [summary.csv](../results/orl_dater/summary.csv). B3 split number agreement ten seeds20–29.

</details>

<details>
<summary>B8. Normal/shrinkage optimization complete comparison</summary>

| branch| n | mean ±SD| lowest – highest| Original table matching changes pp|
|---|---|---|---|---|
| regularization_only／PCA+LDA (Gray) | 10 | 81.78±2.21 | 78.44–85.00 | -1.44 |
| regularization_only／CSA-2+LDA | 10 | 79.56±5.89 | 67.19–86.88 | 2.09 |
| regularization_only／PCA+LDA (Gabor) | 10 | 91.59±1.56 | 89.38–94.06 | -0.50 |
| regularization_only／CSA-3+LDA | 10 | 82.22±2.34 | 78.12–85.94 | 2.56 |
| optimized_ordinary_LDA／PCA+LDA (Gray) | 10 | 82.25±2.35 | 79.06–85.94 | -0.97 |
| optimized_ordinary_LDA／CSA-2+LDA | 10 | 78.56±3.98 | 71.88–84.38 | 1.09 |
| optimized_ordinary_LDA／PCA+LDA (Gabor) | 10 | 91.88±2.20 | 87.19–95.31 | -0.22 |
| optimized_ordinary_LDA／CSA-3+LDA | 10 | 82.47±3.14 | 78.12–87.50 | 2.81 |
| optimized_shrinkage_LDA／PCA+LDA (Gray) | 10 | 82.59±1.97 | 78.44–85.00 | -0.62 |
| shrinkage_ablation_alpha0／PCA+LDA (Gray) | 10 | 82.41±2.60 | 76.56–85.94 | -0.81 |
| optimized_shrinkage_LDA／CSA-2+LDA | 10 | 84.12±2.38 | 81.25–89.38 | 6.66 |
| shrinkage_ablation_alpha0／CSA-2+LDA | 10 | 76.84±4.58 | 67.81–82.81 | -0.62 |
| optimized_shrinkage_LDA／PCA+LDA (Gabor) | 10 | 91.56±1.80 | 89.38–95.00 | -0.53 |
| shrinkage_ablation_alpha0／PCA+LDA (Gabor) | 10 | 91.53±2.00 | 89.06–95.31 | -0.56 |
| optimized_shrinkage_LDA／CSA-3+LDA | 10 | 84.75±4.66 | 74.69–90.31 | 5.09 |
| shrinkage_ablation_alpha0／CSA-3+LDA | 10 | 80.22±4.71 | 72.50–88.44 | 0.56 |

Source: [summary.json](../results/csa_lda_optimized/evaluation/summary.json); B9’s alpha0 is the alpha that removes the selected shrinkage configuration and cannot replace the independent optional parameter ordinary.

</details>

<details>
<summary>B9. Rank/initialization targeted iteration complete comparison</summary>

| branch| n | mean ±SD| lowest – highest| Original table matching changes pp|
|---|---|---|---|---|
| ordinary／CSA-3+LDA | 10 | 83.28±3.30 | 78.75–89.06 | — |
| same_input_paper_case／CSA-3+LDA | 10 | 80.81±3.26 | 75.94–85.00 | — |
| ordinary／PCA+LDA (Gabor) | 10 | 92.09±2.36 | 87.19–95.94 | — |
| ordinary／CSA-3 | 10 | 89.97±2.23 | 86.56–93.44 | — |
| shrinkage／CSA-3+LDA | 10 | 85.47±4.57 | 74.69–90.00 | — |
| shrinkage_alpha0／CSA-3+LDA | 10 | 77.00±8.68 | 65.00–88.75 | — |
| shrinkage／PCA+LDA (Gabor) | 10 | 91.41±2.60 | 85.62–95.00 | — |
| shrinkage／CSA-3 | 10 | 90.12±2.12 | 85.62–93.44 | — |

Source: [summary.json](../results/orl_csa_refined/evaluation/summary.json); B9’s alpha0 is the alpha that removes the selected shrinkage configuration and cannot replace the independent optional parameter ordinary.

</details>


<a id="inventory"></a>

## Appendix C. All results directory and complete data entry

covers all first-level directories and root-level diagnostic files of the current `results/`. Each directory link can continue to enter subdirectories; usually `protocol` describes configuration/candidate/seed, `results`/`fixed_results` records successive accuracy, `summary` summarizes, `predictions` or `evaluation` saves neighbors/predictions, `selection`/`seed*` saves inner candidates and models, `source_snapshot`/freeze saves actual source code/hash, `verification` saves verification. Batches without files with the same name are read according to the actual entry.

**Original data not omitted:** All grid candidates, low scores, close to/exceeding paper index, image-by-image repeated predictions, models, dimension curves and failure records are still in the corresponding directory. Image catalogs/regression copies/failed pre-checks are marked separately, and new experiments are not falsely reported; cross-batch reuse is confirmed according to the agreement. Finally, the public repository can provide compliant streamlined results and download instructions, and the local path cannot be regarded as a published URL.

| Table of Contents| Experiment/Border| shortcut file|
|---|---|---|
| [alignment_diagnosis](../results/alignment_diagnosis) | Early alignment and fixation diagnosis| [protocol.json](../results/alignment_diagnosis/protocol.json)；[summary.json](../results/alignment_diagnosis/summary.json)；[fixed_results.csv](../results/alignment_diagnosis/fixed_results.csv)；[verification.json](../results/alignment_diagnosis/verification.json) |
| [available_reproduction](../results/available_reproduction) | Early ORL/MNIST available reproduction v1, recognition/dimension/reconstruction/convergence| [protocol.json](../results/available_reproduction/protocol.json)；[summary.json](../results/available_reproduction/summary.json)；[fixed_results.csv](../results/available_reproduction/fixed_results.csv) |
| [available_reproduction_v2](../results/available_reproduction_v2) | available with reproduction v2 and shared MNIST source; features/prediction/reconstruction/verification| [protocol.json](../results/available_reproduction_v2/protocol.json)；[summary.json](../results/available_reproduction_v2/summary.json)；[fixed_results.csv](../results/available_reproduction_v2/fixed_results.csv)；[verification.json](../results/available_reproduction_v2/verification.json) |
| [available_tuned](../results/available_tuned) | History parameter selection method by method, input/NN may be different, the shared table is not replaced| [protocol.json](../results/available_tuned/protocol.json)；[summary.json](../results/available_tuned/summary.json)；[fixed_results.csv](../results/available_tuned/fixed_results.csv)；[verification.json](../results/available_tuned/verification.json) |
| [csa_lda_focus](../results/csa_lda_focus) | Low-dimensional CSA+LDA special project/focused selection/energy/Fisher verification| [protocol.json](../results/csa_lda_focus/protocol.json) |
| [csa_lda_optimized](../results/csa_lda_optimized) | Normal/shrinkage LDA; seed* inner layer, evaluation outer layer and alpha0 comparison| [protocol.json](../results/csa_lda_optimized/protocol.json)；[evaluation/summary.json](../results/csa_lda_optimized/evaluation/summary.json)；[evaluation/verification.json](../results/csa_lda_optimized/evaluation/verification.json) |
| [feret_validation_selected](../results/feret_validation_selected) | FERET Verification v1 all candidates/folds/predictions/curves| [protocol.json](../results/feret_validation_selected/protocol.json)；[summary.json](../results/feret_validation_selected/summary.json)；[fixed_results.csv](../results/feret_validation_selected/fixed_results.csv) |
| [feret_validation_selected_v2](../results/feret_validation_selected_v2) | FERET verification v2; candidate changes and fallback retention| [protocol.json](../results/feret_validation_selected_v2/protocol.json)；[summary.json](../results/feret_validation_selected_v2/summary.json)；[fixed_results.csv](../results/feret_validation_selected_v2/fixed_results.csv)；[verification.json](../results/feret_validation_selected_v2/verification.json) |
| [feret_validation_selected_v3](../results/feret_validation_selected_v3) | FERET verification v3/Euclidean/Sw scale/Cosine fixed control; shared source| [protocol.json](../results/feret_validation_selected_v3/protocol.json)；[summary.json](../results/feret_validation_selected_v3/summary.json)；[fixed_results.csv](../results/feret_validation_selected_v3/fixed_results.csv)；[verification.json](../results/feret_validation_selected_v3/verification.json) |
| [mnist_protocol_optimized](../results/mnist_protocol_optimized) | MNIST limited optimization all stages/three old seed pairings; selection inner layer, evaluation prediction| [protocol.json](../results/mnist_protocol_optimized/protocol.json)；[summary.json](../results/mnist_protocol_optimized/summary.json)；[comparison.csv](../results/mnist_protocol_optimized/comparison.csv)；[verification.json](../results/mnist_protocol_optimized/verification.json) |
| [orl_best_search](../results/orl_best_search) | probe exploration; all scores in the scores subdirectory, 6003 configuration statistics/6432 index/best replay| [protocol.json](../results/orl_best_search/protocol.json)；[verification.json](../results/orl_best_search/verification.json) |
| [orl_branches_v2](../results/orl_branches_v2) | ORL Historical Geometry/Eyepoint Branch v2| [protocol.json](../results/orl_branches_v2/protocol.json)；[summary.json](../results/orl_branches_v2/summary.json)；[fixed_results.csv](../results/orl_branches_v2/fixed_results.csv)；[verification.json](../results/orl_branches_v2/verification.json) |
| [orl_branches_v3](../results/orl_branches_v3) | Historical five branches v3, resize does not retain TA binocular processing| [protocol.json](../results/orl_branches_v3/protocol.json)；[summary.json](../results/orl_branches_v3/summary.json)；[fixed_results.csv](../results/orl_branches_v3/fixed_results.csv)；[verification.json](../results/orl_branches_v3/verification.json) |
| [orl_controlled](../results/orl_controlled) | Fixed 2×2/error/cost/1280 perturbation; model and prediction subdirectory| [protocol.json](../results/orl_controlled/protocol.json)；[summary.json](../results/orl_controlled/summary.json)；[summary.csv](../results/orl_controlled/summary.csv)；[verification.json](../results/orl_controlled/verification.json) |
| [orl_csa_refined](../results/orl_csa_refined) | low rank/HOSVD/normal and shrinkage; evaluation, randomness100 split, seed* inner layer| [protocol.json](../results/orl_csa_refined/protocol.json)；[evaluation/summary.json](../results/orl_csa_refined/evaluation/summary.json)；[evaluation/verification.json](../results/orl_csa_refined/evaluation/verification.json) |
| [orl_dater](../results/orl_dater) | DATER model/trajectory/six scores, failed/supplementary verification/sensitivity| [protocol.json](../results/orl_dater/protocol.json)；[summary.json](../results/orl_dater/summary.json)；[summary.csv](../results/orl_dater/summary.csv)；[verification.json](../results/orl_dater/verification.json) |
| [orl_eye_review_v2](../results/orl_eye_review_v2) | 6-image artificial eye point review, non-independent new recognition fitting| [changes.json](../results/orl_eye_review_v2/changes.json) |
| [orl_fixed_input_extensions](../results/orl_fixed_input_extensions) | Three input 120 fitting/model prediction/freeze/verification path correction| [protocol.json](../results/orl_fixed_input_extensions/protocol.json)；[summary.json](../results/orl_fixed_input_extensions/summary.json)；[comparison.csv](../results/orl_fixed_input_extensions/comparison.csv)；[verification.json](../results/orl_fixed_input_extensions/verification.json) |
| [orl_fixed_input_extensions_preflight](../results/orl_fixed_input_extensions_preflight) | The pre-check before grading failed, and the completed grading is not counted.| [protocol.json](../results/orl_fixed_input_extensions_preflight/protocol.json)；[preflight_failure.json](../results/orl_fixed_input_extensions_preflight/preflight_failure.json) |
| [orl_gabor_diagnosis](../results/orl_gabor_diagnosis) | Gabor single factor binocular/resize complete comparison| [protocol.json](../results/orl_gabor_diagnosis/protocol.json)；[summary.json](../results/orl_gabor_diagnosis/summary.json)；[fixed_results.csv](../results/orl_gabor_diagnosis/fixed_results.csv)；[verification.json](../results/orl_gabor_diagnosis/verification.json) |
| [orl_gabor_forced10](../results/orl_gabor_forced10) | Fixed model 3→10 rounds, 0 prediction changes| [protocol.json](../results/orl_gabor_forced10/protocol.json)；[fixed_results.csv](../results/orl_gabor_forced10/fixed_results.csv)；[verification.json](../results/orl_gabor_forced10/verification.json) |
| [orl_gabor_radius_rounding](../results/orl_gabor_radius_rounding) | core supports floating point rounding regression and actual characteristics| [protocol.json](../results/orl_gabor_radius_rounding/protocol.json)；[summary.json](../results/orl_gabor_radius_rounding/summary.json)；[fixed_results.csv](../results/orl_gabor_radius_rounding/fixed_results.csv)；[verification.json](../results/orl_gabor_radius_rounding/verification.json) |
| [orl_gray_improved](../results/orl_gray_improved) | Early G2/V2/P6 five-split option, separated from G2/P8| [protocol.json](../results/orl_gray_improved/protocol.json)；[summary.json](../results/orl_gray_improved/summary.json)；[verification.json](../results/orl_gray_improved/verification.json) |
| [orl_gray_initial](../results/orl_gray_initial) | Early grayscale fixation experiment/LDA curve| [protocol.json](../results/orl_gray_initial/protocol.json)；[summary.json](../results/orl_gray_initial/summary.json) |
| [orl_gray_profile](../results/orl_gray_profile) | Same grayscale running resource analysis copy, non-independent experimental sample| [protocol.json](../results/orl_gray_profile/protocol.json)；[summary.json](../results/orl_gray_profile/summary.json) |
| [orl_gray_regression](../results/orl_gray_regression) | implements regression copy with grayscale, not a new protocol| [protocol.json](../results/orl_gray_regression/protocol.json)；[summary.json](../results/orl_gray_regression/summary.json) |
| [orl_gray_verified](../results/orl_gray_verified) | Grayscale fixing/centering after independent verification| [protocol.json](../results/orl_gray_verified/protocol.json)；[summary.json](../results/orl_gray_verified/summary.json) |
| [orl_mnist_final](../results/orl_mnist_final) | Only the original image sample PNG, not the new ORL/MNIST final score| Enter the picture/subdirectory by directory|
| [orl_pipeline_diagnosis](../results/orl_pipeline_diagnosis) | Valid area/intensity/resampling diagnostics| [protocol.json](../results/orl_pipeline_diagnosis/protocol.json)；[summary.json](../results/orl_pipeline_diagnosis/summary.json)；[fixed_results.csv](../results/orl_pipeline_diagnosis/fixed_results.csv)；[verification.json](../results/orl_pipeline_diagnosis/verification.json) |
| [orl_protocol_audit](../results/orl_protocol_audit) | YuNet/geometric audit; evaluation/selection/contrasts/refinement complete subdirectory| [protocol.json](../results/orl_protocol_audit/protocol.json)；[verification.json](../results/orl_protocol_audit/verification.json)；[evaluation/summary.json](../results/orl_protocol_audit/evaluation/summary.json) |
| [orl_sample_size](../results/orl_sample_size) | Nested G2/G3/G5 with P5, pca_control control/diagnostic statistics| [protocol.json](../results/orl_sample_size/protocol.json)；[summary.json](../results/orl_sample_size/summary.json)；[verification.json](../results/orl_sample_size/verification.json) |
| [orl_ta_crop_optimized](../results/orl_ta_crop_optimized) | clipping the paper's dimensions limited optimization; selection inner layer/evaluation40 new outer layer/history control| [protocol.json](../results/orl_ta_crop_optimized/protocol.json)；[summary.json](../results/orl_ta_crop_optimized/summary.json)；[comparison.csv](../results/orl_ta_crop_optimized/comparison.csv)；[verification.json](../results/orl_ta_crop_optimized/verification.json) |
| [orl_unknown_parameters](../results/orl_unknown_parameters) | A/B/C inner and outer layers and 12 input/power/initialization/NN, including context| [protocol.json](../results/orl_unknown_parameters/protocol.json)；[summary.json](../results/orl_unknown_parameters/summary.json)；[comparison.csv](../results/orl_unknown_parameters/comparison.csv)；[verification.json](../results/orl_unknown_parameters/verification.json) |
| [shared_protocol_final](../results/shared_protocol_final) | step1 shared NN→step2 effective area→step3 core padding→step4 freeze/etc. 64 dimensions; historical process| Enter the picture/subdirectory by directory|
| [visual_comparison](../results/visual_comparison) | Original TableII/Fig7 screenshot and our group diagram, no new fitting| Enter the picture/subdirectory by directory|

| root level file| Purpose|
|---|---|
| [available_numerical_checks.json](../results/available_numerical_checks.json) | Available data algorithm/FFT verification|
| [numerical_checks.json](../results/numerical_checks.json) | Basic Mathematics verification|
| [orl_metric_diagnosis.json](../results/orl_metric_diagnosis.json) | Early distance/column scaling diagnostics|
| [orl_metric_diagnosis_verified.json](../results/orl_metric_diagnosis_verified.json) | Same as diagnosis verification readback|
| [orl_resource_profile.json](../results/orl_resource_profile.json) | Early full script timing/Windows memory|
| [output_audit.json](../results/output_audit.json) | Historical output list audit, not new score|

This index covers35 first-level result directories and6 root-level files; coverage is not a count of independent experiments. Public directory links retain tables, protocols, source snapshots, and verification records. Numeric caches and image-bearing examples described in the local archive are excluded and must be reconstructed locally.



historical implementation entry (located together with the results directory, not based on the number of files in the experiment):

| work| source code entrance|
|---|---|
| Early Grayscale/Resources/Regression| [run_orl_gray.py](../run_orl_gray.py)、[improve_orl_gray.py](../improve_orl_gray.py)、[diagnose_orl_metric.py](../diagnose_orl_metric.py) |
| available in early reproduction/method-by-method selection| [run_available_reproduction.py](../run_available_reproduction.py)、[tune_available.py](../tune_available.py)、[verify_available_results.py](../verify_available_results.py)、[verify_tuned.py](../verify_tuned.py) |
| Geometry/Branch/Gabor/Iteration/Radius| [diagnose_available_alignment.py](../diagnose_available_alignment.py)、[run_orl_branches.py](../run_orl_branches.py)、[diagnose_orl_gabor.py](../diagnose_orl_gabor.py)、[diagnose_orl_iterations.py](../diagnose_orl_iterations.py)、[diagnose_orl_radius_rounding.py](../diagnose_orl_radius_rounding.py) |
| Four-step input/verification/special| [diagnose_orl_pipeline.py](../diagnose_orl_pipeline.py)、[run_shared_protocol.py](../run_shared_protocol.py)、[verify_shared_protocol.py](../verify_shared_protocol.py)、[diagnose_csa_lda.py](../diagnose_csa_lda.py) |
| Basic value/Gabor readback| [check_numerics.py](../check_numerics.py)、[check_available_numerics.py](../check_available_numerics.py)、[verify_orl_gabor.py](../verify_orl_gabor.py)、[verify_orl_followup.py](../verify_orl_followup.py) |
| FERET fixed operation/display diagram| [run_feret.py](../run_feret.py)、[plot_orl_comparison.py](../plot_orl_comparison.py) |

<a id="figures"></a>

## Appendix D. Available figures, location and citations of the paper

| image file| Attribution| Picture title/note of explanation|
|---|---|---|
| [paper_tableII_orl.png](../results/visual_comparison/paper_tableII_orl.png) | Original paper Table II| the original authors best result; caption indicates Xu et al. 2008|
| [paper_fig7_full.png](../results/visual_comparison/paper_fig7_full.png) | Original paperFig7| The author's dimension curve, do not regard it as our group's point-by-point results|
| [comparison.png](../results/orl_protocol_audit/comparison.png) | our group sharing/first round selection| Ten seeds, result categories according to legend|
| [comparison.png](../results/orl_controlled/comparison.png) | our group fixed 2×2| 4200–4219, four inputs, context expansion|
| [historical_error_montage.png](../results/orl_controlled/historical_error_montage.png) | our group original picture/eyespot/neighbor| stageC and PCA, sequential sample selection does not represent full error distribution|
| [historical_aligned_error_montage.png](../results/orl_controlled/historical_aligned_error_montage.png) | our group actual alignment and cropping| The correct mapping to the target does not prove that the eyepoint is a true value|
| [robustness.png](../results/orl_controlled/robustness.png) | our group common eye point disturbance| ±1 original pixel, not universally robust|
| [comparison.png](../results/orl_dater/comparison.png) | our group DATER negative result| fixed 2πcrop twenty split, direct/LDA|
| [comparison.png](../results/mnist_protocol_optimized/comparison.png) | our group before and after MNIST| Same as split , retain drop|
| [paper_comparison.png](../results/feret_validation_selected_v3/paper_comparison.png) | our group FERET verify selection| The validation-selected in the image is not a cosine fixed shared anchor point|
| [lda_curves.png](../results/feret_validation_selected_v3/lda_curves.png) | our group FERET dimension curve| According to the method/q/dimension, do not change the winner after verification|
| [orl_convergence_reconstruction.png](../results/available_reproduction_v2/orl_convergence_reconstruction.png) | our group rebuild/converge| 40 fitting image, old Gabor, √(SSE/N) and scalar CR Among|
| [learning_curve.png](../results/orl_sample_size/learning_curve.png) | our group sample size| P5 fixed, G2/G3/G5 extended|
| [randomness_distribution.png](../results/orl_csa_refined/randomness_distribution.png) | our group 100 split diagnosis| Same as the 400 picture, the highest does not replace the mean|
| [best_distribution.png](../results/orl_best_search/best_distribution.png) | our group probe explore| Clear posterior selection parameters/seed|
| [comparison.png](../results/orl_fixed_input_extensions/comparison.png) | our group three fixed inputs| ten split, TT combination/context|
| [iteration_comparison.png](../results/orl_unknown_parameters/iteration_comparison.png) | our group three-stage selection| A/B/C and negative stage|
| [comparison.png](../results/orl_ta_crop_optimized/comparison.png) | our group limited optimization within cropping| matching only +0.16pp and PCA negative control|

| Source| Usage and Reference Notes|
|---|---|
| [CSA original PDF](../Reconstruction_and_Recognition_of_Tensor-Based_Objects_With_Concurrent_Subspaces_Analysis.pdf)／[DOI](https://doi.org/10.1109/TCSVT.2007.903317)| Main research paper; Procedure1/Fig.2 printed page 39, FERET/ORL Tables I/II page 43, MNIST TableIV page 44; only extract the charts I want to explain and clarify the source of the paper|
| [Wiskott et al. 1997 authors PDF](https://cenl.ucsd.edu/pubs/ieee-1997.pdf)| Gabor／amplitude representation background; our group does not implement complete Elastic Bunch Graph Matching and cannot be written to reuse all its methods|
| [DATER local PDF](./sources/DATER_CVPR2005.pdf)／[Author PDF](https://mmlab.ie.cuhk.edu.hk/archive/2005/01467312.pdf)| Yan et al. CVPR2005 supervised tensor expansion; specific Figure3 initialization/solution is separated from our group’s unknown convention|
| [Evidence of teacher/TA/data author](./HANDOFF.md)/[Original reply record](./HISTORY.md#history-14)| Data size, can omit/disclose differences; email is provided to users, does not pretend to be independently verified from the email; no need to disclose irrelevant private information|
| [Code and dependencies](../README.md) / [FERET instructions](../FERET/README.md) | Group results, implementation/reused components, and data acquisition; include the actual public repository URL in the final submission |

The public basis and historical query records of Tan–Triggs illumination combination, HOSVD, and covariance shrinkage are recorded in [original planning/citation](./REPORT.md#orl-next-directions), [HANDOFF theory and implementation](./HANDOFF.md). Ultimately, if these methods are deployed in the report, the bibliographic information should be completed with actual citations; our group's manual shrinkage grid cannot be written to use the automatic Ledoit–Wolf estimator. This article retains the actual execution recipe and source code, and does not replace the original authors' undisclosed CSA settings with a general reference.


<a id="figure-pack"></a>

## Appendix E. Report and presentation figure pack (updated 2026-10-30)

**27 English figures cover multiple main results, not only the current ORL24→23 representative.** The pack includes all16 paper-corresponding recognition cases, reconstruction/compression and convergence, FERET/ORL dimension curves, matched ORL controls, selection outcomes, DATER, shrinkage, sample size, cost, robustness, and errors. Full reproduction is the project classification within the instructor-approved scope; the figure categories keep numerical agreement and protocol differences explicit.

- [27-page vector PDF atlas](../output/pdf/CSA_figure_atlas_20261030.pdf): one numbered figure per page, with captions and limitations.
- [Complete ZIP package](../results/report_figures_20261030/CSA_report_slide_figures_20261030.zip): atlas,27 high-resolution PNGs,27 editable vector SVGs, captions/source index, plotting data, provenance manifest, and LaTeX snippets.
- [Figure/caption/source catalogue](../results/report_figures_20261030/figure_catalog.csv), [plotted data](../results/report_figures_20261030/plot_data.csv), [provenance manifest](../results/report_figures_20261030/manifest.json), and [LaTeX snippets](../results/report_figures_20261030/latex_figures.tex).
- [Reproducible generator](../plot_report_figures.py): `python plot_report_figures.py`; requires recorded local evidence and, for the last panel, omitted saved model/feature caches.

**Recommended main-result choices:**01-05 summarize all three datasets and paper differences;21-22 cover reconstruction and convergence;24-25 cover FERET and historical ORL dimension curves. Figure27 adds the current ORL input's dimension curves from saved models. Figures06-20 and23 support controlled analysis and extensions. Figure26 introduces the algorithm. For a short talk, select from these groups rather than treating every diagnostic as a main result.

**Statistics and attribution:** Whiskers are sample SD across the stated splits, not confidence intervals. FERET uses a fixed identity partition and has no invented split SD. Paper values are attributed to Xu et al.2008; their best-result aggregation is unspecified. Current grayscale CSA11x2->16 is81.84±1.96; crop/distance and probe-selection details are in captions and REPORT, outside the headline table. Gabor HOSVD/context88.75±2.89 is marked as an extension; full-square88.81±2.97 is separate. Gallery selections, fixed extensions, historical inputs and probe-selected extrema retain distinct captions. Display rounding uses decimal half-up; underlying experiment evidence is unchanged. The [20261027 edition](../results/report_figures_20261027/CSA_report_slide_figures_20261027.zip) is retained solely as history.

**Zero new fits:** Figures01-26 read recorded evidence. Figure27 scores existing models at LDA dimensions1-23, using40 saved model instances and920 scores, with every23D endpoint matching its archived score. These descriptive curves do not reselect the reported23D representative and are not a new blind test. No face images, raw labels, model caches, or datasets are included in the package.

To use vector output in LaTeX, copy the atlas into the report project, load `graphicx`, and select a page, for example:

```latex
% Preamble: \usepackage{graphicx}
\includegraphics[page=2,width=\linewidth]{CSA_figure_atlas_20261030.pdf}
```

| Atlas page | Figure | Category | Individual files |
|---:|---|---|---|
| 01 | Paper versus reproduction: all 16 recognition cases | Main result | [PNG](../results/report_figures_20261030/png/01_all_recognition_cases.png) / [SVG](../results/report_figures_20261030/svg/01_all_recognition_cases.svg) |
| 02 | ORL: six paper-dimension recognition cases | Main result | [PNG](../results/report_figures_20261030/png/02_orl_paper_comparison.png) / [SVG](../results/report_figures_20261030/svg/02_orl_paper_comparison.svg) |
| 03 | MNIST: both gallery sizes, both representations | Main result | [PNG](../results/report_figures_20261030/png/03_mnist_paper_comparison.png) / [SVG](../results/report_figures_20261030/svg/03_mnist_paper_comparison.svg) |
| 04 | FERET: three training sizes, PCA and CSA controls | Main result | [PNG](../results/report_figures_20261030/png/04_feret_paper_comparison.png) / [SVG](../results/report_figures_20261030/svg/04_feret_paper_comparison.svg) |
| 05 | Numerical gaps from the paper across all 16 cases | Main result | [PNG](../results/report_figures_20261030/png/05_all_paper_gaps.png) / [SVG](../results/report_figures_20261030/svg/05_all_paper_gaps.svg) |
| 06 | ORL recovery: every one of the ten observed splits | Context extension | [PNG](../results/report_figures_20261030/png/06_orl_ten_splits.png) / [SVG](../results/report_figures_20261030/svg/06_orl_ten_splits.svg) |
| 07 | ORL: geometry and initialization interactions | Context / start variants | [PNG](../results/report_figures_20261030/png/07_orl_geometry_initialization.png) / [SVG](../results/report_figures_20261030/svg/07_orl_geometry_initialization.svg) |
| 08 | ORL fixed factorial study: sigma by context | Fixed input extension | [PNG](../results/report_figures_20261030/png/08_orl_sigma_context_factorial.png) / [SVG](../results/report_figures_20261030/svg/08_orl_sigma_context_factorial.svg) |
| 09 | ORL three fixed inputs: improvements and regressions | Fixed input extension | [PNG](../results/report_figures_20261030/png/09_orl_three_fixed_inputs.png) / [SVG](../results/report_figures_20261030/svg/09_orl_three_fixed_inputs.svg) |
| 10 | Gallery-only staged selection: most gain comes early | Gallery-only selection | [PNG](../results/report_figures_20261030/png/10_orl_gallery_selection_stages.png) / [SVG](../results/report_figures_20261030/svg/10_orl_gallery_selection_stages.svg) |
| 11 | Crop-only bounded optimization: small gain, negative controls | Gallery-only selection | [PNG](../results/report_figures_20261030/png/11_orl_crop_only_optimization.png) / [SVG](../results/report_figures_20261030/svg/11_orl_crop_only_optimization.svg) |
| 12 | ORL sample-size extension with the same five probes | Sample-size extension | [PNG](../results/report_figures_20261030/png/12_orl_sample_size.png) / [SVG](../results/report_figures_20261030/svg/12_orl_sample_size.svg) |
| 13 | MNIST bounded selection: preserve the negative result | Gallery-only selection | [PNG](../results/report_figures_20261030/png/13_mnist_selection_negative.png) / [SVG](../results/report_figures_20261030/svg/13_mnist_selection_negative.svg) |
| 14 | FERET: validation winners and fixed controls differ | Selection protocol comparison | [PNG](../results/report_figures_20261030/png/14_feret_selection_vs_fixed.png) / [SVG](../results/report_figures_20261030/svg/14_feret_selection_vs_fixed.svg) |
| 15 | DATER supervised tensor extension: a negative result | New-method extension | [PNG](../results/report_figures_20261030/png/15_dater_matched_comparison.png) / [SVG](../results/report_figures_20261030/svg/15_dater_matched_comparison.svg) |
| 16 | Shrinkage ablation: compare both selected and matched variants | Regularization extension | [PNG](../results/report_figures_20261030/png/16_shrinkage_ablation.png) / [SVG](../results/report_figures_20261030/svg/16_shrinkage_ablation.svg) |
| 17 | Representation cost: small weights, explicitly scoped timing | Cost analysis | [PNG](../results/report_figures_20261030/png/17_cost_scope.png) / [SVG](../results/report_figures_20261030/svg/17_cost_scope.svg) |
| 18 | Probe-eye perturbations: local robustness with no refitting | Robustness extension | [PNG](../results/report_figures_20261030/png/18_eye_perturbation.png) / [SVG](../results/report_figures_20261030/svg/18_eye_perturbation.svg) |
| 19 | Error analysis: corrections coexist with new failures | Error analysis | [PNG](../results/report_figures_20261030/png/19_error_tradeoffs.png) / [SVG](../results/report_figures_20261030/svg/19_error_tradeoffs.svg) |
| 20 | Selected configurations: mean versus observed maximum | Exploration / selection bias | [PNG](../results/report_figures_20261030/png/20_mean_vs_maximum.png) / [SVG](../results/report_figures_20261030/svg/20_mean_vs_maximum.svg) |
| 21 | ORL tensor reconstruction: error and representation storage | Main result | [PNG](../results/report_figures_20261030/png/21_orl_reconstruction.png) / [SVG](../results/report_figures_20261030/svg/21_orl_reconstruction.svg) |
| 22 | CSA convergence: rapid stabilization in the recorded input | Main result | [PNG](../results/report_figures_20261030/png/22_csa_convergence.png) / [SVG](../results/report_figures_20261030/svg/22_csa_convergence.svg) |
| 23 | Equal dimension does not imply equal retained variation | Representation diagnosis | [PNG](../results/report_figures_20261030/png/23_retained_variation.png) / [SVG](../results/report_figures_20261030/svg/23_retained_variation.svg) |
| 24 | FERET main experiment: recognition versus LDA dimension | Main result | [PNG](../results/report_figures_20261030/png/24_feret_lda_curves.png) / [SVG](../results/report_figures_20261030/svg/24_feret_lda_curves.svg) |
| 25 | ORL historical dimension curves: three representation settings | Historical main experiment | [PNG](../results/report_figures_20261030/png/25_orl_historical_dimension_curves.png) / [SVG](../results/report_figures_20261030/svg/25_orl_historical_dimension_curves.svg) |
| 26 | CSA pipeline and the full reproduction scope | Main result | [PNG](../results/report_figures_20261030/png/26_method_pipeline.png) / [SVG](../results/report_figures_20261030/svg/26_method_pipeline.svg) |
| 27 | ORL current input: LDA dimension curves from saved models | Zero-fit supplementary analysis | [PNG](../results/report_figures_20261030/png/27_orl_current_lda_curves.png) / [SVG](../results/report_figures_20261030/svg/27_orl_current_lda_curves.svg) |
