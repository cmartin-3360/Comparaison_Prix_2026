import csv
import pandas as pd
##import xlsx
#interaction, os, popup, interagir avec lusager, demander noms fichiers a traiter et emplacement a mettre les fichiers creer
class Lecture:
    """
    def x():
        nom_ficher = "walmart_prices.csv"


        #lecture de contenue du ficher
        #lecture = open( "walmart_prices.csv ")
        #contenu = lecture.read()
        #print(contenu)

        #lecture de ficher ligne par ligne
        with open( nom_ficher ) as ficher:
            ligne = ficher.readline()
        while ligne:
            print(ligne.strip())
            ligne = ficher.readline()

    def kara():
        lecture = open( "walmart_prices.csv ")
        print(lecture.read())
        # lecture de chaque contenue du fichier csv.
        with open("walmart_prices.cssv") as ficher:
            for ligne in ficher:
                print(ligne.strip())
    """

    """
    Entrées: Aucune ensemoment
    Sorties: Un dictionnaire contenant des items(String) comme clé et un prix(float) comme valeur
    But: Lire un fichier excel et retourner de l'information pertinente pour traiter
    """
    @staticmethod
    def lire_xlsx():
        nomFichier = "assets/Costco_Product_Catalog.xlsx"
        item_prix = {}
        with pd.ExcelFile(nomFichier) as excel:
            """
            print(excel_reading.columns) #Index(['Item', 'Category', 'Price'], dtype='str')
            print(excel_reading.axes) # [RangeIndex(start=0, stop=99, step=1), Index(['Item', 'Category', 'Price'], dtype='str')]
            print(excel_reading.columns[0]) # Item
            amount_of_columns = excel_reading.columns.size
            print(excel_reading.columns[amount_of_columns -1])
            """
            excel_reading = pd.read_excel(excel)
            
            for group in excel_reading.values:
                item_prix[group[0]] =group[2]
        return item_prix


        with open("assets/Costco_Product_Catalog.xlsx") as excel:
            return excel.read()

        
        
    """
    Entrées: le nom du fichier à lire
    Sorties: une liste dans lequel le fichier sera stocker.
    But: lire un fichier CSV et à transformer certaines données en dictionnaire.
    """
    nom_fichier = "walmart_price.csv"
  
    def lecture_fichier(nom_fichier) :
     
     
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


     
    

    


