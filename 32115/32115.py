c0 = int(input())
ilosc_krokow = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
        ilosc_krokow += 1
        print(c0)
    else:
        c0 = c0 * 3 + 1
        ilosc_krokow += 1
        print(c0)
print("ilosc_krokow: ", ilosc_krokow)