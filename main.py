from src.Ecriture import Ecriture
from src.Lecture import Lecture 
from src.Traitement import Traitement, traiter

nom_fichier = "assets/walmart_prices.csv"
nomFichier = "assets/Costco_Product_Catalog.xlsx"
info = Traitement.creer_list((40, 40.2, 8,))
dictionnaire = Lecture.lire_csv(nom_fichier)
info = str(dictionnaire)
Ecriture.ecriture_par_dessus_fichier(f"Les produits sont : {f"{info}"}")

info_excel = Lecture.lire_xlsx(nomFichier) 
info_csv = Lecture.lire_csv(nom_fichier)
search_term = input("Enter the product name to search for: ")
traiter (info_csv, info_excel, search_term)
Ecriture.ecriture_Fichier(str(info_excel))


