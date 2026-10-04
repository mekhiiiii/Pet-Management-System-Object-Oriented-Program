from dataclasses import dataclass

#Superclass
@dataclass
class Pets:
    # Pets class 3 attributes
    pet_type:str = ""
    pet_name:str = ""
    pet_age:int = 0

    # life_stage method: tells the user which stage of life their pet is in based on their pets' age
    def life_stage(self):
        if self.pet_age <= 1:
             return("The pet, " + self.pet_name + ", is in its baby stage!")
        elif self.pet_age <= 7:
             return("The pet is in its adult stage!")
        elif self.pet_age > 7:
             return("The pet is in its senior stage")
        else:
              return("I can't tell you your pets' stage in life right now.")
        
     # brief description of the pet by displaying the Pets name and what type pet they are
    def getDescription(self):
        return (self.pet_name + " the " +self.pet_type)
    
    #string object that updates/changes all three attributes
    def __str__(self):
         return ("The pet, " + self.pet_name + " is a " + self.pet_type + " and is " + str(self.pet_age) + " years old!")

#subclass 1
@dataclass
class Dog(Pets):
     dog_breed:str = ""
     #overwrites Pets superclass getDescription whenever the pet_type is known as a dog
     def getDescription(self):
          getdescription = Pets.getDescription(self)
          return (getdescription + " is a " + self.dog_breed + " dog.") 

#subclass 2     
@dataclass     
class Cat(Pets):
     cat_breed:str = ""
     #overwrites Pets superclass getDescription whenever the pet_type is known as a cat
     def getDescription(self):
          getdescription = Pets.getDescription(self)
          return (getdescription + " is a " + self.cat_breed + " cat.") 