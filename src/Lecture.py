#import csv
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
     fichier = nom_fichier.readline()
       
    

     liste_walmart = []
     for ligne in liste_walmart:
        ligne = ligne.strip()
        liste = ligne.split(",")
        liste_article = {
          "item" : liste[0],
          "categories": liste[1],
          "prix" : liste[2]

       }
        liste_article.apppend(liste_walmart)
        print(liste_walmart)
        nom_fichier.close
  



"""
    def lecture_dict(nom_fichier):
      walmart = {}

      with open(nom_fichier) as fichier:
        next(fichier)  # Ignore la première ligne

        for ligne in fichier:
            desirer = ligne.strip().split(",")
            walmart[desirer[0]] = desirer[2]

      return walmart
              """

     
    

    


