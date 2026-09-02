# Functions
#1.palindrome number
def palindrome_num(n):
    temp=abs(n)
    rev=0
    while temp>0:
        last_digit=temp%10
        rev=rev*10+last_digit
        temp=temp//10
    if n<0:
        rev=-rev
    if n==rev:
        return "palindrome"
    else:
        return "not palindrome"
num=int(input('enter num to check palindrome: '))
a=palindrome_num(num)
print(a)
print()
#2.palindrome string
def palindrome_str(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return 'not palindrome'
            break
        i+=1
        j-=1
    return 'palindrome'
s1=input("enter string: ")
a=palindrome_str(s1)
print(a)
print()
#3.prime number
def prime_num(n):
    if n<2:
        return 'not prime'
    for i in range(2,n):
        if n%i==0:
            return 'not prime'
    return 'prime'
num=int(input('enter a num to check prime: '))
a=prime_num(num)
print(a)
print()
#4.reverse a string
def reverse_str(s):
    a=s[::-1]
    return a
s=input('enter string to reverse: ')
x=reverse_str(s)
print(x)
print()
#5.factorial of num
def factorial_num(n):
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
    return fact
num=int(input("enter num to find factorial:"))
a=factorial_num(num)
print(a)
print()
#6.fibonacci
def fibinacci_series(n):
    a,b=0,1
    for x in range(n):
        print(a,end=' ')
        a,b=b,a+b
n1=int(input('enter series: '))
fibinacci_series(n1)
print()
#7.count no.of digits using function
def count_digits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count
num=int(input('enter a num to count: '))
a=count_digits(num)
print(a)
print()
#8.amstrong num
def amstrong_num(n):
    temp=0
    sum=0
    val=len(str(n))
    while temp>0:
        num=temp%10
        sum=sum+num**val
        temp=temp//10
    return sum==n
n=int(input('enter num'))
print(amstrong_num(n))