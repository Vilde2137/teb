tajny_numer = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
while True:
    numer = int(input())
    if numer == tajny_numer:
        print("essssssa")
        break
    else:
        print("nie essa")
