class Calculator:
    def __init__(self):
        self.numarul1 = int(input("nr1"))
        self.numarul2 = int(input("nr2"))
        self.operatie = input("alege operatia")

    def metoda_adunare(self):
        rezultat = self.numarul1 + self.numarul2
        return str(rezultat)

    def metoda_scadere(self):
        rezultat = self.numarul1 - self.numarul2
        return str(rezultat)

    def metoda_impartire(self):
        rezultat = self.numarul1 / self.numarul2
        return str(rezultat)

    def metoda_inmultire(self):
        rezultat = self.numarul1 * self.numarul2
        return str(rezultat)

    def __str__(self):
        if self.operatie == "+":
           return self.metoda_adunare()
        elif self.operatie == "-":
            return self.metoda_scadere()
        elif self.operatie == "*":
            return self.metoda_inmultire()
        elif self.operatie == "/":
            return self.metoda_impartire()
#
# def check()-> int:
#     utilizator = input("Da primul numar")
#     while utilizator.isdigit() == False:
#         utilizator = input("Da primul numar")
#         return int(utilizator)
#
#
# def check2() -> int:
#     utilizator = input("Da al doilea  numar")
#     while utilizator.isdigit() == False:
#         utilizator = input("Da al doilea numar")
#         return int(utilizator)


# utilizator1 = check()
# utilizator2 = check2()


def choice():
    choice = True
    while choice:
        obj_calc1 = Calculator()
        choice = input("Vrei sa faci o alta operatie? Y/N").upper()
            if choice == "N":
                cond = False
            print(obj_calc1)

# def functie_alege_operatie():
#     cond = True
#     while cond:
#         print("""
#                     1. Adunare
#                     2. Scadere
#                     3. Inmultire
#                     4. Impartire
#
#         """)
#         operatie = input("alege un numar de la 1 la 4 in functie de ce operatie doresti")
#         lista_metode = [obj_calc1.metoda_adunare(),obj_calc1.metoda_scadere,
#                         obj_calc1.metoda_inmultire, obj_calc1.metoda_impartire]
#         print(f"Operatia s-a executat cu succes. Rezultatul este: {lista_metode[int(operatie) - 1]}")
#         choice =input("Vrei sa faci o alta operatie? Y/N").upper()
#         if choice == "N":
#             cond = False
#     return True
#
#
# functie_alege_operatie()
