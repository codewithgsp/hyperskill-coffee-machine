class Alien:
    count = 0
    places = []

    def __init__(self, planet, species):
        self.planet = planet
        self.species = species


mart = Alien("Mars", "martian")
mart.places.append("Mars")
mart.count += 1
print(mart.count)

dalek = Alien("Scaro", "dalek")
dalek.places.append("Scaro")
dalek.count += 7
print(dalek.count)
Alien.count += 2
dalek.count += 10

mee = Alien("Mee", "Mee")
print(mee.count)

print(Alien.places)
print(dalek.count)

if dalek.places == mart.places:
    print('True')
