N = int(input("Entrez une valeur de N : "))
somme = 0

for i in range(N + 1):
    somme += i

print("La somme des",N ,"premiers entiers naturels est :", somme)