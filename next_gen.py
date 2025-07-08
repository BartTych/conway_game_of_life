
import numpy as np

def calculate_next_gen(A):
    """
    rule B3/S23
    """
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
