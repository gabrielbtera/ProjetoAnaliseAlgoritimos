import array as arr

import time

inicio = time.time()

a = arr.array('i', range(10_000_000))

l = list(range)

# print(a)


print(time.time()-inicio)