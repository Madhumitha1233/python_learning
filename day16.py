#Iterators
#1.map(it transform elements)
#syntax:map(fuction,sequence)
a=[1,2,3,4,5]
m=map(lambda x:x**2,a)
print(m)   #give map address <map object at 0x0000.....>
seq=list(m)
print(seq)
print(type(m))   #<class map>

#2.filter(Used for selecting elements)
#syntax:filter(fuction,sequence)
a=[1,2,3,4,5]
f=filter(lambda x:x % 2 == 0,a)
print(f)    #give filter address <filter object at 0x0000.....>
l=list(f)
print(l)
print(type(f))  #<class filter>

#3.reduce(combines all elements into single value)
#syntax:functools.reduce(fuction,sequence)
import functools
l=[1,2,3,4,5]
r=functools.reduce(lambda x,y:x+y,l)
print(r)  #give direct output
print(type(r))  #<class 'int'>
print('\n')

#Generator(generate one elements at a time on demand)
#2 types(1.func with yield keyword,2.generator expression)

#1.func with yield keyword
def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
n=numbers()
print(next(n))  #yields only one element  1
print(next(n))   #2
print(n.__next__())  #3 
print()

def numbers():
    for x in range(1,11):
        if x%2==0:
            yield x
n=numbers()
print(next(n)) 
print(n.__next__())  
print(next(n))   
print(n.__next__()) 
print(n.__next__()) 
print(n.__next__())  
print()

#2.generator expression
a = (x for x in range(1, 11))
print(next(a))  #1
print(next(a))  #2
print(next(a))  #3
print(next(a))  #4
print(type(a))
print()

a=(x for x in range(1,11))
print(a)   #<generator object <genexpr> at 0x000001836A748860>
print(list(a))
print()

numbers = (x * x for x in range(5))
print(numbers) #<generator object <genexpr> at 0x000001836A748860>
print(list(numbers))
print('\n')

#list comprehension
#(shortcut of creating a list)
a=[x for x in range(1,6)]
print(a)

b=[x for x in range(1,11) if x%2==0]
print(b)
print(type(b))