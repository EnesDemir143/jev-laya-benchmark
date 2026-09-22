# Jev vs. Laya Benchmark Report

## Summary

This benchmark compares TypeSafe Jev with `laya-mlx` on the same 100 open
oh-my-pi issues. Both models completed all 100 issues successfully.

| Metric | Jev | Laya |
|---|---:|---:|
| Mean latency | 328.1 ms | 309.2 ms |
| P50 latency | 318.4 ms | 307.8 ms |
| P95 latency | 423.0 ms | 329.1 ms |

Laya was faster in this run, especially at the 95th percentile.

## Agreement

| Question | Agreement |
|---|---:|
| Beginner-friendly | 80/100 (80.0%) |
| CV fit | 42/100 (42.0%) |
| Difficulty | 61/100 (61.0%) |

For continuous Noul scores:

| Score | Mean absolute difference | Maximum difference |
|---|---:|---:|
| Beginner-friendly | 0.1745 | 0.4555 |
| CV fit | 0.1815 | 0.4637 |

## Configuration

- Sample size: 100 issues
- Laya model: `aac6fef/laya-mlx`
- Numeric type: `float16`
- Batch size: 16
- Warm-up: enabled before timing
- Raw results: `data/jev-laya-benchmark-fp16-warm.json`

The raw JSON remains local because `data/` is ignored by Git. This keeps issue
dumps and benchmark outputs out of commits while preserving the reproducible
summary here.

## Interpretation

Latency favors Laya for this local warm-run benchmark. Jev and Laya agree most
often on beginner-friendliness, while CV-fit agreement is materially lower.
The Noul-score differences show that CV-fit disagreement is not only caused by
the 0.5 threshold; the underlying scores also diverge.
