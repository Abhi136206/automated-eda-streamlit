import numpy as np
arr = np.array((1, 2, 3, 4, 5))
print(arr)
print(type(arr))

#0D array
import numpy as np
arr = np.array(43)
print(arr)

#1D array
import numpy as np
arr  = np.array([1, 2, 3, 4, 5])
print(arr)

#2D array
import numpy as np
arr = np.array([[1, 2, 3], [5, 6, 7]])
print(arr)

#3D array
import numpy as np
arr = np .array([[[1, 2, 3, 4], [3, 4, 5, 6], [6, 7, 8, 9]]])
print(arr)

#CHECK DIMENSIONS
import numpy as np
a = np.array(43)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [5, 6, 7]])
d = np .array([[[1, 2, 3, 4], [3, 4, 5, 6], [6, 7, 8, 9]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#HIGHER DIMENSIONAL ARRAY
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin = 5)
print(arr)
print("number of dimensions :", arr.ndim)