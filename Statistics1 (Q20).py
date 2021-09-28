#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
from scipy import stats


# In[5]:


df=pd.read_csv("C:\\Users\\hp\\Downloads\\cars.csv")


# In[10]:


mean=df.MPG.mean()
mean


# In[12]:


std_dev=df.MPG.std()
std_dev


# In[13]:


#P(MPG>38)
1-stats.norm.cdf(38,mean,std_dev)


# In[14]:


#P(MPG<40)
stats.norm.cdf(40,mean,std_dev)


# In[15]:


#P(20<MPG<50
stats.norm.cdf(50,mean,std_dev)-stats.norm.cdf(20,mean,std_dev)


# In[ ]:




