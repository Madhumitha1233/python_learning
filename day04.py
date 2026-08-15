#String methods

#1.delete(strip,lstrip,rstrip)
a='   python is simple   '
print(a.strip()) #python is simple
print(a.lstrip()) #python is simple    
print(a.rstrip()) #   python is simple

#2.1 update(replace)
a='python is simple, python is easy, python is allrounder'
b=a.replace('python', 'java')
print(a) #python is simple, python is easy, python is allrounder
print(b) #java is simple, java is easy, java is allrounder

#2.2 update(upper,lower,swapecase,title,capitalize)
a='PYTHON is siMPle'
print(a.lower()) #python is simple
print(a.upper()) #PYTHON IS SIMPLE
print(a.swapcase()) #python IS SImpLE
print(a.title()) #Python Is Simple
print(a.capitalize()) #Python is simple

#3.1 read(count,startswith,endswith)
a='abacad'
b=a.startswith('a') 
c=a.startswith('ad')
d=a.endswith('d')
e=a.endswith('de')
f=a.count('a')
g=a.count('ad')
print(b) #True
print(c) #False
print(d) #True
print(e) #False
print(f) #3
print(g) #1

#3.2 read(find,rfind,index,rindex)
s='abacada'
print(s.find('a')) #0
print(s.find('a', 3)) #4
print(s.find('a', 4, 8)) #4
print(s.rfind('a')) #6
print(s.rfind('a', 3)) #6
print(s.rfind('a', 4, 8)) #6
print(s.index('a')) #0
print(s.index('a', 3)) #4
print(s.index('a', 4, 8)) #4
print(s.rindex('a')) #6
print(s.rindex('a', 3)) #6
print(s.rindex('a', 4, 8)) #6


#4.others(isspace,isalpha,isdigit,isalnum,isupper,islower)
#in this it only return true or false
a=' '
print(a.isspace()) #True
b= ' a'
print(b.isspace()) #False
c='aBcD'
print(c.isalpha()) #True
d='aBcD1'
print(d.isalpha()) #False
e='aBc@D'
print(e.isalpha()) #False

f='13'
print(f.isdigit()) #True 
g='12a'
print(g.isdigit()) #False

h='ABC123'
print(h.isalnum()) #True
i='AB#C2'
print(i.isalnum()) #False

j='23$U'
print(j.isupper()) #True, should be there atleast 1 uppercase letter with any element without lowercase
k='23%Ua'
print(k.isupper()) #False
l='23$u'
print(l.islower()) #True, should be there atleast 1 lowercase letter with any element without uppercase
m='23$uA'
print(m.islower()) #False

#others(split,join)
#split
a='badac'
print(a.split('a')) #[b,d,c]
b= '   '
print(b.split(' ')) #['','','','','']
c='abaca'
print(c.split('a')) #['',b,c,'']
d='iam a good person'
print(d.split())

#join
a='@'
l=[1,2,3]
t=(1,2,3)
s={1,2,3}
d={'3':1, '2':3, '3':1}
'''
print(a.join(l)) #error ,because in seq no strings are there like '1'
print(a.join(t))
print(a.join(s))
print(a.join(d)) #1@2@3
'''

