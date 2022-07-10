# Database Structure

## MIMIC-IV modules

MIMIC-IV is a modular dataset, comprising of a core set of clinical data (MIMIC-IV Clinical) that can be linked to datasets such as:

- MIMIC-IV-ED: emergency department data;
- MIMIC-IV-ED: chest X-ray images;
- MIMIC-IV-ECG: 10-second 12-lead diagnostic ECGs;
- MIMIC-IV-waveform: varying-length, high-time-resolution waveforms such as ECG and PPG.

Typically the datasets are linked by unique patient ID (`subject_id`) and unique hospital stay ID (`hadm_id`). For the purposes of this workshop, we will focus on the MIMIC-IV waveform dataset.

## Available monitor data

The MIMIC-IV Waveform Database consists of raw data that is sampled by the bedside monitor.  The available types of data vary from one patient to another.

### ECG

Virtually all patients have a continuous ECG monitor, measuring electrical activity in the heart.  For MIMIC-IV patients, typically two or three channels are measured (one or two limb leads, one chest lead.)  Each channel is sampled at 250 samples per second.

Measurements derived from the ECG include:
- Heart rate (averaged once per 1.024 seconds)
- Instantaneous ("beat to beat") heart rate
- ST elevation
- QT interval

The same electrodes are also used to measure impedance across the chest ("Resp", 62.5 samples per second), which is used to derive respiration rate ("RR").

### PPG

Virtually all patients have a PPG (photoplethysmogram) sensor, measuring blood oxygen in the fingertip or other extremity.  This sensor provides:
- A continuous waveform ("Pleth", 125 samples per second)
- Average oxygen saturation ("SpO2", once per 1.024 seconds)
- Perfusion index ("Perf")
- Pulse rate ("Pulse (SpO2)")

### Blood pressure

Blood pressure is measured using an automatic cuff at set intervals (e.g. every 5, 15, 30, or 60 minutes).  This is recorded as "NBPs", "NBPd", and "NBPm" (systolic, diastolic, and mean).

Some patients also have a continuous, invasive arterial pressure sensor, which provides:
- A pressure waveform ("ABP", 125 samples per second)
- Systolic pressure ("ABPs", once per 1.024 seconds)
- Diastolic pressure ("ABPd")
- Mean pressure ("ABPm")
- Pulse rate ("Pulse (ABP)")

### Other measurements

Other measurements may be collected depending on the patient, such as:

- Temperature ("Tblood", "Tcore", "Tesoph", etc.)
- Other pressure waveforms ("CVP", "ICP", etc.)
