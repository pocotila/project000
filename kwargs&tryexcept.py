#def add(x, y):
#   return x + y
#
#
#print(add(2, 3))

#def functia_mea(*args):
#    return args
#
#address = ("Bucuresti", 56, 'Cluj', 'Ilfov', 'Romania')
#street, *rest = address
#print(street)
#print(rest)

#def functie_kwargs(**kwargs):
#    for x, y in kwargs.items():
#        print(x, y)
#    return kwargs
#
#
#print(functie_kwargs(city='Bucuresti', street='Pipera'))
#print(type(functie_kwargs(city='Bucuresti', street='Pipera')))

#def my_func(*args, **kwargs):
#    arguments = {
#        'args': args,
#        'kwargs': kwargs
#    }
#    return arguments
#
#
#print(my_func(1, 2, 3, 4, 5, city='Cluj', street='Strada Unirii'))

#var = None
#def myFunction():
#    global var
#    var = 20
#    return var
#
#var = 10
#print(var)
#myFunction()
#print(var)

suma = 0
try:
    suma = sum(2, 2)
    print('Hello')
except Exception as e:
    print('exceptie', e)
else:
    print('nimic')
finally:
    print('final')

#if suma == 4:
#    print('succes')


