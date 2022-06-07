import numpy as np
BK_Color = np.array([[32, 15, 19],[96, 81, 85],[207, 193, 195]])
state = np.array([[32, 15, 19],[96, 81, 85],[207, 193, 195]])
state += 100
print(BK_Color - state)

"""
(base) C:\Users\user\ALEXLEE\imgDetection_carColor\METHOD2>PYTHON 2test.py
[[0 0 0]
 [0 0 0]
 [0 0 0]]

(base) C:\Users\user\ALEXLEE\imgDetection_carColor\METHOD2>PYTHON 2test.py 
[[-100 -100 -100]
 [-100 -100 -100]
 [-100 -100 -100]]
"""

####################################################################################
"""
# STATUS: FAIL
BK_Color = [[32, 15, 19][ 96, 81, 85][207, 193, 195]]
state =  [[32, 15, 19][ 96, 81, 85][207, 193, 195]]
# Traceback (most recent call last):
#   File "2test.py", line 1, in <module>
#     BK_Color = [[32, 15, 19][ 96, 81, 85][207, 193, 195]]
# TypeError: list indices must be integers or slices, not tuple
"""

"""
BK_Color = np.array([[32, 15, 19][96, 81, 85][207, 193, 195]])
# TypeError: list indices must be integers or slices, not tuple
"""
"""
# STATUS: both SUCCESS
BK_Color = np.array([[32, 15, 19],[96, 81, 85],[207, 193, 195]])
C = [[32, 15, 19],[96, 81, 85],[207, 193, 195]]
"""



