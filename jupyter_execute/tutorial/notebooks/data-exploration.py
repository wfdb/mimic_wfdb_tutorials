# Data Exploration

Exploring MIMIC waveform data.

## Identify records

Identify the records in the MIMIC III Waveform Database

# setup
import sys
import wfdb

# get a list of records in the database
database_name = 'mimic3wdb'
records = wfdb.get_record_list(database_name)
print("Loaded list of records for {} database".format(database_name))

# Display the first few records
print(" - First ten records: {}".format(records[0:10]))
# print(" - Last ten records: {}".format(records[-10:]))

## Look at files in a record
Inspect the files that make up a record



