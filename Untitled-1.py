kilometr = input()
metr = int(kilometr) * 1000
centymetr = int(metr) * 100 * 1000
milimetr = int(centymetr) * 10
mila = float(kilometr) * 0.6214
stopa = float(metr) * 3.28
cal = float(centymetr) * 0.39
print(f"{kilometr} kilometrow to: {metr} metrow, {centymetr} centymetrow, {milimetr} milimetrow, {mila} mil, {stopa} stop, {cal} cali")