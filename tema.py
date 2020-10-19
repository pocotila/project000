#1.	Scrieti un program ce va numara cate caractere
# are un sir de caractere dat de utilizator.
# Aceasta numarare sa se realizeze
# cu ajutorul unui for fara a utiliza len(). La final afisati rezultatul.
#rezolvare:

#string = "Am fost la munte si am instalat cortul"
#count = 0
#for i in string:
#    count = count+1
#print("Am fost la munte si am instalat cortul=", count)

#2.	Creati un program in care utilizatorul sa introduca o adresa de email
# de formatul litere_sau_cifre@litere_sau_cifre.litere.
# Validati acest sir de caractere si informati utilizatorul de raspuns.
# @ sau .(punct) trebuie sa exista o singura data in sirul de caractere.
#explicatie: Programul trebuie sa stie (valideze) ca este adresa de email corecta,
# in cazul in care se introduce una gresita sa ii afiseze utilizatorului acest lucru.
#Iar daca adresa de email este corecta sa ii confirme acest lucru utilizatorului.


#3.	Scrieti un program care sa valideze nr de telefon al unui utilizator
# scris de la tastatura.
#conditie: sa fie numere de mobil (sa aiba 10 cifre si sa inceapa cu 0).
#rezolvare:

numar = int(input())
for i in range(numar):
    a = str(input())
    if(len(a)==10):
        if(a.isnumeric()):
            if(a[0]=="0"):
                print("Numar valid")
            else:
                print("Numar invalid")
        else:
            print("Numar invalid")
    else:
        print("Numar invalid")