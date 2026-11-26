"""Render report figures from included recorded group results.

Requires matplotlib. Run from any directory with: python make_figures.py
The metric CSV retains unrounded means from results/orl_euclidean_20261104/summary.csv.
Reconstruction/convergence files come from results/available_reproduction_v2.
No experiment is fitted or run by this script.
"""
from pathlib import Path
import csv
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
rows = list(csv.DictReader((ROOT / "data/metric_comparison.csv").open()))
plt.rcParams.update({"font.size": 10, "pdf.fonttype": 42, "ps.fonttype": 42})
fig, ax = plt.subplots(figsize=(4.6, 1.65))
for method, marker, color in [("CSA + LDA", "o", "#147878"),
                               ("PCA + LDA", "s", "#9D510D")]:
    vals = [float(next(r["mean_percent"] for r in rows
                      if r["method"] == method and r["metric"] == metric))
            for metric in ["euclidean", "centered_cosine"]]
    ax.plot([0, 1], vals, marker=marker, color=color, linewidth=1.4,
            markersize=5.5, label=method)
    for x, y in enumerate(vals):
        ax.annotate(f"{y:.2f}", (x, y), xytext=(7, 0),
                    textcoords="offset points", va="center", fontsize=9)
ax.set_xticks([0, 1], ["Euclidean", "Centered cosine"])
ax.set_xlim(-0.12, 1.35)
ax.set_ylim(84.5, 92.0)
ax.set_yticks([85, 88, 91])
ax.set_ylabel("Accuracy (%)")
ax.grid(axis="y", color="#D5D5D5", linewidth=0.5)
ax.set_axisbelow(True)
for side in ["top", "right"]:
    ax.spines[side].set_visible(False)
ax.legend(loc="upper left", bbox_to_anchor=(0, 1.34), ncol=2,
          frameon=False, fontsize=9)
fig.subplots_adjust(left=0.15, right=0.98, bottom=0.23, top=0.76)
(ROOT / "figures").mkdir(exist_ok=True)
fig.savefig(ROOT / "figures/metric_comparison.pdf", bbox_inches="tight")
fig.savefig(ROOT / "figures/metric_comparison.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# Supplementary diagnostics: preserve the original recorded definitions/grids.
records = list(csv.DictReader((ROOT / "data/orl_reconstruction.csv").open()))
diagnostic = json.loads((ROOT / "data/orl_convergence.json").read_text())
fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.35))
for name, label, color, marker in [("PCA", "PCA", "#9D510D", "s"),
                                     ("CSA-3", "CSA", "#147878", "o")]:
    points = sorted((r for r in records if r["method"] == name),
                    key=lambda r: float(r["compression_ratio"]))
    axes[0].plot([float(r["compression_ratio"]) for r in points],
                 [float(r["paper_rmse"]) for r in points],
                 marker=marker, markersize=2.7, linewidth=1, color=color,
                 label=label)
axes[0].set(xlim=(1, 40), ylim=(0, 4000), xlabel="Compression ratio",
            ylabel=r"RMSE: $\sqrt{\mathrm{SSE}/N}$", title="(a) Reconstruction")
axes[0].legend(frameon=False, fontsize=8, loc="lower right")
for mode, color, marker in [(0, "#147878", "o"), (1, "#9D510D", "s"),
                             (2, "#64578C", "^")]:
    axes[1].plot([h["iteration"] for h in diagnostic["history"]],
                 [h["basis_similarity"][mode] for h in diagnostic["history"]],
                 label=f"Mode {mode+1}", color=color, marker=marker,
                 markersize=3, linewidth=1)
axes[1].set(xlim=(1, 10), ylim=(0, 1.04), xlabel="Sweep", ylabel="Basis similarity",
            title="(b) Convergence")
axes[1].set_xticks([1, 3, 5, 7, 10])
axes[1].legend(frameon=False, fontsize=8, loc="lower right")
for ax in axes:
    ax.grid(axis="y", color="#D5D5D5", linewidth=0.5)
    ax.set_axisbelow(True)
    for side in ["top", "right"]:
        ax.spines[side].set_visible(False)
    ax.tick_params(labelsize=8)
    ax.xaxis.label.set_size(9)
    ax.yaxis.label.set_size(9)
    ax.title.set_size(10)
fig.tight_layout(w_pad=1.3)
fig.savefig(ROOT / "figures/reconstruction_convergence.pdf", bbox_inches="tight")
fig.savefig(ROOT / "figures/reconstruction_convergence.png", dpi=200,
            bbox_inches="tight")
plt.close(fig)
