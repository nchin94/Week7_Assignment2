#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import create_engine


# In[3]:


# Connect to sqlite db
db_file = r'datasets/sales.db'


# In[6]:


engine = create_engine(r"sqlite:///{}".format(db_file))


# In[ ]:




