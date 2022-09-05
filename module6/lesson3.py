import numpy as np

even_no = np.arange(1,101,2)
#print(even_no)

x = np.lcm.reduce(even_no)
print(x)