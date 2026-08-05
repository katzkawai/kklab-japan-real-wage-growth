# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A data-analysis workspace (not a software project — no build, test, or lint tooling) examining Japan's real wage stagnation since 1990, comparing Japan against South Korea, the U.S., the U.K., Australia, France, Canada, and Italy. Germany is excluded (its OECD series starts in 1991, post-reunification, so it cannot share the 1990 base). Published via GitHub Pages at https://katzkawai.org/kklab-japan-real-wage-growth/ (repo: katzkawai/kklab-japan-real-wage-growth; push to `main` deploys). The deliverables are in Japanese; work in Japanese when editing the page or note.

## Files

- `index.html` — the published page. Contains an interactive SVG line chart (vanilla JS at the bottom of the file, data embedded inline) with hover crosshair/tooltip, keyboard access, and dark-mode support via CSS custom properties. The chart data is duplicated in three places that must stay in sync: the CSV, the inline JS `SERIES` arrays, and the milestone table/stat cards in the page body.
- `oecd_real_wage_growth_1990base.csv` — the dataset. Columns: `TIME_PERIOD` (1990–2025) and cumulative % change in real average annual wages since 1990 for `JPN, KOR, USA, GBR, AUS, FRA, ITA, CAN`. All series are 0.0 in 1990 (base year).
- `japan_real_wage_growth.png` — static chart (noscript fallback, og:image, download link). Regenerate with `python3 make_chart.py` (matplotlib + IPAexGothic font).
- `make_chart.py` — generates the PNG from the CSV.
- `日本の実質賃金停滞ノート.docx` — Japanese methodological note interpreting the data (author's source note; git-ignored, local only, covers the original 5 countries). The substantive analysis on the page derives from it.

## Chart design

Series colors are a CVD-validated 8-slot categorical palette defined as CSS vars `--s1`…`--s8` (light and dark steps) in `index.html`; the same light-mode hexes are hardcoded in `make_chart.py`. Slot assignment is fixed per country (Japan=blue s1 … Italy=red s8); keep it stable, and keep the PNG and SVG charts visually in sync when changing either.

## Data provenance

Fetched from the OECD SDMX API, dataset `DSD_EARNINGS@AV_AN_WAGE` ("Average annual wages"): real terms (constant 2025 prices), national currency units, transformed to cumulative % change with 1990 = 0%. If refreshing the data, keep this exact series definition and base-year transformation so the CSV, chart, and note stay consistent.

## Analytical caveats (from the note — preserve these when editing)

The note's core argument is that "only Japan is flat" is robust, but the *size* of the stagnation depends on measurement choices. Do not simplify these away:

- The OECD series is per full-time-equivalent (FTE) wages (SNA wage bill ÷ employees × FTE adjustment), deflated by the household final consumption deflator — not the headcount-based MHLW Monthly Labour Survey (毎勤) real wage index, which uses CPI ex-imputed rent. The two differ in numerator, denominator, and deflator.
- Japan's part-time share rose from ~13% (1990) to ~32%, so composition effects matter: stagnation appears larger on a headcount basis, near zero on the FTE basis (this chart), and slightly positive on an hourly basis (annual hours fell from ~2,030 to ~1,600).
- Japan's 2025 figure of −1.2% must not be described as "a full-time worker's real wage fell over 30 years" — the FTE series still contains part-time hourly-wage composition effects.
- Korea's +107.7% partly reflects catch-up from a low 1990 wage level and a shift from self-employment to salaried employment.
- With the comparison widened to 8 countries, Italy (−2.1% in 2025) is also stagnant — so say "only Japan and Italy are flat", not "only Japan". Japan-specific stagnation claims must be scoped accordingly.
