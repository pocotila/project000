def message(functie):
    def functie_parametru(parametru):
        if parametru == 'Alex':
            return f"{functie(parametru)} si am varsta de 15 ani"
        else:
           return functie(parametru)
    return functie_parametru

@message
def user1(nume):
    return f"Numele meu este {nume}"

print(user1('Alex'))
