#operators

#Arithmetic operators
print(10+5*2)  #20
print(2 ** 3 ** 2) #right to left so,512
print(10 // 3) #3
print(10 % 3) #1
print(5 / 2) #2.5
print([1,2,3]+[4,5,6]) #[1,2,3,4,5,6]
print((1,2,3)+(4,5,6)) #(1,2,3,4,5,6)
#print({1,2,3}+{4,5,6}) #give error because sets cannot add
print([1,2,3] * 4) #[1,2,3,1,2,3,1,2,3,1,2,3]
print(*[1,2,43]) #unpacking the objects 1,2,43
#print([1,2,3]+(1,2,3)) #error because this two are not belong to same sequence
#print([1,2,3]+'dog') #error because this two are not belong to same sequence


#Relational and logical operators
print(10>5 and 20<30) #true
print(10>20 and 5<10) #false
print(not 1==1) #false
print(1 < 2 < 3) #True
print(1 > 2 > 3) #false
print('abc' > 'def') #false
print([1,2,3] > [1,3,4]) #false


#assighment and walrus operators
#print(a=10)    error
print(a:=10) #10
if (n:=34) > 10:
    print(n) #34


#Identity and equality
a=[1,2,3]
b=[1,2,3]
print(a==b) #true
print(a is b) #false
a='abc'
b='abc'
print(a == b) #true
print(a is b) #true
a=(1,2,3)
b=(1,2,3)
print(a == b) #true
print(a is b) #true

#membership operator
a=[1,2,3,4,5]
print(6 in a) #false
print(6 not in a) #true
print('abc' in 'abcde') #true