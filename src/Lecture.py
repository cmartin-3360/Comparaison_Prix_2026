import pandas as pd

class Lecture:
    """
    Entrées: nom_fichier_un et nom_fichier_deux
    Sorties: Un tuple contenant deux dictionnaires représentant les informations des deux fichiers
    But: Retourner les deux dictionnaires voulant être traiter tout en gérant les fichiers incompatible pour notre programme
    """
    @staticmethod
    def lire(nom_fichier_un, nom_fichier_deux):
        dictionnaire_un = Lecture.__lire_excel_csv_autre(nom_fichier_un)
        dictionnaire_deux = Lecture.__lire_excel_csv_autre(nom_fichier_deux)
        dictionnaires = (dictionnaire_un, dictionnaire_deux)
        return dictionnaires

    """
    Entrées: nom_fichier
    Sorties: Dictionnaire contenant l'information du fichier sous forme "item":prix
    But: Lire un fichier en fonction de son type avec son nom
    """
    @staticmethod
    def __lire_excel_csv_autre(nom_fichier): # Méthode static et "privée"
        if ".xlsx" in nom_fichier:
            return Lecture.__lire_xlsx(nom_fichier)
        elif ".csv" in nom_fichier:
            return Lecture.__lire_csv(nom_fichier)
        else: # erreur gérer dans interaction, mis au cas ou
            return {} # retourne un dictionnaire vide si le type de fichier n'est pas compatible avec notre programme

    """
    Entrées: nom_fichier
    Sorties: Un dictionnaire contenant des items(String) comme clé et un prix(float) comme valeur
    But: Lire un fichier excel et retourner de l'information pertinente pour traiter sous forme d'un dictionnaire
    """
    @staticmethod
    def __lire_xlsx(nom_fichier): # Méthode static et "privée"
        item_prix = {} # création d'un dictionnaire item_prix vide
        try:
            with pd.ExcelFile(nom_fichier) as excel:
                lecture_excel = pd.read_excel(excel)
                for group in lecture_excel.values:
                    item_prix[group[0]] =group[2]
        except OSError:
            print(f"Erreur : Le fichier {nom_fichier} est introuvable.")
        except:
            print(f"Erreur de leture du fichier: {nom_fichier}")
        return item_prix

    """
    Entrées: nom_fichier
    Sorties: Un dictionnaire contenant des items(String) comme clé et un prix(float) comme valeur
    But: Lire un fichier CSV et retourner de l'information pertinente pour traiter sous forme d'un dictionnaire.
    """
    @staticmethod
    def __lire_csv(nom_fichier) : # Méthode static et "privée"
        item_prix = {} # dictionnaire dans lequel les articles seront stocké
        try:
            with open(nom_fichier, "r") as fichier :
                next(fichier) # skip la prémière ligne du fichier csv
                lignes = fichier.readlines() # retourne une liste où chaque élément est une ligne.
                for ligne in lignes:
                    valeurs = ligne.strip().split(",")
                    item_prix[valeurs[0]] =valeurs[2]
        except FileNotFoundError :
            print(f"Erreur : Le fichier {nom_fichier} est introuvable.")
        except:
            print(f"Erreur de leture du fichier: {nom_fichier}")
        return item_prix

