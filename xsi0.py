import random
continua = "Da"

while continua == "Da":
    tablaDeJoc = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    mutari = 0
    # cu ce se incepe random
    if random.randint(0, 1) == 0:
        start = 'X'
    else:
        start = '0'

    # cine incepe primul random
    if random.randint(0, 1) == 0:
        primul = 'Calculator'
    else:
        primul = 'Utilizator'

    if start == 'X':
        urmator = '0'
    else:
        urmator = 'X'

    if primul == 'Calculator':
        calculator = start
        utilizator = urmator
    else:
        utilizator = start
        calculator = urmator

    rand = primul

    while mutari < 9:
        verific = True
        while verific:
            if rand == 'Calculator':
                x = random.randint(0,2)
                y = random.randint(0,2)
                if tablaDeJoc[x][y] == '_':
                    tablaDeJoc[x][y] = calculator
                    verific = False
                    rand = 'Utilizator'
                    mutari += 1
                    print(tablaDeJoc[0], f"\n{tablaDeJoc[1]}", f'\n{tablaDeJoc[2]}')
            else:
                x = int(input('Alege: '))
                y = int(input('Alege: '))
                if tablaDeJoc[x][y] == '_':
                    tablaDeJoc[x][y] = utilizator
                    verific = False
                    rand = 'Calculator'
                    mutari += 1
                    print(tablaDeJoc[0], f"\n{tablaDeJoc[1]}", f'\n{tablaDeJoc[2]}')
        # verificare daca a castigat
        if mutari > 4:
            if 'X' in tablaDeJoc[0] and not '0' in tablaDeJoc[0] and not '_' in tablaDeJoc[0]:
                print('A castigat "X"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif 'X' in tablaDeJoc[1] and not '0' in tablaDeJoc[1] and not '_' in tablaDeJoc[1]:
                print('A castigat "X"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif 'X' in tablaDeJoc[2] and not '0' in tablaDeJoc[2] and not '_' in tablaDeJoc[2]:
                print('A castigat "X"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif '0' in tablaDeJoc[0] and not 'X' in tablaDeJoc[0] and not '_' in tablaDeJoc[0]:
                print('A castigat "0"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif '0' in tablaDeJoc[1] and not '0' in tablaDeJoc[1] and not '_' in tablaDeJoc[1]:
                print('A castigat "0"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif '0' in tablaDeJoc[2] and not '0' in tablaDeJoc[2] and not '_' in tablaDeJoc[2]:
                print('A castigat "0"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            if tablaDeJoc[0][0] == 'X' and tablaDeJoc[1][0] == 'X' and tablaDeJoc[2][0] == 'X':
                print('A castigat "X"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif tablaDeJoc[0][1] == 'X' and tablaDeJoc[1][1] == 'X' and tablaDeJoc[2][1] == 'X':
                print('A castigat "X"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif tablaDeJoc[0][2] == 'X' and tablaDeJoc[1][2] == 'X' and tablaDeJoc[2][2] == 'X':
                print('A castigat "X"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif tablaDeJoc[0][0] == '0' and tablaDeJoc[1][0] == '0' and tablaDeJoc[2][0] == '0':
                print('A castigat "0"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif tablaDeJoc[0][1] == '0' and tablaDeJoc[1][1] == '0' and tablaDeJoc[2][1] == '0':
                print('A castigat "0"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif tablaDeJoc[0][2] == '0' and tablaDeJoc[1][2] == '0' and tablaDeJoc[2][2] == '0':
                print('A castigat "0"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif tablaDeJoc[0][0] == 'X' and tablaDeJoc[1][1] == 'X' and tablaDeJoc[2][2] == 'X':
                print('A castigat "X"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif tablaDeJoc[0][0] == '0' and tablaDeJoc[1][1] == '0' and tablaDeJoc[2][2] == '0':
                print('A castigat "0"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif tablaDeJoc[0][2] == 'X' and tablaDeJoc[1][1] == 'X' and tablaDeJoc[2][0] == 'X':
                print('A castigat "X"')
                continua = input('Tastati daca vreti sa continuati ')
                break
            elif tablaDeJoc[0][2] == '0' and tablaDeJoc[1][1] == '0' and tablaDeJoc[2][0] == '0':
                print('A castigat "0"')
                continua = input('Tastati daca vreti sa continuati ')
                break
    #verificare daca e egalitate
    if mutari > 9:
        print('Este egalitate')
        print(tablaDeJoc[0], f"\n{tablaDeJoc[1]}",f'\n{tablaDeJoc[2]}')
        continua = input('Tastati daca vreti sa continuati ')
