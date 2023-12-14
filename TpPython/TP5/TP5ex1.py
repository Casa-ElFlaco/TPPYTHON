def afficher_nom_prenom(nom, prenom):
    print(f"{prenom.capitalize()} {nom.upper()}")

nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")

nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")

if (nom1, prenom1) < (nom2, prenom2):
    afficher_nom_prenom(nom1, prenom1)
    afficher_nom_prenom(nom2, prenom2)
else:
    afficher_nom_prenom(nom2, prenom2)
    afficher_nom_prenom(nom1, prenom1)

