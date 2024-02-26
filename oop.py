class Human:
    def __init__(self, nm, age, h, w, g, cntry):
        self.name = nm
        self.age = age
        self.height = h
        self.weight = w
        self.gender = g
        self.country = cntry

    def show(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height}')
        print(f'Weight: {self.weight}')

# making objects
        
h1 = Human('Ram', 23, 5.6, 67, 'M', 'Nepal')
h2 = Human('Shyam', 25, 5.5, 65, 'M', 'India')
h3 = Human('Gita', 22, 5.2, 50, 'F', 'Bhutan')

print(h1)
print(h2)
print(h3)

print(h1.name)
print(h2.name)

h1.show()
print('-'*15)
h3.show()