#Loops exercise
#1- print numbers 0 to 150
for i in range(0,150+1):
    print(i)
#2- Print numbers 5 to 5000 multiplies by 5  
for i in range(5,5000+1):
    if(i%5 == 0):
        print(i)    

for i in range(5,5000+1,5):
    print(i)        
#3- Multiplies by 5 and 10
for i in range(1,100+1):
    if (i%10==0):
        print("Coding Dojo")
    elif(i%5==0):
        print("Coding")
    else:
        print(i)  
#4- Odd sum
s = 0
for i in range(1,5000,2):
    s += i
print(s)
#5- Countdown
for i in range(2018,0,-4):
    print(i)
print("0")
#6- Flexible counter
lowNum=2; highNum=9; mult=3
for i in range(lowNum,highNum+1):
    if (i%mult==0):
        print(i)
#Optional - prime numbers
# Program to check if a number is prime or not

num = 407

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
num = 17
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")

for num in range(0, 100 + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)