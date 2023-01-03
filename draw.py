from matplotlib import animation
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


plt.rcParams["figure.figsize"] = [8,8]
plt.rcParams["figure.autolayout"] = True

data2D = np.zeros((50,50))
p1 = [25,35]
data2D[p1[0],p1[1]]=50

def animate(i):
    UD = random.randrange(-1,2)
    LR = random.randrange(-1,2)
    data2D[p1[0],p1[1]]= 0
    p1[0] += UD; p1[1] += LR
    data2D[p1[0],p1[1]]=200
    im = plt.imshow(data2D)





ani = FuncAnimation(plt.gcf(), animate, interval = 1)

# plt.show()
