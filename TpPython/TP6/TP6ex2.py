lst1 = [0, 1, 2]

# déclaration de la fonction ajouter_elt(liste, elt):
def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

lst2 = ajouter_elt(lst1, len(lst1))

print("Contenu, type et identifiant de lst1 :")
print("   Contenu :", lst1)
print("   Type    :", type(lst1))
print("   ID      :", id(lst1))

print("\nContenu, type et identifiant de lst2 :")
print("   Contenu :", lst2)
print("   Type    :", type(lst2))
print("   ID      :", id(lst2))
