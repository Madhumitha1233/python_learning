#datatypes

#int
a=12
print(type(a))

#float
b=15.5
print(type(b))

#complex
c=7j
print(type(c))

#bool
d=False
print(type(d))

#Nonetype
e=None
print(type(e))

#string
name="madhumitha"
print(type(name))

#range
R1=range(15,30,5)
print(type(R1))

#list
L1=[4,'madhu',9.6]
print(type(L1))

#tuple
T1=(5,3,9.6,6)
print(type(T1))

#set
S={8,3,6,2,7,9}
print(type(S))

#dict
D1={'c':3,'a':1,'t':20}
print(type(D1))


#conversions
X=float(a) #int to float
print("int to float :",X)

Y=int(b) #float to int
print("float to int :",Y)

Z=str(a) #int to str
print("int to str:",Z)

'''
W=int(name) #str to int
print("str to int :",W)
'''
V=tuple(L1) #list to tuple
print("list to tuple :",V)

U=list(T1) #tuple to list
print("tuple to list :",U)

M=set(L1) #list to set
print("list to set :",M)

N=list(R1) #range to list
print("range to list :" ,N)