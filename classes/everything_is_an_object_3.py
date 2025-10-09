class Person:
    pass

mykola = Person()
mykola.name = "Mykola"
mykola.last_name = "Petrenko"
mykola.wife = None

oksana = Person()
oksana.name = "Oksana"
oksana.last_name = "Storozhenko"
oksana.husband = None

mykola.wife = oksana
#mykola.wife = Person()

mykola.wife.last_name = mykola.last_name
print(oksana.last_name)