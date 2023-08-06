# tsbs_rg
---
This package computes the baseline for a time series

## Input

Compute baseline for a time series data

## Arguments:
### Positional Arg:
- data (array): time series data (reverse chronological)
### Keyword Arg:
- crit (float): critical multiplier value (default=None)
- perc (float): critical baselining percentage (default=None)
- false_positive_threshold (boolean): whether to use any false_positive_threshold (default=None)
- is_low (boolean): whether anomalies for the lower thresholds are to be detected   (default=False)

# usage

`Baseline(data, crit, perc, false_positive_threshold=None, is_low=True).baseline()`