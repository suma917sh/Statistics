#!/usr/bin/env python
# coding: utf-8

# # Q9a)Skewness, Kurtosis & inferences on the Cars speed and distance

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


df=pd.read_csv("C:\\Users\\hp\\Downloads\\Q9_a.csv")


# In[22]:


df.describe()


# In[23]:


#skewness
df.skew()


# skewness Inference: 1. speed distributioon is left skewed (negative skewness) 2. dist distribution is right skewed (positive
#                                                                                                                    skewness)

# In[25]:


#Kurtosis
df.kurtosis()


# Kurtosis Inference: 1.speed distributions is left kurtosis(negative kurtosis)2.dist distribution is right kurtosis(positive kurtosis)

# In[ ]:




