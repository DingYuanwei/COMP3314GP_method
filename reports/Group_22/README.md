# Group 22 report

Main document: `main.tex`. Overleaf compiler: **pdfLaTeX**.
The supplied NeurIPS 2026 style uses the required `preprint` option, with names
and affiliation visible. The PDF submission filename is `Group_22.pdf`.

Reference revision (November 26, 2026): removed lecture-slide bibliography
entries and their in-text citations, while retaining the course-concept
connections. The PCA equivalence and sample-space computational caveat now
point to the original CSA paper. DATER's conference volume, pages, and publisher
are included, and the official ORL dataset webpage has an access date.
The bibliography contains five directly cited research/data sources.
Author--year citations use the standard `plainnat` bibliography style, with
references sorted alphabetically by author.

## Contents

- Four pages of main text, including the abstract, equations, table, and figure.
- One separate page of references.
- Three appendix pages with the detailed optimization proof, reproduction
  protocols, an exact recognition-configuration table, supplementary results,
  and recorded ORL reconstruction/convergence diagnostics.
- `sections/02_methods.tex` contains the complete revised Method section.
- All substantive subheadings use numbered LaTeX subsections consistently.

The central conditional-optimization argument remains in the main text. Its
longer projector and eigenvalue-weight derivation is in Appendix A, so the
professor's Q&A topic does not dominate the report. Section 4 combines critical
analysis with team insights to avoid repeating the Method section.

## Compile

Upload this ZIP to Overleaf, select `main.tex`, and compile with pdfLaTeX. The
figure PDFs are already included; Python is not needed to compile the report.
Locally:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

To regenerate the figures, install matplotlib and run `python make_figures.py`.
`data/metric_comparison.csv` is an unrounded four-row extract of the recorded
group score table. `data/orl_reconstruction.csv` and `data/orl_convergence.json`
are copies of saved historical group records, not new experiments or digitized
paper values. The figure script does not fit models or rerun experiments.

## Sources and verification

The report integrates the original Xu et al. paper, COMP3314 lecture materials
and project guidance, the final supplied slides, the group presentation scripts,
the existing report project, the professor's optimization question, and the
group's saved experimental records. Experimental numbers were checked against
their source tables/CSV records; theoretical claims were reviewed against the
paper and lectures. Paper values, recorded group results, and proposed future
work are explicitly distinguished.

The final public repository is
https://github.com/gwdsd1/COMP3314GP, confirmed by the user. Live access from this
environment was unavailable; this does not imply a repository problem. Author
code/indices and unspecified author preprocessing choices cannot be recovered
from the supplied material; the report discloses the resulting limitations.
We did not rerun all experiments or claim new results. Rebuilding cache-based
experimental checks requires the separately obtained datasets and generated
files described in the repository.

The previous Overview, Critical Analysis, and Team Insights placeholders have
all been replaced. No report has been submitted to the course submission system.
Deliverables are a PDF and a self-contained Overleaf source ZIP.
