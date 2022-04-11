#!/usr/bin/env python
# coding: utf-8

# # Identify records
# 
# Identify the first adult record in the MIMIC III Waveform Database

# In[1]:


# setup
import sys
import wfdb


# In[2]:


# get a list of records in the database
database_name = 'bidmc'
records = wfdb.get_record_list(database_name) #'mimic3wdb')
print("List of records loaded for {} database".format(database_name))


# In[3]:


# Select the first record
selected_record = records[0]
print("Selected record: {}".format(selected_record))


# # Plot record
# Plot the signals contained in this record

# In[4]:


# load data from this record
no_seconds_to_load = 5
record_data = wfdb.rdrecord(record_name=selected_record, sampfrom=0, sampto=125*no_seconds_to_load, pn_dir=database_name) 
print("{} seconds of data loaded from {}".format(no_seconds_to_load, selected_record))


# In[5]:


# plot the data loaded from this record
title_text = "First record from " + database_name + " (record: " + selected_record + ")"
wfdb.plot_wfdb(record=record_data, title=title_text, time_units='seconds') 


# In[6]:


a = 'RESP,' in record_data.sig_name
a


# In[7]:


# plot just the signals of interest from this record
title_text = "Selected signals from: " + selected_record
wfdb.plot_items(signal=record_data.p_signal[:,0:2], title = title_text, ylabel = record_data.sig_name[0:2])


# In[ ]:





# In[ ]:




