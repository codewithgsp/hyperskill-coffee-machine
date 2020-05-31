class Pet:
    kind = 'mammal'
    n_pets = 0
    pet_names = []

    def __init__(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4


# create 3 objects
tom = Pet('dog', 'Tom')
avocado = Pet('cat', 'Avocado')
ben = Pet('fish', 'Ben')

# change the n_pets
Pet.n_pets += 3

print(tom.n_pets)
print(avocado.n_pets)
print(ben.n_pets)

# access class attribute through instances
tom.n_pets += 1
avocado.n_pets += 1
ben.n_pets += 1

print(Pet.n_pets)
print(tom.n_pets)
print(avocado.n_pets)
print(ben.n_pets)

# access class attribute - pet names from instances
tom.pet_names.append('Tom')
avocado.pet_names.append('Avocado')
ben.pet_names.append('Ben')

print(Pet.pet_names)
print(tom.pet_names)
print(avocado.pet_names)
print(ben.pet_names)

# string and integers are immutable objects and hence the instance and class attributes will be different
# lists is mutable and instance and class attributes share the same memory location.
