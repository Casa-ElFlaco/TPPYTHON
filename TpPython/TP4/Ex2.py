nombre_etudiants = int(input("Donnez le nombre d'étudiants : "))
moyenne = 0.0
notes = []

for i in range(nombre_etudiants):
    note = float(input(f"Entrez la note de l'étudiant {i + 1} : "))
    
    while note < 0 or note > 20:
        print("La note doit être comprise entre 0 et 20.")
        note = float(input(f"Entrez une note valide pour l'étudiant {i + 1} : "))
    
    notes.append(note)
    moyenne += note

moyenne /= nombre_etudiants

print("\nMoyenne de classe :", moyenne)

for i in range(nombre_etudiants):
    ecart = notes[i] - moyenne
    print(f"Étudiant {i + 1} : Note = {notes[i]}, Écart à la moyenne = {ecart}")
