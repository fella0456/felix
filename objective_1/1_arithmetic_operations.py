'''
Design a Simple Calculator using;
1. Add
     def add(a,b):
        return a+b
3. Multiply
     def multiply(a,b):
        return a*b
3. Subtract
     def subtract(a,b):
        return a-b;
4. Divide
     def divide(a,b):
        return a/b;
5. Quit

'''
#Function to add numbers
number_list = []

def get_numbers():
    numbers = int(input("Number of numbers : "))
    for i in range(numbers):
        n = int(input(f"Enter number {i+1} : "))
        number_list.append(n)
    return number_list

def add(a:list):
    result= sum(a)
    return result

#Function to subtract numbers
def subract(a:list):
    result = a[0] - sum(a[1:])
    return result

#Function to multiply numbers
def multiply(a:list):
    result = 1
    for i in a:
        result = result*i
    return result

#Function to divide numbers
#a=[1,2,3,4]
def divide(a:list):
    x = a[0]
    for i in a[1:]:
        x = x/i
    return x
def operations():
    text = "please select the function below. \n1.Add numbers. \n2.Subtract numbers. \n3.Multiply.\n4.divide. "
    options = int(input(text))
    if options == 1:
        print(add(get_numbers()))
    elif options == 2:
        print(subract(get_numbers()))
    elif options == 3:
        print(multiply(get_numbers()))
    elif options == 4:
        print(divide(get_numbers()))
    else:
        print("option not defined")

while True:
    operations()
