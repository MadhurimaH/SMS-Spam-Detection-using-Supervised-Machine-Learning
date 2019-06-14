#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


cd ..


# In[3]:


cd ..


# In[4]:


cd ..


# In[5]:


cd /dataset/


# In[6]:


#load dataset
ds=pd.read_csv("SPAM.csv")


# In[7]:


ds.head()


# In[8]:


ds['lower'] = ds['Message'].apply(lambda x: len([x for x in x.split() if x.islower()]))
ds[['Message','lower']].head()


# In[ ]:




