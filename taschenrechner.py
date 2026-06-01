def addieren(a,b):
    summe = a+b
    return summe
def subtrahieren(a,b):
    summe = a-b
    return summe
def multiplizieren (a,b):
    summe = a*b
    return summe
def dividieren (a,b):
    summe = a/b
    return summe
zahl1 = float(input("Erste Zahl eingeben: "))
operator = input("Operator wählen(+,-,*,/,)")
zahl2 = float(input("Zweite zahl wählen: "))
if operator =="+":
    summe = round(addieren(zahl1,zahl2), 2)
    print(f"Das Ergebnis lautet {summe}")
elif operator =="-":
    summe = round(subtrahieren(zahl1,zahl2), 2)
    print(f"Das Ergebnis lautet {summe}")
elif operator=="*":
    summe = round(multiplizieren(zahl1,zahl2), 2)
    print(f"Das Ergebnis lautet {summe}")
elif operator =="/":
    if zahl2==0:
        print("Diviedieren durch 0 nicht erlaubt")
    else:
        summe = round(dividieren(zahl1,zahl2), 2)
        print(f"Das Ergebnis lautet {summe}")
else:
    print("Falscher Operator")
input("Zum schließen ENTER drücken")