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
        while not dictionnaire_un:
            nom_fichier = input(f"Le nom du fichier est invalide {nom_fichier_un}, veuillez le retapez:")
            dictionnaire_un = Lecture.__lire_excel_csv_autre(nom_fichier)
        while not dictionnaire_deux:
            nom_fichier = input(f"Le nom du fichier est invalide {nom_fichier_deux}, veuillez le retapez:")
            dictionnaire_deux = Lecture.__lire_excel_csv_autre(nom_fichier)
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
        else:
            return {} # retourne un dictionnaire vide si le type de fichier n'est pas compatible avec notre programme

    """
    Entrées: nom_fichier
    Sorties: Un dictionnaire contenant des items(String) comme clé et un prix(float) comme valeur
    But: Lire un fichier excel et retourner de l'information pertinente pour traiter sous forme d'un dictionnaire
    """
    @staticmethod
    def __lire_xlsx(nom_fichier): # Méthode static et "privée"
        item_prix = {}
        with pd.ExcelFile(nom_fichier) as excel:
            excel_reading = pd.read_excel(excel)
            for group in excel_reading.values:
                item_prix[group[0]] =group[2]
        return item_prix

    """
    Entrées: nom_fichier
    Sorties: Un dictionnaire contenant des items(String) comme clé et un prix(float) comme valeur
    But: Lire un fichier CSV et retourner de l'information pertinente pour traiter sous forme d'un dictionnaire.
    """
    @staticmethod
    def __lire_csv(nom_fichier): # Méthode static et "privée"
            with open(nom_fichier, "r") as fichier :
                next(fichier)
                lignes = fichier.readlines()
                liste_walmart = []
                for ligne in lignes: 
                    liste = ligne.strip().split(",")
                    liste_article = {
                    liste[0],
                    liste[1],
                    liste[2]
                    }
                    liste_walmart.append(liste_article)
            return liste_walmart

