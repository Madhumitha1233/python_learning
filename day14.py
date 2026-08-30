#star pattern
#1.right angle triangle
n=int(input("enter a num: "))
for i in range(1,n+1):
    print(i*' * ')
print()

#2.reverse right angle triangle
n=int(input("enter a num: "))
for i in range(n,0,-1):
    print(i*' * ')
print()

#3.pyramid
n=int(input("enter a num:"))
for i in range(1,n+1):
    print((n-i)*' '+i*'* ')
print()

#4.reverse pyramid
n=int(input("enter a num:"))
for i in range(n,0,-1):
    print((n-i)*' '+i*'* ')
print()

#5.diamond
n=int(input("enter a num:"))
for i in range(1,n+1):
    print((n-i)*' '+i*'* ')
for i in range(n-1,0,-1):
    print((n-i)*' '+i*'* ')
print()

#6.boundary pattern
n=int(input("enter a num: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()

#7.star pattern,index from 0,for only this pattern
n=int(input("enter a num: "))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 or i==j or j==n-i-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()

#printing  stars of Z
n=int(input('enter num:'))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
print()

#print hallow 
n=int(input('enter a num:'))



#numbers patten
#right angle triangle
n=int(input("enter a num: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print()
#reverse right angled
n=int(input("enter a num: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print()

#right angled with row numbers
n=int(input("enter a num: "))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=' ')
    print()
print()
#reverse right angled with row numbers
n=int(input("enter a num: "))
for i in range(n,0,-1):
    for j in range(i):
        print(i,end=' ')
    print()
print()
#right angled with all 1's
n=int(input("enter a num: "))
for i in range(1,n+1):
    for j in range(i):
        print('1',end=' ')
    print()
print()
#reverse right angled with 1's
n=int(input("enter a num: "))
for i in range(n,0,-1):
    for j in range(i):
        print('1',end=' ')
    print()
print()
#right angled with i in reverse
n=int(input("enter a num: "))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

#reverse right angled with i in reverse
n=int(input("enter a num: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
print()

#pyramid numbers
n=int(input('enter num:'))
for i in range(1,n+1):
    print((n-i)*' ',end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
#reverse pyramid numbers
n=int(input('enter num:'))
for i in range(n,0,-1):
    print((n-i)*' ',end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print()

#floyd's triangle
n=int(input('enter a num:'))
c=1
for i in range(1,n+1):
    for j in range(i):
        print(c,end=' ')
        c+=1
    print()
#reverse floyd's triangle
n=int(input('enter a num:'))
c=1
for i in range(n,0,-1):
    for j in range(i):
        print(c,end=' ')
        c+=1
    print()
print()
#pascal's triangle
n=int(input('enter a num:'))
for i in range(n):
    num=1
    for j in range(i+1):
        print(num,end=' ')
        num=num*(i-j)//(j+1)
    print()
print()

#alphabet pattern
n=int(input('enter num:'))
for i in range(1,n+1):
    print((n-i)*' ',end=' ')
    for j in range(1,i+1):
        print(chr(j+64),end=' ')
    print()
#reverse 
n=int(input('enter num:'))
for i in range(n,0,-1):
    print((n-i)*' ',end=' ')
    for j in range(1,i+1):
        print(chr(j+64),end=' ')
    print()