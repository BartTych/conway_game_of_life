import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


A = np.zeros([248,248])
A[3,1] = 1
A[3,2] = 1
A[1,2] = 1
A[2,4] = 1
A[3,5] = 1
A[3,6] = 1
A[3,7] = 1



# Reinterpret with last column as the first
def calculate_next_gen(A):

    i_shift = [-1, 0, 1]
    j_shift = [-1, 0, 1]

    sum_arr = np.zeros_like(A)

    for i in i_shift:
        A_i_rotated = np.roll(A, shift=i, axis=0)
        for j in j_shift:
            if i == 0 and j == 0:
                continue
            A_i_j_rotated = np.roll(A_i_rotated, shift=j, axis=1)
            sum_arr += A_i_j_rotated

    lives_on = ((A == 1) & ((sum_arr == 2) | (sum_arr==3))).astype(int)
    becomes_alive = ((A == 0) & (sum_arr == 3)).astype(int)

    return lives_on + becomes_alive

simulation = [A]

print(f"start: \n {A}")
for n in range(20_000):
    A = calculate_next_gen(A)
    simulation.append(A)
    print(f"next gen:\n{A}")

fig, ax = plt.subplots()
scatter = ax.scatter([], [], s = 0.7)
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
