#!/usr/bin/env python
# coding: utf-8

# # Data Extraction
# 
# Extract data from a MIMIC Waveform record.

# ## Identify a record

# In[1]:


# setup
import sys
import wfdb


# In[2]:


# get a list of records in the database
database_name = 'bidmc'
records = wfdb.get_record_list(database_name)
print("List of records loaded for {} database".format(database_name))


# In[3]:


# Select the first record
selected_record = records[0]
print("Selected record: {}".format(selected_record))


# ## Extract data from this record

# In[4]:


# load data from this record
record_data = wfdb.rdrecord(record_name=selected_record, pn_dir=database_name) 
print("Data loaded from record: {}".format(selected_record))


# In[5]:


# Look at class type of the object in which the data are stored:
print("Data stored in class of type: {}".format(type(record_data)))


# In[6]:


# look at variables contained within the object
from pprint import pprint
pprint(vars(record_data))


# In[ ]:





# In[ ]:




