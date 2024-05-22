def l100kmtompg(litry):

    galonyNaKilometr = litry/ 3.785411784
    mileNaKilometr = 100 / 1.609344
    mile = mileNaKilometr / galonyNaKilometr
    return mile
def mpgtol100km(mile):

    kmNaGalon = mile * 1.609344
    litry = 3.785411784 / kmNaGalon
    litrNaStoKm = litry * 100
    return litrNaStoKm

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
