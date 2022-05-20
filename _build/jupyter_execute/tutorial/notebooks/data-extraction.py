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


# Select the first record
selected_record = '3000063_0013'
print("Selected record: {}".format(selected_record))


# ## Extract data from this record

# In[3]:


# load data from this record
database_name = 'mimic3wdb/1.0/30/3000063/'
record_data = wfdb.rdrecord(record_name=selected_record, pn_dir=database_name) 
print("Data loaded from record: {}".format(selected_record))


# In[4]:


# Look at class type of the object in which the data are stored:
print("Data stored in class of type: {}".format(type(record_data)))


# In[5]:


# look at variables contained within the object
from pprint import pprint
pprint(vars(record_data))


# In[ ]:




