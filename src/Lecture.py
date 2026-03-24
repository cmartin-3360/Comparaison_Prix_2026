import csv
#import xlsx
#interaction, os, popup, interagir avec lusager, demander noms fichiers a traiter et emplacement a mettre les fichiers creer
class Lecture:
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


     
    

    


