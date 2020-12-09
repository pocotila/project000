# class SuperClass:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'Numele meu este {self.name}'
#
# class SubClass(SuperClass):
#     def __init__(self, name):
#         # SuperClass.__init__(self, name)
#         super().__init__(name)
#
#     def __str__(self):
#         return f"Ma numesc {self.name}"
#
# obj = SubClass('Ovidiu')
# print(obj)

# class SuperClass:
#     def __init__(self):
#         self.super_variabila = 11
#
# class SubClass(SuperClass):
#     def __init__(self):
#         super().__init__()
#         self.sub_variabila = 12
#         self.super_variabila = 111
#
# obj = SubClass()
# print(obj.sub_variabila)
# print(obj.super_variabila)

#
# class SuperClass:
#     def __init__(self):
#         self.super_variabila = 11
#
#     def metoda1(self):
#         return 'superclass'
#
# class SubClass(SuperClass):
#     def __init__(self):
#         super().__init__()
#         self.sub_variabila = 12
#         self.super_variabila = 111

#     def metoda1(self):
#         return 'subclasa'
#
# obj = SubClass()
# print(obj.sub_variabila)
# print(obj.super_variabila)
# print(obj.metoda1)


# tema calculator cu functii

# class Calculator:
#     def add(self, a, b):
#         self.a = a
#         self.b = b
#         r = self.a + self.b
#         return r
# print(r)
