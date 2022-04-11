#!/usr/bin/env python
# coding: utf-8

# # Data Visualisation
# 
# Visualise signals in a MIMIC Waveform record.

# ## Extract data from a record

# In[1]:


# setup
import sys
import wfdb


# In[2]:


# Specify a record
database_name = 'bidmc'
selected_record = "bidmc01"
print("Selected record: {}".format(selected_record))


# In[3]:


# load data from this record
no_seconds_to_load = 5
record_data = wfdb.rdrecord(record_name=selected_record, sampfrom=0, sampto=125*no_seconds_to_load, pn_dir=database_name) 
print("{} seconds of data loaded from: {}".format(no_seconds_to_load, selected_record))


# ## Plot signals in this record
# Plot the signals contained in this record

# In[4]:


# plot the data loaded from this record
title_text = "First record from " + database_name + " (record: " + selected_record + ")"
wfdb.plot_wfdb(record=record_data, title=title_text, time_units='seconds') 


# In[5]:


record_contains_signals_log = 'RESP,' in record_data.sig_name and 'PLETH,' in record_data.sig_name
if record_contains_signals_log:
    print('This record contains the required signals')
else:
    print('This record doesn\'t contain the required signals')


# In[6]:


# plot just the signals of interest from this record
title_text = "Selected signals from: " + selected_record
wfdb.plot_items(signal=record_data.p_signal[:,0:2], title = title_text, ylabel = record_data.sig_name[0:2])


# In[ ]:





# In[ ]:




