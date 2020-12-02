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




