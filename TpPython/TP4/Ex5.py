def est_bissextile(annee):
    # Vérifie si une année est bissextile
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def est_date_valide(date):
    # Vérifie si une date est valide
    if len(date) != 8:
        return False, "Format de date incorrect. La date doit être au format jjmmaaaa."

    jour = int(date[:2])
    mois = int(date[2:4])
    annee = int(date[4:])

    if mois < 1 or mois > 12:
        return False, "Mois invalide. Le mois doit être compris entre 01 et 12."

    jours_par_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if est_bissextile(annee):
        jours_par_mois[2] = 29  

    if jour < 1 or jour > jours_par_mois[mois]:
        return False, "Jour invalide pour le mois spécifié."

    return True, "Date valide."

def saisir_date():
    while True:
        date = input("Veuillez entrer une date au format jjmmaaaa : ")
        est_valide, message = est_date_valide(date)
        if est_valide:
            return date
        else:
            print(f"Date invalide : {message}")

date_saisie = saisir_date()
print(f"La date {date_saisie} est valide.")
