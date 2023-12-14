def decomposer_somme(somme):
    billets_100 = 100
    billets_50 = 50
    billets_10 = 10
    pieces_2 = 2
    pieces_1 = 1

    nb_billets_100 = somme // billets_100
    reste = somme % billets_100

    nb_billets_50 = reste // billets_50
    reste %= billets_50

    nb_billets_10 = reste // billets_10
    reste %= billets_10

    nb_pieces_2 = reste // pieces_2
    reste %= pieces_2

    nb_pieces_1 = reste // pieces_1

    print(f"{somme} euros, c'est donc {nb_billets_100} billets de 100, {nb_billets_50} billets de 50, "
          f"{nb_billets_10} billets de 10, {nb_pieces_2} pièces de 2 et {nb_pieces_1} pièce de 1.")

somme = int(input("Veuillez entrer une somme d'argent en euros : "))

decomposer_somme(somme)
