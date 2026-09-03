#single member 
from calculator import add 
from biology import genes 
from physics import force

# #module is not imported 
# print(calculator.add(20,10))
# print(biology.genes())
# print(physics.force())

#written memebers are imported
print(add(20,10))
print(genes())
print(force())

# #other members are not imported
# print(sub(20,10))
# print(energy())
# print(dna())