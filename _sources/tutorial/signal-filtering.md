# Signal filtering

_Tutorial on signal filtering_

```{admonition} Suggestions
I'd suggest we use filtering functions from `scipy.signal`.
Perhaps we could allow the user to specify the filter type (from a couple of options), and also the cut-off frequencies (as both the filter type and cut-off frequencies influence the shape of the filtered PPG pulse wave).

We should note that the PPG signals in MIMIC have already been filtered somewhat by the clinical monitors used to record them.

Ideally, it would be nice to:
1. Provide options for different types of filters (e.g. Chebyshev filter, Butterworth filter). [This article](https://doi.org/10.1038/sdata.2018.76) lists potential filter types (on pp.8-9).
2. Allow the user to adjust the filter cut-off frequencies (e.g. low and high pass filter cut-offs).
```