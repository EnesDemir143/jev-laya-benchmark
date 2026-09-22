# Jev Tryout

Benchmarking TypeSafe Jev against `laya-mlx` for classifying open oh-my-pi
GitHub issues by beginner-friendliness, CV fit, and difficulty.

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

The benchmark completed all 100 issues successfully. On the local machine used
for this run—a Mac14,9 with Apple M2 Pro, 10 logical CPU cores, 16 GB RAM, and
arm64 Darwin—Laya was faster:

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
