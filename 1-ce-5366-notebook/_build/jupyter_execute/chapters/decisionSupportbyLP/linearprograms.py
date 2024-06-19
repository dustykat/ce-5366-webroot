#!/usr/bin/env python
# coding: utf-8

# # Linear Programming for Decision Support
# 
# Linear Programming (LP) is a powerful mathematical technique used for optimization. It involves maximizing or minimizing a **linear** objective function, subject to a set of **linear** constraints. The objective function represents the quantity to be optimized (such as profit or cost), while the constraints define the limitations or conditions within which the optimization must occur (like resource availability or production capacities).
# 
# LP is widely applied in various fields such as economics, engineering, business management, and logistics, where decisions need to be made to allocate limited resources efficiently. The method is particularly valuable because it provides a systematic way to find the best possible solution given these constraints, ensuring optimal decision-making and resource allocation. Through LP, complex real-world problems can be transformed into a structured mathematical framework, facilitating informed decision-making and maximizing outcomes.
# 
# ## Solving Linear Programs
# Danzig's algorithm also known as the simplex method, is a fundamental technique within Linear Programming for solving optimization problems. Developed by George Dantzig in the late 1940s, it revolutionized the field by providing an efficient way to find the optimal solution to linear programming problems.
# 
# Here's how Danzig's algorithm fits into the broader context of Linear Programming:
# Linear Programming (LP):
# 
# LP involves optimizing a linear objective function subject to linear constraints. The general form is: <br>
# 
#   Maximize: $c^T x$ <br>
# Subject to: 
# $Ax <= b$;$Ix >= 0$
# 
# 
# Where:
# 
# - $x$ is the vector of decision variables to be determined,
# - $c$ is the vector of coefficients representing the objective function to maximize,
# - $A$ is the matrix of coefficients of the constraints,
# - $I$ is the identity matrix
# - $b$ is the vector of constants on the right-hand side of the constraints.
# 
# ### Danzig's Algorithm (Simplex Method):
# 
# [Danzig's algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm) is an iterative procedure that systematically moves from one feasible solution to another along the edges of the feasible region until the optimal solution is found. The steps involved typically include:
# 
# - Initialization: Start with a feasible solution.
# - Iteration: Move to an adjacent feasible solution that improves the objective function (if possible).
# - Termination: Stop when no further improvements can be made, indicating the optimal solution has been reached.
# 
# The simplex method operates by pivoting among the variables to gradually improve the objective function value. It ensures that each iteration moves closer to the optimal solution by following a strategic path through the vertices (corners) of the feasible region defined by the constraints.
# Benefits and Applications:
# 
# - Efficiency: Despite its theoretical worst-case exponential time complexity, the simplex method often performs efficiently in practice for many real-world problems.
# - Versatility: It can handle large-scale linear programming problems with numerous variables and constraints, making it applicable in diverse fields such as economics (production planning), logistics (supply chain optimization), and finance (portfolio optimization).
# - Optimality: Danzig's algorithm **guarantees** finding the optimal solution under certain conditions, providing confidence in decision-making processes.
# 
# The simplex method is a cornerstone of Linear Programming (there is a similarily named method in non-linear programming), offering a systematic approach to solving optimization problems by iteratively improving feasible solutions until the best possible outcome is achieved, within the constraints provided. Its practical applications and theoretical underpinnings make it indispensable in various industries for making informed decisions and optimizing resource allocations.
# 
# ### Practical Implementation
# 
# Except for really small (trivial) problems, LP is unworkable by hand.  Usually some specalized tool is used including:
# 
# 1. **MS Excel Solver Add-In**.  Farily simple to implement, but limited in overall problem scale.  Many significant problems have millions of decision variables, Excel cannot handle those size problems. An internet search produces a lot of tutorials such as: [Linear Programming with Solver](https://www.msubillings.edu/asc/writingcenter/resources/math/tutorials/finitemathhelps/Lin%20Prog%20with%20Excel.pdf)
# 2. **R Packages**.  Harder to implement; requires some understanding of R libraries, but can handle larger scale problems and is far easier to automate multi-stage programming.  An example package is [dummy](dummy)
# 3. **Python Packages**.  Like R, requires some understanding of python libraries, but can handle large scale problems, is inherently automatable.  An example is shown beloy using the `scipy` kernel library; there are other libraries - see the reference list.  One thing to note is the python tools are very architecture dependent - some only work on Intel/AMD architecture (specific hardware) others are more general and can run on ARM architecture.  The example below runs fine on Raspberry Pi, or an Intel laptop, or an AWS virtual private server.
# 4. **Commercial Software** For really big problems, one will use commercial software such as [LINDO](https://lindo.com/), [MINOS](https://en.wikipedia.org/wiki/MINOS_(optimization_software)) or [IBM CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio/cplex-optimizer)

# ## Example using `scipy`
# 
# The example below is verbatim from [Mirko Stojiljković (2020) Hands-On Linear Programming: Optimization With Python. Real Python (Blog Post)](https://realpython.com/linear-programming-python/)

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


# ## Example using `PuLP`
# 
# The example below is verbatim from [Priyansh Soni (2020) Linear Programming using Python. Towards Data Science (Blog Post)](https://towardsdatascience.com/linear-programming-using-python-priyansh-22b5ee888fe0)
# 
# :::{note}
# This example does not play well with a Raspberry Pi, my guess is some apsect in PuLP is not compiling correctly for the ARM processor.
# The change in solver type produces correct output - this is typical for packages regardless of host type.  The user needs to mess with things to get it working.
# :::

# In[5]:


from pulp import * # pulp needs to be installed into the kernel first
import pandas as pd
import numpy as np

n_warehouses = 2
n_customers = 4

# Cost Matrix
cost_matrix = np.array([[1, 3, 0.5, 4],
                       [2.5, 5, 1.5, 2.5]])
# Demand Matrix
cust_demands = np.array([35000, 22000, 18000, 30000])

# Supply Matrix
warehouse_supply = np.array([60000, 80000])

model = LpProblem("Supply-Demand-Problem", LpMinimize)

variable_names = [str(i)+str(j) for j in range(1, n_customers+1) for i in range(1, n_warehouses+1)]
variable_names.sort()
print("Variable Indices:", variable_names)

DV_variables = LpVariable.matrix("X", variable_names, cat = "Integer", lowBound= 0 )
allocation = np.array(DV_variables).reshape(2,4)
print("Decision Variable/Allocation Matrix: ")
print(allocation)

obj_func = lpSum(allocation*cost_matrix)
print(obj_func)
model +=  obj_func
print(model)


# In[6]:


#Supply Constraints
for i in range(n_warehouses):
    print(lpSum(allocation[i][j] for j in range(n_customers)) <= warehouse_supply[i])
    model += lpSum(allocation[i][j] for j in range(n_customers)) <= warehouse_supply[i] , "Supply Constraints " + str(i)


# In[7]:


# Demand Constraints
for j in range(n_customers):
    print(lpSum(allocation[i][j] for i in range(n_warehouses)) >= cust_demands[j])
    model += lpSum(allocation[i][j] for i in range(n_warehouses)) >= cust_demands[j] , "Demand Constraints " + str(j)


# In[8]:


model.writeMPS("Supply_demand_prob.lp") # write problem set-up to a text file


# In[9]:


from pulp import GLPK # A working solver needs to be loaded explicit on ARM!

#model.solve()

model.solve(solver=GLPK(msg=True))

status =  LpStatus[model.status]

print(status)


# In[10]:


print("Total Cost:", model.objective.value())

# Decision Variables

for v in model.variables():
    try:
        print(v.name,"=", v.value())
    except:
        print("error couldnt find value")


# In[11]:


# Warehouse 1 and Warehouse 2 required capacity

for i in range(n_warehouses):
    print("Warehouse ", str(i+1))
    print(lpSum(allocation[i][j].value() for j in range(n_customers)))


# This package looks more complicated than the other example, the value is the ability to save a file.  There is at the time of writing some issue with reading in the file, but it will undoubtable be solved in time.  As a practical matter, the analyst should code the entire model in such a way that reconstruction is simple.

# ## Example using `R`
# 
# Consider another really simple example:
# 
#  $\text{   minimize : }20 x_1 + 60 x_2$<br>
#  $\text{ subject to : }30 x_1 + 20 x_2 <= 2700$<br>
#  $~~~~~~~~~~~~~~~~~~~~~ 5 x_1 + 10 x_2 <=   850$<br>
#  $~~~~~~~~~~~~~~~~~~~~~~~~~~~   x_1 +    x_2 >=    95$<br>
#  
# The screen capture below solves the LP above in R.  It uses the library LpSolve.  The syntax is awkward compared to the python scripts, but is otherwise similar. 
# 
# ![](LPinR.png)
# 
# [Modeling and Solving Linear Programs with R](http://54.243.252.9/ce-5366-webroot/3-Readings/ModelingAndSolvingLinearProgramsWithR.pdf) is a good starting place if you want to use R to do your computations.
# 

# ## Summary
# 
# This section introduced practical approaches to solving Linear Programs, and illustrated use of Python packages to do so.

# 

# ## References
# 1. [Mirko Stojiljković (2020) Hands-On Linear Programming: Optimization With Python. Real Python (Blog Post)](https://realpython.com/linear-programming-python/)
# 2. [scipy.optimize.linprog (Documentation)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html) 
# 3. [Priyansh Soni (2020) Linear Programming using Python. Towards Data Science (Blog Post)](https://towardsdatascience.com/linear-programming-using-python-priyansh-22b5ee888fe0)
# 5. [Disser, Y. and Skutella, M. (2014). The Simplex Algorithm is NP-mighty. TU Berlin, Inst. of Mathematics, MA 5-2, Str. des 17. Juni
# 136, 10623 Berlin, Germany.](https://www2.mathematik.tu-darmstadt.de/~disser/pdfs/DisserSkutella15.pdf)
# 4. [Gross, O (1962). A LINEAR PROGRAM OF PRAGER'S; Notes on Linear Programming and Extensions. MEMORANDUM
# RM-2993-PR (Rand Corporation Memorandum to U.S. Air Force Research Headquarters)](https://apps.dtic.mil/sti/tr/pdf/AD0274596.pdf)
# 

# In[ ]:





# ## Addendum `Python-MIP`
# 
# Python-MIP is one of many LP solvers avaialble on the mighty internet; it is used in this course because it appears to run on a Raspberry Pi withou a lot of fuss (this is an architecture issue, for students using X86-64 machines, the Anaconda install should be just fine, and you can use any LP solver you wish).
# 
# MIP means mixed integer programs, which are hard to solve efficiently.  The example below is the script to solve a knapsack problem.
# 

# ```
# from mip import Model, xsum, maximize, BINARY # need to install mip into the kernel first!!
# 
# p = [10, 13, 18, 31, 7, 15]
# w = [11, 15, 20, 35, 10, 33]
# c, I = 47, range(len(w))
# 
# m = Model("knapsack")
# 
# x = [m.add_var(var_type=BINARY) for i in I]
# 
# m.objective = maximize(xsum(p[i] * x[i] for i in I))
# 
# m += xsum(w[i] * x[i] for i in I) <= c
# 
# m.optimize()
# 
# selected = [i for i in I if x[i].x >= 0.99]
# print("selected items: {}".format(selected))
# ```

# In[ ]:




