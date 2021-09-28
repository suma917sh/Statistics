#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[49]:


df=pd.read_excel("C:\\Users\\hp\\Documents\\Que1data.xlsx")


# In[50]:


df.info()


# In[51]:


df.sort_values(by='MeasureX')


# In[66]:


Dataset=df.loc[:,'MeasureX']
Dataset


# In[100]:


Dataset.describe()


# In[101]:


Dataset.var()


# In[99]:


plt.boxplot(Dataset)
plt.show()


# Find outliers by using IQR technique

# In[85]:


quantile1, quantile3= np.percentile(Dataset,[25,75])


# In[86]:


print(quantile1,quantile3)


# In[87]:


#find the IQR
iqr_value=quantile3-quantile1
iqr_value


# In[88]:


#find the lower bound and higher bound
lower_bound_value=quantile1-(1.5*iqr_value)
higher_bound_value=quantile3+(1.5*iqr_value)


# In[89]:


print(lower_bound_value,higher_bound_value)


# SO, Data points below 0.127 and above 0.467 consider as outliers.
