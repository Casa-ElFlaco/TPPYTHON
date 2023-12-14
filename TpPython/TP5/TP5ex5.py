def calcul_salaire(heures_travaillees, salaire_horaire):
    seuil_1 = 160
    seuil_2 = 200

    salaire = min(heures_travaillees, seuil_1) * salaire_horaire

    if heures_travaillees > seuil_1:
        heures_sup_25 = min(heures_travaillees - seuil_1, seuil_2 - seuil_1)
        salaire += heures_sup_25 * 1.25 * salaire_horaire

    if heures_travaillees > seuil_2:
        heures_sup_50 = heures_travaillees - seuil_2
        salaire += heures_sup_50 * 1.5 * salaire_horaire

    return salaire

heures_travaillees = float(input("Veuillez entrer le nombre d'heures travaillées : "))
salaire_horaire = float(input("Veuillez entrer le salaire horaire : "))

salaire_total = calcul_salaire(heures_travaillees, salaire_horaire)

print(f"Le salaire total pour {heures_travaillees} heures travaillées est de {salaire_total} euros.")
