from src.Ecriture import Ecriture
#from src.Lecture import Lecture 
from src.Traitement import Traitement 

info = Traitement.compare_products(40, 40.2, 8)
Ecriture.ecriture_Fichier(info)
Ecriture.ecriture_par_dessus_fichier(info)

