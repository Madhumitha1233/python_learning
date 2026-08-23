#important problems
#1.print numbers from 1 to 10
for x in range(1,11):
    print(x,end =' ')
print()
print()

list=[4,3,5,2,5,2,9,1,7,4,6,8]

#2.print even umbers from 5 to 30 and above list
for x in range(5,31):
    if x%2==0:
        print(x,end=' ')
print()
for x in list:
    if x%2==0:
        print(x,end=' ')
print('\n\n')

#3.print odd numbers from 1 to 30 and above list
for x in range(5,31):
    if x%2!=0:
        print(x,end=' ')
print()
for x in list:
    if x%2!=0:
        print(x,end=' ')
print('\n\n')

#4.print numbers divisible by 5 from 1 to 30 and above list
for x in range(1,31):
    if x%5==0:
        print(x,end=' ')
print()
for x in list:
    if x %5==0:
        print(x,end=' ')
print('\n\n')

#5.print numbers divisible  by both 5 and 7 from 1 to 100 and above list
for x in range(1,101):
    if x%5==0 and x%7==0:
        print(x,end =' ')
print()
for x in list:
    if x%5==0 and x%7==0:
        print(x,end=' ')
print('\n\n')

#6.sum of numbers from 10 to 25 and above list
sum=0
for x in range(10,26):
    sum+=x
print("Sum of numbers :" , sum)
print()
sum=0
for x in list:
    sum+=x
print("Sum of list :" ,sum)
print('\n')

#7.multiplication table of a number 
n=int(input("enter num for * : "))
for i in range(1,11):
    print(f'{n} x {i} = {n*i}')
print('\n')

#8.factorial #multiplication of 1 to n
n=int(input('enter n for factorial : '))
product=1
for x in range(1,n+1):
    product*=x
print('factorial of n is : ',product)
print('\n')

#9.fibonacci #1st time 0,2nd time 1,next sum of previous 2 terms 
n=int(input('enter no.of terms: '))
a,b=0,1
for x in range(n): #for running  loop n times,default from 0
    print(a,end=' ')
    a,b=b,a+b
print('\n')

#10.reverse a string
rev=' '
str=input('enter a string: ')
for x in range(len(str)-1,-1,-1):
    rev+=str[x]
print('reverse string:',rev)
print('\n')
#11.count vowels in a string
str=input('enter string: ')
count=0
for x in str:
    if x in 'aeiouAEIOU':
        count+=1
print(count)
print('\n')
#12.check whether a number is prime or not
num=int(input('enter a num:'))
for x in range(2,n):
    if n%i==0:
        print("Not prime")
        break
else:
    print("Prime")