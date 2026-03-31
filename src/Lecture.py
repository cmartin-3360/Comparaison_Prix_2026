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
    def lire_xlsx():
        nomFichier = "assets/Costco_Product_Catalog.xlsx"
        item_prix = {}# créeation d'un dictionnaire item_prix vide
        try:
              with pd.ExcelFile(nomFichier) as excel:# Ouverture et lecture du fichier excelavec bibliothèque pd(pandas)
                   """
                 print(excel_reading.columns) #Index(['Item', 'Category', 'Price'], dtype='str')
                 print(excel_reading.axes) # [RangeIndex(start=0, stop=99, step=1), Index(['Item', 'Category', 'Price'], dtype='str')]
                 print(excel_reading.columns[0]) # Item
                 amount_of_columns = excel_reading.columns.size
                 print(excel_reading.columns[amount_of_columns -1])
                   """
              excel_reading = pd.read_excel(excel)# lecture du fichier excel avec bibliothèque pd(pandas)
                        
              for group in excel_reading.values:
                 item_prix[group[0]] =group[2]
                    
        except OSError:
            print(f"Erreur : Le fichier {nomFichier} est introuvable.")
        else:
            print("Lecture réussie avec succèe")
        return item_prix
  

    """
    Entrées: le nom du fichier à lire
    Sorties: une liste dans lequel le fichier sera stocker les items(string), et le prix(float).
    But: lire un fichier CSV et retourner les informations pour le traiter.
    Entrées: nom_fichier
    Sorties: Un dictionnaire contenant des items(String) comme clé et un prix(float) comme valeur
    But: Lire un fichier CSV et retourner de l'information pertinente pour traiter sous forme d'un dictionnaire.
    """
    @staticmethod
    def lecture_fichier(nom_fichier) :
        liste_item_prix = {}# liste dans laquelle les articles seront stocké
        try:
            with open(nom_fichier, "r") as fichier :# Ouverture et lecture du fichier csv 

                next(fichier)# skip la prémière ligne du fichier csv
                lignes = fichier.readlines()# lit tout et retourne une liste où chaque élément est une ligne.
                for ligne in lignes: 
                    liste_item_prix[ligne[0]] =ligne[2]
            
        except FileNotFoundError :
          print(f"Erreur : Le fichier {nom_fichier} est introuvable.")
        else:
            print("Lecture réussie avec succèe")
        return liste_item_prix 
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

