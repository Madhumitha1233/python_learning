list = [4, 3, 2, 5, 6]
#print elements in list with for each loop
for i in list:
    print(i, end=' ')
print()
print()

#print elements in list with index based for loop
for i in range(len(list)):
    print(list[i])
print()
#skip printing even numbers in list
for i in list:
    if i%2==0:
        continue
    print(i, end=' ')
print()
print()
#skip printing odd numbers in list
for i in list:
    if i%2!=0:
        continue
    print(i,end=' ')
print()
print()
#when number 2 comes stop printing  
for i in list:
    if i==2:
        break
    print(i,end=' ')
print()
print()
#when first odd number comes stop printing
for i in list:
    if i%2!=0:
        break
    print(i,end=' ')
print()
print()
#print numbers from 1 to 10, when all numbers are printed, print 'All numbers printed'
for i in range(1,11):
    print(i,end=' ')
else:
    print('All numbers printed')
print()
print()
#print numbers from 1 to 10, skipping even numbers, when all numbers are printed, print 'All numbers printed'
for i in range(1,11):
    if i%2==0:
        continue
    print(i,end=' ')
else:
    print('All numbers printed')
print()
print()
#print numbers from 10 to 1, when 5 comes stop printing, when all numbers are print, print 'All numbers printed'
for i in range(10,0,-1):
    if i==5:
        break
    print(i,end=' ')
else:
    print('All numbers printed')