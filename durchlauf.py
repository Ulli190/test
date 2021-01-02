def durchlauf(satz1,satz2):
    ausgabe = ""
    while len(satz1) < len(satz2):
        satz1 += " "
    for i in range(len(satz1)):
        ausgabe = satz1[i] + "     " + satz2[i]
        print(ausgabe)
while input().upper() != "X":
    eingabe1 = input("Bitte schreiben \n:")
    eingabe2 = input("Schreibe noch etwas \n:")
    durchlauf(eingabe1, eingabe2)