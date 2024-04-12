slowo_uzytkownika = input()
slowo_uzytkownika = slowo_uzytkownika.upper()
wspolgloski = []

for litera in slowo_uzytkownika:
    if litera in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        wspolgloski.append(litera)
slowo_bez_samoglosek = ''.join(wspolgloski)
print(slowo_bez_samoglosek)
