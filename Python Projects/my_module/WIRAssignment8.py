#!/usr/bin/env python
# coding: utf-8

# # Assignment 8 _ Web as Graph

# ## Function to accept any 2D 'matrix' which is a representation of a graph and:
# - Calculate the indegree and the outdegree
# - generate a Stochastic Transition Matrix
# - Calculate the rank after 'n' interations

# In[1]:
from __future__ import division

import numpy as np
np.seterr(divide='ignore', invalid='ignore')



# In[2]:


A = np.array ([[0,0,0,0,0,0],[1,0,0,0,0,0], [1,0,0,1,0,0],[1,1,0,0,1,0], [0,0,1,1,0,1],[0,1,0,0,0,0]])
A=A.astype('float64')


# ### Degree calculation (deg_Calc)

# In[3]:


def deg_Calc(adj_mat):
    return (adj_mat.sum(axis=0), adj_mat.sum(axis=1))


# In[4]:


in_d, out_d = deg_Calc(A)


# In[5]:


in_d, out_d


# ### Stochastic Matrix  (stm_Calc)

# In[6]:


def stm_Calc(adj_mat, alpha):
    count = adj_mat.sum(axis=1)
    print ("Count ", count)
    z_row = np.where(~adj_mat.any(axis=1))[0]
    print (z_row)
    if (z_row.size):
        for item in z_row:
#             print item 
            adj_mat[item, :] = float(1/len(adj_mat))
        
    print ("\n When encountering a row with all Zeros\n", adj_mat)
    
    for i in range(len(count)):
        if (i in z_row):
            continue
        else:
            adj_mat[i] = adj_mat[i]/count[i]
    
    adj_mat =  np.where(np.isnan(adj_mat), 0, adj_mat)
    print ("\n Divide all rows by the number of 1s in that row \n", adj_mat)
    
    adj_mat = (adj_mat*(1-alpha))
    print ("\n Multiply matrix by 1-alpha \n", adj_mat)
    
    adj_mat = adj_mat + (alpha/len(count))
    print ("\n Adding alpha/N to all elements \n ", adj_mat)
    
    return (adj_mat)


# In[7]:


S_T_M = ([[0.0333,0.4333,0.4333,0.0333,0.0333,0.0333],[0.0333,0.0333,0.0333,0.4333,0.0333,0.4333], [0.0333,0.0333,0.0333,0.0333,0.0333,0.8333],[0.0333,0.0333,0.0333,0.0333,0.0333,0.8333], [0.0333,0.3,0.3,0.3,0.0333,0.0333],[0.1666,0.1666,0.1666,0.1666,0.1666,0.1666]])
print ("\n Stochastic Transition Matrix \n", S_T_M)


# ### Rank

# In[8]:


def rank_Calc(stm, X):
    c = len(stm.sum(axis=1))
    prob = 1/c
    
    
    vec_x0 = np.full((1,c),prob)
    print ("\ninitial vector", vec_x0)
    
    while(X!=0):
        vec_x0 = np.dot(vec_x0, stm)
        X = X-1
        print (vec_x0)


# In[9]:


rank_Calc(S_T_M, 5)


# In[10]:


# def rank_Calc(stm, X):
#     c = len(stm)
#     prob = 1/c
#
#
#     vec_x0 = np.full((1,c),prob)
#     print ("initial vector", vec_x0)
#
#     while(X!=0):
#         vec_x0 = np.matmul(vec_x0, stm)
#         X = X-1
#         print (vec_x0)
#
#
# # In[11]:
#
#
# rank_Calc(S_T_M, 5)

