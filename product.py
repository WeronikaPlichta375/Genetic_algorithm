class Product():
    def __init__(self, name, weight, width, hight, depth, price):
        self.name = name
        self.weight = weight
        self.space = round(width*hight*depth, 2)
        self.price = price



