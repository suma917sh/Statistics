#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# In[4]:


# we have normal distribution with 
mean= 45
std = 8


# In[6]:


# find z-score ,X=50 and z=(X-mean)/std
z=(50-45)/8
z


# In[7]:


# Find probability P(X>50) = 1-stats.norm.cdf(abs(z_score))
1-stats.norm.cdf(abs(0.625))


# cannot meet his commitement
