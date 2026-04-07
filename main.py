from src.Ecriture import Ecriture
from src.Lecture import Lecture 
from src.Traitement import Traitement 
from src.Interaction import Interaction
"""
    But: Fichier principal du programme qui utilise les autres classes pour faire le travail demandé par l'utilisateur
"""
try: 
    ### Interaction Utilisateur ###
    nom_fichier_un = Interaction.interagir_lecture("premier")
    nom_fichier_deux = Interaction.interagir_lecture("deuxieme")

    emplacement = Interaction.interagir_ecriture()

    ### Lecture ###
    dictionnaires = Lecture.lire(nom_fichier_un, nom_fichier_deux)

    ### Traitement ###
    info = Traitement.traiter(dictionnaires[0], dictionnaires[1])

    ### Ecriture ###
    Ecriture.ecrire(info, emplacement) # ecrit dans deux.txt

    print("="*30 + "Fin du programme" + "="*30)
except KeyboardInterrupt: # Si ctrl+C(interruption par clavier du programme)
    print(" \n ====== Fin du programme =====")



