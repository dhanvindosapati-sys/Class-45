class parrot:

    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blue = parrot("Blue", 10)
woodstock = parrot("Woodstock", 6)

print("Blue is a", blue.species)
print("Woodstock is also a", woodstock.species)
print("Blue is", blue.age, "years old")
print("Woodstock is", woodstock.age, "years old")
