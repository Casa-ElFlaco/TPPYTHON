def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    return lst

resultat_a = ajouter_elt()
print(resultat_a)

resultat_b = ajouter_elt()
print(resultat_b)

def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

resultat_d = ajouter_carac()
print(resultat_d)

resultat_e = ajouter_carac()
print(resultat_e)
