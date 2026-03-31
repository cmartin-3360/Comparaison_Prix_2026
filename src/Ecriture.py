import os
class Ecriture:
    """
    Entrées: nom_fichier, sous le format nom.extension
    Sorties: String, qui représente le nom complet de l'emplacement du fichier à utiliser
    But: Identifier l'emplacement complet d'un fichier voulant être créer, et créer un dossier "data" si n'existe pas déjà à l'endroit indiquer
    """
    @staticmethod
    def __emplacement_fichier(nom_fichier): # Méthode static et "privée"
        emplacement_actuel = os.path.dirname(os.path.abspath(__file__))
        emplacement_projet = os.path.dirname(emplacement_actuel)
        emplacement_data = os.path.join(emplacement_projet, "data")
        os.makedirs(emplacement_data, exist_ok=True)
        return os.path.join(emplacement_data, nom_fichier)

    #TODO: Supprimer(16-27) si reste un code mort
    """
    Entrées: info
    Sorties: Aucune
    But: Écrire à la fin du fichier ce qui correspond à la varaible info à l'emplacement fichier
    """
    @staticmethod
    def ecriture_Fichier(info):
        fichier = Ecriture.__emplacement_fichier("ecriture.txt")
        with open(fichier, "a") as fichier:
            fichier.write(info)
            fichier.write("\n")

    """
    Entrées: info
    Sorties: Aucune
    But: Écrire par-dessus le fichier ce qui correspond à la varaible info à l'emplacement fichier
    """
    @staticmethod
    def ecriture_par_dessus_fichier(info):
        fichier = Ecriture.__emplacement_fichier("deux.txt")
        with open(fichier, "w") as fichier:
            fichier.write(info)
            fichier.write("\n")

