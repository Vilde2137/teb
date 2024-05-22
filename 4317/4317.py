def czy_przestepny(rok):

    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        return True
    else:
        return False

def dni_w_miesiacu(rok, miesiac):

    if czy_przestepny(rok) == True and miesiac == 2:
        return 29
    elif czy_przestepny(rok) == False and miesiac == 2:
        return 28

    if miesiac == 1 or miesiac == 3 or miesiac == 5 or miesiac == 7 or miesiac == 8 or miesiac == 10 or miesiac == 12:
        return 31
    else:
        return 30

testuj_lata = [1900, 2000, 2016, 1987]
testuj_miesiace = [2, 2, 1, 11]
testuj_wynik = [28, 29, 31, 30]
for i in range(len(testuj_lata)):
	r = testuj_lata[i]
	m = testuj_miesiace[i]
	print(r, m, "-> ", end="")
	wynik = dni_w_miesiacu(r, m)
	if wynik == testuj_wynik[i]:
		print("OK")
	else:
		print("Nie powiodło się")
