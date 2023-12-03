
import random
from functools import reduce
"""
Requirents:
1. Generate a list of 100 random numbers
2. Use a generator to filter the numbers, selecting only the even ones
3. Use a list comprehension to calculate the square of each number in the filtered list
4. Use lambda expression and `reduce` (from the ` funtools` module) to calculate the sum of all squared numbers
5. Print the original list, the filtered list, and the final sum 


Implentation:

"""
numbers = [random.randint(1,10) for _ in range(5)]

numbers_even = (num for num in numbers if num%2==0)

numbers_squared = [num**2 for num in numbers_even]

numbers_squared_sum = reduce(lambda a,b:a+b,numbers_squared)

print(numbers)
print(numbers_squared)
print(numbers_squared_sum)

        


    
