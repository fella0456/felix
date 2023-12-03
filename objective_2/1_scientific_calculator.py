'''
designing a scientific calculator using:
1.Add
 -def(a,b):
 request for first number ,a= input("Enter first number")
 request for second number ,b=input("Enter second number")
 return a+b
2.Subraction
 -def(a,b):
 request for first number ,a= input("Enter first number")
 request for second number ,b=input("Enter second number")
 return a-b
3.Multiplication
 -def(a,b):
 request for first number ,a= input("Enter first number")
 request for second number ,b=input("Enter second number")
 return a*b
4.Division
 -def(a,b):
 request for first number ,a= input("Enter first number")
 request for second number ,b=input("Enter second number")
 return a\b
5.Exponential
 -def(a,b):
 request for first number ,a= input("Enter first number")
 request for second number ,b=input("Enter second number")
 return a**b
6.Square root
 -def(x):
 return math.sqrt(x)
7.Sine
 -def(x):
 request for value ,x= input("Enter value")
 return math.sin(x)
8.Cosine
 -def(x):
 request for value ,x=input("Enter value")
 return math.cos(x)
9.Tangent
 -def(x):
 request for value ,x=input("Enter value")
 return math.tan(x)
10.Factorial
 -def(x):
 request for value ,x=input("Enter value")
 return math.factorial(x)
11.logarith(base 10)
 -def(x):
 request for value ,x=input("Enter value")
 return math.log(x,base)
12.Quit

'''
import math
#Function to add numbers
numbers = []
#function to add numbers
def add_numbers(int):
 numbers = input(int("Enter numbers"))
 return("sum of numbers")
#function to subtract numbers
def subtract_numbers(int):
 numbers = input(int("Enter numbers"))
 return("difference of numbers")
#function to multiply numbers
def multiply_numbers(int):
 numbers = input(int("Enter numbers"))
 return("product of numbers")
#function to divide numbers
def divide_numbers(int):
 numbers = input("Enter numerator and denominator")
 numerator = input(int("Enter num"))
 denominator = input(int("Enter denom"))
 return ("num \ denom")
