# def message(functie):
#     def functie_parametru(parametru):
#         if parametru == 'Alex':
#             return f"{functie(parametru)} si am varsta de 15 ani"
#         else:
#            return functie(parametru)
#     return functie_parametru
#
# @message
# def user1(nume):
#     return f"Numele meu este {nume}"
#
# print(user1('Alex'))

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_message(self):
        return f'Hello and welcome'

    @staticmethod
    def print_message():
        return "Hello and welcome"

    def __str__(self):
        return f"{self.print_message()} 11"

user_object = User("Andrei", 'Musat', 22)
# print(user_object.print_message())



