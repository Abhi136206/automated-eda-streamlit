def add(a, b):

    print(a + b)



add(5, 3)

def multiply(x, y):

    return x * y

result = multiply(4, 5)

print(result)
    
def greet(name = "user"):
    print("hello", name)
greet()


def student(name, age):
    print(f"My name is {name}  and i am {age} year old")
student(name = "rohan", age = 20)


def total(*numbers):
    print(sum(numbers))
    
total(10,20,30)

def info(**data):
    print(data)
    
info(name = "Rohan", age = 20, study = "AI")
def say_hello(n):

    if n == 0:      # base case

        return

    print(“Hello”)
def factorial(n):

    if n == 0 or n == 1:   # base case

        return 1

    return n * factorial(n - 1)

print(factorial(5))