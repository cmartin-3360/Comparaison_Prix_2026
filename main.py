from src.Ecriture import Ecriture
from src.Lecture import Lecture 
from src.Traitement import Traitement 

info = Traitement.creer_list((40, 40.2, 8,))
print("Le produit le plus petit est : ", info )
dictionnaire = Lecture.lecture_dict("assets/walmart_prices.csv")
info = str(dictionnaire)
Ecriture.ecriture_Fichier(f"Le produit le plus petit est : {info}")
Ecriture.ecriture_par_dessus_fichier(f"Le produit le plus petit est : {f"{info}"}")

