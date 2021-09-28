#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("C:\\Users\\hp\\Downloads\\Cars.csv")


# In[3]:


df


# In[4]:


df.MPG.mean()


# In[5]:


df.MPG.median()


# Inference:MPG of Cars does follow normal distribution approximately (as mean and median are approx. same)

# In[14]:


sns.distplot(df.MPG, label='df-MPG')
plt.legend();
plt.xlabel('MPG')
plt.ylabel('Density')


# In[ ]:





# In[ ]:




