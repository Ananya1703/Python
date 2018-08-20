
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


x = np.random.random(10000000)


# In[7]:


sum(x)/len(x)


# In[8]:


np.mean(x)


# In[10]:


y = np.array([1,2,3,4,5])


# In[11]:


print(y)
print(type(y))


# In[13]:


y.shape


# In[15]:


z=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[16]:


print(z)
z.shape


# In[17]:


z.size


# In[18]:


np.save('my_array',z)


# In[22]:


a = np.zeros((2,4))
print(a)


# In[23]:


b = np.ones((2,2))
print(b)


# In[24]:


c = np.full((3,3),10)
print(c)


# In[26]:


d = np.eye((4))
print(d)

