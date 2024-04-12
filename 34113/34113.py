
beatles = []
print("Krok 1:", beatles)

newList = ["John Lennon", "Paul McCartney", "George Harrison"] #nie wiem po kiego grzyba trzeba tu uzyc append
beatles.extend(newList)
print("Krok 2:", beatles)

for i in range(2):
    beatles.append((input()))
print("Krok 3:", beatles)
del beatles[4]
del beatles[3]
print("Krok 4:", beatles)

beatles.insert(3, "Ringo Starr")
print("Krok 5:", beatles)


# Sprawdzanie długości listy.
print("The Fab", len(beatles))
