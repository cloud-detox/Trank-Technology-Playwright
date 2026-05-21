# xercise 1: Print first 10 natural numbers using while loop
# Exercise 2: Calculate sum of all numbers from 1 to a given number
# Exercise 3: Print multiplication table of a given number
# Exercise 4: Display numbers from a string using a loop
# Exercise 5: Count the total number of digits in a number

for i in range(11):
    print(i,end=" ")

a=int(input("Enter a number"))
total=0
for i in range(a+1):
    total = i + total
print(total)

num=int(input("Enter a number"))
for i in range(10+1):
    print( num * i)

a=int(input("Enter a number"))
b=str(a)
for i in b:
    print(i)

a=int(input("Enter a number"))
count=0
while a!=0:
    count+=1
    a=a//10
print(count)