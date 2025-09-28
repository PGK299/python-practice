import random as rd
import numpy as np
num_py = np.random.random()
num = rd.randint(1, 1000)
# rounded_num_int = round(num, 4)
rounded_num_float = round(num_py, 6)
print(f"The rounded num is: {num}")
print(f"The rounded num_py is: {rounded_num_float}")