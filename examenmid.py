# 1.
# num_calls = 0
#
# def exercitiu(x):
#     global num_calls
#     num_calls = 3
#     num_calls += 1
#     return x * x
#
# print(exercitiu(4))
#
# rezultat: 16

# 2.
# x = 1
#
# def f():
#     return x
#
# print(x)
# print(f())
#
# rezultat: 1 1

# 3.
# x = [1, 2, "hello", "world", ["another", "list"]]
#
# print(len(x[3]))
#
# rezultat: 5

# 4.
# x = (1, 2, 3)
# x[1] = 4
#
# rezultat: TypeError

# 5.
# a = [1, 2, 3]
# b = [4, 5]
#
# print(a+b*3)
#
# rezultat: [1, 2, 3, 4, 5, 4, 5, 4, 5]

# 6.
# x = [1, 2, 3, 4]
# print(x[-1:])
#
# rezultat: 4

# 7.
# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)
#
# rezultat: [0, 1, 2]

# 8.
# def exercitiu(i):
#     for i in range(i):
#         return i
#
# x = exercitiu(3)
# print(x)
#
# rezultat: 0    ??

# 9.
# a = range(10)
# y = [x*x for x in a if x%2 == 0]
# print(y)
#
# rezultat: [0, 4, 16, 36, 64]
#
# 10.
# def make_account():
#     return {'balance': 0}
#
# def deposit(account, amount):
#     account['balance'] += amount
#     return account['balance']
#
# a = make_account()
# print(deposit(a, 10))
#
# rezultat: 10

# 11.
# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#
# a = BankAccount()
# b = BankAccount()
# print(a.deposit(100))
#
# rezultat: 100

# 12.
# "foo" + 2
#
# rezultat: can only concatenate str (not "int") to str

# 13.
# try:
#     print("a")
# except:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")
#
# # rezultat: a c d

# 14.
# for k in {"x": 1, "y": 2}
#     print(k)
#
# rezultat: error

# 15.
# print(list("python"))
#
# rezultat: [‘p’, ‘y’, ‘t’, ‘h’, ‘o’, ‘n’]

# 16.
# def func(*args):
#     return 3 + len(args)
#
# print(func(4, 4, 4))
#
# rezultat: 6

# 17.
# count = (3, 2, 5, 4)
# while len(count) < 5:
#     count0 = count[0] + 1
#     print ("Hello Geek")
#
# rezultat: loop infinit in care se afiseaza Hello Geek

# 18.
# def exercitiu(var):
#     for letter in 'geeksforgeeks':
#         if letter == 'e' or letter == 's':
#             continue
#         print('Current Letter :', letter)
#         var = 10
#         return var
#
# print(exercitiu(20))
#
# rezultat: Current Letter : g    10

# 19.
# Care este diferenta intre liste si tupluri:
#
# rezultat: Listele sunt mutabile, tuplurile sunt imutabile

# 20.
# def f(a, list=[]):
#     for i in range(a):
#         list.append(i*i)
#     print(list)
#
# f(3)
# f(2, [1, 2, 3])
# f(2)
#
# rezultat: [0, 1, 4] [1,2,3,0,1] [0, 1, 4, 0,1]

# 21.
# list = ['1', '2', '3', '4', '5']
# print(list[12:])
#
# rezultat: []

# 22.
# class ClasaMea:
#     def Met1(self, a):
#             global var1
#             var1 = a
# obj=ClasaMea()
# obj.Met1("Salut Lume")
#
# rezultat: Nu returneaza eroare

# 23.
# Cum creez atributul x ce stocheaza valoarea 77777
# al obiectului obj_test123, obiect ce apartine clasei definite mai jos (Test123)?
# Obiectul nu este creat in avans.
#
# Class Test123():
#     def __str__(self):
#             self.x=77777
#             return str(self.x)
#
# rezultat: ???
# a. obj_test123=test123()
# obj_test123.y=77777
# b. test123.x=77777
# c. obj_test123=Test123()
# print obj_test123
# d. Nu pot crea atributul x deoarece interpretorul returneaza eroare

# 24.
# Ce va returna interpretorul daca apelez
# obiect1.Ad(1,2,3)ca in imaginea de mai jos?
#
# class X(object):
#     """Clasa adunare"""
#     def Ad(self, a, b, c):
#             return self.a+self.b+self.c
#
# obiect1=X()
# obiect1.Ad(1, 2, 3)
#
# rezultat: Eroare: Variabilele locale self.a, self.b si self.c nu sunt definite

# 25.
# Cum creez atributul y cu valoarea 77777 al obiectului obj_test123,
# obiect ce apartine clasei definite mai jos? Obiectul nu este creat.
#
# class test123(object):
#     def rezultat(self):
#             self.y=77777

# rezultat: ???
# a. obj_test123=test123()
#    obj_test123.rezultat()
# b. obj_test123=test123()
# c. Nu pot crea atributul y deoarece interpretorul returneaza eroare
# d. test123.y=77777

# 26.
# Ce va returna Interpretorul la rularea obiect1=X()
# ca in imaginea de mai jos?
# Cum creez un obiect in Python? Alegeti doua variante.
#
# class X(object):
#     """Clasa adunare"""
#     def Ad():
#             print("Imi place Python!")
#
# obiect1=X()
#
# rezultat = ????
# a. Interpretorul va returna eroare deoarece metoda Ad ce creaza un obiect nu are nici un parametru.
# b.  Interpretorul va returna sirul de caractere <<Imi place Python!>>.
# c. Pentru a crea un obiect al clasei X trebuie sa apelam Ad().
# d. Interpretorul nu va returna nimic si va crea obiectul obiect1

# 27.
# Ce returneaza interpretorul la rularea codului de mai jos?
#
# class Test123():
#     def __init__(self, x):
#             self.x=x
#
# obj_test123=Test123()
#
# rezultat: a. Interpretorul returneaza eroare
# deoarece metoda speciala __init__ are doi parametri
# (self,x), dar la apelare noi transmitem doar un singur parametru

# 28.
