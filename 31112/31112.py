rok = int(input("Wprowadź rok: "))

if rok % 4 == 0:
    print("Rok zwykly")
elif rok % 100 == 0:
    print("Rok przestepny")
elif rok % 400 == 0:
    print("Rok zwykly")
elif rok < 1582:
    print("Nie w kalendarzu gregorianskim")
else:
    print("Rok przestepny")

