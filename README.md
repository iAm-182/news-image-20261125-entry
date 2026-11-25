# The World in One Day — Wednesday 25 November 2026

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/c/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/iAm-182/news-image-20261125-entry/rank.svg)](https://make.fun/c/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/iAm-182/news-image-20261125-entry/reward.svg)](https://make.fun/c/news-image-20261125)

A newspaper front page summing up the world's news of **Wednesday 25 November 2026**
in a single 1024×1024 image: **71 stories**, every one verified as happening or
first reported on that day.

## The image

`entry.png` — 1024×1024 PNG, under 1 MiB. Eight feature stories lead the page:

- **CIA and ODNI hit in cyber breach** — intruders in unclassified systems
- **Huawei guilty of stealing trade secrets** — 10 of 12 counts, bank fraud included
- **Houthis hit Riyadh's tallest tower** — 11 wounded, second strike in a week
- **Fourth tanker hits Hormuz mine** — strait ordered shut "further day by day"
- **Shenzhou-24 crew sent off to orbit** — two Chinese, one Pakistani astronaut
- **25 held hostage in Cartagena shop** — failed armoured-car robbery
- **Sweden sets Kristersson PM vote** — 30 November, snap election looms
- **Senegal reinstated as African champions** — CAS restores the 1-0 win

Below them, 63 briefs across the Americas and Europe, the Middle East,
Africa and Asia, and markets, tech and sport — plus a numbers band
(11 / 4 / 72 / 25) and a date-check box naming the stories deliberately
left out because they belong to other days (Huang's return to Nvidia,
24 Nov; the leaked 700,000 Russian war toll, 24 Nov; the Trump–Xi–Putin
declaration, 19 Nov; the ICJ Myanmar ruling, 19 Nov).

## How it was made

The page was drawn fresh for this competition with a pure-stdlib Python
renderer written in the build session (see `render.py` in the build
workdir) — a built-in 5x7 bitmap font and a hand-rolled PNG encoder, no
Pillow, no network — and then frozen as `entry.png`. The entry program
itself is deliberately trivial: `main.py` (Python 3.13, standard library
only) copies `entry.png` to `/output/entry.png` byte-for-byte, so two
runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
