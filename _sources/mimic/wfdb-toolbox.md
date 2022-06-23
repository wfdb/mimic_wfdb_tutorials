# WFDB Toolbox

## Overview

The Waveform Database (WFDB) is a set of file standards designed for reading and storing physiologic signal data, and associated annotations. See the [WFDB Spec repository](https://github.com/wfdb/wfdb-spec/) for the specification details.

Example signal types include ECG and EEG. Example annotation types include automated machine-labelled heart-beats, and clinician comments regarding specific signal artifacts.

There are several available software packages that implement the WFDB specifications. Consider using one of them if you want to conduct research or build algorithms using physiologic data.

## Software Packages

The WFDB specification is openly-licensed, so anyone can implement and modify software according to the spec. Here are the main packages and implementations:

- [WFDB Software Package](https://doi.org/10.13026/gjvw-1m31): The original software package written in C. Contains the core library, command line tools, and WAVE. See also the PhysioNet publication. Associated documents:
- [WFDB Python Package](https://wfdb.readthedocs.io/en/stable/): A native Python implementation of WFDB.
- [WFDB Toolbox for Matlab](https://archive.physionet.org/physiotools/matlab/wfdb-swig-matlab/new_version.shtml): A set of Java, GUI, and m-code wrapper functions, which make system calls to WFDB Software Package and other applications.

## WFDB-Python

For the purposes of this workshop, we will be using the [WFDB Python Package](https://wfdb.readthedocs.io/en/stable/).

[More detail about Python package.]
