import csv
#import xlsx
#interaction, os, popup, interagir avec lusager, demander noms fichiers a traiter et emplacement a mettre les fichiers creer
class Lecture:
    """
    Entrées: le nom du fichier à lire
    Sorties:
    But: lire un fichier CSV et à transformer certaines données en dictionnaire.
    """
    """def lecture_dict(nom_fichier):
        walmart = {} #dictionnaire
        grand_tuple = [] #liste
        with open(nom_fichier) as fichier:
            #lignes = fichier.readline()
            i = 0
            for ligne in fichier: #lignes:
                if i == 0:
                    i += 1
                    continue
                #ligne = fichier.readline(i)
                desirer = ligne.split(",")
                #print(desirer)
                tuple = (desirer[0], desirer[2].split("\n")[0])
                grand_tuple.append(tuple)
        for obj in grand_tuple:
            walmart[obj[0]] = obj[1]
        return walmart"""



    def lecture_dict(nom_fichier):
      walmart = {}

      with open(nom_fichier) as fichier:
        next(fichier)  # Ignore la première ligne

        for ligne in fichier:
            desirer = ligne.strip().split(",")
            walmart[desirer[0]] = desirer[2]

      return walmart
              

     
    

    


