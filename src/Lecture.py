import pandas as pd



class Lecture:
    """
    Entrées: nom_fichier_un et nom_fichier_deux
    Sorties: Un tuple contenant deux dictionnaires représentant les informations des deux fichiers
    But: Retourner les deux dictionnaires voulant être traiter tout en gérant les fichiers incompatible pour notre programme
    """
    @staticmethod
    def lire(nom_fichier_un, nom_fichier_deux):
        dictionnaire_un = Lecture.__lire_xlsx_csv_autre(nom_fichier_un)
        dictionnaire_deux = Lecture.__lire_xlsx_csv_autre(nom_fichier_deux)
        dictionnaires = (dictionnaire_un, dictionnaire_deux)
        return dictionnaires

    """
    Entrées: nom_fichier
    Sorties: Dictionnaire contenant l'information du fichier sous forme "item":prix
    But: Lire un fichier en fonction de son type avec son nom
    """
    @staticmethod
    def __lire_xlsx_csv_autre(nom_fichier): # Méthode static et "privée"
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
    def __lire_xlsx(nomFichier):
        item_prix = {}
        try:
            with pd.ExcelFile(nomFichier) as excel:
                excel_lire = pd.read_excel(excel)
                for group in excel_lire.values:
                    if pd.notna(group[0]) and pd.notna(group[2]):
                        item_prix[str(group[0])] = float(group[2])
        except OSError:
            print(f"Le fichier {nomFichier} n'a pas été trouvé.")
        except Exception as e:  
            print(f"Erreur de lecture du fichier : {nomFichier}") 
            print(f"Détails de l'erreur : {e}")
        return item_prix

    """
    Entrées: nom_fichier
    Sorties: Un dictionnaire contenant des items(String) comme clé et un prix(float) comme valeur
    But: Lire un fichier CSV et retourner de l'information pertinente pour traiter sous forme d'un dictionnaire.
    """
    @staticmethod
    def __lire_csv(nom_fichier): 
        dict_item_prix = {}
        try:
            with open(nom_fichier, 'r') as fichier:
                next(fichier)
                lignes = fichier.readlines()
                for ligne in lignes:
                    valeurs = ligne.strip().split(",")
                    dict_item_prix[str(valeurs[0])] = float(valeurs[2])
        except FileNotFoundError:
            print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        except Exception as e:
            print(f"Erreur de lecture du fichier : {nom_fichier}")
            print(f"Détails de l'erreur : {e}")
        return dict_item_prix