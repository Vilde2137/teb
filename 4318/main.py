from datetime import datetime

def czy_przestepny(rok):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        return True
    else:
        return False


def dni_w_miesiacu(rok, miesiac):

    if miesiac > 12:
        return None

    if czy_przestepny(rok) == True and miesiac == 2:
        return 29
    elif czy_przestepny(rok) == False and miesiac == 2:
        return 28

    if miesiac == 1 or miesiac == 3 or miesiac == 5 or miesiac == 7 or miesiac == 8 or miesiac == 10 or miesiac == 12:
        return 31
    else:
        return 30

def dzien_w_roku(rok, miesiac, dzien):

    try:
        data = datetime(rok, miesiac, dzien)
        dzien_roku = data.timetuple().tm_yday
        return dzien_roku
    except ValueError:
        return None

print(dzien_w_roku(2000, 12, 31))
