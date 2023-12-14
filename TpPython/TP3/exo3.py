import random

devine = random.randint(0, 100)

tentatives = 0

while True:
    tentativejoueur = int(input("Devinez la valeur entre 0 et 100 : "))
    
    tentatives = tentatives + 1

    if tentativejoueur < devine:
        print("La valeur à deviner est plus grande.")
    elif tentativejoueur > devine:
        print("La valeur à deviner est plus petite.")
    else:
        print("Bravo ! Vous avez deviné la valeur en", tentatives, "tentatives.")
        break