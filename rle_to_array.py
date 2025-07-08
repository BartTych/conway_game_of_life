import re
import numpy as np

def rle_to_numpy_array(rle_str):
    header_lines = [line for line in rle_str.strip().splitlines() if line.startswith('x')]
    match = re.search(r'x\s*=\s*(\d+),\s*y\s*=\s*(\d+)', header_lines[0])
    width, height = int(match.group(1)), int(match.group(2))

    data_lines = [line.strip() for line in rle_str.strip().splitlines() if not line.startswith(('#', 'x'))]
    pattern = ''.join(data_lines)

    array = np.zeros((height, width), dtype=int)
    x = y = 0
    num = ''

    for char in pattern:
        if char.isdigit():
            num += char
        elif char in 'bo':
            count = int(num) if num else 1
            if char == 'o':
                array[y, x:x+count] = 1
            x += count
            num = ''
        elif char == '$':
            count = int(num) if num else 1
            y += count
            x = 0
            num = ''
        elif char == '!':
            break
    return array