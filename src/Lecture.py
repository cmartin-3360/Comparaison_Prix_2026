import pandas as pd



class Lecture:

    @staticmethod
    def lire_xlsx(nomFichier):
        """
        Lit un fichier Excel et retourne un dictionnaire des prix des articles. 
        """
        item_prix = {}
        try:
            with pd.ExcelFile(nomFichier) as excel:
                excel_lire = pd.read_excel(excel)
                for group in excel_lire.values:
                    item_prix[group[0]] = group[2]
        except OSError:
            print(f"Le fichier {nomFichier} n'a pas été trouvé.")
        except Exception as e:  
            print(f"Erreur de lecture du fichier : {nomFichier}") 
            print(f"Détails de l'erreur : {e}")
        return item_prix
    

    @staticmethod
    def lire_csv(nom_fichier): 
        dict_item_prix = {}
        try:
            with open(nom_fichier, 'r') as fichier:
                next(fichier)
                lignes = fichier.readlines()
                for ligne in lignes:
                    valeurs = ligne.strip().split(",")
                    dict_item_prix[valeurs[0]] = float(valeurs[2])
        except FileNotFoundError:
            print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        except Exception as e:
            print(f"Erreur de lecture du fichier : {nom_fichier}")
            print(f"Détails de l'erreur : {e}")
        return dict_item_prix