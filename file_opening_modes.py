class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    
    def __init__(self):
        self.__file_name = 'products.txt'

    def file_name(self):
        return self.__file_name

    def get_products(self):
        file = open(self.file_name(), 'r')
        string = ''
        for i in file.read():
            string += i
        file.close()
        return  string

    def add(self, *products):
        file = open(self.file_name(), 'r')
        content = file.read()
        file.close()
        for product in products:
            if product.name not in content:
                prod1= product.__str__()
                file = open(self.file_name(), 'a')
                file.write(prod1)
                file.write('\n')
                file.close()
            else: print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())