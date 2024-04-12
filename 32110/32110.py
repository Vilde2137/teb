slowo_uzytkownika = input()
slowo_uzytkownika = slowo_uzytkownika.upper()
wspolgloski = []

for litera in slowo_uzytkownika:
    if litera in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        wspolgloski.append(litera)
for litera in wspolgloski:
    print(litera)
