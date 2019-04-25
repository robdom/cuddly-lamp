import math
import random
import statistics

print(math.pow(3, 3))

print(random.randint(0,30))

nums = [3, 56, 29, 18, 8, 22, 52]
print(statistics.mean(nums)) # Average
print(statistics.median(nums)) # Middle Value
print(statistics.median_high(nums))
print(statistics.median_low(nums))


import cubed

result = cubed.cube_it(3)
print(result)
