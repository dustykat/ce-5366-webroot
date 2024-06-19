#!/usr/bin/env python
# coding: utf-8

# # Linear Programming for Decision Support

# ## Example using `scipy`

# In[1]:


from scipy.optimize import linprog


# In[2]:


obj = [-1, -2]
lhs_ineq = [[ 2,  1],  # Red constraint left side
[-4,  5],  # Blue constraint left side
[ 1, -2]]  # Yellow constraint left side

rhs_ineq = [20,  # Red constraint right side
10,  # Blue constraint right side
2]  # Yellow constraint right side

lhs_eq = [[-1, 5]]  # Green constraint left side
rhs_eq = [15]       # Green constraint right side


# In[3]:


bnd = [(0, float("inf")),  # Bounds of x
(0, float("inf"))]  # Bounds of y


# In[4]:


opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
              method="revised simplex")
opt


# ## Example using `Python-MIP`
# 
# Python-MIP is one of many LP solvers avaialble on the mighty internet; it is used in this course because it appears to run on a Raspberry Pi withou a lot of fuss (this is an architecture issue, for students using X86-64 machines, the Anaconda install should be just fine, and you can use any LP solver you wish)
# 
# 
from mip import Model, xsum, maximize, BINARY

p = [10, 13, 18, 31, 7, 15]
w = [11, 15, 20, 35, 10, 33]
c, I = 47, range(len(w))

m = Model("knapsack")

x = [m.add_var(var_type=BINARY) for i in I]

m.objective = maximize(xsum(p[i] * x[i] for i in I))

m += xsum(w[i] * x[i] for i in I) <= c

m.optimize()

selected = [i for i in I if x[i].x >= 0.99]
print("selected items: {}".format(selected))

# ## References
# 1. [Mirko Stojiljković (2020) Hands-On Linear Programming: Optimization With Python. Real Python (Blog Post)](https://realpython.com/linear-programming-python/)
# 2. [scipy.optimize.linprog (Documentation)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html) 
# 3. [Priyansh Soni (2020) Linear Programming using Python. Towards Data Science (Blog Post)](https://towardsdatascience.com/linear-programming-using-python-priyansh-22b5ee888fe0)
# 

# In[ ]:




