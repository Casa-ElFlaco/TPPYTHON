def produit_scalaire(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

nMax = 3

v1 = []
v2 = []

n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))

while n < 1 or n > nMax:
    n = int(input(f"Veuillez entrer une valeur entre 1 et {nMax} : "))

print("Saisie du premier vecteur :")
v1 = [float(input(f"v1[{i}] = ")) for i in range(n)]

print("Saisie du second vecteur :")
v2 = [float(input(f"v2[{i}] = ")) for i in range(n)]

resultat = produit_scalaire(v1, v2)

print(f"Le produit scalaire de v1 par v2 vaut {resultat}")
