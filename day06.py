#SET METHODS
#create a empty dict and print its type
d={}
print(type(d))
#create a empty set and print its type
s=set()
print(type(s))
#add 5 non-sequences and 6 sequences to that set with add method
s.add(3)
s.add(3.4)
s.add(4j)
s.add(True)
s.add(None)
print(s)
print()
s.add('madhu')
# s.add([2,6]) #error,set accept only immutable datatypes
s.add((2,6))
# s.add({2,6}) #error,set accept only immutable datatypes
# s.add({1:'a',2:'b'}) #error,set accept only immutable datatypes
s.add(range(1,10))
print(s)
print()
#add 5 non-sequences and 6 sequences with update method
s=set()
# s.update(3)  #update method cannot accept non-sequences
# s.update(3.5)
# s.update(6j)
# s.update(True)
# s.update(None)
# print(s)
s.update('madhu')
s.update([2,4],(7,8))
s.update((2,4))
s.update({2,4})
s.update({1:'a',2:'b'})
print(s)
print()


#print a set and remove first element from that set
print(s)
s.pop()
print(s)
print()


#remove one existing and one non-existing element from that set
s.remove('m') #error ,element not found
# print(s)
# s.remove(9)
# print(s) #error,keyerror because 9 not found in set
print(s)


#discard one existing and one non-existing element from that set
s.discard(3.4)
print(s)
s.discard(100) #not throw any error if element not found also
print(s)
print()


#remove all elements from the set
s.clear()
print(s)
print()


#create a set {1,2,3,4}, a list [3,4,5,6]. 
s={1,2,3,4}
l=[3,4,5,6]
#write union of set and list
print(s.union(l))
#write intersection of set and list
print(s.intersection(l))
#write difference of set and list
print(s.difference(l))
#write symmetric difference of set and list
print(s.symmetric_difference(l))
print()

#use union, intersection, difference, symmetric difference operators on set and another set. try to change second type of list and see outputs
s1={1,2,3,4}
s2={1,2,5,6}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)
print()

#DICT METHODS
#create a empty dict
d={}
#update dict with another dict
d.update({'a':1,'b':2})   
print(d)
#extend dict with another list
# d.update([1,2])
d.update([[1,'a'],[2,'b']]) #actual list is error ,it accepts only key,valye pairs
print(d)
#extend dict with another tuple
d.update(((1,'a'),(2,'b')))
print(d) 
print()
#extend dict with another set
# d.update({1,2}) #error,because no key value pair
# print(d)


#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d={1:'a', 2:'b', 3:'c', 4:'d'}
#remove the pair with key 4
d.pop(4)
print(d)
#remove the pair with key 100
# d.pop(100) #error 100 not found in d
#remove the pair with key 100 if not there return 'z'
print(d.pop(100, 'Z'))
print(d)
print()

#remove the last pair
d.popitem()
print(d)
#remove all elements from the dict
d.clear()
print(d)
print()

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d={1:'a', 2:'b', 3:'c', 4:'d'}
#get the value of key 4
print(d.get(4))
#get the value of key 100
print(d.get(100)) #if element not found return none
#get the value of key 100, if key is not present get 'z'
print(d.get(100, 'Z'))
print()

#get the value of key 4 with setdefault
d={1:'a', 2:'b', 3:'c', 4:'d'}
print(d.setdefault(4))
print(d)
#get the value of key 100 with setdefault
print(d.setdefault(100)) #if element not found add value and none to dict
print(d)
#get the value of key 100 with setdefault, if key is not there add 101 with 'z'
print(d.setdefault(101, 'Z' )) #when element not found if we give second element it  add value and 2nd value todict
print(d)
print()

#get all keys of dict and print its type
print(d.keys())
print(type(d))
#get all values in dict and print its type
print(d.values())
print(type(d))
#get all items in dict and print its type
print(d.items())
print(type(d))


