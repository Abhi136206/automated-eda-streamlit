#LOOPS
count = 1
while count <= 5:
    print("hello")
    count += 1
print(count)

i = 1
while i <= 5: #STOPING CONDITION
    print(i)
    i += 1
print("loop ended")

i = 5
while i >= 1:
    print(i)
    i -= 1
print("loop ended")

#PRINT THE MULTIPLICATION TABLE OF A NUMBER N.
n = int(input("enter number : "))
i = 1
while i <= 10:
    print(n * i)
    i += 1
    
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
    
#WAP TO FIND X IN TUPLE USING LOOP
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at i", i)
        i += 1

#BREAK
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
    print("end of loop")
    
#CONTINUE
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

#FOR loop
nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)
    
#PRINT THE ELEMENT OF THE FOLLOWING LIST USING A LOOP
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in list:
    print(el)
    
#SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP:
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49

idx = 0
for el in tup:
    if(el == x):
        print("number found at idx", idx)
    idx += 1
    
#RANGE
for i in range(10):#range(stop)
    print(i)
    
for i in range(2, 10):#range(start, stop)
    print(i)
    
for i in range(2, 10, 2):#range(start, stop, step)
    print(i)
    
#PRINT NUMBERS FROM 1 TO 100
for i in range(1, 101):
    print(i)
    
#PRINT NUMBERS FROM 100 TO 1
for i in range(100, 0, -1):
    print(i)
    
#PRINT THE MULTIPLICATION TABLE OF A NUMBER N
n = int(input("enter number : "))   

for i in range(1, 11):
    print(n * i)
    
#WAP to find the sum of first n numbers,
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

    print("total sum =", sum)
    
#WAP to find the factorial of first n numbers.

n = 5
fact = 1

for i in range(1, n+1):
    fact *= i
    

    print("factorial =", fact)
    
