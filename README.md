# Jev-laya Benchmark

A local benchmark comparing [TypeSafe Jev](https://typesafe.ai/) and
[`laya-mlx`](https://github.com/mizorewww/laya-mlx) for structured issue
classification.

Tags: `jev` · `laya` · `mlx` · `rlcd` · `benchmark` · `issue-classification`

This is a local benchmark experiment, not a production performance claim.

## Setup

```bash
uv sync
cp .env.example .env
```

Set `TYPESAFE_API_KEY` in `.env`. Issue data, resume files, and generated
classification outputs are local inputs and are intentionally ignored by Git.

## Run classification

```bash
uv run python main.py --help
uv run python main.py --input data/oh-my-pi-open-issues.json \
  --resume /path/to/resume.md
```

The classifier uses TypeSafe Jev with `Noul` scores for beginner-friendliness
and CV fit, plus a categorical difficulty choice. Results are checkpointed
atomically under `data/`.

## Benchmark

```bash
uv run python scripts/benchmark_jev_laya.py \
  --resume /path/to/resume.md \
  --limit 100 \
  --dtype float16 \
  --batch-size 16 \
  --output data/jev-laya-benchmark-fp16-warm.json
```

See the full English report: [Jev vs. Laya Benchmark Report](docs/jev-laya-benchmark-report.md).

## Results

The benchmark completed all 100 issues successfully. On an Apple Silicon
macOS laptop with 16 GB RAM, Laya was faster. This run warmed Laya before timing, but did not
warm Jev, so the latency numbers are directional rather than an apples-to-apples
warm-run comparison:

| Metric | Jev | Laya |
|---|---:|---:|
| Mean latency | 328.1 ms | 309.2 ms |
| P50 latency | 318.4 ms | 307.8 ms |
| P95 latency | 423.0 ms | 329.1 ms |

Agreement was 80% for beginner-friendliness, 42% for CV fit, and 61% for
difficulty. The raw benchmark output is
`data/jev-laya-benchmark-fp16-warm.json`; it is ignored because benchmark and
issue data are local artifacts.

## Project layout

- `src/issue_classifier/`: reusable classifier code
- `main.py`: CLI entry point
- `scripts/`: benchmark scripts
- `docs/`: benchmark and issue reports
