def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


print("Calculator app \n")
print("Enter your choice: \n 1.Addition 2.Subtraction 3.Multiplication 4.Division: \n ")
ch= int(input())
n1=int(input("Enter the first number: \n"))
n2=int(input("Enter the second number: \n"))
if ch == 1:
    print("The sum is: ",add(n1, n2))

elif ch == 2:
    print("The difference is: ",sub(n1, n2))

elif ch == 3:
    print("The product is: ",mul(n1, n2))

elif ch == 4:
    print("The division is: ",div(n1, n2))