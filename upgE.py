#
def omkrets(s1,s2):
    omkrets = s1 + s1 + s2 + s2
    return omkrets


def area(s1,s2):
    area = s1 * s2
    return area


#
def kvadrat(s1,s2):
    if s1 == s2:
        svar = "yes"
    else:
        svar = "no"
    return svar


#
arealista = []
s1lista = []
s2lista = []
kvadratlista = []
omkretslista = []


miniräknare = 0


#
while True:
    dank = str(input("vill du räkna j/n?:"))
    if dank == "n":
        break

    miniräknare += 1

    #Gör skriv fält kunden
    s1 =int(input("ange sida 1: "))
    s2 =int(input("ange sida 2: "))
    while True:
        try:
            h =int(input("ange höjd: "))
            break
        except:
            print("inget heltal")

    if h < 0:
        h = 1
    elif h > 10:
        h = 10

    #
    s1lista.append(s1)
    s2lista.append(s2)
    arealista.append(area(s1,s2))
    omkretslista.append(omkrets(s1,s2))
    kvadratlista.append(kvadrat(s1,s2))
    print(f"{kvadrat(s1,s2)}kvadrat")

    #
    for i in range(h + 1):
        volym = s1 * s2 * i
        print(volym)


#
for io in range(miniräknare):
    print(f"{io} beräkning1 {s1lista[io]}{s2lista[io]} är de en kvadrat? {kvadratlista[io]} area {arealista[io]} omkrets {omkretslista[io]} ")