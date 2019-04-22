from OOP import Animal

#this is inheritance. we are importing the code (or properties) from the OOP.py (code) file

#creates a reptile with its own properties, as well as properties of an animal

class Reptile(Animal):


    def __init__(self):
        super().__init__()    # this line of code needs to be here to initialise as an Animal
        self.cold_blooded = True
        self.heart_chambers = [3,4]

    def seek_heat(self):
        print("need to get some sun to get that vitamin D")

    def hunt(self):
        print("wait.....wait for it....")

lizard = Reptile()
lizard.potty()              ##.potty is from the Animal class and it can be used in the Reptile class (inheritance)
lizard.hunt()
