


class Grapes:

    def __init__(self, color, flavor, shape):
        self.color= color
        self.flavor = flavor
        self.shape = shape




    def __str__(self):#formats the method to print with just object varriable nameie f"{Green}"
        return f"{self.color} {self.flavor} {self.shape}"



GreenGrapes = Grapes("Green", "Sour", "Oval")
Red = Grapes("Red", "Sweet", "Cirle")

print (f"{GreenGrapes.color} grapes are {GreenGrapes.flavor.lower()} and {GreenGrapes.shape.lower()} in shape.")
print (f"Let's descrip these grapes: {GreenGrapes}.")


class Apples:
    
    def __init__(self, color, flavor, shape):
        self.color= color
        self.flavor = flavor
        self.shape = shape


GrannySmith = Apples("Green", "Sour", "Oblong")



print(f"What can I say about these apples: {GrannySmith.color.upper()} {GrannySmith.flavor.upper()} {GrannySmith.shape.upper()}. \n")
print (f"Just my opinion, {GrannySmith.color.upper()} apples are better than {GreenGrapes.color.upper()} grapes.")

