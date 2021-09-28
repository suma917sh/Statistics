#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df=pd.read_csv("C:\\Users\\hp\\Downloads\\Q9_b.csv")


# In[7]:


df.describe()


# In[9]:


#Skewness
df.skew()


# Skewness Inference: 1. SP distributioon is Right skewed (Positive skewness) 2. WT distribution is Left skewed (Negative skewness)

# In[10]:


#Kurtosis
df.kurtosis()


# Kurtosis Inference: Both the SP and WT distributions are leptokurtic (have positive kurtosis i.e. Peaked than normal distribution)

# In[ ]:




