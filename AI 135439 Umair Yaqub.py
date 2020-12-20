#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[5]:


a = np.arange(20).reshape(5, 4)


# In[6]:


a


# In[7]:


a.shape


# In[8]:


a.ndim


# In[9]:


a.dtype.name


# In[10]:


a.itemsize


# In[11]:


a.size


# In[12]:


type(a)


# In[15]:


b = np.array([10, 12, 16])


# In[16]:


b


# In[17]:


type(b)


# In[18]:


np.zeros((2, 8))


# In[19]:


np.ones( (10,13,24), dtype=np.int16 )


# In[20]:


np.empty( (27,38) )


# In[28]:


np.arange( 1, 4, 2 )


# In[27]:


np.arange( 1, 5, 0.3 )


# In[29]:


np.linspace( 2, 22, 9 )


# In[31]:


x = np.linspace( 0, 2*3.14, 20 )


# In[32]:


f = np.sin(x)


# In[33]:


a = np.arange(12)


# In[34]:


print(a)


# In[36]:


b = np.arange(10).reshape(2,5)


# In[37]:


print(b)


# In[38]:


c = np.arange(24).reshape(2,3,4)


# In[39]:


print(c)


# In[40]:


print(np.arange(10000))


# In[41]:


print(np.arange(10000).reshape(100,100))


# In[42]:


a = np.array( [20,30,40,50] )


# In[43]:


b = np.arange( 4 )


# In[44]:


b


# In[45]:


c = a-b


# In[46]:


c


# In[47]:


b**2


# In[48]:


10*np.sin(a)


# In[49]:


a<35


# In[50]:


A = np.array( [[1,1],
               [0,1]] )


# In[51]:


B = np.array( [[2,0],
               [3,4]] )


# In[52]:


A * B


# In[53]:


A @ B


# In[54]:


A.dot(B)


# In[ ]:




