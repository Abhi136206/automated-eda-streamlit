#RECURSION
#When a function calls itself repeatedly.
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    
show(5)

#RECURSION RETURN n!
def func(n):
    if(n == 0 or n == 1):
        return 1
    return func(n-1) * n

print(func(5))
        
#WAR function to calculate the sum of first n natural number.
def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(10)
print(sum)

#WAR function to print all elements in a list
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list(idx))
    print_list(list, idx+1)
    
    fruits = ["mango", "litchi", "apple", "banana"]
    
    print_list(fruits)