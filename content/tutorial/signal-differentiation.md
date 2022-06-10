# Differentiation

_Tutorial on signal differentiation_

```{admonition} Suggestions
I'd suggest we use a similar approach to that used in the Matlab function [PulseAnalyse](https://peterhcharlton.github.io/pulse-analyse/):
- Savitzky-Golay filtering, as described in [this article](https://doi.org/0.1021/ac60214a047).
- The coefficients for using Savitzky-Golay filtering to obtain derivatives are provided in the 'savitzky_golay' function within PulseAnalyse (see line 2294 [here](https://github.com/peterhcharlton/pulse-analyse/blob/master/pulse-analyse_v.1.3beta/PulseAnalyse.m)).

```