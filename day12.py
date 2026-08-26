#while loop

#1.infinite loop
# n=4
# while n>=0:  #loop will not end
#     print('hi')
# print('bye')


#2.decrementing numbers
n=4
while n>=0:
    print('hi')
    n-=1
print('bye')
print('\n')

#3.incrementing numbers
n=4
while n<=10:
    print('hello')
    n+=1
print('bye')
print()

#4.using continue
n=4
while n<10:
    if n==6:
        n+=1
        continue
    print(n, end=' ')
    n+=1
else:
    print('Loop successful')
print()

#5.using break
n=4
while n>0:
    if n==2:
        break
    print(n, end=' ')
    n-=1
else:
    print('loop Successful')
print('\n')

#6.print  1 to 10 using while loop
n=1
while n<=10:
    print(n, end=' ')
    n+=1
print('\n')

#7.print even numbers from 1 to 10 using while loop
n=2
while n<=10:
    print(n,end=' ')
    n+=2
print('\n')

#8.print numbers divisible by both 5 and 7 from 1 to 500 using whileloop
n=1
while n<=500:
    if n%5==0 and n%7==0:
        print(n, end=' ')
    n+=1
print('\n')

#9.count no.of digits in number
n=int(input("enter a num to count digits : "))
count=0
while n>0:
    n=n//10
    count+=1
print(count)
print()


#10.reverse a number
n=int(input("enter a num for reverse a num: "))
temp=abs(n)
rev=0
while temp>0:
    last_digit=temp%10
    rev=rev*10+last_digit
    temp=temp//10
if n<0:  #if given n is -ve then this condition will execute ,if -ve then skip this condition
    rev=-rev
print(rev)
print()

#11.palindrome or not (left to right = right to left)
n=int(input("enter a num to check palindrome: "))
temp=abs(n)
rev=0
while temp>0:
    last_digit=temp%10
    rev=rev*10+last_digit
    temp=temp//10
if n<0:
    rev=-rev
if n==rev:
    print('Is a palindrome')
else:
    print('Not a palindrome')
print()

#12.armstrong number
n=int(input("enter a num to check armstrong or not: "))
temp=n
sum=0
val=len(str(n))
while temp>0:
    num=temp%10
    sum=sum+num**val
    temp=temp//10
if sum==n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
print()

#13.palindrome string without slicing,without built in functions
#method 1
rev=''
str=input('enter a string : ')
for x in range(len(str)-1,-1,-1):
    rev+=str[x]
if str==rev:
    print('palindrome')
else:
    print('Not palindrome')
print()

#method 2 palindrome string (pointers)
s=input("enter a string to check palindrome: ")
i,j=0,len(s)-1
while i<j:
    if s[i]!=s[j]:
        print("Not a palindrome")
        break
    i+=1
    j-=1
else:
    print("Palindrome")

#method 3 palindrome (slicing)
s=input("enter a string to check palindrome: ")
if s==s[::-1]:
    print("palindrome")
else:
    print("not a palindrome")