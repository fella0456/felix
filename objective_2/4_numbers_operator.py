'''
enhanced data processing with generators and comprehensions.
1.generate random numbers
2.filter even and calculate their squares
3.additional data processing
4.calculate statistics
5.quit
'''

import random
from functools import reduce
import math

numbers = [random.randint(1,100) for _ in range(20)]

numbers_even = (num for num in numbers if num%2==0)

numbers_squared = [num**2 for num in numbers_even]

numbers_odd = (num for num in numbers if num%2!=0)

numbers_osquared = [num**2 for num in numbers_odd]

import statistics

mean_value = statistics.mean(numbers)
median_value =statistics.median(numbers)
variance_value = statistics.variance(numbers)
stedv_value = statistics.stdev(numbers)

print(numbers)
print(numbers_squared)
print(numbers_osquared)
print(mean_value)
print(median_value)
print(variance_value)
print(stedv_value)
