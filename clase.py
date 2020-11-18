class SuperClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Numele meu este {self.name}'

class SubClass(SuperClass):
    def __init__(self, name):
        # SuperClass.__init__(self, name)
        super().__init__(name)

    def __str__(self):
        return f"Ma numesc {self.name}"

obj = SubClass('Ovidiu')
print(obj)
