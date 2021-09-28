#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import statistics as stats


# In[20]:


df=pd.read_csv("C:\\Users\\hp\\Downloads\\Q7.csv")


# In[21]:


print(df)


# In[22]:


df.dtypes


# In[23]:


df.mean


# In[24]:


df.columns


# In[25]:


df.describe


# In[26]:


df.mean()


# In[27]:


df.std()


# In[28]:


df.median()


# In[29]:


df.var()


# In[32]:


df.mode()


# In[33]:


df.max()


# In[34]:


df.min()


# In[ ]:




