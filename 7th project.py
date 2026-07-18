#FUNCTION :
def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(5, 10)

calc_sum(2, 10)

calc_sum(12, 17)


#another short code"
def calc_sum(a, b):

    return a + b

sum = calc_sum(5, 10)
print(sum)
###
def print_hello():
    print("hello")
    
print_hello()
#AVERAGE OF 3 NUMBERS
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(92, 27, 39)

#PARAMETERS
def cal_prod(a=4, b=2):
    print(a * b)
    return a * b

cal_prod()

#WAF to print the length of a list.
cities = ["delhi", "gurgaon", "noida", "pune"]
heroes = ["thor", "ironman", "captain", "shaktiman"]

def print_len(list):
    print(len(list))
        
print_len(cities)
print_len(heroes)

#WAF to print the elements of a list in a single line.
heroes = ["thor", "ironman", "captain", "shaktiman"]

print(heroes[0], end="\n")
print(heroes[1], end="\n")

def print_len(list):
    print(len(list))
        
def print_list(list):
    for item in list:
        print(item, end=" ")
        
print_list(heroes)
print()

#WAF to find the factorial of n.
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)
        
cal_fact(5)

#WAF to convert USD to INR
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")
    
converter(100)