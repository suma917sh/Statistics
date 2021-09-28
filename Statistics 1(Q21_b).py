#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv("C:\\Users\\hp\\Downloads\\wc-at.csv")


# In[3]:


df


# In[5]:


# plotting distribution for Waist Circumference (Waist) 
sns.distplot(df.Waist)
plt.ylabel('density');


# In[6]:


# plotting distribution for Adipose Tissue (AT) 
sns.distplot(df.AT)
plt.ylabel('density')


# In[8]:


# WC
df.Waist.mean(),df.Waist.median()


# In[10]:


# AT
df.AT.mean() , df.AT.median()


# Inference: Both the Adipose Tissue (AT) and Waist Circumference(Waist) data set do follow the normal distribution approximately (as mean and median of both the data are approximately same)

# In[ ]:




