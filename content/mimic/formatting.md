# Waveform Data Formats

The waveform database is organized into "records".  Each record represents a single patient and roughly corresponds to a single ICU stay (not always, because the bedside monitor may be temporarily shut off.)  Each record is stored in a separate subdirectory.

To avoid providing information that could identify individual patients, the record does not include any actual date or time information.  Instead, measurements are recorded according to the "elapsed time" from the beginning of the record.  To allow cross-referencing events with the other MIMIC-IV modules, the *surrogate date and time* for the start of the record are also provided.

An example of the file structure is shown below.  Here there are two patients (`subject_id` 10014354 and 10039708).  There is one record (81739927) belonging to the first patient, and two records (83411188 and 85583557) belonging to the second.

```
waves
└── p100
    ├── p10014354
    │   └── 81739927
    │       ├── 81739927.dat
    │       ├── 81739927_0000.hea
    │       ├── 81739927_0001.hea
    │       ├── 81739927_0001e.dat
    │       ├── 81739927_0001r.dat
    │       ├── 81739927_0002.hea
    │       ├── 81739927_0002e.dat
    │       ├── 81739927_0002p.dat
    │       ├── 81739927_0002r.dat
    │       ├── ...
    │       └── 81739927n.csv.gz
    └── p10039708
        ├── 83411188
        │   ├── 83411188.hea
        │   ├── ...
        │   └── 83411188n.csv.gz
        └── 85583557
            ├── 85583557.hea
            ├── ...
            └── 85583557n.csv.gz
```

## Numerics

"Numerics" are defined as measurements that are sampled irregularly or infrequently (less than once per second.)  These measurements are stored as a single table, such as [83411188n.csv.gz](https://physionet.org/content/mimic4wdb/0.1.0/waves/p100/p10039708/83411188/83411188n.csv.gz).

This file is a gzip-compressed CSV file, which can be loaded using software packages such as [Pandas](https://pandas.pydata.org/), or it can be unpacked using [gzip](https://www.gnu.org/software/gzip/) and parsed as you would parse any CSV file.  Note that in contrast to most other MIMIC-IV data tables, the list of *columns* in this table are not the same from one patient to another.

Note that "elapsed time" for numeric values is measured in counter ticks (1/999.52 second, or about one millisecond.)

## Waveforms

"Waveforms" are defined as measurements that are sampled regularly at high resolution (62.47 samples per second or more.)  These measurements are stored as a set of files in WFDB (Waveform Database) format.

For the sake of storage and processing efficiency, waveforms are broken into multiple *segments* representing different time intervals.  It's common for some signals not to be available for the entire duration of a patient's ICU stay, but within a given segment, the available signals are sampled continously and the list of available signals doesn't change.

A segment, in turn, consists of a *header file* (such as [83411188_0001.hea](https://physionet.org/content/mimic4wdb/0.1.0/waves/p100/p10039708/83411188/83411188_0001.hea) and one or more *signal files* (such as [83411188_0001e.dat](https://physionet.org/content/mimic4wdb/0.1.0/waves/p100/p10039708/83411188/83411188_0001e.dat) and [83411188_0001r.dat](https://physionet.org/content/mimic4wdb/0.1.0/waves/p100/p10039708/83411188/83411188_0001r.dat).

In general, you do not need to parse these files yourself, and it is easiest to use one of the existing software packages for doing so: the [WFDB Python Package](https://github.com/MIT-LCP/wfdb-python) or the original [WFDB Software Package](https://physionet.org/content/wfdb/).  Data can also be converted into other formats using tools such as `rdsamp` or `wfdb2mat` from the WFDB Software Package.
