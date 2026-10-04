import random
from SuperclassPets import Pets, Dog, Cat
# The actual output that displays
def show_pets(pets):
    print("PETS")
    print("--------------------------------------------------------------------------")
    print("Description:", pets)
    print("Life stage:", pets.life_stage())
    print("--------------------------------------------------------------------------")

    #checks to see if the pet_type is dog or cat. and if it is, then it will output what specific breed it is
    if isinstance(pets, Dog):
        print("BREED")
        print("-------------------------------------------------------------------------")
        print(Dog.getDescription(pets))

    if isinstance(pets, Cat):
        print("BREED")
        print("--------------------------------------------------------------------------")
        print(Cat.getDescription(pets))
    
#main function
def main():
    print("--------------------------------------------------------------------------")
    print("WELCOME TO MY PETS PROGRAM!")
    print("--------------------------------------------------------------------------")
    
    #Creating objects of all of my pets
    pet1 = Pets("Hamster", "Jack", 1,)
    pet2 = Dog("Dog", "Jasmine", 2, "Pitbull mixed w/Lab")
    pet3 = Cat("Cat", "Frisky", 1, "British Shorthair")
    pet4 = Pets("Betta Fish", "Fishy", 1,)
    pet5 = Dog("Dog", "Zeus", 6, "Pitbull")
    pet6 = Dog("Dog", "Duke", 8, "Rottweiler")
    pet7 = Cat("Cat", "Milo", 2, "Tabby")
    pet8 = Pets("Rabbit", "Thumper", 2)
    pet9 = Pets("Parrot", "Kiwi", 5)
    pet10 = Pets("Goldfish", "Bubbles", 1)

    #list of pets
    pets_list = [pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10]

    #randomly selected pet
    random_pet = random.choice(pets_list)

    show_pets(random_pet)
    

if __name__ == "__main__": 
    main()
        
