#print(2 > 3)
#a = None
#if 2!= 3: #nu este egal
#    a = True
#else:
#    a = False

# print(a)

a = False
b = True
if a is False:
    print(a)

a = input('introdu un numar')
b = None
if a.isdigit() or int(a) < 100:
    b = False
elif a.isdigit():
    b = True
print(b)
