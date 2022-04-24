# Extracting Reference BP

_Tutorial on obtaining reference BPs from MIMIC_

```{admonition} Suggestions
There are two potential approaches:
1. Obtaining BPs directly from the numerics:
   - This has the advantage that no signal processing is required
   - But the disadvantage that it does require reading additional numerics files (although perhaps it would be helpful to provide an example of this anyway).
2. Obtaining BPs from the ABP signal
   - This has the advantage that the BP signal data are already in the waveform files containing PPG signals.
   - But it would require signal processing. At a minimum, it would require detecting the maximum and minimum values of the BP signal in a given period (to give SBP and DBP), and potentially the signal processing could be much more complex, _e.g._ BP beat detection, signal quality assessment, detection of systolic peaks and diastolic troughs.
```
