# Setup
import sys
from pathlib import Path
import pandas as pd

import wfdb # The WFDB Toolbox

wfdb.set_db_index_url('https://challenge.physionet.org/benjamin/db')

records = []
database_name = 'mimic4wdb/0.1.0' # The name of the MIMIC IV Waveform Demo Database on Physionet (see URL: )
subjects = wfdb.get_record_list(f'{database_name}')
for subject in subjects:
    studies = wfdb.get_record_list(f'{database_name}/{subject}')
    for study in studies:
        records.append(Path(f'{subject}{study}'))
print("Done: Loaded list of {} records for '{}' database".format(len(records), database_name))

# Find how many records have segments with PPG + ABP and are 10 minutes long
matching_recs = {}
for record in records:
    record_dir = f'{database_name}/{record.parent}'
    record_name = record.name
    record_data = wfdb.rdheader(record_name, pn_dir=record_dir, rd_segments=True)
    # Get the segments for the record
    segments = record_data.seg_name
    # First check to see if the segment is 10 min long, if not move onto the next one
    gen = (segment for segment in segments if segment != '~')
    for segment in gen:
        segment_metadata = wfdb.rdheader(record_name=segment, pn_dir=record_dir)
        seg_length = segment_metadata.sig_len/(segment_metadata.fs*60)
        if seg_length < 10:
            continue
        # Next check that both PPG and ABP are present in the segment
        sigs_present = segment_metadata.sig_name
        required_sigs = ['ABP', 'PPG']
        if all(x in sigs_present for x in required_sigs):
            matching_recs['dir'] = record_dir
            matching_recs['seg_name'] = segment
            matching_recs['length'] = seg_length
            # Since we only need one segment per record break out of loop
            break

df_matching_recs = pd.DataFrame(data=matching_recs)
df_matching_recs.to_csv('matching_records.csv', index=False)
p=1