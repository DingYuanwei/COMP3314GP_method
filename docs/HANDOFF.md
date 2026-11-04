# COMP3314 CSA project complete handover document

**Current matched Euclidean ORL results,2026-11-04:** Gray CSA11x2->LDA16 is81.72% +/- 2.06%, with matched PCA30->18 at77.22% +/- 2.35% and PCA22->16 at77.13% +/- 2.89%. Gabor CSA24->23 is87.53% +/- 2.91%, with matched PCA33->25 at88.41% +/- 1.96% and PCA24->23 at85.72% +/- 2.61%. Direct Gabor PCA76/CSA390 are86.91% +/- 1.60% /89.66% +/- 1.92%. Within grayscale and within Gabor, all methods share the same frozen input array, seeds20-29/G2-P8 and Euclidean NN; LDA uses unit columns. Gray CSA beats both PCA controls; Gabor CSA24 beats equal-budget PCA24 but not PCA33. Historical cosine81.84/88.75 results are preserved with their original labels. Thirty missing controls were fitted, fifty saved models reused, and all80 models/160 metric scores were verified. The20261104 figure edition is current; earlier editions remain historical. [Current protocol and full results](./REPORT.md#orl-euclidean-20261104).

> **Default protocol decision,2026-11-04:** Subsequent ORL comparisons use Euclidean NN, as requested by the user; CSA and PCA share inputs/splits/metric and retain unit-length LDA columns. The paper/TA specify NN without confirming a recognition distance. Existing Euclidean means: gray CSA22->16,81.72%, matched PCA30->18,77.22%; Gabor HOSVD CSA24->23,87.53%, matched PCA24->23,85.72%. Recorded cosine81.84/88.75 values and historical runner defaults must not be relabeled as Euclidean. See [decision and precise scores](./REPORT.md#orl-distance-default-20261104). New ORL entry points should explicitly implement this default; frozen evidence remains intact.

> **Historical cosine grayscale experiment,2026-10-30:** CSA11x2 -> ordinary LDA16 now reaches**81.84% +/- 1.96%** over the ten existing seeds20-29, versus shared77.47% +/- 5.41% and paper84.10%; +4.38pp, nine improved/one lower split. Fixed YuNet target eyes(15.5,24)/(30.5,24), linear/replicate/PIL input, uncentered identity/Tmax3, unit-column centered-cosine NN; HOSVD ties. Matched PCA30->18 / PCA22->16:83.50% +/- 2.29% /81.44% +/- 2.24%. Two finite batches total960 verified models; selection uses observed probes, including adaptive crop refinement. Pool maximum85.9375% is a separate single run. Keep shared77.47, this original-dimension exploratory81.84, and earlier shrinkage/rank-extension84.13 distinct. Gabor88.75 remains unchanged. [Current evidence and limits](./REPORT.md#orl-gray-recovery-20261030), [final analysis](../results/orl_gray_recovery_20261030/final_analysis.json). The20261030 README/main charts used81.84%;77.47% remains historical. The20261030 figure pack is historical; the20261027 pack is archived. No further automatic search follows this completed pool.

> **Current handoff update, 2026-10-27:** The public repository is [gwdsd1/COMP3314GP](https://github.com/gwdsd1/COMP3314GP). The project is classified as **full reproduction within the instructor-approved ORL/MNIST/grayscale FERET scope**. PIE omission and numerical/protocol differences remain disclosed. All seven Markdown documents are now English; this supersedes the earlier Chinese-document exceptions. Frozen source/protocol files retain original bytes/language. All three datasets and generated numeric caches remain excluded. The original dated history below is retained and may describe earlier publication/planning states.
>
> Historical cosine ORL24→23 representative: **88.75%±2.89%** (HOSVD start, context extension; ten splits, −2.15pp versus the paper90.90%). Keep **88.81%±2.97%** (full-square identity initialization variant; −2.09pp) as a separate initialization variant. The bounded study fitted90 CSA+30 PCA models on all ten seeds20–29; no mean reaches90.9. The pool single maximum93.125% is exploratory. Context and the full-square start are disclosed extensions/variants; unknown author settings remain unconfirmed. Historical shared/gallery-selected/fixed-twenty-split/other-dimension results below retain their batch labels. Read [TEAM_BRIEF](./TEAM_BRIEF.md#reproduction-status) and [the current REPORT section](./REPORT.md#orl-recovery-20261027).



Updated: 2026-10-30. Dated experiment entries retain their original execution dates. Workspace: `D:\HKU\COURSE\y2s1\COMP3314\COMP3314GP`.

**Purpose: Let new sessions understand why the project is being done, how the course is graded, what the paper and instructor requirements are, what has been implemented and verified, what results can be reported, and what to do next, without reading the entire chat.** This article is about status and decision handover; complete explanations and email files are in [HISTORY.md](./HISTORY.md), and detailed current reports are in [REPORT.md](./REPORT.md). The "final", "pending" and "unavailable" in the historical files may be out of date, and should be judged based on this article and the current results file.

## 0. What to read first in a new session

**Read [TEAM_BRIEF.md](./TEAM_BRIEF.md) first when peers are preparing reports/presentations**: Organized by paper research, implementation/protocol, data comparison, critical analysis and delivery; all experimental families and statistics are placed in the folded appendix, and the complete results directory is traceable. REPORT retains detailed historical explanations.

1. This article: full sources, constraints, current results and next steps.
2. [README.md](../README.md): Directory, dependencies, results navigation.
3. [REPORT.md](./REPORT.md): Explanation of results, all protocol differences, running commands.
   Among them [Section 10: Overview of all experiments and data](./REPORT.md#experiment-overview) summarizes shared anchors, gallery-only validation selection, fixed control, expansion, probe exploration maximum and paper gaps by batch; including differences between early G2/V2/P6 and subsequent G2/P8, failure/regression, reconstruction/numeric verification/error cases/cost/perturbation. The unpublished original authors settings are not deduced from the overview, and the protocol and original result files must still be read back for specific runs.
4. When you need to modify an experiment, read the `protocol.json`, parameter record, `source_snapshot/` and corresponding script in the result directory again; do not guess the current configuration from the old report numbers.
5. When the dispute involves the paper, go back to the original PDF. When it comes to emails, go back to Section 3 of this article and the original sentence corresponding to HISTORY.

### The conclusion of the current sentence

We independently implement CSA/PCA/LDA within the instructor-approved ORL/MNIST/grayscale FERET scope. Current matched Euclidean gray CSA22->16 is81.72% versus PCA30->18 at77.22%; Gabor CSA24->23 is87.53% versus PCA24->23 at85.72% and PCA33->25 at88.41%. Every comparison shares the input array, ten splits and NN rule within its representation. Context/input exploration and unknown author settings remain disclosed. Earlier cosine81.84/88.75 representatives and other historical protocols are retained as history. DATER remains a negative extension.

**The latest 2026-10-08 DATER extension is completed and stopped according to subsequent authorization:** The user is now required to complete the DATER execution; [Full results, protocols and limitations](./REPORT.md#orl-dater), source `dater.py`/`run_orl_dater.py`, independent verification `verify_orl_dater.py`, score read correction `evaluate_orl_dater.py`, result `results/orl_dater/`. Fixed 2π clipping, 4200–4219, G2/P8, (4,2,3)=24 dimensions; DATER direct NN71.64±3.18%, plus ordinary LDA 23 is 67.11±3.59%, with the same conditions CSA74.33/80.13 and PCA82.70/88.81; the relative CSA is −2.69/−13.02pp respectively, which is not improved. 20 new DATER models, 40 reuse controls, 1194 mode updates and 38,400 prediction verification passed. 19 models reached the upper limit of 20 rounds, only the 18th round of 4219 met the threshold, and the joint DTC dropped 165 times, which is not called full convergence/global optimum. The initial free path strict verification failure record is retained; instead, independent actual trajectory verification is added and 20 free references are added to the recalculation sensitivity report. The maximum free final direction difference is about 1.01e−5, and it is not claimed to be completely equal round by round. The first scoring JSON misreading failure occurred before writing the score. A new reading correction entry was added, and the fitting source code/model/history remained unchanged. The two correction verification entries were frozen before successful scoring, and the failure and sensitivity cannot be omitted. DATER's complete unit initialization and generalized feature update are as shown in Figure 3; unit-norm columns/symbols, Tmax20, ε.001 are fixed conventions of our group, and there is no ridge/QR/singular fallback. TA's Tmax3 is suitable for CSA; DATER is a new method extension, TA has not confirmed its parameters, and the paper does not match the ORL24D line; CSA paper 90.9 is only a reference for different methods. Original sharing, gallery parameter selection, context expansion and probe extreme value remain independent; formal submission materials are still to be implemented, and MNIST/FERET has not been changed. To rerun, you must press REPORT to use the supplementary verification and read correction entries, and do not call the verify_models/evaluate path that the original driver is known to have failed.

**The latest controlled experiment on 2026-10-08, three items were completed and stopped:** The user requested comprehensive planning and implementation of previous recommendations, and then selected "Complete the controlled experiment first, DATER and submit material retention plan". Source code `run_orl_controlled.py`, result `results/orl_controlled/`, [complete evidence and retention plan](./REPORT.md#orl-controlled). Freeze seeds 4200–4219 before scoring, σ2π/π×crop/context four inputs, the paper's dimensions four methods, identity/Tmax3/ordinary LDA/unit-norm columns mean-centered cosine and all source/input/index/used historical evidence hashes. 320 new experimental models and 160 CSA independent numerical calculations, 160 PCA characteristic equations and 102400 NN predictions passed. The four inputs of CSA24→23 are 80.13±3.49/84.56±2.44/81.25±3.03/87.08±2.30%, and the π context is +6.95pp (2 0/0/0), still 3.82pp behind the paper, with the same budget PCAπ context 91.08%; σ within-crop effect +1.13, context effect +2.52, difference in difference +1.39pp, only descriptive evidence. CSA390 four-input 88.66/91.16/88.70/90.09%, the context decreases σ but decreases by 1.06pp. Reusing the 320 model, probe both eyes along the original image x/y±1 pixel, 1280 score zero fitting, 409600 independent NN predictions and all 1280 saved file readbacks passed; the low-dimensional CSAπ context average −0.08pp, the worst direction mean −0.52pp, the worst single split/direction −1.875pp, does not cover single-eye misdetection/rotation/large offset, and does not prove universal robustness. There are 3200 records of stage_C errors covering 400 different photos, 224 corrections/111 new additions, CSAonly158/PCAonly249, the original image/alignment image/nearest neighbor has been verified; there is no artificial eye point true value, and it is not attributed to the only reason. Measured 830/618792 weights, calculated deployment array 228272/5171968 bytes, native CoreUltra9 275HX two-thread precomputed feature 320probe projection + LDA + NN about 21–29/60–82ms, pairing 2.08–3.29 times, excluding Gabor/training, not peak memory. The protocol and code have not been changed, and the environmental information/all negative controls are retained; manual visual/summary readback and disturbance graphs are not part of the standard stage automatic output. The context is extended, and the unknown setting has not been confirmed by the author; history 79.66/81.41/87.84 and exploration maximum are not replaced, and pairing improvements cannot be calculated across different splits. DATER was not implemented in this controlled round at that time; subsequent DATER has been completed separately, and reports/displays and public repository releases have not yet been implemented; detailed 20 model extensions, 3–4 pages/9 minutes, and repository planning have been recorded in REPORT, and MNIST/FERET has not been adjusted.

**The latest limited optimization within the 2026-10-08 cut has been completed and stopped according to user authorization:**[Before and after comparison, parameters and evidence](./REPORT.md#orl-ta-crop), source code `optimize_orl_ta_crop.py`, result `results/orl_ta_crop_optimized/`. Fixed original 400 images of 40 categories, G2/P8, seeds 20–29, binocular alignment/balanced 56×46, 5×8 Gabor output 28×23×40, Tmax3, ordinary LDA and paper dimension. Four inputs σ=2π/π×zero/reflect, 39×39 core, λ₀=4, stride00 after cropping inner filter; no context/power transformation/shrinkage/new rank. My own 80 gallery complete 16-fold selection of the first two inputs, and then two initialization × six NN rules; 960 inner models, 280 candidates, ten groups of selections frozen and independently verified, 40 new outer layer fittings + 40 historical baselines. CSA24→23 is**81.25→81.41±2.41%** (+0.16pp, 2 wins,4 ties,and4 losses, the highest is 85.63%, 0/10 reaches 90.9%), CS A390 is 90.00→88.41%, PCA24→23 is 88.63→88.41%, PCA33→25 is 92.72→91.69% (paper 87.2%). The inner layer 508/800 → 566/800 → 568/800 improvement has not been translated into substantial outer layer income, and the reason has not been independently confirmed. In the end, there are six groups of π/reflect, one group of π/zero, three groups of 2π/zero, identity/HOSVD=8/2, all unit-norm columns / mean-centered cosine; you cannot press probe to select another unified configuration. 304 selected inner layer CSA independent recalculations, 22,400 inner layer predictions, 20 outer layer CSA independent recalculations, 20 PCA verification, 40 baseline NN replays and 25,600 outer layer predictions passed; the source code/input/selection hash has not changed, and there is manual JSON readback before scoring and supplementary statistics. Meet the clear TA quantity, size, model and sharing conditions; TA has not confirmed σ/padding/NN/column scale/initialization item by item, and unknown settings cannot be written as an author agreement. The old shared 79.66% different configurations, 81.41−79.66=1.75pp is not the matching gain of this round; the previous 87.84% was an expansion rather than an internal score of this round of tailoring. Negative results, old main table and probe extreme value are kept intact; the search will no longer be automatically expanded in this round.

**Previously limited iteration of ORL unknown parameters, the user has authorized the execution and completion:** [Three-stage evidence and parameters](./REPORT.md#orl-unknown-parameters), source code `optimize_orl_unknowns.py`, output `results/orl_unknown_parameters/`. Keep G2/P8, seeds 20–29, Tmax3, CSA24→ordinary LDA 23/CSA390/PCA24→23/PCA33→25. Each group's own gallery of 80 photos has a complete 16-fold validation: 12 inputs to choose the first two → three powers → two initial values ​​and six NN rules; 3520 inner models, 900 candidates, ten groups of selections are frozen and verified before scoring, 120 new outer layers plus 80 historical controls. CSA24→23 is 81.25→84.31→A87.81→B87.78→C**87.84±3.28%**, the final relative context is +3.53pp (8/1/1), the paper gap is 3.06pp, 2/10 reaches 90.9%, and the highest is 91.56%. The final eight groups of σ=π context, 1 group of original context, 1 group of CDF_min; power 1/0.75 is 7/3, identity/HOSVD is 6/4, all unit-norm columns / mean-centered cosine. Shared C pure CSA390 is 91.03±1.43%, which is 0.53pp lower than the context 91.56; PCA24/33 is 90.69/94.16%, which is also slightly lower. It is not called the joint optimal of the four methods. 416 selected inner layer CSAs were independently recalculated, 72,000 verification predictions, 120 new outer layer models/64,000 outer layer prediction verification passed, and the source code frozen hash has not changed. Keep all negative phases with the old table, extensions and unknown author agreements continue to be single columns. The gap cannot be concluded to be a protocol error; this is still not a blind test, nor is it a global optimum proof. The entire round has been stopped and the search will not be expanded automatically.

**This subsequent MNIST update:** The four-step limited optimization of user authorization has been completed, and independent verification has passed; the CSA gap has not been narrowed. Ten identical seeds G30/G40: original CSA89.66%/90.50%→new gallery-only validation selection 88.89%/90.18%; PCA86.67%/88.03%→86.94%/88.26%. Original 20–22 three-seed CSA90.34%/91.04%→89.33%/90.34%. The old shared master table and all negative results are retained; cubic and decimal means cannot be mixed for optimization gain. For details, see [REPORT's latest MNIST segment](./REPORT.md#mnist-bounded-optimization), the result is `results/mnist_protocol_optimized/`.

**MNIST wrap-up with ORL three-input latest implementation:** REPORT has documented MNIST full reproduction evidence/limitations within the approved scope and Euclidean distance drop ablation, the teacher/TA did not specify Euclidean or cosine. The user then authorized [three sets of fixed input](./REPORT.md#orl-next-directions), and all 120 fittings have been completed and verified: ten identical G2/P8, the paper's dimensions/shared mean-centered cosine, CSA24+ ordinary LDA 23 baseline 81.25%→light combination 78.31%/context 84.31% (context +3.06pp, 9/10 improvement); pure CSA390 is 90.00%→89.56%/91.56% (context +1.56pp, 8 increase, 1 level and 1 decrease). The context PCA24→23/PCA33→25 is 91.00%/94.38%. The two new inputs are extended as single columns and do not replace the shared main table/training-only validation selection/exploration maximum. Source code `run_orl_fixed_inputs.py`, output `results/orl_fixed_input_extensions/`; verification 120 models, 38,400 predictions, 60 independent CSA three rounds of recalculation, and 30 historical baseline correct numbers. The first canvas interpolation verification failure is corrected and retained before scoring. Subsequent verification path corrections are only recorded in `verifier_amendment.json`; the fitting code or scores are not changed. The negative lighting results are retained, and the three-input round has been stopped; DATER was not implemented at that time, and subsequent separate executions are shown in the latest section; inputs are not automatically merged, the grid is expanded, or seeds are added.

---

## 1. Project source, user goals and work agreement

### 1.1 Source

- HKU COMP3314, the working directory belongs to `y2s1/COMP3314`.
- Course Introduction: [Lec0 Introduction.pdf](<../../Lec0 Introduction.pdf>), the user was initially asked to study the 12 papers listed on pages 6–7, ranked by group project rating, difficulty of explanation, and reproducibility.
- , I selected **Concurrent Subspaces Analysis, CSA**, and gradually shifted from topic selection evaluation to experimental reproduction according to the original paper.
- 12 paper rankings, early Chinese and English teaching, reproduction planning and the initial full reproduction experiment list are all saved in [HISTORY History 01/02](./HISTORY.md#history-01). The ranking of historical topics should not be regarded as the conclusion of this round of experiments.
- The course requirements for Section 2 of this article come from user uploaded screenshots, not the CSA paper. Section 3 is the teacher/TA email provided by the user; the email was not read through the connected mailbox, and the record date is not equal to the verifiable email sending date.

### 1.2 How user goals evolve

1. is to complete the research paper and reproduce it as fully as possible. It is required to check the original code first, then plan to implement it by yourself and download the necessary data.
2. The teacher's reply allowed the omission of unobtainable data sets; FERET subsequently obtained it, PIE ultimately failed to obtain it, and the actual range became three data sets.
3. Users wish to adopt reasonable, accurate "our group conventions" for details not published by the author, and note differences.
4. ORL, especially ordinary Gabor CSA+LDA, has a large gap; multiple rounds of requests require comparison of papers, TA requirements and code positioning reasons. You cannot just explain without performing authorized troubleshooting.
5. Subsequent authorization sample size expansion, shrinkage regularization expansion, low-dimensional rank and initialization optimization, fixed configuration multi-split diagnosis.
6. recently authorized finer parameter searches, more splits, and reported results close to/exceeding the paper using the paper's best-results syntax. A 200-split limited grid search has been performed, retaining all low-scoring records, and making it clear that this is an exploration using probe score selection for extreme value .
7. This requirement: Evaluate how far away from the reproduction of the thesis is, propose valuable supplements, and create a comprehensive handover document containing all core requirements including project sources, thesis, teacher/TA requirements, reproduction requirements, and course screenshots. There is no requirement to start new experiments, publish to repositories, or create new chats this time.
8. New request after handover: The user reiterates the course screenshot requirements, clearly authorizes the execution of MNIST four-step limited optimization and provides before and after/paper comparison and TA/the paper compliance range. The experiment has now been completed and verified, CSA has not been improved and the results are retained in single columns; there has been no expansion to the new full grid search.
9. then authorized the completion of the ORL three-input fixed comparison, and then authorized the listing of unknown parameters and actual limited iteration; both rounds have been completed and verified. In this round, the paper's dimensions CSA24→23 are 87.84%. Only the input/parameter sensitivity results are listed in a single column without rewriting the old shared master table or exploring the maximum.
10. is re-authorized to do four cropping inputs according to TA's clear conditions, and limited optimization of the paper's dimensions shared parameters; has been completed and verified, CSA24→23 is 81.41% (only +0.16pp relative to the paired baseline), and other controls have declined. 87.84% were retained as previous context expansion; no searches were automatically expanded based on negative results.
11. authorizes execution of previous planning and subsequently clarifies that only controlled experiments, DATER/submittal retention planning will be completed. Error cases/costs, 320 model-fixed σ × context, and 1280 zero-fit probe perturbations all completed verification; 87.08% of π context was a fixed twenty-split result, not renamed the training-only validation selection winner or the original authors setting.
12. then expressly authorizes the completion of DATER: a fixed input, 20-supervised tensor model, direct 24-dimensional and 23-dimensional LDA, reused CSA/PCA comparison, single column of negative results after verification; no expansion of search or production of submission materials.

### 1.3 User working principles

- Use concise and natural Chinese; the teaching content should clearly explain the relationship between background, shape, formula and code. Previously, Chinese and English translations were required, and formal English reports/presentations can continue to be prepared accordingly.
- Key assumptions affecting the conclusions must be stated. Reasonable and reversible details can be explained before execution; ask again when the scope of the task changes significantly.
- makes precise modifications, retains existing directories, historical results, and failed experiments, and does not easily reconstruct or delete irrelevant files.
- user thought there was too much Markdown, so it has been merged into `REPORT.md`, `HISTORY.md` and the entrance README. This article was added only upon explicit request; priority will be given to updating existing documents in the future.
- Modified verification actual output and prediction, do not treat "script exit successfully" as the experiment has been verified.
- Do not send emails, publish repositories, upload data, or change system settings without authorization.

---

## 2. Course Group Project requirements and scoring: organized by uploaded screenshots

### 2.1 Topic Selection Requirements / Paper Selection

- Select and delve into a machine learning paper related to the course topic.
- Priority is given to major conferences/journals: ICML, ICLR, NeurIPS; AAAI, CVPR, ACL; JMLR, Machine Learning, TMLR; IEEE TNNLS, TPAMI, TIP, TCSVT, etc.
- If you are not sure whether it is appropriate, please consult the teacher/TA. Selected CSAs are published in TCSVT and are clearly related to PCA, dimensionality reduction, feature representation, and linear algebra.

### 2.2 Paper Study and Critical Analysis that must be completed

- Explain problem definition, motivation, methodology, and main contributions.
- Links thesis methods to course concepts.
- Explain experimental setup and results, and determine which evidence supports which claims.
- Critically analyze assumptions, strengths, limitations, and propose reasonable improvements/extensions.
- Reflects the group's own understanding, reasoning, and learning process; simply reciting a summary or demonstrating high accuracy is not sufficient to cover the requirements.

### 2.3 Optional reproduction bonus points / Optional Bonus: Experiment Reproduction

- Reproduction can cover numerical values, graphics, or experiments; bonus assessment considers scope, implementation quality, comparisons, and analysis. This project uses the full-reproduction classification for its approved scope.
- Describe the scope of work, compare with the paper results, and analyze differences and difficulties.
- implemented from scratch, especially when no official code is publicly available, will receive additional consideration in bonus evaluation.
- When submitting code, a clearly organized **public GitHub repository** and `README.md` are required: paper information, environment/setup, running method, reproduction results.
- makes it clear that our group contributes and reuses code, acknowledging the original source.
- Bonus is rated based on quality of work, scope, clarity of documentation, and depth of analysis; not "more runs" or "more than one number" automatically gets full points.
- can use the CS department GPU farm; this project is currently mainly completed using the local CPU, and there is no mandatory GPU requirement.

### 2.4 Deliverables

- **Written Report: About 3–4 pages, written in LaTeX.** Recommendations include: problem/motivation/contribution; key methods, algorithms, theories and course connections; experimental setup and result interpretation; hypotheses, advantages, disadvantages and limitations; group insights, improvements or extensions; reproduction setup, comparison with original results, difficulties, code links.
- Correctly cite the paper and other sources; label results/figures from the paper differently from those produced by our group.
- reproduction submission requires a public code repository, operating instructions and documentation.
- Existing `docs/REPORT.md` is detailed project material, **not a formatted final 3–4 page LaTeX report**.

### 2.5 Presentation & Q&A / Presentation & Q&A

- **9 minutes presentation + 3 minutes Q&A**; all team members should participate in presentation and Q&A.
- Required content: overview (problem/motivation/contribution), methods (core algorithm and course connection), evidence/results (setting, main findings and whether the evidence supports the claim), critical analysis (hypotheses, advantages and disadvantages, limitations, extensions), team insights (what was learned and conceptual difficulties overcome).
- If doing reproduction, briefly present the method, results, comparison with the paper, and experience within the specified time.
- Use clear diagrams and cite sources; slides are concise and focused; emphasize team understanding and reasoning.

### 2.6 Rating / Evaluation Criteria

| project| weight| Core Requirements|
|---|---:|---|
| Paper Understanding | 40% | Accurate and in-depth explanation of issues, methods, contributions and course relevance|
| Critical Analysis & Insight | 30% | Interpret evidence, evaluate assumptions and limitations, and provide supported insights and extensions|
| Written Report | 10% | Clarity, organization and coherence, correct figures and references|
| Presentation & Q&A | 20% | Structure, visual expression, quality of Q&A|
| Optional reproduction bonus | Up to 10 additional percentage points| Separate from base scoring; quality, scope, documentation, depth of analysis|

**Decision Impact: 70% of the foundational component focuses on understanding and critical analysis. There is a wealth of reproduction material out there, but it still needs to be translated into clear reports and 9-minute narratives. There is no guarantee of final results or full bonuses.**

---

<a id="correspondence"></a>

## 3. Communication between teacher, TA and author: original sentence and implementation meaning

### 3.1 Agreement confirmed by teacher (email provided by user)

> FERET and CMU PIE are not held by the teaching team. Request them here:
>
> - FERET Fa/Fb, 1,195 subjects: https://www.nist.gov/itl/products-and-services/color-feret-database
> - CMU PIE: https://www.cs.cmu.edu/afs/cs/project/PIE/MultiPie/Multi-Pie/Home.html
>
> Use 63 subjects, poses C27, C05, C29, C09 and C07, illuminations 08/11 for PIE-1 and 10/13 for PIE-2.
>
> **If either set cannot be obtained in time, skip it. ORL and MNIST are enough.**
>
> Align FERET, ORL and PIE by fixing the two eyes, then normalize and apply histogram equalization: FERET 41×27, ORL 56×46, PIE 64×64. MNIST stays 28×28; use 500 images per digit.
>
> Gabor uses five scales and eight orientations. Reconstruction keeps 56×46×40 (ORL) and 64×64×40 (PIE-1). Recognition downsamples to 28×23×40 (ORL) and 16×16×40 (PIE); MNIST stays 28×28×40.
>
> FERET: first 50/100/200 subjects for training, the rest for testing; Fa is gallery, Fb is probe. ORL: 2 images per subject at random for training/gallery, the other 8 as probe. PIE: 3 per subject at random as gallery, the other 7 as probe. MNIST: G30/P470 and G40/P460. Classify with nearest neighbour.
>
> Tmax is the iteration limit of CSA. The paper sets Tmax = 3 for the recognition experiments. N is the number of training images and Nc is the number of classes; before LDA, keep the PCA or CSA dimension at most N − Nc, so the within-class scatter is not singular.
>
> If a dataset or setting cannot be matched exactly, **state the difference in the report. That will not affect the final grade**.

Complete email and application process: [HISTORY History 03](./HISTORY.md#history-03). The image size uses the array height × width in the code; the eye coordinates are (x, y) and cannot be reversed.

Implementation instructions: FERET our group uses Fa/Fb of the former q identity to learn, other identities Fa is used as gallery, and Fb is used as probe; define "previous q" in the order retained in the official matching table, and the order belongs to the record agreement. LDA front dimension ≤ N − Nc is a necessary rank upper limit control. **There is no guarantee that all actual input within-class scatter will satisfy rank** and numerical zero space processing is still required.

### 3.2 TA Qiyuan latest reply

> Dear Zhengwei,
>
> This is a 2008 project and is no longer maintained. The teaching team does not have the original code or hyperparameter records, so please set the remaining ORL alignment and Gabor choices from the public literature and standard practice. Keep them fixed across methods, and state each difference in the report. An exact match to the published numbers is not required and will not affect the grade.
>
> Best regards,
> Qiyuan
> TA, COMP3314

Original sentence: [HISTORY follow-up communication](./HISTORY.md#history-14). Meaning: The remaining ORL alignment/Gabor can be determined according to public literature and common practice, but the same comparison conditions are fixed and consistent across methods**, and the differences will be explained item by item. There is no cancellation of eye alignment, training volume, Tmax or NN requirements, nor confirmation that our group's new settings are equal to the author's original settings.

### 3.3 PIE obtained the conclusion: both letters are from Terence Sim

> Unfortunately, I do not have the rights to distribute the CMU PIE dataset. The rights belong to CMU.

> I do not have Simon's current contact. But he left cmu a long time ago.
>
> He also does not have the rights to distribute.

The user confirmed that Simon refers to Simon Baker. Record: [HISTORY 12](./HISTORY.md#history-12).

- our group did not obtain the **original CMU PIE** within the time limit, which is omitted by permission of the instructor.
- The correct reason is that the author contacted does not have distribution rights and the rights belong to CMU; the reply stated that Baker has left CMU and does not have distribution rights.
- **Cannot be adapted to indicate that the author does not have access, that the data has been destroyed, or that it is not available worldwide.** No unprovided headers/sent date attached.
- Multi-PIE is not an equivalent replacement for the original PIE. The official website link given does not prove that the 63-person subset of the original paper has been obtained.
- Do not fill in Table III, Fig.5(b), Fig.8 of PIE.

can be used for formal English reports:

> We were unable to obtain the original CMU PIE dataset within the project timeframe. Terence Sim informed us that he does not have distribution rights, which belong to CMU. He also explained that Simon Baker had left CMU and likewise did not have distribution rights. We therefore omit the PIE experiments, as permitted by the instructor, and report our reproduction scope as ORL, MNIST, and grayscale FERET.

---

## 4. Target paper, background knowledge and scientific claims

### 4.1 Paper identity and source

**Dong Xu, Shuicheng Yan, Lei Zhang, Stephen Lin, Hong-Jiang Zhang, Thomas S. Huang.** *Reconstruction and Recognition of Tensor-Based Objects With Concurrent Subspaces Analysis*. IEEE Transactions on Circuits and Systems for Video Technology, 18(1),36–47,January2008. DOI:10.1109/TCSVT.2007.903317。

- [Local original PDF](../Reconstruction_and_Recognition_of_Tensor-Based_Objects_With_Concurrent_Subspaces_Analysis.pdf)
- [HKU agent IEEE page given by user](https://ieeexplore-ieee-org.eproxy.lib.hku.hk/document/4358655)
- [DOI page](https://doi.org/10.1109/TCSVT.2007.903317)
- the paper text has been extracted at `tmp/pdfs/csa_audit_text.txt`. The extracted tables/formulas may be missing characters, and the key values ​​must be seen on the PDF page.
- Page picture `tmp/pdfs/csa_audit-08.png` is printed page 43: Table I/II and best-results description; `-09.png` is page 44: Fig.7/8 and Table III/IV. The actual content of the PDF shall prevail, and there shall be no confusion between the document page and the printed page.

### 4.2 What questions it raises and what it does

- The image is originally a two-dimensional matrix; the Gabor image is a third-order tensor of height × width × channels. Traditional PCA pulls all elements into vectors, and the projection matrix may be very large; the direction learned under high-dimensional small samples is limited by the number of samples.
- CSA maintains multiple modes (modes) of the object, learns projection bases such as rows, columns, and channels respectively, and turns the object into a smaller core tensor.
- is to minimize the reconstruction error, not to directly maximize the classification accuracy. Using column orthogonal projection is equivalent to maximizing the total energy of the core tensor after projection.
- alternately fixes other modes and updates the leading feature subspace of the current mode; the updated basis is immediately used for subsequent modes.
- When recognizing, expand the core tensor into features, directly NN, or connect to ordinary Fisher LDA and then NN. Unsupervised CSA uses fitting images; LDA also uses learned identity labels.
- two-dimensional CSA is used for grayscale faces; three-dimensional CSA is used for 40-channel Gabor. The sample axis is not an object mode, and the sample axis of N pictures cannot be compressed together.

### 4.3 Key Mathematical and English Terms

| Concept How| English| Meaning in this project|
|---|---|---|
| tensor| tensor | Multidimensional array, such as ORL recognition tensor 28×23×40|
| mode /Expand| mode / unfolding | fixes a certain dimension and arranges the other dimensions in columns to facilitate finding the mode covariance|
| core tensor| core tensor | The projected r₁×r₂×r₃ representation, not a classification label|
| Orthonormal basis| orthonormal basis | UₖᵀUₖ=I, maintain projection/reconstruction equivalence|
| Parallel subspace analysis| concurrent subspaces analysis | Multiple mode subspaces are jointly optimized, and the actual algorithm is updated alternately by mode.|
| intra-class/between-class scatter| within-/between-class scatter | Fisher LDA wants compactness within classes and separation between classes|
| Small sample problem| small sample size problem | N has small relative dimensions and unstable covariance/divergence estimates|
| gallery/probe| gallery / probe | NN reference image and image to be recognized|
| shrinkage regularization| covariance shrinkage | our group expansion, suppress the excessive amplification of small eigenvalues ​​within-class scatter|

core formula (illustrated, ×ₖ is the k-th mode product):

```text
Gᵢ = Xᵢ ×₁ U₁ᵀ ×₂ U₂ᵀ … ×K U_Kᵀ
Xhatᵢ = Gᵢ ×₁ U₁ ×₂ U₂ … ×K U_K
min Σᵢ ||Xᵢ − Xhatᵢ||²_F, subject to UₖᵀUₖ=I
```

After other modes of the current mode are projected into Yᵢ, `Σᵢ Yᵢ(k)Yᵢ(k)ᵀ` is constructed, and the leading eigenvector is taken as Uₖ. PCA is an eigendecomposition of vector space; CSA imposes a separable multi-mode structure. The two cannot be considered to have exactly the same parameters/expressive capabilities just by saying "the feature dimensions are the same".

ordinary LDA solution `S_b w = λ S_w w`; ORL G2: N=80, Nc=40, so the pre-LDA dimension is ≤ 40, and the final dimension is also limited by the effective Sw rank and Nc−1. Even if the eigenvalues ​​within small classes are not zero, sampling noise may be amplified.

### 4.4 Contribution, background and limitations

- In the research on traditional visual representation and small sample dimensionality reduction around 2008, the emphasis on retaining the tensor structure, reducing projection parameters, and expanding the available projection directions is an important contribution of this paper.
- The representation method does not rely on a complete identity × pose × illumination set like Tensorface; the reconstruction experiment can be learned with only one picture per person.
- "The advantage of small samples" is an important proposition, but it does not only study small samples; the paper also uses MNIST to examine high-dimensional digital representation. CSA cannot be said to be a supervised algorithm specially optimized for the classification of small face samples.
- Large reconstruction energy does not necessarily retain more discriminative information; alternating optimization has structural limitations, and limited iteration, initialization, mode rank, and input details can affect the results.
- the paper's CSA390 and PCA76, as well as pure CSA390 and CSA24+LDA23, are not equal features/equal storage budgets.
- The results of the old small data set cannot directly infer the superiority of modern large-scale face or digit recognition; the goal of this project is to reproduce and analyze the paper, not to establish a modern SOTA.

### 4.5 Accurate explanation of “best results” in the original paper

the paper IV-C (printed page 43) states:

> we report the best results, with the optimal parameter configurations given in brackets.

then explained that the brackets mainly represent the optimal dimensionality reduction dimension/pre- and post-level dimensions. The paper does not explain the number of repeated splits, random seeds, mean /SD, or whether to choose the maximum value among many random splits.

**Can confirm that it reports the best parameter results; cannot confirm that it reports multiple averages, nor can it confirm that it selects the maximum value across 200 splits like our group's latest experiment. There is no evidence to accuse the author of seed selection or fraud.**

---

## 5. Data acquisition, existing documentation and specific protocols

### 5.1 Data List

| data| current status| Location and Source|
|---|---|---|
| ORL / AT&T faces | has downloaded verification, 40 people × 10 photos = 400, original 112 × 92| `data/raw/orl/`；Cambridge AT&T archive |
| MNIST | Official test IDX 10,000 pictures have been downloaded; the first 500 pictures of each category constitute 5,000 samples| `data/raw/mnist/`; OSSci MNIST mirror, which has been used by the official MD5|
| original grayscale FERET| has been authorized to download the required subset, 3680 TIFFs, official 1195Fa/Fb pair| `FERET/`, gray_feret included in NIST authorization archive|
| Original CMU PIE| Not obtained, omitted with teacher permission| See Section 3.3 for the acquisition process.|

ORL download source: [att_faces.zip](https://www.cl.cam.ac.uk/research/dtg/attarchive/pub/data/att_faces.zip). MNIST source and hash see `data/dataset_manifest.json`. **This list is a snapshot of the early download stage. The scopes of "FERET not obtained" and "not yet implemented" are now obsolete and should not be used to cover subsequent FERET facts.**

MNIST paper says both "the first half of the test set" and "500 images per category", but the actual official first 5,000 images are not balanced. Our group selected the first 500 pictures of each number according to the teacher's requirement of "500 pictures per category"; the specific original authors sample index is still unknown.

### 5.2 Document conventions that FERET must comply with

- Read [FERET/README.md](../FERET/README.md), `download_report.json`, `verification.json` first.
- **Priority to use `official_fa_fb_pairs.csv`**: 1195 identity 2390 pictures, all valid eye coordinates; match the identity according to the official gallery list. The recognition graph cannot be re-picked from additional candidates.
- All 3680 TIFFs, each original width 256, height 384, attached `.gnd` and XML; 2390 standard pairing included.
- has 1196 people in the official gallery list and 1195 people in Fb; unique 00989 will not enter the matching. Don't just increase it to 1196 pairs.
- TIFF exists in L and grayscale palette P mode, reads `Image.open(path).convert('L')`.
- The official left and right eyes refer to the left and right of the human body, sorted by x and converted to the left and right of the screen, with coordinates (x, y). An additional 317 candidate missing eye coordinates are not part of the standard pairing.
- is not to convert the Color FERET color image to gray, but to authorize the original grayscale library that comes with the large archive.
- "Not yet preprocessed" in the download description is only the status when the download is completed; `data/processed/feret/` and experimental output will be available later.
- Do not publicly upload raw FERET or restricted feature caches; retrieval instructions and scripts can be organized separately from restricted data. No account number or password is written in the handover or public documents.

### 5.3 Confirmed agreement with our group Unknown details

| project| Confirmation request| our group agreement/unknown content|
|---|---|---|
| ORL grayscale| 56×46, binocular alignment, normalization, histeq, G2/P8| YuNet/Haar approximate eye point, target eye distance, cropping padding, interpolation; the original manual eye point is unknown|
| ORL Gabor recognition| 28×23×40, 5 scales and 8 directions| Core size, boundaries, amplitude processing, channel order, sampling; saved per protocol|
| MNIST | 28×28, 500 per category, G30/P470 or G40/P460, Gabor28×28×40| Top 500 indexes of each category, specific Gabor numerical parameters, random seeds|
| FERET | 41×27, q50/100/200, other identities Fa/Fb recognition| Official Pairing Order as Training Identity Order, Eye Target, Intensity Processing, Distance|
| CSA | recognition Tmax=3, orthogonal alternating update| identity/random/HOSVD initial value, optional centering, epsilon=.001|
| LDA | front dimension ≤N−Nc, ordinary LDA baseline| Numerical zero space threshold, direction column normalization, final dimension|
| Category| nearest neighbor| Centered/origin cosine, Euclidean; same condition across methods|

The old Gabor basic formula λ=4√2^s (s=0...4), θ=oπ/8 (o=0...7), σ=2π, DC-free review and response amplitude; `gabor.py` retains the old reflect process. Subsequent ORL experiments used theoretical support for zero bounds and 39×39 zero bounds, without replacing the MNIST/old reconstructed cache.

In the latest exploration, the target eye point of d20 is (13,24)/(33,24), affine replicate; d18 is (14,25)/(32,25), affine zero. Gabor has 39×39 cores, zero padding, first 56×46 filtering, and then `[::2,::2]` sampling. **Affine clipping padding and Gabor convolution padding are different settings.**

has been previously queried and used in the document:

- [CSU official normalization description](https://www.cs.colostate.edu/evalfacerec/data/normalization.html): fixed eye point, cropping and intensity processing; not proof of the author's ORL protocol.
- [Wiskott et al. 1997 paper](https://cenl.ucsd.edu/pubs/ieee-1997.pdf): Multi-scale direction Gabor and amplitude representation; our group process cannot be called its complete elastic graph matching.
- [Kolda–Bader tensor review](https://www.mathsci.ai/publication/TensorReview.pdf): HOSVD with alternating updates; HOSVD is our group initialization, not the restored author code.

---

## 6. Code implementation, reproduction type and verification boundary

### 6.1?

has previously searched the original authors/paper-related pages, but did not obtain the **official CSA reproduction code that has been verified to be runnable**; the teaching team clearly has no original code/hyperparameter records. "Our group was not found" should not be written as "prove there was never any code". Currently, it is implemented by itself according to the formula of the paper, and the basic operations are provided by NumPy/SciPy, without calling the ready-made CSA/Tucker/PCA/LDA learning algorithm.

The code is written with the help of Codex. The team should read, understand, verify, and truthfully disclose the auxiliary sources and member work according to the course regulations. Don’t wrap AI-generated/reused content into completely independent handwriting.

### 6.2 core implementation

- `csa.py`: General n-order CSA, projection/reconstruction, PCA, general Fisher LDA, NN. mode is updated sequentially; sample axis is not compressed.
- Added optional `initial_bases` for HOSVD basis input generated by training, verifying shape, finiteness and orthogonality, and copying the incoming array. The identity/random path without this parameter has returned to the same element-by-element consistency as the historical implementation.
- PCA centering; The original baseline of CSA is not centered, and the centering can be compared explicitly later. Both treatments must be recorded.
- ordinary LDA uses Sw positive feature subspace whitening and numerical zero space elimination, α=0, and no new ridge.
- LDA column scale can be unit-norm columns or Sw metric scale; NN can be gallery mean mean-centered cosine, origin cosine, centered Euclidean. Any scale in the linear mapping direction will affect the actual distance and cannot be treated as an irrelevant detail.
- HOSVD mode covariance and training mean are generated only from the current fitting image.

### 6.3 shrinkage, sample size and large budget are extensions

```text
Sw(α) = (1−α)Sw + α trace(Sw)/p · I
```

α candidate 0/.01/.05/.15/.35/.65/1, selected through in-gallery verification. Positive α changes the ordinary LDA objective, so the single column expands our group; not the original algorithm of the paper, nor the automatic Ledoit–Wolf estimator. Fixed sample size experiments also have α=.15 controls.

- The added training graph for G3/G5 is an extension and cannot be written as G2/P8 reproduction success.
- Pure CSA560/720/1120 does not connect to LDA, so it is not restricted by ≤N−Nc before LDA, but has a larger budget than the original pure CSA390 and is single-column.
- The current NN/Gabor convention can be explored with instructor permission; the respective maxima of different methods using different inputs cannot be used to prove that the method is stronger.

### 6.4 The four types of results must be separated

1. **Shared input, fixed paper dimension control**: used for cross-method comparison, retaining the original table dimension.
2. **gallery-only validation selection**: Selection only uses gallery fold; the outer probe is not used for this round of selection. However, the historical probe has been developed and observed and cannot be called a new blind test.
3. **probe selected exploration maximum**: the latest 200 split grid; the learning model only fits the gallery, but the probe score selects the configuration and seed, and the test information has been used in the selection stage.
4. **Our group expansion**: positive α shrinkage, larger pure CSA budget, G3/G5 training volume, etc.

The 200 mean of the fixed configuration of the posterior winner is also selected by the configuration and cannot be called an independent unbiased generalized estimate. The new random seed still reuses the same 400 images, and the observed data cannot be turned into an independent blind test by changing the seed.

### 6.5 What has been checked

- The original eye point/cropping has an impact, it has been corrected, and there is a fixed parameter comparison that only replaces the eye coordinates.
- independently checked CSA for mode-by-mode covariance, projection, reconstruction, LDA divergence and generalized characteristic equations, NN; no core computational errors were found that were sufficient to explain the remaining gap.
- Checks spatial axes, channel displacement, realignment, distance from origin/orientation scaling, kernel support/rounding, and increased iteration; no single setting restores all normal CSA+LDA values.
- FFT Gabor and direct two-dimensional convolution check, the error is about 3.1×10⁻⁷.
- fully preserves split, prediction, configuration, source code/feature hash, mean/SD; verification that the records and calculations are internally consistent does not prove that the unknown author protocol has been matched, nor does it mean that all historical runs were independently refitted by another program**.

---

## 7. Current results and distance from the paper

The value unit is %, and the difference unit is percentage point (pp). The following is a juxtaposition of different calibers, and each row has been marked; it cannot be combined into a ranking list of "our group comprehensively exceeds the paper".

### 7.1 Main differences between the three data sets

| condition/method| paper| Current results| Digital Gap and Judgment|
|---|---:|---:|---|
| FERET q50 CSA+LDA, shared fixed cosine| 88.2 | 88.73 | +0.53pp, the value is close|
| FERET q100 CSA+LDA, same as above| 92.2 | 94.25 | +2.05pp |
| FERET q200 CSA+LDA, same as above| 95.2 | 95.38 | +0.18pp |
| MNIST G30/P470 CSA, 3 seeds| 92.8 | 90.34±0.15 | −2.46pp; CSA outperforms PCA with same input for trend preservation|
| MNIST G40/P460 CSA, 3 seeds| 92.4 | 91.04±0.25 | −1.36pp |
| ORL pure Gabor CSA390, shared paper dimension, 10 seeds| 94.4 | 90.19±2.37 | −4.21pp |
| ORL Gabor CSA24→LDA23, HOSVD start/context extension,10 splits |90.9|**88.75±2.89**|−2.15pp; current representative, exploratory comparison |
| ORL Gabor CSA24→LDA23, full-square identity/context variant,10 splits |90.9|88.81±2.97|−2.09pp; separate initialization-shape variant |
| ORL ordinary Gabor CSA+LDA, historical rank-refinement gallery selection, 10 seeds| 90.9 | 83.28±3.30 | −7.62pp; up to 89.06, but the dimension is adjusted according to gallery|
| ORL grayscale CSA+ ordinary LDA, subsequent optimization, 10 seeds| 84.1 | 78.56±3.98 | −5.54pp, the original value has not been restored yet|
| ORL grayscale CSA+ shrinkage LDA extension, 10 seeds| original ordinary LDA 84.1| 84.13±2.38 | The numbers are close, but the algorithm has changed and the original ordinary LDA cannot be claimed to match|
| ORL Gabor CSA+ shrinkage LDA latest extension, 10 seeds| original ordinary LDA 90.9| 85.47±4.57 | is still 5.43pp lower and is extended|

The grayscale follow-up of 78.56 is not the largest mean among all historical results; the previous ORL audit gallery selected the grayscale CSA as 79.75±4.33. Don’t use “latest” to imply that every parameter adjustment will be better. This article only lists the clearly named processes and keeps negative results.

FERET fixed cosine PCA+LDA: 89.08/90.87/93.87; the paper 84.6/90.6/93.4. q50 our group PCA is higher than CSA, q100/q200 CSA is higher, **all relative advantages and disadvantages of the paper are not fully restored**. FERET is a fixed identity split, without random SD; the old table SD=0 is a placeholder, and the current main table is left blank.

MNIST fixed PCA: G30=87.52±.40 (paper 88.5); G40=88.58±.37 (paper 90.5). Historical method-by-method training-only validation selection: PCA90.12/90.75, CSA90.22/91.22, because the method can use different inputs, single column exploration, and no replacement of the shared main table.

The follow-up MNIST shared input limited optimization is listed separately: four Gabor supports/boundaries, each outer split is independent, pre-screening up to two inputs in the 5-fold gallery, and then selecting shared NN and identity/HOSVD; the paper PCA60/50, CSA810/975, Tmax3 remains unchanged, no LDA is connected, and no training maps are added. All 20 groups selected were frozen and the 200 selected inner models were replayed before scoring; 20 groups all selected identity. 160 ratings, 744000 predictions, projection sampling/orthogonality of 78 different outer models and all NN verification passed. The CSA updates of the two Gs were independently recalculated with a maximum subspace error of 4.13×10⁻¹⁰. The ten-time mean of the new CSA is 88.89%/90.18%, which is a negative result and **does not replace the previous three seed main tables of 90.34/91.04**. The input and distance are only our group's conventions: satisfy the confirmed teacher constraints, retain Table IV dimensions, and do not indicate that the unknown author settings have been confirmed; this round does not expand the rank grid or press probe to select another input/seed. G40 only changes 90.62% of the input for subsequent ablation and does not change the name to verify the winner.

Authoritative positioning: The current share table is `results/orl_protocol_audit/shared_comparison.csv`. `results/shared_protocol_final/shared_comparison.csv` is an **earlier version**, and the old ORL scores and FERET SD placeholders cannot be used as the current final table.

### 7.2 200 split Best observation search: completed, verified

Range: seeds 3000–3199, 200 in total; 3 input branches × 15 CSA cases, 45 fits per split, **9000 fits**in total; 6003 effective fixed configurations × 200,**1,200,600 scoring grid**. The same 400 figures were reused, not millions of independent experiments.

| record| maximum/correct number| seed | Fixed winner configuration 200 mean ±SD| reaches the number of papers|
|---|---:|---:|---:|---:|
| Ordinary CSA32→LDA24| **95.00 / 304 of 320** | 3158 | 86.415625±2.446007 | ≥90.9：5/200 |
| Pure CSA560| **97.50 / 312 of 320** | 3188 | 91.43125±1.860908 | ≥94.4：8/200 |
| Pure CSA390, the paper's dimensions budget| **97.1875 / 311 of 320** | 3025 | 91.998438±1.915624 | ≥94.4：15/200 |
| Normal CSA24→LDA23, the paper's dimensions configuration| **88.4375 / 283 of 320** | 3166 | 80.159375±2.901389 | ≥90.9：0/200 |

Complete winner configuration:

| parameter| Normal 95.00| Pure 560: 97.50| Pure 390: 97.1875|
|---|---|---|---|
| input| d20, replicate affine, fixed39 zero Gabor| d18, zero affine, fixed39 zero Gabor| Tongchun560|
| Amplitude processing| x^0.75 | sqrt(x) | sqrt(x) |
| CSA rank| 4×1×8=32 | 14×2×20=560 | 15×1×26=390 |
| initial base| learning set HOSVD| learning set HOSVD| identity |
| CSA centering| false | false | false |
| LDA | Normal α=0, 24 dimensions, unit-norm columns direction| None| None|
| NN | gallery mean centered Euclidean| gallery mean mean-centered cosine| origin cosine|
| Tmax | 3 | 3 | 3 |

Original 24→23 highest configuration: d18/sqrt/identity/noncentered, unit-norm columns LDA, gallery mean mean-centered cosine.

- output root: `results/orl_best_search/`.
- `best_results.json`: global winner of both methods; `paper_dimension_best.json`: original 390 and 24→23 subgroup.
- `configuration_summary.csv`: 6003 configuration statistics; `scores/*.npz`: All 200 scores; `near_or_exceed.csv`: 6432 records of papers with a bar spacing of no less than −1pp.
- Ordinary CSA+LDA has 2306 grids ≥90.9, involving 62 seeds; pure CSA has 133 grids ≥94.4, involving 28 seeds. This is the number of successfully configured seeds for the entire grid and cannot be used as a fixed configuration success rate.
- `verification.json` passed: 20 different high-scoring models were refitted and 6400 predictions were independently checked; all CSVs correspond to the scoring grid. Not equal to 9000 models all being refitted independently.
- `statistical_readback.json` passed: independent readback of 6003 configuration statistics, replay of two winners of the paper's dimensions, comparison of 6 shared inputs, consistent frozen source code hash.
- `verified_best/` retains high score embedding and replay records, `source_snapshot/` retains the source code, and `best_distribution.png` is the corresponding winner distribution map.
- `statistical_readback.json` and `same_input_controls.json` are generated by supplementary readback code and should not be claimed to be automatically generated by the standard stage without checking.

is the same as the winner split, post hoc comparison of input and distance: seed3158 ordinary CSA32+LDA24=95, original CSA24+LDA23=84.0625, pure CSA390=87.1875, PCA33+LDA25=85.3125. seed3188 pure CSA560=97.5, original CSA24+LDA23=81.875, pure CSA390 and PCA33+LDA25 are both 96.5625. These are not full split advantages, nor are they a budget comparison.

The English sentence pattern that users request to retain and the accompanying instructions:

> we report the best results, with the optimal parameter configurations given in brackets.
>
> In this reproduction, “best” denotes the maximum probe accuracy observed across 200 predefined random splits and the finite configuration grid. “Optimal” is restricted to that grid. Probe scores were used to select the configuration and split, so these results are exploratory maxima, not an independently validated estimate of generalization. We also report the corresponding fixed configuration's mean and standard deviation over all 200 splits and retain the complete search records.

**Judgment: The high-scoring run is replayable; a single value exceeding 94.4 can occur even if the original CSA390 budget is retained. However, the original CSA24 → LDA23 is still 2.4625pp lower in the current grid. It cannot be said that all the configurations of the original table have been restored.**

### 7.3 Targeted iteration and 100 split diagnosis in gallery

`results/orl_csa_refined/`, seeds 20–29, usually only α=0; shrinkage single column. 16 inner layer folds, each fold 75 learning/5 verification, 40 categories reserved, each gallery is verified once; the front dimension of the inner layer is ≤35, and the outer layer is ≤40. The initial screening of candidates is fitted in the complete gallery, which is approximate pruning and cannot be called unbiased LOO scoring.

- Ordinary Gabor CSA+LDA83.28125±3.298154, max89.0625; previously 82.46875, mean increased by .8125pp, 3 increased/4 same/3 decreased.
- shrinkage 85.46875±4.574447, max90; previously 84.75, 4 increased/4 same/2 decreased.
- is the same as ordinary input pure CSA39089.96875±2.226585, max93.4375; original 24→23 anchor point 80.8125±3.261598; same input PCA33+ ordinary LDA 92.09375±2.357253.
- selected ordinary CSA to retain the total training change energy of 22.60%, the inter-class change of 26.07%, and the original 24 anchor points of 19.11/22.11%. This is not an identifying percentage.
- shrinkage The winner is 77±8.68 after removing α; the configuration is selected by shrinkage, and this number cannot be used to replace the reselected ordinary 83.28.
- `evaluation/verification.json`: 80 ratings, 25600 predictions, recalculation of 60 selected inner targets, Fisher relative residual error at most about 2.45×10⁻¹³, ​​passed.

100 fixed configuration diagnosis is frozen before this round of probe scoring, seeds1000–1099, no amplitude power processing, d20/fixed39, identity/noncentered, unit-norm columns mean-centered cosine:

| fixed configuration| mean ±SD| Highest|
|---|---:|---:|
| Original CSA24→LDA23| 80.925±2.97656 | 87.50 |
| CSA32(4×2×4)→LDA28 | 84.35625±2.84157 | 90.3125 |
| Pure CSA390| 89.26875±1.99095 | 93.75 |

The original 24→23 did not reach 90.9 even after 100 times, which means that under this input, "just change random split" did not restore the original number. The new 200 times also changed the amplitude, rank, initialization, and distance. The difference cannot be attributed entirely to running 100 more times. 100 times of verification, 300 ratings, 96,000 prediction records; does not mean 96,000 independent pictures.

### 7.4 Add extension of training graph: completed

`results/orl_sample_size/`: Seeds 20–29. The first 5 random pictures for each person are used as a training pool, and the last 5 are fixed probes; the first 2/3/5 are taken to form G2⊂G3⊂G5. The unused training pool map of smaller G does not enter P5; G2 also has P8 original protocol anchor point.

| Same fixed P5, 10 times mean| G2 | G3 | G5 |
|---|---:|---:|---:|
| Pure CSA390| 89.80 | 93.95 | 97.45 |
| Pure CSA24| 76.40 | 82.95 | 90.60 |
| CSA24+ ordinary LDA 23| 81.30 | 88.10 | 94.50 |
| CSA24+fixed α=.15 LDA23| 81.90 | 88.40 | 93.90 |
| PCA24+ ordinary LDA 23| 88.45 | 94.05 | 97.45 |
| Pure PCA24| 82.70 | 88.00 | 93.45 |

All four CSA configurations improved with increasing training volume across all 10 seeds. 90 models, 280 ratings, 64400 prediction verification passed, the projection difference of three independent rounds of mode is about 1.31×10⁻¹². Supports the explanation of sample size/small sample estimate effect, but **not the success of the original experiment of G2/P8**.

also explained: the same as 24-dimensional pure CSA → adding LDA increases from 76.4 to 81.3, so "pure 390 is higher than low dimension + LDA" cannot be simply interpreted as LDA must be harmful; the pre-amplification budget is very different.

### 7.5 Reconstruction, Convergence and Graph Coverage

- Qualitative convergence/reconstruction experiments corresponding to ORL Fig.4/5(a), together with early recognition dimension curves, are preserved in `results/available_reproduction_v2/`.
- Use the first image per person, N=40; Gabor56×46×40; equal mode ranks r×r×r. This is **fitting-sample Gabor tensor reconstruction**, not Gabor inversion to grayscale faces or generalization to unseen images.
- `RMSE=sqrt(SSE/N)`, not per-pixel RMSE divided by ND. D is the number of elements in one input tensor.
- PCA storage amount d(N+D); etc. rank CSA storage Nr³+r(56+46+40); CR=ND/number of stored floating point parameters, including shared base, not file byte compression rate.
- `orl_convergence_reconstruction.png`, `orl_reconstruction.csv`, `orl_convergence.json`, `dimension_curves.csv`, `orl_lda_curves.png` are reserved.
- They still use the **early Gabor/eyepoint process** and have not optimized and recalculated with the new recognition; the paper Gabor absolute amplitude is unknown, does not claim that the vertical axes are exactly equal, and does not use post-multiplication coefficients to attach the curve.
- FERET has `paper_comparison.png` and `lda_curves.png` for the tables/dimension curves. Do not label all existing figures as one final input version.
- PIE Fig.5(b)/8/Table III are omitted. Corresponding work for the other figures does not mean every original curve point/configuration was matched.

---

## 8. Explaining the current gap: distinguish evidence strength

### Supported observations

1. Alignment and cropping affect scores, as fixed controls demonstrate. Old low-scoring pipelines must not be presented as the latest result.
2. Low-dimensional mode ranks, initialization, and downstream distance affect ordinary CSA+LDA. Moving to32 dimensions helped, but individual contributions are not isolated.
3. G2 gives less stable Sw estimation; more fitting images improve recognition substantially. Shrinkage helps some settings but does not recover the original ordinary-LDA result.
4. Small-budget CSA maximizes projected energy and may discard discriminative differences; matched-input low-dimensional PCA controls are often stronger.
5. Selection and split aggregation widen the difference between maxima and means. A200-split maximum above the paper does not imply an above-paper mean.

### Still not uniquely determined

- The authors' complete eye/crop procedure, finite Gabor support, magnitude normalization, distance and LDA scaling, initialization, MNIST indices, FERET ordering, and random-split/aggregation conventions remain unknown.
- Original author code/hyperparameters are unavailable for line-by-line comparison. TA permits literature-based choices with disclosed differences; these unknowns no longer block course completion.
- Not finding a core numerical error does not establish identical author inputs, and these results do not establish that the authors selected the best of many random splits.
- Repeated splits overlap on the same400 ORL images. SD describes the split distribution; all probe records cannot be treated as independent observations for significance claims.

### Why CSA need not beat PCA

CSA's separable structure reduces basis parameters and changes inductive bias, while restricting the projection space. Benefits depend on data/ranks. The current4×2×3 representation may be mismatched to the inputs, and CSA is not supervised discrimination. CSA390 and24+LDA have different budgets; our matched24-dimensional experiments also do not establish universal CSA superiority. Failure to recover the relative advantage is a critical-analysis result, not proof that the code must be wrong.

---

## 9. Implementation navigation, environment, and reruns

### 9.1 Key directories/scripts

| File/result| Purpose and status|
|---|---|
| `csa.py`, `gabor.py` | Core CSA/PCA/LDA/NN and historical Gabor implementation|
| `prepare_available_data.py`, `run_available_reproduction.py` | Early ORL/MNIST preparation, fixed experiments, reconstruction/curves|
| `prepare_feret.py`, `run_feret.py`, `select_feret.py`, `verify_feret.py` | Official FERET pairing preparation, initial experiments, training-only selection/checks|
| `audit_orl_protocol.py` → `orl_protocol_audit` | Eye/crop correction, shared-input comparison, gallery selection, fixed controls, rank checks|
| `diagnose_csa_lda.py` → `csa_lda_focus` | Ordinary-LDA numerics, origin, axes/channels, with failed selections retained|
| `optimize_csa_lda.py` → `csa_lda_optimized` | Gallery-only ordinary/shrinkage optimization for grayscale/Gabor, including removal-of-shrinkage ablation|
| `refine_orl_csa.py` → `orl_csa_refined` | Targeted Gabor, HOSVD, ranks, normalization, ten-split results and100 fixed splits|
| `search_orl_best.py` → `orl_best_search` | 200-split exploratory grid, complete statistics, and maximum replay|
| `run_orl_sample_size.py` → `orl_sample_size` | SharedP5 withG2/G3/G5 and matched24-dimensional PCA controls|
| `optimize_mnist_protocol.py` → `mnist_protocol_optimized` | MNIST four inputs,5-fold shared gallery selection, ten-split negative results, and TA/paper scope|
| `run_shared_protocol.py`, `verify_shared_protocol.py` | Historical four-step shared controls; later ORL updates supersede them|
| `docs/HISTORY.md` | Merged13 early documents and subsequent TA correspondence|

Older result directories retain valuable exploratory evidence. Do not delete raw CSVs, protocols, or snapshots for tidiness. The earlier authorization covered Markdown consolidation, not experiment-data deletion.

### 9.2 Environment

Windows PowerShell, Python3.11 (recorded interpreter `C:\Users\gwdsd\AppData\Local\Programs\Python\Python311\python.exe`).

Pinned dependencies: NumPy2.4.6, SciPy1.17.1, Pillow12.3.0, Matplotlib3.11.1, threadpoolctl3.6.0; preprocessing OpenCV-headless4.12.0.88 is installed in project `.deps/`. See both requirements files.

```powershell
Set-Location 'D:\HKU\COURSE\y2s1\COMP3314\COMP3314GP'
# Install dependencies only if the environment is not already prepared.
python -m pip install -r requirements.txt
python -m pip install --no-deps --target .deps -r requirements-preprocess.txt
```

These experiments ran on the local CPU without a GPU requirement. The recent search used3 processes with2 BLAS threads each and took about23 minutes. Timing depends on caches/hardware; peak memory was not measured and no other-laptop resource guarantee is made. No experiment was pending at this handoff date.

### 9.3 Minimal high-score replay

```powershell
python search_orl_best.py --stage replay --family 'CSA+LDA'
python search_orl_best.py --stage replay --family CSA
```

Replay the saved95% and97.5% winners separately without reselection; these are not typical random runs. Complete390-dimensional and original24→23 winners appear in `paper_dimension_best.json`; this CLI has no separate390 family option.

### 9.4 Rerunning all200 splits: only when needed

```powershell
python search_orl_best.py --stage prepare --output results/orl_best_search_rerun
python search_orl_best.py --stage run --output results/orl_best_search_rerun
python search_orl_best.py --stage summarize --output results/orl_best_search_rerun
python search_orl_best.py --stage verify --output results/orl_best_search_rerun
python search_orl_best.py --stage plot --output results/orl_best_search_rerun
```

Proceed after each stage and result check succeeds. The prepare output directory must not exist. Run disjoint batches using `--start/--stop`, with exclusive stop; full range3000–3199. **Existing ORL feature caches are required; this is not a single fresh-checkout download/reconstruction entry point.**

The freeze includes source and feature hashes. After editing search/core code, use a new output root and disclose the version difference rather than resuming old scores. Do not bypass hashes by editing source. Preserve historical winner indices when rereading statistics.

### 9.5 Rerunning gallery-only refinement

```powershell
python refine_orl_csa.py --stage prepare --output results/orl_csa_refined_rerun
python refine_orl_csa.py --stage select --output results/orl_csa_refined_rerun
python refine_orl_csa.py --stage randomness-plan --output results/orl_csa_refined_rerun
python refine_orl_csa.py --stage evaluate --output results/orl_csa_refined_rerun
python refine_orl_csa.py --stage randomness --output results/orl_csa_refined_rerun
python refine_orl_csa.py --stage analyze --output results/orl_csa_refined_rerun
```

Freeze all selections for seeds20–29 before scoring; randomness-plan precedes scoring. Evaluate includes checks. To verify existing outputs: `python refine_orl_csa.py --stage verify`. This depends on preceding csa_lda_optimized inputs/eyes/references, not an empty-data checkout.

### 9.6 Rerunning the sample-size extension

```powershell
python run_orl_sample_size.py --output results/orl_sample_size_rerun
python run_orl_sample_size.py --diagnostic --output results/orl_sample_size_rerun
python run_orl_sample_size.py --analyze --output results/orl_sample_size_rerun
```

Use a new output root and stage checks. To verify existing outputs only: `python run_orl_sample_size.py --verify`. Requires the ORL audit catalogue/caches.

Other entry points may have older dependencies/default outputs. Check `--help` and REPORT§9 first, rather than overwriting defaults. A clean public checkout needs a genuine raw-data-to-final-input sequence, not only commands depending on unpublished result caches.

---

## 10. Verification and evidence: read these first

| Evidence| Location| Meaning of recorded checks|
|---|---|---|
| Current shared three-dataset table| `results/orl_protocol_audit/shared_comparison.csv` | Current ORL and reused MNIST/FERET, separate from old shared tables|
| Latest exploratory high scores| `results/orl_best_search/best_results.json` | Correct counts, parameters, mean/SD, and selection convention|
| High scores at original paper dimensions| `results/orl_best_search/paper_dimension_best.json` | Original390 and24→23 subgroup replay|
| Exploratory-model verification| `results/orl_best_search/verification.json` | 200 complete split scores;20 models/6400 predictions independently checked|
| Supplementary statistical readback| `results/orl_best_search/statistical_readback.json` | 6003 configuration statistics, two paper-dimension replays, six shared-condition controls, source hashes|
| Gallery-only refinement| `results/orl_csa_refined/evaluation/results.csv`、`summary.json`、`verification.json` | 80 scores,25600 predictions; ordinary methods and extensions separated|
| Parameters and energy| `results/orl_csa_refined/selected_settings.csv`、`training_energy.csv` | Actual selections and fitting diagnostics for each seed|
| Fixed100-split diagnosis| `results/orl_csa_refined/randomness/results.csv` and `verification.json`| All100 retained;300 scores/96000 records|
| sample size expansion| `results/orl_sample_size/summary.json`、`analysis.json`、`verification.json` | 90 models and genuine paired comparisons at fixedP5|
| FERET | `results/feret_validation_selected_v3/fixed_results.csv`、`selected_configs.json`、`verification.json` | Distinguish validation_selected and cosine_control|
| MNIST/early reconstruction| `results/available_reproduction_v2/fixed_results.csv`、`verification.json` | Old inputs and three seeds, not presented as a latest rerun|
| Latest bounded MNIST optimization| `results/mnist_protocol_optimized/comparison.csv`、`original_three_seed_comparison.csv`、`protocol.json`、`verification.json` | Ten paired baseline/selected runs, original three-seed control, and complete negative results. Supplementary statistics/compliance appear in `supplementary_readback.json`, not a standard stage-generated output.|

Numerical verification does not eliminate selection bias; correct data hashes do not establish the authors' exact image indices. If CSV and prose conflict, inspect workflow labels, protocols, and predictions rather than silently choosing the maximum.

---

## 11. Most useful next work: priorities and acceptance criteria

These were recommendations at the initial handoff, not completed work. Subsequent bounded MNIST optimization is separately completed; no experiment was pending then. New experiments depend on the next explicit user task.

### P0: Course deliverables and result categories (highest priority)

1. Freeze a paper-comparison table labeling shared/original-dimension results, gallery selections, exploratory best, and extensions separately. Do not invent a paper SD or call its number a mean.
2. 3–4-page LaTeX report: state ORL/MNIST/grayscale FERET scope and authorized PIE omission; disclose input/distance/order/index/statistical differences.
3. 9-minute presentation and3-minute Q&A: tensor→CSA updates→NN/LDA→evidence→limits/team insight; avoid narrating every search run.
4. Public GitHub and README: environment, acquisition, raw-data-to-input preparation, fixed experiments, plots, expected results, references, AI assistance/member contributions. Cache dependencies are a real delivery limitation to document.

Acceptance: a clean environment can run the selected final experiment or clearly states authorized-data prerequisites; tables trace to correct counts; page/time limits and figure attribution are met. **At this historical point no completed.tex/.pptx deliverables or confirmed public repository were found.**

### P1: Consistent figures and one explanatory supplementary study

- Organize Table I/II/IV comparisons and existing Fig.4/5(a)/6/7 curves. To claim one final pipeline, regenerate reconstruction/convergence from the final fixed input, retaining earlier plots and never rescaling ordinates arbitrarily.
- The most useful new study is a **matched-split/input ablation** of24→32 ranks, identity→HOSVD, magnitude→power0.75, cosine→Euclidean, and LDA23→24, isolating factors and necessary interactions. The95% winner changes several factors simultaneously, so their separate contributions are unknown.
- Share input, distance, and splits with PCA; match pre/post-reduction dimensions or storage budgets. Existing24-dimensional controls can be organized before adding any full grid.

Acceptance: freeze a bounded control design first, report every split and failed case, and derive gains from explicit paired comparisons. A new seed is not automatically a blind test; do not discard low scores.

### P2: Additional explanatory materials

- Error examples: CSA/PCA neighbors and gallery images for the same probe; discuss pose, lighting, and eye errors as post-hoc diagnostics.
- Accuracy distributions/ranges: the existing200-split distribution illustrates best versus mean; no endless seed expansion is needed.
- Compute/compression costs: record timing and basis/coefficient storage with matched hardware/threads/inputs; define any measured memory. Do not guess unmeasured peak usage.
- With limited time, existing fixedP5 sample-size controls, matched24-dimensional LDA controls, and distributions usually support stronger analysis than hundreds of additional parameter trials.

### Suggested9-minute narrative

| Time| content|
|---|---|
| 0:00–1:00 | Vectorization versus tensors: problem/motivation|
| 1:00–3:00 | CSA projection, alternating updates, and PCA/LDA course connections|
| 3:00–4:00 | Paper experiments, group scope, instructor protocol, and PIE omission|
| 4:00–6:00 | Three-dataset main results, separating original-dimension ORL and exploratory maxima|
| 6:00–8:00 | Evidence concerning small samples, mode budgets, LDA, and inputs|
| 8:00–9:00 | Contributions, limitations, team learning, and conclusions|

Q&A: why not compress the sample axis; why reconstruction need not imply classification; fairness of390 versus24+LDA; why rankSw≤N−Nc; why positivealpha is an extension; why95% is not a mean; PIE omission; group code/analysis contributions.

---

## 12. New-session cautions and reusable opening

### Avoid repeating these mistakes

- Do not replace gallery-only means such as83.28 with exploratory95/97.5; fitting isolation alone does not establish test-free selection.
- Do not claim the paper reports a repeated mean or proves best-seed selection; its aggregation rule is unspecified.
- Do not say only Gabor remains unmatched: grayscale ordinaryCSA+LDA is also lower, MNIST has gaps, PIE is absent, and some original-dimension relative rankings differ.
- Positivealpha, G5/P5, and560-dimensional CSA are not exact original protocols.
- TA permission for differences does not waive shared-input, fitting-count, or Tmax requirements.
- Historical manifest scopes, shared tables, figures, and download-time statuses do not override current results.
- Retain historical evidence and avoid many additional planning Markdown files.
- Never upload FERET/caches or expose download credentials without authorization.
- Do not begin by rerunning all experiments; read verified records and the next specific user request first.

### Reusable prompt for a new session

> First read `D:\HKU\COURSE\y2s1\COMP3314\COMP3314GP\docs\HANDOFF.md`, then follow its navigation to `README.md`, `docs/REPORT.md`, and relevant result protocols. These cover provenance, the CSA paper, coursework screenshots, instructor/TA/author replies, data, code, key results, and diagnoses. Preserve distinctions among shared paper-dimension references, gallery-only selections, probe-selected exploratory maxima, and extensions. Do not turn unknown protocols into author-confirmed settings. PIE omission is instructor-authorized. Briefly state your understanding, then execute the next user-specified task; do not automatically rerun a full grid or create many Markdown files.

The initial handoff reread records and checked all then-current local links. It added this document/README navigation, clarified probe selection and FERET labels, and changed no algorithms, parameters, data, or scores. Subsequent bounded MNIST work added its own script/results and updated navigation documents; core algorithms, original data, historical scores, and other datasets remain preserved.
