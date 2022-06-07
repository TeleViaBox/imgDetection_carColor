# STATUS: SUCCESS
"""
# (base) C:\Users\user\ALEXLEE\imgDetection_carColor\METHOD2>PYTHON array.py
[1 2 3 4 5 6]
[[1 2]
 [3 4]
 [5 6]]
2

""""

import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
# px = a[0,2]
print(b)
px = b[0,1]
print(px)

# blue = b[0,0,2]
