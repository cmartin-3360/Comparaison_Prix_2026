import pandas as pd

class Lecture:
    """
    Lecture de fichiers excel et CSV
    """

    @staticmethod
    def lire_xlsx():
        """
        Entrées: Aucune (utilise un chemin fixe)
        Sorties: Un dictionnaire contenant des items(String) comme clé et un prix(float) comme valeur
        But: Lire un fichier excel et retourner de l'information pertinente pour traiter
        """
        nomFichier = "assets/Costco_Product_Catalog.xlsx"
        item_prix = {}
        try:
            with pd.ExcelFile(nomFichier) as excel:
                excel_reading = pd.read_excel(excel)
                for group in excel_reading.values:
                    item_prix[group[0]] = group[2]
        except OSError:
            print(f"Erreur : Le fichier {nomFichier} est introuvable.")
        else:
            print("Lecture réussie avec succès")
        return item_prix

    @staticmethod
    def lecture_fichier(nom_fichier):
        """
        Entrées: le nom du fichier à lire
        Sorties: un dictionnaire contenant les items(string) et leur prix(float).
        But: lire un fichier CSV et retourner les informations pour le traiter.
        """
        dict_item_prix = {}
        try:
            with open(nom_fichier, "r") as fichier:
                next(fichier)
                lignes = fichier.readlines()
                for ligne in lignes:
                    valeurs = ligne.strip().split(",")
                    item = valeurs[0]
                    price = float(valeurs[2].replace(',', ''))
                    dict_item_prix[item] = price
        except FileNotFoundError:
            print(f"Erreur : Le fichier {nom_fichier} est introuvable.")
        except Exception as e:
            print(f"Erreur de lecture du fichier: {nom_fichier}")
            print("Erreur :", e)
        return dict_item_prix

    @staticmethod
    def lire_xlsx_param(nom_fichier):
        """
        Entrées: nom_fichier
        Sorties: Un dictionnaire contenant des items(String) comme clé et un prix(float) comme valeur
        But: Lire un fichier excel et retourner de l'information pertinente pour traiter sous forme d'un dictionnaire
        """
        item_prix = {}
        try:
            with pd.ExcelFile(nom_fichier) as excel:
                lecture_excel = pd.read_excel(excel)
                for group in lecture_excel.values:
                    item_prix[group[0]] = group[2]
        except OSError:
            print(f"Erreur : Le fichier {nom_fichier} est introuvable.")
        except Exception as e:
            print(f"Erreur de lecture du fichier: {nom_fichier}")
            print("Erreur :", e)
        return item_prix

    @staticmethod
    def lire_csv(nom_fichier):
        """
        Entrées: nom_fichier
        Sorties: Un dictionnaire contenant des items(String) comme clé et un prix(float) comme valeur
        But: Lire un fichier CSV et retourner de l'information pertinente pour traiter sous forme d'un dictionnaire.
        """
        item_prix = {}
        try:
            with open(nom_fichier, "r") as fichier:
                next(fichier)
                lignes = fichier.readlines()
                for ligne in lignes:
                    valeurs = ligne.strip().split(",")
                    item_prix[valeurs[0]] = valeurs[2]
        except FileNotFoundError:
            print(f"Erreur : Le fichier {nom_fichier} est introuvable.")
        except Exception as e:
            print(f"Erreur de lecture du fichier: {nom_fichier}")
            print("Erreur :", e)
        return item_prix

