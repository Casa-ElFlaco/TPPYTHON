def factorielle_for(n):
    factorielle = 1
    for i in range(1, n + 1):
        factorielle *= i
        print(f"Étape {i}: {factorielle}")
    return factorielle

def factorielle_while(n):
    factorielle = 1
    i = 1
    while i <= n:
        factorielle *= i
        print(f"Étape {i}: {factorielle}")
        i += 1
    return factorielle

n = int(input("Entrez un entier n pour calculer sa factorielle : "))

qboucle = input("Choisissez la boucle for ou la boule while : ")

if qboucle == 'for':
    resultat = factorielle_for(n)
elif qboucle == 'while':
    resultat = factorielle_while(n)
else:
    print("Le choix de la boucle n'est pas bon, choisir : 'for' ou 'while'.")

print(f"La factorielle de {n} est : {resultat}")