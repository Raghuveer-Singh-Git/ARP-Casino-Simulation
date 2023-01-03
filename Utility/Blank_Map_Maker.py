import numpy as np

map = np.random.rand(37,37)
map[0][:] = 1
map[-1][:] = 1
map[:,0] = 1
map[:,-1] = 1
print(map)

np.savetxt("data100.csv", map , delimiter = ",")

map = np.genfromtxt("data100.csv", delimiter="," )
print(map)
