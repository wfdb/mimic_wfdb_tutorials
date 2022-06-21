# Database Structure

## MIMIC-IV modules

MIMIC-IV is a modular dataset, comprising of a core set of clinical data (MIMIC-IV Clinical) that can be linked to datasets such as:

- MIMIC-IV-ED: emergency department data;
- MIMIC-IV-ED: chest X-ray images;
- MIMIC-IV-ECG: 10-second 12-lead diagnostic ECGs;
- MIMIC-IV-waveform: varying-length, high-time-resolution waveforms such as ECG and PPG.

Typically the datasets are linked by unique patient ID (`subject_id`) and unique hospital stay ID (`hadm_id`). For the purposes of this workshop, we will focus on the MIMIC-IV waveform dataset.

## MIMIC-IV waveforms

The MIMIC-IV waveform dataset comprises of a tabular file that contains structured metadata, such as `subject_id`, `signal length`, and `signal filename`. This metadata is accompanied by a collection of signal files that comprise of `.hea` files and associated `.dat` binary files. The files are formatted according to the [WFDB specification](https://wfdb.io/).

## MIMIC-IV waveform demo

Perhaps the easiest way to become familiar with the MIMIC-IV waveforms is to explore the [MIMIC-IV waveform demo dataset](http://physionet.org/), which contains a subset of X00 records. After scrolling to the files section, you should see the data is stored in the following folder structure:

```
files
├── p10001725
│   └── s102147240
│       ├── 102147240.dat
│       └── 102147240.hea
├── p10002495
    ├── s101633856
    │   ├── 101633856.dat
    │   └── 101633856.hea
    ├── s102447237
    │   ├── 102447237.dat
    │   └── 102447237.hea
    └── s107316808
        ├── 107316808.dat
        └── 107316808.hea
```

In this example, "p10001725" indicates the patient with the subject_id `10001725` and "s102147240" indicates a study_id of `102147240`. The `102147240.dat` file is a binary file containing the waveform data and the `102147240.hea` file contains header information such as date, sample frequency, and channel information. 

[More detail about demo waveforms. e.g. file structure]

