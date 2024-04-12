blokow = int(input("Wprowadź liczbę bloków: "))
wysokosc = 0
bloki_w_poziomie = 1
while blokow >= bloki_w_poziomie:
    wysokosc += 1
    blokow -= bloki_w_poziomie
    bloki_w_poziomie += 1
print("Wysokość piramidy wynosi:", wysokosc)
