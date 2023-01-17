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


p = binom.pmf(70,144,.5)


# In[4]:


print('Вероятность, что орел выпадет ровно 70 раз =',p)

