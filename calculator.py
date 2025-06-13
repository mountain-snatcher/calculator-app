import math

while True:
    try:
        x = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        y = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")


def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def divide(x,y):
    if y==0:
        print("Invalid choice")
    else:
        return x/y

def multiply(x,y):
    return x*y

def square_root(x):
    return x**(1/2)

def cube_root(x):
    return x**(1/3)

def natural_log(x):
    return math.log(x)

def reciprocal(x):
    return 1/x

def square(x):
    return x**2

while True:
    print("\n WELCOME TO THE CALCULATOR")
    print("Press 1 to do Adition")
    print("Press 2 to do Subtraction")
    print("Press 3 to do Division")
    print("Press 4 to do Multiplication")
    print("Press 5 to find the square root")
    print("Press 6 to find the cube root")
    print("Press 7 to find natural log")
    print("Press 8 to find Reciprocal")
    print("Press 9 to find Square")
    print("Press 10 to exit")

    choice = int(input ("Enter your choice here:"))

    
    if choice==1:
        print("addition is:",add(x,y))
    elif choice==2:
        print("subtraction is:",subtract(x,y))
    elif choice==3:
        print("division is:",divide(x,y))
    elif choice==4:
        print("multiplication is:",multiply(x,y))
    elif choice==5:
        print("square root of first number is:",square_root(x))
    elif choice==6:
        print("cube root of first number is:",cube_root(x))
    elif choice==7:
        print("natural log of first number is:",natural_log(x))
    elif choice==8:
        print("reciprocal of first number is:",reciprocal(x))
    elif choice==9:
        print("square of first number is:",square(x))
    elif choice==10:
        print("exiting the calculator")
        break
    else:
        print("Invalid Choice. Please Try again")






    
    
    