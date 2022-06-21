# Data formatting

There are a few important concepts that should be well understood before using the WFDB software. These concepts include records; signals, samples, and time; and annotations.

## Records

The databases for which the WFDB library was designed consist of a number of records. Each record contains a continuous recording from a single subject, which might be only a few seconds or might be multiple days in length. A typical application program accesses only a single record, and in most cases, it reads the record in order from beginning to end. Each record is identified by a name consisting of letters, digits, and/or underscores. For example, record names in the MIT-BIH Arrhythmia Database are three-digit numbers.

Case is significant in record names that contain letters, even in environments such as MS-Windows for which case translation is normally performed by the operating system on file names; thus ‘e0104’ is the name of a record found in the European ST-T Database, whereas ‘E0104’ is not. A record is made up of several files, which contain signals, annotations, and specifications of signal attributes; each file belonging to a given record normally includes the record name as the first part of its name. A record is an extensible collection of files, which need not all be located in the same directory, or even on the same physical device.

## Signals, Samples, and Time

Signals are commonly understood to be functions of time obtained by observation of physical variables. In our case, a signal is defined more restrictively as a finite sequence of integer samples, usually obtained by digitizing a continuous observed function of time at a fixed sampling frequency expressed in Hz (samples per second). The time interval between any pair of adjacent samples in a given signal is a sample interval; all sample intervals for a given signal are equal. The integer value of each sample is usually interpreted as a voltage, and the units are called analog-to-digital converter units, or adu. The gain defined for each signal specifies how many adus correspond to one physical unit (usually one millivolt, the nominal amplitude of a normal QRS complex on a body-surface ECG lead roughly parallel to the mean cardiac electrical axis). All signals in a given record are usually sampled at the same frequency, but not necessarily at the same gain. Records in the MIT-BIH Arrhythmia Database are sampled at 360 Hz; other database records may be sampled at 250 Hz or even 500 Hz.

The sample number is an attribute of a sample, defined as the number of samples of the same signal that precede it; thus the sample number of the first sample in each signal is zero. The units of time are sample intervals; hence the “time” of a sample is synonymous with its sample number.

Samples having the same sample number in different signals of the same record are treated as simultaneous. In truth, they are usually not precisely simultaneous, since most multi-channel digitizers sample signals in “round-robin” fashion. If this subtlety makes a difference to you, you should be prepared to compensate for inter-signal sampling skew in your programs.

## Annotations

Annotation files provide additional information about a record, for example providing beat labels or highlighting when an alarm was triggered. The “time” of an annotation is simply the sample number of the sample with which the annotation is associated. Annotations may be associated with a single signal, if desired. No more than one annotation in a given annotation file may be associated with any given sample of any given signal. There may be many annotation files associated with the same record, however; they are distinguished by annotator names. The annotator name ‘atr’ is reserved to identify reference annotation files supplied by the developers of the databases to document correct beat labels. You may use other annotator names (which may contain letters, digits and underscores, as for record names) to identify annotation files that you create. You may wish to adopt the convention that the annotator name is the name of the file’s creator (a program or a person).

Annotations are visible to the WFDB library user as C structures, the fields of which specify time, beat type, and several user-definable variables. The WFDB library performs efficient conversions between these structures and a compact bit-packed representation used for storage of annotations in annotation files.


