#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# In[2]:


# Apply One-Sample One-Tail z-test


# calculate z-score or value z_scores = (p̂-p)/√(p(1-p)/n) ...N(0,1)

# In[4]:


z_scores=(0.046-0.05)/(np.sqrt((0.05*(1-0.05))/2000))
z_scores


# In[5]:


# Find Probability assuming null hyposthesis, so as to compare with Type-1 error α = 0.05


# In[6]:


p_value=1-stats.norm.cdf(abs(z_scores))
p_value

