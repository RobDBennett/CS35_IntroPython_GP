# lets create a class to hold our category data

class Category:
    def __init__(self, name): 
        self.name = name

    def __str__(self):
        return f"No Products in {self.name}"

#How can you represent this class data as a string? My guess is __str__
