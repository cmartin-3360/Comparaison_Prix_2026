import pandas as pd

class Lecture:
    """
    Entrées: Aucune ensemoment
    Sorties: Un dictionnaire contenant des items(String) comme clé et un prix(float) comme valeur
    But: Lire un fichier excel et retourner de l'information pertinente pour traiter
    """
    @staticmethod
    def lire_xlsx():
        nomFichier = "assets/Costco_Product_Catalog.xlsx"
        item_prix = {}# créeation d'un dictionnaire item_prix vide
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
        return item_prix
  
  

    """
    Entrées: le nom du fichier à lire
    Sorties: une liste dans lequel le fichier sera stocker les items(string), et le prix(float).
    But: lire un fichier CSV et retourner les informations pour le traiter.
    """
    @staticmethod
    def lecture_fichier(nom_fichier) :
        with open(nom_fichier, "r") as fichier :# Ouverture et lecture du fichier csv 

            next(fichier)# skip la prémière ligne du fichier csv
            lignes = fichier.readlines()# lit tout et retourne une liste où chaque élément est une ligne.
            liste_item_prix = {}# liste dans laquelle les articles seront stocké
            for ligne in lignes: 
                liste_item_prix[ligne[0]] =ligne[2]
        return liste_item_prix 


