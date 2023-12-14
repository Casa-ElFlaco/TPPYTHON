
heureok = False
heure_2 = 0
heure_1 = 0


while heureok == False:    
    heuredebut =int(input("Donnez l’heure de début de la location (mettre un entier) : "))
    heurefin = int(input("Donnez l’heure de fin de la location (mettre un entier) : "))
    if heuredebut > 24 or heurefin > 24 or heuredebut < 0 or heurefin < 0:
        print("Les heures doivent être comprises entre 0 et 24 !")
    elif heuredebut == heurefin: 
        print(" Attention ! L’heure de fin est la même que l’heure de début. ")        
    elif heuredebut > heurefin:
        print("« Attention ! Le début de la location est après la fin ... ")    
    else: 
        heureok = True


heuretot = heurefin - heuredebut
for i in range(heuretot):
    if (heuredebut +i+1) <= 7 or (heuredebut +i+1) >17 :
        heure_1 += 1
    else:
        heure_2 += 1
prixf = heure_1 * 1 + heure_2 * 2


print("Vous avez loué votre vélo pendant")
print("{} heure(s) au tarif horaire de 1.0 euro".format(heure_1))
print("{} heure(s) au tarif horaire de 2.0 euros".format(heure_2))
print("Le montant total à payer est de {} euro(s).".format(prixf))
