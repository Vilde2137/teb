liczby_z_kapelusza = [1, 2, 3, 4, 5]  # Istniejąca lista liczb ukrytych w kapeluszu.
dlugosc_listy = len(liczby_z_kapelusza)
# Krok 1: Napisz wiersz kodu, który prosi użytkownika
# o zastąpienie środkowego numeru liczbą całkowitą wprowadzoną przez użytkownika.
liczby_z_kapelusza[dlugosc_listy//2] = int(input())
# Krok 2: Napisz tutaj wiersz kodu, który usuwa ostatni element z listy.
liczby_z_kapelusza.pop()
# Krok 3: Napisz tutaj wiersz kodu, który wypisuje długość istniejącej listy.
print(len(liczby_z_kapelusza))
print(liczby_z_kapelusza)  # Wyświetlanie zawartości listy.
