import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Patch
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────────
groups = ['MIMIC-IV', 'LabCorp-Syn', 'FinTrans-Syn', 'MIA %']

holoclean  = [0.94, 0.92, 0.90, 0.71]
federated  = [0.86, 0.84, 0.82, 0.64]
dp_only    = [0.80, 0.78, 0.77, 0.64]
ppdc_iq    = [0.91, 0.88, 0.86, 0.64]

n_groups = len(groups)
x = np.arange(n_groups)
width = 0.18
gap = 0.01

# ── Figure ────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5.5))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# ── Bar positions ─────────────────────────────────────────────────────────
pos0 = x - 1.5 * (width + gap)
pos1 = x - 0.5 * (width + gap)
pos2 = x + 0.5 * (width + gap)
pos3 = x + 1.5 * (width + gap)

blue  = '#4472C4'
red   = '#C0504D'
green = '#76923C'

# ── Draw bars ─────────────────────────────────────────────────────────────
b0 = ax.bar(pos0, holoclean, width, color=blue, edgecolor=blue, linewidth=0.8, zorder=3)

b1 = ax.bar(pos1, federated, width, color='white', edgecolor=blue,
            linewidth=0.8, zorder=3, hatch='////')

b2 = ax.bar(pos2, dp_only, width, color='white', edgecolor=red,
            linewidth=0.8, zorder=3, hatch='----')

b3 = ax.bar(pos3, ppdc_iq, width, color='white', edgecolor=green,
            linewidth=1.2, zorder=3, hatch='xxxx')

# ── Value labels on top of each bar ───────────────────────────────────────
def label_bars(bars, bold=False):
    for bar in bars:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            h + 0.008,
            f'{h:.2f}',
            ha='center', va='bottom',
            fontsize=8,
            fontfamily='serif',
            fontweight='bold' if bold else 'normal',
            color='black'
        )

label_bars(b0)
label_bars(b1)
label_bars(b2)
label_bars(b3)
label_bars(b3, bold=True)  # PPDC-IQ bold

# ── Dashed reference line at 52.3% ────────────────────────────────────────
ax.axhline(y=0.523, color=green, linestyle='--', linewidth=1.2,
           xmin=0, xmax=1.0, zorder=4)
ax.text(n_groups - 0.42, 0.535, 'PPDC-IQ 52.3%',
        fontsize=8, color=green, fontfamily='serif')
ax.text(n_groups - 0.42, 0.505, '~random',
        fontsize=7.5, color='gray', fontfamily='serif')

# ── Axes formatting ───────────────────────────────────────────────────────
ax.set_ylim(0, 1.0)
ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_yticklabels(['0.0', '0.2', '0.4', '0.6', '0.8', '1.0'],
                   fontfamily='serif', fontsize=10)
ax.set_ylabel('F1 Score / MIA Rate (normalized)',
              fontfamily='serif', fontsize=11)

ax.set_xticks(x)
ax.set_xticklabels(groups, fontfamily='serif', fontsize=11)

ax.yaxis.grid(True, color='#dddddd', linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#333333')
ax.spines['bottom'].set_color('#333333')

# ── Title ─────────────────────────────────────────────────────────────────
ax.set_title('Fig. 4. Experimental Results: Detection F1 Score and Privacy (MIA%) by Method',
             fontfamily='serif', fontstyle='italic', fontsize=11, pad=12)

# ── Legend ────────────────────────────────────────────────────────────────
legend_handles = [
    Patch(facecolor=blue,    edgecolor=blue,  label='HoloClean (no priv.)'),
    Patch(facecolor='white', edgecolor=blue,  hatch='////', label='Federated only'),
    Patch(facecolor='white', edgecolor=red,   hatch='----', label='DP only (local)'),
    Patch(facecolor='white', edgecolor=green, hatch='xxxx', label='PPDC-IQ (proposed)'),
]
ax.legend(handles=legend_handles, loc='lower center',
          bbox_to_anchor=(0.5, -0.18), ncol=4,
          fontsize=9, frameon=False,
          prop={'family': 'serif', 'size': 9})

# ── Caption ───────────────────────────────────────────────────────────────
fig.text(0.5, -0.03,
         'Lower MIA bar = better privacy. Dashed line = PPDC-IQ 52.3% approx. random guessing baseline.',
         ha='center', fontfamily='serif', fontstyle='italic', fontsize=8.5, color='#444')

fig.text(0.5, -0.08,
         'Fig. 4 — Experimental Results: F1 Score and MIA% by Method',
         ha='center', fontfamily='serif', fontstyle='italic', fontsize=10)

# ── Save & Show ───────────────────────────────────────────────────────────
plt.tight_layout()
plt.savefig('figure4.png', dpi=300, bbox_inches='tight',
            facecolor='white', format='png')
plt.savefig('figure4.pdf', bbox_inches='tight',
            facecolor='white', format='pdf')
print("Saved: figure4.png and figure4.pdf")
plt.show()