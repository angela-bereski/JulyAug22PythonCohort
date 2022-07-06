# Basic
for i in range(151):
    print(i)

# Multiples of 5
for i in range(5,1001,5):
    print(i)

#Counting, the Dojo Way
for i in range(1,101):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)

#Whoa, That Sucker's Huge
sum = 0
for i in range(0,500001):
    if i%2 != 0:
        sum=sum+i
print(sum)

#Countdown by Fours
for i in range(2018,-1, -4):
    print(i)

# Flexible Counter
lowNum=1
highNum=27
mult=4
for i in range(lowNum,(highNum+1)):
    if i%mult==0:
        print(i)