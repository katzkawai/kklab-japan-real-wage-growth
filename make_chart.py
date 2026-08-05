"""Regenerate japan_real_wage_growth.png — 8 countries, Japanese labels, validated palette."""
import csv
import glob

import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager
import matplotlib.pyplot as plt

font_path = None
for pat in ("/usr/share/fonts/**/ipaexg.ttf", "/usr/share/fonts/**/IPAexGothic*"):
    hits = glob.glob(pat, recursive=True)
    if hits:
        font_path = hits[0]
        break
assert font_path, "IPAexGothic not found"
font_manager.fontManager.addfont(font_path)
plt.rcParams["font.family"] = "IPAexGothic"
plt.rcParams["axes.unicode_minus"] = False

import pathlib
HERE = pathlib.Path(__file__).resolve().parent
CSV = HERE / "oecd_real_wage_growth_1990base.csv"
OUT = HERE / "japan_real_wage_growth.png"

KEYS = ["JPN", "KOR", "USA", "GBR", "AUS", "FRA", "ITA", "CAN"]
years, data = [], {k: [] for k in KEYS}
with open(CSV) as f:
    for row in csv.DictReader(f):
        years.append(int(row["TIME_PERIOD"]))
        for k in KEYS:
            data[k].append(float(row[k]))

# categorical slots 1-8 (light mode), fixed entity->slot assignment — validated
SERIES = [
    ("JPN", "日本", "#2a78d6"),
    ("KOR", "韓国", "#eb6834"),
    ("USA", "米国", "#1baf7a"),
    ("GBR", "英国", "#eda100"),
    ("AUS", "豪州", "#e87ba4"),
    ("FRA", "フランス", "#008300"),
    ("CAN", "カナダ", "#4a3aa7"),
    ("ITA", "イタリア", "#e34948"),
]
INK = "#1a1f2b"
INK2 = "#5a6272"
MUTED = "#898781"
GRID = "#e3e6ec"
BASE = "#c3c2b7"

fig, ax = plt.subplots(figsize=(12.8, 7.6), dpi=100)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
fig.subplots_adjust(left=0.055, right=0.865, top=0.80, bottom=0.10)

for y in range(-20, 121, 20):
    ax.axhline(y, color=GRID, lw=0.8, zorder=1)
ax.axhline(0, color=BASE, lw=1.2, zorder=1)

for key, name, color in SERIES:
    z = 3.5 if key == "JPN" else 3  # the story series stays on top
    ax.plot(years, data[key], color=color, lw=2, solid_capstyle="round",
            solid_joinstyle="round", zorder=z, label=name)
    ax.plot(years[-1], data[key][-1], "o", ms=9, mfc=color, mec="white",
            mew=1.8, zorder=z + 1, clip_on=False)

END = {k: data[k][-1] for k in KEYS}

def end_label(key, name, value_text=None, label_y=None):
    y_dot = END[key]
    y_lab = y_dot if label_y is None else label_y
    if label_y is not None:  # leader line from dot to displaced label
        ax.plot([2025.35, 2025.7], [y_dot, y_lab], color=MUTED, lw=0.8,
                zorder=2, clip_on=False)
    ax.text(2025.9, y_lab + (3.5 if value_text else 0), name, fontsize=13,
            fontweight="bold", color=INK, va="center", clip_on=False)
    if value_text:
        ax.text(2025.9, y_lab - 4.5, value_text, fontsize=11.5, color=INK2,
                va="center", clip_on=False)

# direct labels: extremes + the story (Japan, Italy); mid-cluster carried by legend
end_label("KOR", "韓国", "+107.7%")
end_label("USA", "米国")
end_label("JPN", "日本", "-1.2%", label_y=8)
end_label("ITA", "イタリア", "-2.1%", label_y=-13)

ax.set_xlim(1989.4, 2025.6)
ax.set_ylim(-22, 122)
ax.set_yticks(range(-20, 121, 20))
ax.set_xticks(range(1990, 2026, 5))
ax.tick_params(colors=MUTED, labelsize=11.5, length=0)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(BASE)
ax.spines["bottom"].set_linewidth(1)

leg = ax.legend(loc="lower left", bbox_to_anchor=(0, 1.015), ncol=8,
                frameon=False, fontsize=11.5, handlelength=1.3,
                handletextpad=0.5, columnspacing=1.1)
for t in leg.get_texts():
    t.set_color(INK2)

fig.text(0.055, 0.945, "実質賃金が上がらないのは、主要国では日本とイタリアだけ",
         fontsize=20, fontweight="bold", color=INK, ha="left")
fig.text(0.055, 0.905, "実質平均年間賃金の1990年比変化率(%、自国通貨建て・2025年基準価格)",
         fontsize=12.5, color=INK2, ha="left")
fig.text(0.055, 0.025, "出所: OECD, Average annual wages(データセット DSD_EARNINGS@AV_AN_WAGE)より作成。ドイツは系列が1991年開始のため対象外。",
         fontsize=10, color=MUTED, ha="left")

fig.savefig(OUT, facecolor="white")
print("saved", OUT)
