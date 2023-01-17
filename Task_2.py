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


p1 = binom.pmf(0,5000,0.0004)


# In[4]:


p2 = binom.pmf(2,5000,0.0004)


# In[5]:


lam = 5000*0.0004


# In[6]:


p3 = poisson.pmf(0,lam)


# In[7]:


p4 = poisson.pmf(2,lam)


# In[8]:


print('Вероятность, что ни одна из них не перегорит в первый день (binom) =',p1)


# In[9]:


print('Вероятность, что ни одна из них не перегорит в первый день (poisson) =',p3)


# In[10]:


print('Вероятность, что перегорят ровно две (binom) =',p2)


# In[11]:


print('Вероятность, что перегорят ровно две (poisson) =',p4)

