def saisie_notes_coefficients():
    notes = []
    coefficients = []

    for i in range(5):
        entree = input(f"Veuillez entrer la note du module {i + 1} et le coefficient correspondant : ")
        valeurs = entree.split()
        notes.append(float(valeurs[0]))
        coefficients.append(int(valeurs[1]))

    return notes, coefficients

def calcul_moyenne_generale(notes, coefficients):
    somme = 0
    somme_coefficients = 0

    for i in range(5):
        somme += notes[i] * coefficients[i]
        somme_coefficients += coefficients[i]

    moyenne_generale = somme / somme_coefficients
    return moyenne_generale

def est_admis(moyenne_generale, notes):
    return moyenne_generale > 10 and all(note >= 8 for note in notes)

notes, coefficients = saisie_notes_coefficients()

moyenne_generale = calcul_moyenne_generale(notes, coefficients)

if est_admis(moyenne_generale, notes):
    print(f"L'étudiant est admis avec une moyenne générale de {moyenne_generale:.2f}.")
else:
    print(f"L'étudiant n'est pas admis avec une moyenne générale de {moyenne_generale:.2f}.")
