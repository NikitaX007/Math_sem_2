#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import  binom
from scipy.stats import  poisson


# In[2]:


def combinations(n, k):
    return (np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))


# In[3]:


t1 = combinations(10, 2)


# In[4]:


t2 = combinations(11, 2)


# In[5]:


a1 = combinations(7, 2)


# In[6]:


a2 = combinations(9, 2)


# In[7]:


p1=a1/t1


# In[8]:


p2=a2/t2


# In[9]:


p=p1*p2


# In[10]:


print('Вероятность того, что все мячи белые p=',p)


# In[11]:


# Какова вероятность того, что ровно два мяча белые?


# In[12]:


# Всего 3 варианта: 2 белых + 0 белых, 1 белый + 1 белый, 0 белых + 2 белых


# In[13]:


a1 = combinations(7, 2)


# In[14]:


a2 = combinations(2, 2)


# In[15]:


p1=a1/t1


# In[16]:


p2=a2/t2


# In[17]:


pa=p1*p2


# In[18]:


print('2 белых + 0 белых pa =',pa)


# In[19]:


a1 = combinations(2, 2)


# In[20]:


a2 = combinations(9, 2)


# In[21]:


p1=a1/t1


# In[22]:


p2=a2/t2


# In[23]:


pb=p1*p2


# In[24]:


print('0 белых + 2 белых pb=',pb)


# In[25]:


a1 = combinations(7, 1)


# In[26]:


a2 = combinations(9, 1)


# In[27]:


b1 = combinations(3, 1)


# In[28]:


b2 = combinations(2, 1)


# In[29]:


p1=(a1*b1)/t1


# In[30]:


p2=(a2*b2)/t2


# In[31]:


pc=p1*p2


# In[32]:


print('1 белый + 1 белый pc =',pc)


# In[33]:


p=pa+pb+pc


# In[34]:


print('Вероятность того, что ровно два мяча белые p =',p)


# In[35]:


a1 = combinations(3, 2)


# In[36]:


a2 = combinations(2, 2)


# In[37]:


p1=a1/t1


# In[38]:


p2=a2/t2


# In[39]:


p=1-p1*p2


# In[40]:


print('Вероятность того, что хотя бы один мяч белый p =',p)

