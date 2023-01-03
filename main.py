import numpy as np
import random
import csv
import sys
import matplotlib
from matplotlib import animation
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from games import  *
from PlayerClasses import *


'''      ToDo     '''
# |- Load map from csv / generate map
# |- Generate population
# |- Run simulation
# |- Display using draw

'''      Load Map From CSV     '''
map_path = '50x50-Maze-V3.csv'
map = np.genfromtxt(map_path, delimiter=",");
ref_map = np.genfromtxt(map_path, delimiter=","); # for refrencing will not be edited

# np.set_printoptions(threshold=sys.maxsize) # Allow np to print large arrays
# print(map)

'''    Generate Population & Load on Map'''
population = []

def populate(map,population):
    pos = [1,25]
    player_type = random.choices(['hg','cp','hr'], weights = (45,40,15)) # 45,40,15
    if player_type[0] == 'hg':
        population.append(HotelGuest())
    if player_type[0] == 'cp':
        population.append(CasualPlayer())
    if player_type[0] == 'hr':
        population.append(HighRoller())
        LeftRight = random.choices(['L','R'], weights = (50,50))
        population[-1].direction = LeftRight[0]
    population[-1].position = pos
    map = population[-1].LoadOnMap(map)

    return map,population

def run(map,ref_map,population):
    if map[1,1] < 20 and  map[1,25]==40:
        map,population = populate(map,population)
        map[1,1] += 1

    random.shuffle(population)
    for j in range(len(population)):
        map = population[j].exit(map,ref_map)
        map = population[j].move(map,ref_map)
        population[j].CheckForGames(ref_map)

    return map,population





'''         draw        '''
# https://matplotlib.org/stable/gallery/animation/dynamic_image.html
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

colors = ['#ffffff', '#3a892e', '#e7dec7', '#cc0010', '#ff6a40', '#ac6b40', '#3c5f5c', '#6b1c38',
          '#3c5f5c', '#ff3172', '#dd944b', '#00955c', '#ff8a35', '#a63172', '#000000']

scale = [-1, 2, 41, 51, 61, 71, 101, 251, 301, 351, 401, 451, 501, 601, 701, 1001]

cmap=matplotlib.colors.ListedColormap(colors)
norm=matplotlib.colors.BoundaryNorm(scale, len(colors))

fig, ax = plt.subplots()


ims = []
for i in range(1000):
    if i == 0:
        ax.imshow(map, cmap=cmap, norm=norm)  # show an initial one first
    map,population = run(map,ref_map,population)
    im = ax.imshow(map,cmap=cmap, norm=norm, animated=True)

    ims.append([im])

'''|--- Final Stats ---|'''
hr_satisfaction = sum([i.satisfaction for i in population if i.type == 'high-roller'])
hg_satisfaction = sum([i.satisfaction for i in population if i.type == 'hotel-guest'])
cp_satisfaction = sum([i.satisfaction for i in population if i.type == 'casual-player'])

'''print('High Roller Satisfaction: ' + str(hr_satisfaction) )
print('Hotel Guests Satisfaction: ' + str(hg_satisfaction) )
print('Casual Players Satisfaction: ' + str(cp_satisfaction))'''
print(str(hr_satisfaction),str(hg_satisfaction),str(cp_satisfaction))


ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=2000)


plt.show()
