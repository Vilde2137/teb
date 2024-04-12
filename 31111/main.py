dochod = float(input("Wprowadź swój roczny dochód: "))

if dochod <= 0:
    podatek = 0
if dochod <= 85528:
    podatek = dochod * 0.18 - 556.02
else:
    podatek = 14839.02 + (dochod - 85528) * 0.32

podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)
