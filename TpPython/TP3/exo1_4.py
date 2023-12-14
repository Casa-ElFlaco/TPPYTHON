X = float(input("Entrez la valeur de X (supérieure à 1) : "))

N = 0
somme = 0

while somme <= X:
    N += 1
    somme += N

print("Le plus grand nombre N tel que la somme soit inférieure ou égale à", X, "est :", N - 1)