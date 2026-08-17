#create a list with 3 elements
l=[3,2,5]

#INSERT OPERATIONS
#appending
#add 5 types of non-sequence elements to it with append
l.append(4) #[3,2,5,4]
l.append(4.1)  #[3,2,5,4,4.1]
l.append(6j) #[3,2,5,4,4.1,6j] 
l.append(True) #[3,2,5,4,4.1,6j,True]
l.append(None) #[3,2,5,4,4.1,6j,True,None]
print(l)

#add 5 types of sequences to it with append
l1=[3,2,5]
l1.append('madhu') #[3, 2, 5, 'madhu']
l1.append([1,6]) #[3, 2, 5, 'madhu', [1, 6]]
l1.append((1,6)) #[3, 2, 5, 'madhu', [1, 6], (1, 6)]
l1.append({1,6}) #[3, 2, 5, 'madhu', [1, 6], (1, 6), {1, 6}]
l1.append({'a':1,'b':6}) #[3, 2, 5, 'madhu', [1, 6], (1, 6), {1, 6}, {'a': 1, 'b': 6}]
print(l1)


#extending
#add 5 types of non-sequence elements to it with extend
l=[3,2,1]
'''
l.extend(4) #error,TypeError: 'int' object is not iterable
l.extend(4.1)  #TypeError: 'float' object is not iterable
l.extend(6j) #TypeError: 'complex' object is not iterable
l.extend(True) #TypeError: 'bool' object is not iterable
l.extend(None) #TypeError: 'NoneType' object is not iterable
print(l)

In extend argument must me only sequence
'''
#add 5 types of sequence elements to it with extend
l=[3,2,1]
l.extend('madhu') #[3, 2, 5, 'm','a','d','h','u']
l.extend([1,6]) #[3, 2, 5, 'm','a','d','h','u', 1, 6]
l.extend((1,6)) #[3, 2, 5, 'm','a','d','h','u', 1, 6, 1, 6]
l.extend({1,6}) #[3, 2, 5, 'm','a','d','h','u', 1, 6, 1, 6, 1, 6]
l.extend({'a':1,'b':6}) #[3, 2, 1, 'm', 'a', 'd', 'h', 'u', 1, 6, 1, 6, 1, 6, 'a', 'b']
print(l)

#inserting
l=[3,2,1]
#insert an element at index 1 and print
l.insert(1,4)
#insert an element at index -1 and print
l.insert(-1,'m')
#insert an element at index 10000 and print
l.insert(10000,'b')
#insert an element at index -10000 and print
l.insert(-10000,7)
print(l)

#DELETE OPERATIONS
#create a list with 1,2,1,3,4,1
l2=[1,2,1,3,4,1]
#pop element at index 3 and print element and list
b=l2.pop(3)
print(b) #3
print(l2) #[1,2,1,4,1]
#pop last element and print element and list
a=l2.pop()
print(a) #1
print(l2) #[1,2,1,4]
#remove first 1 from list and print element and list
l2.remove(1)
print(l2) #[2,1,4]
#clear all elements in the list
l2.clear() #[]
print(l2)

#UPDATE OPERATIONS
#create a list with 3,2,1,5,4 
l=[3,2,1,5,4]
#sort the list in ascending and print
l.sort()
print(l) #[1,2,3,4,5]
#create a list with 3,2,1,5,4 
l1=[3,2,1,5,4]
#sort the list in descending and print
l1.sort(reverse=True) #[5,4,3,2,1]
print(l1)
#create a list with 3,2,1,5,4 
l2=[3,2,1,5,4]
#reverse the list and print
l2.reverse()
print(l2)

#READ OPERATIONS
#create a list with 1,2,1,3,1, 2
l=[1,2,1,3,1,2]
#find count of 1 and 2 in list
a=l.count(1)
print(a)
#find index of 1 from start
b=l.index(1)
print(b)
#find index of 1 from 2nd index
c=l.index(1,2)
print(c)
#find index of 1 from 5th index
# d=l.index(1,5)  #error ,element not found in list
# print(d)



#TUPLE
#create a tuple with 1,2,1,3,1, 2
t=(1,2,1,3,1,2)
#find count of 1 and 2 in tuple
print(t.count(1),t.count(2))
#find index of 1 from start
print(t.index(1))
#find index of 1 from 2nd index
print(t.index(1,2))
#find index of 1 from 5th index
#print(t.index(1,5)) #error
