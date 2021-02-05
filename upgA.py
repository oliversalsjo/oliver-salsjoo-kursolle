#Gör skriv fält kunden
s1 =int(input("ange sida 1: "))
s2 =int(input("ange sida 2: "))

#Multiplicerar båda sidorna och får därmed ut arean
area = s1 * s2
print (area)

#Jag skapade en if sats för att kontrollera om sida 1 = sida 2 och ifall dom är samma så skrivs kvadrat ut
if s1 == s2:
    print ("kvadrat")
else:
    pass

#
for i in range(11):
    volym = s1 * s2 * i
    print(volym)