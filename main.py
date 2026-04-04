from src.Ecriture import Ecriture
from src.Lecture import Lecture 
from src.Traitement import Traitement 
from src.Interaction import Interaction

### Interaction Utilisateur ###
nom_fichier_un = Interaction.interagir_lecture("premier")
nom_fichier_deux = Interaction.interagir_lecture("deuxieme")

emplacement = Interaction.interagir_ecriture()
### Lecture ###
dictionnaires = Lecture.lire(nom_fichier_un, nom_fichier_deux)

### Traitement ###
#informations = Traitement.traiter(dictionnaires)
#informations = str(informations) #securite
search_term = input("Enter the product name to search for: ")
informations = Traitement.traiter(dictionnaires[0], dictionnaires[1], search_term)
info_temp = str(dictionnaires[0])


### Ecriture ###
Ecriture.ecriture_par_dessus_fichier(f"Les produits sont : {info_temp}", emplacement) # ecrit dans deux.txt

print("="*30 + "Fin du programme" + "="*30)



