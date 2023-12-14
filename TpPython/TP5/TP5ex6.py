def taille_chaine(T):
    i = 0
    while T[i] != '\0' and i < 100:
        i += 1
    return i

def pourcentage_voyelles(T):
    taille = taille_chaine(T)
    
    if taille == 0:
        return 0  

    nb_voyelles = 0
    voyelles = set("aeiouAEIOU")

    for char in T[:taille]:
        if char in voyelles:
            nb_voyelles += 1

    pourcentage = (nb_voyelles / taille) * 100
    return pourcentage

def recherche_wagon(T):
    taille = taille_chaine(T)
    
    i = 0
    trouve = False

    while i <= taille - 5 and not trouve:
        if T[i:i+5] == 'wagon':
            trouve = True
        else:
            i += 1

    if trouve:
        return i
    else:
        return -1

def compter_occurrences_wagon(T):
    taille = taille_chaine(T)
    
    i = 0
    occurrences = 0

    while i <= taille - 5:
        if T[i:i+5] == 'wagon':
            occurrences += 1
            i += 5  
        else:
            i += 1

    return occurrences

T = "Il y a un wagon dans le train. Un deuxième wagon arrive."
resultat_taille = taille_chaine(T)
resultat_voyelles = pourcentage_voyelles(T)
resultat_recherche_wagon = recherche_wagon(T)
resultat_occurrences_wagon = compter_occurrences_wagon(T)

print(f"Taille de la chaîne : {resultat_taille}")
print(f"Pourcentage de voyelles : {resultat_voyelles:.2f}%")
print(f"Recherche de 'wagon' : début de la première occurrence à l'index {resultat_recherche_wagon}")
print(f"Occurrences de 'wagon' : {resultat_occurrences_wagon}")
