#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


# In[3]:


df=pd.Series([34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56])


# In[11]:


#Mean
df.mean()


# In[12]:


# Median
df.median()


# In[13]:


#Mode
df.mode()


# In[14]:


#Variance
df.var()


# In[15]:


#Standard Deviaton
df.std()


# In[16]:


#Box plot
plt.boxplot(df)


# Inference: 1. There are 2 Outliars in Student's marks: 49 and 56
# 

# In[ ]:




