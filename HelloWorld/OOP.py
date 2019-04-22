class Animal:
    #define how the animal looks, by initialising
    #create methods for this class object

    def __init__(self):     # the animals will look like this, or have these features
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("BRREAAATHEE")

    def eat(self):
        print("EAT EAT EAT")

    def potty(self):
        print(".............")

cat = Animal()
cat.breathe()
cat.eat()
cat.potty()