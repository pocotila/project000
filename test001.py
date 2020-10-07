# if conditie1:
#    sintaxa1
# elif conditie2:
#    sintaxa2
# else:
#    sintaxa3

# if conditie1:
#    sintaxa1
# elif conditie2:
#    sintaxa2
#...
# elif conditie4
 #   sintaxa4
# else:
#    sintaxa

# nu se recomanda if in if, if in elif etc.

a = 1
b = 2
c = 3

if a < 4:
    print(a)
elif a > b:
    print(b)
elif c < a:
    print(c)
else:
    print("Niciun rezultat gasit")
#va afisa Niciun rezultat gasit - trece prin toate conditiile si nu gaseste nicio conditie adevarata

d = None
if a < b:
   d = a + b
else:
    print(d)
