import random

class Product:

    def __init__(self,
            name: str,
            price: int = 10,
            weight: int = 20,
            flammability: float = 0.5):

        self.identifier = random.randint(1000000, 9999999)
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def stealability(self):
        if self.price/self.weight < 0.5:
            print ("Not so stealable...")
        if 0.5 <= self.price/self.weight < 1:
            print ("Kinda stealable.")
        else:
            print ("Very stealable!")

    def explode(self):
        if self.flammability*self.weight < 10:
            print ("...fizzle.")
        if 10 <= self.flammability*self.weight < 50:
            print ("...boom!")
        else:
            print ("...BABOOM!!")

class BoxingGlove(Product):
        def __init__(self, 
                name: str, 
                price: int = 10,
                weight: int = 10,
                flammability: float = 0.5):

            super().__init__(name=name,
                        price=price,
                        weight=weight,
                        flammability=flammability)

        def explode(self):
            print ("...it's a glove.")

        def punch(self):
            if self.weight < 5:
                print ("That tickles.")
            if 5 <= self.weight < 15:
                print ("Hey that hurt!")
            else:
                print ("OUCH!")