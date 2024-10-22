import numpy as np
data = np.genfromtxt('data.txt',delimiter=',')
data = data.astype('int64')
print(data > 3)
