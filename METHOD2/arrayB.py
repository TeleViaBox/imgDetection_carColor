# STATUS: SUCCESS
# GOAL: I found that it is same:
"""
px = b[0][1]
px = b[0,1]
"""

import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
# px = a[0,2]
print(b)
px = b[0][1]
# px = b[0,1]
print(px)

# blue = b[0,0,2]
