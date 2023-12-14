import string

def est_palindrome(chaine):
    chaine_epuree = ''.join(char.lower() for char in chaine if char.isalpha())

    return chaine_epuree == chaine_epuree[::-1]

entree = input("Veuillez entrer une chaîne de caractères : ")

if est_palindrome(entree):
    print("La chaîne est un palindrome.")
else:
    print("La chaîne n'est pas un palindrome.")
