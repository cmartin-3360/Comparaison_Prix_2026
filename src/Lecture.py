import csv
import pandas as pd
##import xlsx
#interaction, os, popup, interagir avec lusager, demander noms fichiers a traiter et emplacement a mettre les fichiers creer
class Lecture:

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

    @staticmethod
    def lire_xlsx():
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


     
    

    


