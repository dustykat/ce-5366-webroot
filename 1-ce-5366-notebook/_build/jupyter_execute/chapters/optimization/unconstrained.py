#!/usr/bin/env python
# coding: utf-8

# <!--![downhill-004.png](attachment:e5cc2360-f341-41d2-b854-dce2031abdde.png)# Gradient Descent Methods-->
# 
# # Python Unconstrained Minimization Methods
# 
# Unconstrained minimization finds the minimum value of a function $f(x)$ without any restrictions or constraints on the variables $x$. This is a fundamental problem in optimization where the goal is to find the point at which the function attains its lowest value within the entire domain.
# 
# Some background is found in [Ossenbruggen (1985-ish)](http://54.243.252.9/ce-5333-systems-webroot/3-Readings/OptimizeOssenbruggen/OptimizeOssenbruggen.pdf)
# 
# ## Packages
# 
# An example problem is to minimize
# 
# $$f(x) = \sum_{i = 1}^{N-1} \:100(x_i - x_{i-1}^{2})$$
# 
# without any constraints. A couple of favorite methods are outlined below.

# ### Nelder-Mead Method 
# 
# Also called Downhill Simplex, but not the same as the Simplex Method for Linear Programs!
# 
# Advantages:
# - Function calls only
# 
# Disadvantages:
# - Needs a starting vector that is non-degenerate 
# 

# In[1]:


import numpy as np
from scipy.optimize import minimize

def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead',options={'disp': True})

print(res.x)


# ### Powell's Direction Set Method
# 
# I like this method a lot.  
# 
# Advantages:
# - Function calls only
# 
# Disadvantages:
# - Needs a starting vector that is non-degenerate 
# 
# :::{note}
# Below is the FORTRAN code to implement the method below.  Notice the distinct usability of a python package over the old ways.
# :::

# In[2]:


import numpy as np
from scipy.optimize import minimize

def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='powell',options={'disp': True})

print(res.x)


# FORTRAN search engine using Powell's method.
# 
# ```
#       PROGRAM SEARCH
# C
# C MULTI-DIMENSIONAL SEARCHING METHOD FOR MINIMIZATION OF A SCALAR FUNCTION
# C OF AN N-DIMENSIONAL VECTOR ARGUMENT.  SEARCH USES POWELL'S SEARCHING METHOD
# C WHICH HAS FINITE CONVERGENCE FOR QUADRATIC FUNCTIONS
# C
# C PROGRAM ASSUMES A FUNCTION NAMED FUNC IS THE FUNCTION TO BE MINIMIZED
# C FUNC IS THE USER DEFINED FUNCTION WHICH MUST BE LINKED WITH THE PROGRAM
# C
# C REF:  AVRIEL, M., 1976.  NONLINEAR PROGRAMMING; ANALYSIS AND METHODS, 
# C       PRENTICE HALL, ENGLEWOOD CLIFFS, NEW JERSEY.
# C
# C       PRESS, W.H., FLANNERY, B.P., TEUKOLSKY, S.A., AND W.T. VETTERLING,
# C       1986.  NUMERICAL RECIPES; THE ART OF SCIENTIFIC COMPUTING, CAMBRIDGE
# C       UNIVERSITY PRESS, NEW YORK.
# C
#       IMPLICIT REAL*8 (A-H,O-Z)
#       PARAMETER(NP=10)
#       DIMENSION P(NP),XI(NP,NP)
# C
# C OPEN INPUT FILE AND READ INITIAL GUESS AND ORTHOGONAL SEARCH DIRECTIONS
# C
#       OPEN(UNIT=11,STATUS='UNKNOWN',ACCESS='SEQUENTIAL',
#      1     FILE='POWELL.DAT')
#       REWIND(11)
#       READ(11,*)N,FTOL
#       READ(11,*)(P(I),I=1,N)
#       DO 101 IROW=1,N
#          READ(11,*)(XI(IROW,ICOL),ICOL=1,N)
#  101  CONTINUE
#       CLOSE(11)
# C
# C ECHO INPUT
# C
#       WRITE(*,*)'POWELL SEARCH METHOD FOR MINIMIZATION OF F(X)'
#       WRITE(*,*)'INITIAL STARTING VECTOR'
#       WRITE(*,1990)(P(I),I=1,N)
#       WRITE(*,*)'INITIAL ORTHOGONAL SEARCH DIRECTION SET'
#       DO 102 IROW=1,N
#          WRITE(*,1990)(XI(IROW,ICOL),ICOL=1,N)
#  102  CONTINUE
#       FRET=FUNC(P)
#       WRITE(*,*)'INITIAL FUNCTION VALUE =',FRET
# C
#  1990 FORMAT(1X,10(G12.6,1X))
# C
# C BEGIN SEARCH
# C
#       WRITE(*,*)'BEGINNING SEARCH -- COMMAND ESCAPE TO ABORT'
#       CALL POWELL(P,XI,N,NP,FTOL,ITER,FRET)
#       WRITE(*,*)'NORMAL EXIT FROM POWELL SEARCH METHOD'
#       WRITE(*,*)'ITERATIONS REQUIRED =',ITER
#       WRITE(*,*)'FUNCTION TOLERANCE  =',FTOL
#       WRITE(*,*)'POLICY VECTOR UPON EXIT'
#       WRITE(*,1990)(P(I),I=1,N)
#       WRITE(*,*)'FUNCTION VALUE UPON EXIT =',FRET
# C
#       STOP
#       END
# C
#       SUBROUTINE POWELL(P,XI,N,NP,FTOL,ITER,FRET)
# C
# C POWELL.F FROM NUMERICAL RECIPES.  MODIFIED FOR DOUBLE PRECISION ON 
# C MACINTOSH COMPUTERS BY THEODORE G. CLEVELAND MARCH-1992
# C
#       IMPLICIT REAL*8 (A-H,O-Z)
#       PARAMETER (NMAX=20,ITMAX=200)
#       DIMENSION P(NP),XI(NP,NP),PT(NMAX),PTT(NMAX),XIT(NMAX)
#       FRET=FUNC(P)
#       DO 11 J=1,N
#         PT(J)=P(J)
#  11   CONTINUE
#       ITER=0
#  1    ITER=ITER+1
#       FP=FRET
#       IBIG=0
#       DEL=0.
#       DO 13 I=1,N
#         DO 12 J=1,N
#           XIT(J)=XI(J,I)
#  12     CONTINUE
#         CALL LINMIN(P,XIT,N,FRET)
#         IF(ABS(FP-FRET).GT.DEL)THEN
#           DEL=ABS(FP-FRET)
#           IBIG=I
#         ENDIF
#  13   CONTINUE
#       IF(2.*ABS(FP-FRET).LE.FTOL*(ABS(FP)+ABS(FRET)))RETURN
# C      IF(ITER.EQ.ITMAX) PAUSE 'Powell exceeding maximum iterations.'
#       IF(ITER .EQ. ITMAX) WRITE(*,*)'POWELL MAXIMUM ITERATIONS'
#       DO 14 J=1,N
#         PTT(J)=2.*P(J)-PT(J)
#         XIT(J)=P(J)-PT(J)
#         PT(J)=P(J)
#  14   CONTINUE
#       FPTT=FUNC(PTT)
#       IF(FPTT.GE.FP)GO TO 1
#       T=2.*(FP-2.*FRET+FPTT)*(FP-FRET-DEL)**2-DEL*(FP-FPTT)**2
#       IF(T.GE.0.)GO TO 1
#       CALL LINMIN(P,XIT,N,FRET)
#       DO 15 J=1,N
#         XI(J,IBIG)=XIT(J)
#  15   CONTINUE
#       GO TO 1
#       END
# C
#       SUBROUTINE LINMIN(P,XI,N,FRET)
# C
# C LIMMIN.F FROM NUMERICAL RECIPES.  MODIFIED FOR DOUBLE PRECISION ON 
# C MACINTOSH COMPUTERS BY THEODORE G. CLEVELAND MARCH-1992
# C
#       IMPLICIT REAL*8 (A-H,O-Z)
#       PARAMETER (NMAX=50,TOL=1.D-4)
#       EXTERNAL F1DIM
#       DIMENSION P(N),XI(N)
#       COMMON /F1COM/ NCOM,PCOM(NMAX),XICOM(NMAX)
#       NCOM=N
#       DO 11 J=1,N
#         PCOM(J)=P(J)
#         XICOM(J)=XI(J)
#  11   CONTINUE
#       AX=0.
#       XX=1.
#       BX=2.
#       CALL MNBRAK(AX,XX,BX,FA,FX,FB,F1DIM)
#       FRET=BRENT(AX,XX,BX,F1DIM,TOL,XMIN)
#       DO 12 J=1,N
#         XI(J)=XMIN*XI(J)
#         P(J)=P(J)+XI(J)
#  12   CONTINUE
#       RETURN
#       END
# C
#       FUNCTION F1DIM(X)
# C
# C F1DIM.F FROM NUMERICAL RECIPES.  MODIFIED FOR DOUBLE PRECISION ON 
# C MACINTOSH COMPUTERS BY THEODORE G. CLEVELAND MARCH-1992
# C
#       IMPLICIT REAL*8 (A-H,O-Z)
#       PARAMETER (NMAX=50)
#       COMMON /F1COM/ NCOM,PCOM(NMAX),XICOM(NMAX)
#       DIMENSION XT(NMAX)
#       DO 11 J=1,NCOM
#         XT(J)=PCOM(J)+X*XICOM(J)
#  11   CONTINUE
#       F1DIM=FUNC(XT)
#       RETURN
#       END
# C
#       FUNCTION BRENT(AX,BX,CX,F,TOL,XMIN)
# C
# C BRENT.F FROM NUMERICAL RECIPES.  MODIFIED FOR DOUBLE PRECISION ON 
# C MACINTOSH COMPUTERS BY THEODORE G. CLEVELAND MARCH-1992
# C
#       IMPLICIT REAL*8 (A-H,O-Z)
#       PARAMETER (ITMAX=100,CGOLD=.3819660,ZEPS=1.0E-10)
#       A=MIN(AX,CX)
#       B=MAX(AX,CX)
#       V=BX
#       W=V
#       X=V
#       E=0.
#       FX=F(X)
#       FV=FX
#       FW=FX
#       DO 11 ITER=1,ITMAX
#         XM=0.5*(A+B)
#         TOL1=TOL*ABS(X)+ZEPS
#         TOL2=2.*TOL1
#         IF(ABS(X-XM).LE.(TOL2-.5*(B-A))) GOTO 3
#         IF(ABS(E).GT.TOL1) THEN
#           R=(X-W)*(FX-FV)
#           Q=(X-V)*(FX-FW)
#           P=(X-V)*Q-(X-W)*R
#           Q=2.*(Q-R)
#           IF(Q.GT.0.) P=-P
#           Q=ABS(Q)
#           ETEMP=E
#           E=D
#           IF(ABS(P).GE.ABS(.5*Q*ETEMP).OR.P.LE.Q*(A-X).OR. 
#      1        P.GE.Q*(B-X)) GOTO 1
#           D=P/Q
#           U=X+D
#           IF(U-A.LT.TOL2 .OR. B-U.LT.TOL2) D=SIGN(TOL1,XM-X)
#           GOTO 2
#         ENDIF
#  1      IF(X.GE.XM) THEN
#           E=A-X
#         ELSE
#           E=B-X
#         ENDIF
#         D=CGOLD*E
#  2      IF(ABS(D).GE.TOL1) THEN
#           U=X+D
#         ELSE
#           U=X+SIGN(TOL1,D)
#         ENDIF
#         FU=F(U)
#         IF(FU.LE.FX) THEN
#           IF(U.GE.X) THEN
#             A=X
#           ELSE
#             B=X
#           ENDIF
#           V=W
#           FV=FW
#           W=X
#           FW=FX
#           X=U
#           FX=FU
#         ELSE
#           IF(U.LT.X) THEN
#             A=U
#           ELSE
#             B=U
#           ENDIF
#           IF(FU.LE.FW .OR. W.EQ.X) THEN
#             V=W
#             FV=FW
#             W=U
#             FW=FU
#           ELSE IF(FU.LE.FV .OR. V.EQ.X .OR. V.EQ.W) THEN
#             V=U
#             FV=FU
#           ENDIF
#         ENDIF
#  11   CONTINUE
# C      PAUSE 'Brent exceed maximum iterations.'
#       WRITE(*,*)'BRENT MAXIMUM ITERATIONS'
#  3    XMIN=X
#       BRENT=FX
#       RETURN
#       END
# C
#       SUBROUTINE MNBRAK(AX,BX,CX,FA,FB,FC,FUNC)
# C
# C MNBRAK.F FROM NUMERICAL RECIPES.  MODIFIED FOR DOUBLE PRECISION ON 
# C MACINTOSH COMPUTERS BY THEODORE G. CLEVELAND MARCH-1992
# C
#       IMPLICIT REAL*8 (A-H,O-Z)
#       PARAMETER (GOLD=1.618034, GLIMIT=100., TINY=1.E-20)
#       FA=FUNC(AX)
#       FB=FUNC(BX)
#       IF(FB.GT.FA)THEN
#         DUM=AX
#         AX=BX
#         BX=DUM
#         DUM=FB
#         FB=FA
#         FA=DUM
#       ENDIF
#       CX=BX+GOLD*(BX-AX)
#       FC=FUNC(CX)
#  1    IF(FB.GE.FC)THEN
#         R=(BX-AX)*(FB-FC)
#         Q=(BX-CX)*(FB-FA)
#         U=BX-((BX-CX)*Q-(BX-AX)*R)/(2.*SIGN(MAX(ABS(Q-R),TINY),Q-R))
#         ULIM=BX+GLIMIT*(CX-BX)
#         IF((BX-U)*(U-CX).GT.0.)THEN
#           FU=FUNC(U)
#           IF(FU.LT.FC)THEN
#             AX=BX
#             FA=FB
#             BX=U
#             FB=FU
#             GO TO 1
#           ELSE IF(FU.GT.FB)THEN
#             CX=U
#             FC=FU
#             GO TO 1
#           ENDIF
#           U=CX+GOLD*(CX-BX)
#           FU=FUNC(U)
#         ELSE IF((CX-U)*(U-ULIM).GT.0.)THEN
#           FU=FUNC(U)
#           IF(FU.LT.FC)THEN
#             BX=CX
#             CX=U
#             U=CX+GOLD*(CX-BX)
#             FB=FC
#             FC=FU
#             FU=FUNC(U)
#           ENDIF
#         ELSE IF((U-ULIM)*(ULIM-CX).GE.0.)THEN
#           U=ULIM
#           FU=FUNC(U)
#         ELSE
#           U=CX+GOLD*(CX-BX)
#           FU=FUNC(U)
#         ENDIF
#         AX=BX
#         BX=CX
#         CX=U
#         FA=FB
#         FB=FC
#         FC=FU
#         GO TO 1
#       ENDIF
#       RETURN
#       END
# 
# ```
# Here is the function to be minimized
# 
# ```
#       FUNCTION FUNC(X)
# C234567890
#       IMPLICIT REAL*8 (A-H,O-Z)
#       DIMENSION X(*)
# C      FUNC=(3.D0/2.D0)*X(1)*X(1)+(1.D0/2.D0)*X(2)*X(2)-X(1)*X(2)-2.D0*X(1)
#       FUNC=(3.D0/2.D0)*X(1)*X(1)+(1.D0/2.D0)*X(2)*X(2)
#      1     -X(1)*X(2)-2.D0*X(1)
#       RETURN
#       END
# ```
# 
# Here is the initial values, and desired solution tolerance contained in a file named `POWELL.DAT`
# ```
#   2  0.001                       N, FUNCTION TOLERANCE
#  -2. 4.                          INITIAL STARTING VECTOR
#   1. 0.                          INITIAL BASIS
#   0. 1.
#   
# ```
# Here is the result of the program
# 
# ```
# POWELL SEARCH METHOD FOR MINIMIZATION OF F(X)
#  INITIAL STARTING VECTOR
#  -2.00000      4.00000    
#  INITIAL ORTHOGONAL SEARCH DIRECTION SET
#   1.00000      0.00000    
#   0.00000      1.00000    
#  INITIAL FUNCTION VALUE =   26.000000000000000     
#  BEGINNING SEARCH -- COMMAND ESCAPE TO ABORT
#  NORMAL EXIT FROM POWELL SEARCH METHOD
#  ITERATIONS REQUIRED =           3
#  FUNCTION TOLERANCE  =   1.0000000000000000E-003
#  POLICY VECTOR UPON EXIT
#   1.00000      1.00000    
#  FUNCTION VALUE UPON EXIT =  -1.0000000000000000     
#  ```
#  
#  Now compare to using Python packages:

# In[3]:


def func(x): # same function in FORTRAN above
    acc = (3./2.)*x[0]**2+(1./2.)*x[1]**2-x[0]*x[1]-2.*x[0]
    return acc

x0 = np.array([-2.0,4.0])
res = minimize(func, x0, method='powell',options={'disp': True})

print(res.x)


# ### Bounded Unconstrained Least Squares
# 
# An interesting unconstrained tool is a bounded least squares in `scipy`.  You can read about it at  [Bounded Least Squares](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html).  The default bounds are $-\infty,\infty$, unless set to a different range by the analyst.

# In[4]:


import numpy as np
from scipy.optimize import minimize

#Rosenbrock Function
def fun_rosenbrock(x):
    return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])
   
from scipy.optimize import least_squares
input = np.array([2, 2])
res = least_squares(fun_rosenbrock, input)

print(res)


# In[ ]:




