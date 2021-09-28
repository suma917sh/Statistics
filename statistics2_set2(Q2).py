#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# In[2]:


#we have normal distribution with mean=38 and std=6. number of employees N= 400
mean=38
std=6


# A)More employees at the processing center are older than 44 than between 38 and 44.

# In[3]:


# p(X>44); Employees older than 44 yrs of age
1-stats.norm.cdf(44,loc=38,scale=6)


# In[4]:


# p(38<X<44); Employees between 38 to 44 yrs of age
stats.norm.cdf(44,38,6)-stats.norm.cdf(38,38,6)


# Inference: Statement A is false as Probability of employees aged between 38 to 44 is more

# B)A training program for employees under the age of 30 at the center would be expected to attract about 36 employees.

# In[5]:


# P(X<30); Employees under 30 yrs of age
stats.norm.cdf(30,38,6)


# In[6]:


# No. of employees attending training program from 400 nos. is N*P(X<30)
400*stats.norm.cdf(30,38,6)


# Inference: Statement B is true as no. of employees aged below 33 yrs attending training is 36
