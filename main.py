import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from next_gen import calculate_next_gen
from rle_to_array import rle_to_numpy_array as str_to_arr



rle_data = """
x = 76, y = 50, rule = B3/S23
15bo$14bobo$15bo3$9b2o$9b2o23b2o$b2o31bo$2bo29bobo$2bobo27b2o$3b2o4b2o
11b2o$9b2o11b2o$17bo$16bob2o23b2o$16bo3bo4bo17bo$20bo4bo15bobo$3bob2o
14bo3bo15b2o$b3ob2o14b2o$o18bo2b2o20b2o$b3ob2o12b2obo21b2o$3bobo24b2o$
3bobo23bo2bo$4bo25b2o$41bo$42b2o$41b2o2$71bo$70bobo$70bobo$30b2o19b2o
16b2ob3o$30b2o19b2o22bo$69b2ob3o$33b2o34b2obo$32bobo$32bo$31b2o2$65b2o
$65b2o4b2o$42b2o27bobo$41bobo29bo$41bo31b2o$40b2o23b2o$65b2o3$60bo$59b
obo$60bo!
"""

patern = str_to_arr(rle_data)
x,y = patern.shape

A = np.zeros([80,80])
A[0:x,0:y]=patern

simulation = [A]

print(f"start: \n {A}")
for n in range(20_000):
    A = calculate_next_gen(A)
    simulation.append(A)
    #print(f"next gen:\n{A}")

fig, ax = plt.subplots()
scatter = ax.scatter([], [], s = 2)
ax.set_aspect('equal')
plt.gca().set_aspect('equal')
ax.set_xlim(-0.5, simulation[0].shape[1] - 0.5)
ax.set_ylim(-0.5, simulation[0].shape[0] - 0.5)
ax.invert_yaxis()

#ax.grid(True)


# Update function for animation
def update(frame):
    matrix = simulation[frame]
    y, x = np.where(matrix == 1)
    scatter.set_offsets(np.c_[x, y])
    fig.suptitle(f'Frame: {frame}', fontsize=12)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=len(simulation), interval=25, blit=False)

plt.show()
