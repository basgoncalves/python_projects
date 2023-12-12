# owner proof numeber
# ownerproof-3702452-1701787635-47877ea1e020

import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join( dir_path, 'day1.txt')

sum_all = int()
with open(filename) as topo_file:
    for line in topo_file:
        pattern = r'\d\one\two'
        numbers = re.findall(pattern, line)
        print(numbers[0],numbers[-1])
        number_line = int(str(numbers[0]) + str(numbers[-1]))
        sum_all = sum_all + number_line
        break

print(sum_all)