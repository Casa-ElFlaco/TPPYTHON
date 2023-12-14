L1 = [0] * 3
print("a) Liste L1 :", L1)
print("   Type de L1 :", type(L1))
print("   ID de L1   :", id(L1))

print("\nb) Détails des éléments de la liste L1 :")
for element in L1:
    print(f"   Valeur : {element}, Type : {type(element)}, ID : {id(element)}")

L1[1] += 1
print("\nc) Liste L1 après modification :", L1)
print("   Type de L1 après modification :", type(L1))
print("   ID de L1 après modification   :", id(L1))

print("\nd) Détails des éléments de la liste L1 après modification :")
for element in L1:
    print(f"   Valeur : {element}, Type : {type(element)}, ID : {id(element)}")

chaine = "machaine"
print("\ne) ID de la variable 'chaine' :", id(chaine))
print("   Détails des caractères de la chaîne 'chaine' :")
for char in chaine:
    print(f"   Caractère : {char}, Type : {type(char)}, ID : {id(char)}")
