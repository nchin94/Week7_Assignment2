#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import glob


# In[15]:


weekly_calls = pd.DataFrame()


# In[16]:


for calls in glob.glob("C:\\Users\\nchin\\Data Viz\\weekly_call_data\\weekdata*.xlsx"):
    df = pd.read_excel(calls)
    weekly_calls = weekly_calls.append(df,ignore_index = True)
weekly_calls.describe


# In[ ]:





# In[ ]:




