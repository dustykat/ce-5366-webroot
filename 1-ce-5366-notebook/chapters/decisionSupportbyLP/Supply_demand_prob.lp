*SENSE:Minimize
NAME          Supply-Demand-Problem
ROWS
 N  OBJ
 L  Supply_Constraints_0
 L  Supply_Constraints_1
 G  Demand_Constraints_0
 G  Demand_Constraints_1
 G  Demand_Constraints_2
 G  Demand_Constraints_3
COLUMNS
    MARK      'MARKER'                 'INTORG'
    X_11      Supply_Constraints_0   1.000000000000e+00
    X_11      Demand_Constraints_0   1.000000000000e+00
    X_11      OBJ        1.000000000000e+00
    MARK      'MARKER'                 'INTEND'
    MARK      'MARKER'                 'INTORG'
    X_12      Supply_Constraints_0   1.000000000000e+00
    X_12      Demand_Constraints_1   1.000000000000e+00
    X_12      OBJ        3.000000000000e+00
    MARK      'MARKER'                 'INTEND'
    MARK      'MARKER'                 'INTORG'
    X_13      Supply_Constraints_0   1.000000000000e+00
    X_13      Demand_Constraints_2   1.000000000000e+00
    X_13      OBJ        5.000000000000e-01
    MARK      'MARKER'                 'INTEND'
    MARK      'MARKER'                 'INTORG'
    X_14      Supply_Constraints_0   1.000000000000e+00
    X_14      Demand_Constraints_3   1.000000000000e+00
    X_14      OBJ        4.000000000000e+00
    MARK      'MARKER'                 'INTEND'
    MARK      'MARKER'                 'INTORG'
    X_21      Supply_Constraints_1   1.000000000000e+00
    X_21      Demand_Constraints_0   1.000000000000e+00
    X_21      OBJ        2.500000000000e+00
    MARK      'MARKER'                 'INTEND'
    MARK      'MARKER'                 'INTORG'
    X_22      Supply_Constraints_1   1.000000000000e+00
    X_22      Demand_Constraints_1   1.000000000000e+00
    X_22      OBJ        5.000000000000e+00
    MARK      'MARKER'                 'INTEND'
    MARK      'MARKER'                 'INTORG'
    X_23      Supply_Constraints_1   1.000000000000e+00
    X_23      Demand_Constraints_2   1.000000000000e+00
    X_23      OBJ        1.500000000000e+00
    MARK      'MARKER'                 'INTEND'
    MARK      'MARKER'                 'INTORG'
    X_24      Supply_Constraints_1   1.000000000000e+00
    X_24      Demand_Constraints_3   1.000000000000e+00
    X_24      OBJ        2.500000000000e+00
    MARK      'MARKER'                 'INTEND'
RHS
    RHS       Supply_Constraints_0   6.000000000000e+04
    RHS       Supply_Constraints_1   8.000000000000e+04
    RHS       Demand_Constraints_0   3.500000000000e+04
    RHS       Demand_Constraints_1   2.200000000000e+04
    RHS       Demand_Constraints_2   1.800000000000e+04
    RHS       Demand_Constraints_3   3.000000000000e+04
BOUNDS
 LO BND       X_11       0.000000000000e+00
 LO BND       X_12       0.000000000000e+00
 LO BND       X_13       0.000000000000e+00
 LO BND       X_14       0.000000000000e+00
 LO BND       X_21       0.000000000000e+00
 LO BND       X_22       0.000000000000e+00
 LO BND       X_23       0.000000000000e+00
 LO BND       X_24       0.000000000000e+00
ENDATA
