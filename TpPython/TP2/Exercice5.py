nb = int(input("Entrez un nombre entier : "))

if nb > 0:
    signe = "positif"
elif nb < 0:
    signe = "négatif"
else:
    signe = "zéro"

if nb % 2 == 0:
    parite = "pair"
else:
    parite = "impair"

# Afficher le résultat
if signe == "zéro":
    print(f"Le nombre est {signe} (et il est {parite})")
else:
    print(f"Le nombre est {signe} et {parite}")
