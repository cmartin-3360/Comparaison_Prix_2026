from src.Ecriture import Ecriture
from src.Lecture import Lecture 
from src.Traitement import Traitement 

### Interaction Utilisateur ###
nom_fichier_un = "assets/walmart_prices.csv"
nom_fichier_deux = "assets/Costco_Product_Catalog.xlsx"

### Lecture ###
dictionnaires = Lecture.lire(nom_fichier_un, nom_fichier_deux)

### Traitement ###
#info = Traitement.creer_list((40, 40.2, 8,))
#informations = Traitement.traiter(dictionnaires)
#informations = str(informations) #securite
info_temp = str(dictionnaires[0])

### Ecriture ###
Ecriture.ecriture_par_dessus_fichier(f"Les produits sont : {info_temp}") # ecrit dans deux.txt

