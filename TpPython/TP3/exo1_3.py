valeurs_inf_10 = 0
valeurs_10_15 = 0
valeurs_sup_15 = 0

for _ in range(10):
    valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))
    
    if 0 <= valeur < 10:
        valeurs_inf_10 += 1
    elif 10 <= valeur < 15:
        valeurs_10_15 += 1
    elif valeur >= 15:
        valeurs_sup_15 += 1

print("Nombre de valeurs inférieures à 10 :", valeurs_inf_10)
print("Nombre de valeurs entre 10 et 14.99 :", valeurs_10_15)
print("Nombre de valeurs supérieures ou égales à 15 :", valeurs_sup_15)