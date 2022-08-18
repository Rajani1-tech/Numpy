#!/usr/bin/env python
# coding: utf-8
Numpy is another main library of python that is used to solve linear algebra or mathetical matrix.
# In[1]:


import numpy as np


# In[2]:


my_array = np.array([10,12,14,16,20,25])
print(my_array)
print(my_array.dtype)
print(my_array.dtype.itemsize)


# In[3]:


my_array = np.array(["Red","Green","Orange"])
print(my_array)
print(my_array.dtype)
print(my_array.dtype.itemsize)


# In[5]:


my_array = np.array(["1990-10-04","1989-05-06", "1990-11-04"]
            )
print(my_array)
print(my_array.dtype)
print(my_array.dtype.itemsize)


# In[7]:


nums_list = [10,12,14,16,20]
nums_array = np.array(nums_list)
type(nums_array)


# In[9]:


row1 = [10,12,13]
row2 = [45,32,16]
row3 = [45,32,16]
nums_2d = np.array([row1, row2, row3])
print(nums_2d)
nums_2d.shape


# In[10]:


nums_arr = np.arange(5, 11)
print(nums_arr)


# In[11]:


nums_arr = np.arange(5,12,2)
print(nums_arr)


# In[13]:


ones_array = np.ones(6)
print(ones_array)


# In[ ]:




