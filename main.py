from src.Ecriture import Ecriture
from src.Lecture import Lecture
from src.Interaction import Interaction
from src.Traitement import Traitement

### Interaction Utilisateur ###
nom_fichier_un = Interaction.interagir_lecture("premier")
nom_fichier_deux = Interaction.interagir_lecture("deuxieme")

emplacement = Interaction.interagir_ecriture()

### Lecture ###
dictionnaires = Lecture.lire(nom_fichier_un, nom_fichier_deux)

### Traitement ###
resultats = Traitement.traiter(dictionnaires)
texte_sortie = "\n".join(resultats) if resultats else "Aucun résultat de recherche."
print("\nRésultats de la recherche :")
print(texte_sortie)

### Ecriture ###
Ecriture.ecrire(texte_sortie, emplacement)

print("="*30 + "Fin du programme" + "="*30)



