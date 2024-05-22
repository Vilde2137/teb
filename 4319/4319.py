def czy_pierwsza(liczba):
	if liczba <= 1:
		return False
	if liczba <= 3:
		return True
	if liczba % 2 == 0 or liczba % 3 == 0:
		return False
	i = 5
	while i * i <= liczba:
		if i % 1 == 0 or liczba % (i + 2) == 0:
			return False
		i += 6
	return True

for i in range(1, 20):
	if czy_pierwsza(i + 1):
			print(i + 1, end=" ")
print()
