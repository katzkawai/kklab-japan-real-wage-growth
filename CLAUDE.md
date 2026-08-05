# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A data-analysis workspace (not a software project — no build, test, or lint tooling) examining Japan's real wage stagnation since 1990, comparing Japan against South Korea, the U.S., the U.K., and Australia. The primary written deliverable is in Japanese; work in Japanese when editing or extending the note.

## Files

- `oecd_real_wage_growth_1990base.csv` — the dataset. Columns: `TIME_PERIOD` (1990–2025) and cumulative % change in real average annual wages since 1990 for `JPN, KOR, USA, GBR, AUS`. All series are 0.0 in 1990 (base year).
- `japan_real_wage_growth.png` — line chart rendered from the CSV ("Japan's real wage growth has been stagnant"). The script that generated it is not in this repo; if the chart needs regenerating, recreate the plotting code (Python/matplotlib style) from the CSV.
- `日本の実質賃金停滞ノート.docx` — Japanese methodological note ("Notes on Japan's real wage stagnation") interpreting the data. This is the substantive document; the CSV/PNG are its supporting materials.
- `files.zip` — bundle of the three files above (a distribution copy, not additional content).

## Data provenance

Fetched from the OECD SDMX API, dataset `DSD_EARNINGS@AV_AN_WAGE` ("Average annual wages"): real terms (constant 2025 prices), national currency units, transformed to cumulative % change with 1990 = 0%. If refreshing the data, keep this exact series definition and base-year transformation so the CSV, chart, and note stay consistent.

## Analytical caveats (from the note — preserve these when editing)

The note's core argument is that "only Japan is flat" is robust, but the *size* of the stagnation depends on measurement choices. Do not simplify these away:

- The OECD series is per full-time-equivalent (FTE) wages (SNA wage bill ÷ employees × FTE adjustment), deflated by the household final consumption deflator — not the headcount-based MHLW Monthly Labour Survey (毎勤) real wage index, which uses CPI ex-imputed rent. The two differ in numerator, denominator, and deflator.
- Japan's part-time share rose from ~13% (1990) to ~32%, so composition effects matter: stagnation appears larger on a headcount basis, near zero on the FTE basis (this chart), and slightly positive on an hourly basis (annual hours fell from ~2,030 to ~1,600).
- Japan's 2025 figure of −1.2% must not be described as "a full-time worker's real wage fell over 30 years" — the FTE series still contains part-time hourly-wage composition effects.
- Korea's +107.7% partly reflects catch-up from a low 1990 wage level and a shift from self-employment to salaried employment.
