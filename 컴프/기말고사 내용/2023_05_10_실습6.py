#add(), min(), mul(), div()

def add(num1, num2):
    print(num1 + num2)

def min(num1, num2):
    print(num1 - num2)

def mul(num1, num2):
    print(num1 * num2)

def div(num1, num2):
    print(num1 / num2)

a, b = map(int,input().split())
add(a,b)
min(a,b)
mul(a,b)
div(a,b)