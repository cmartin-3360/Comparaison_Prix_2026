import csv
#import xlsx
#interaction, os, popup, interagir avec lusager, demander noms fichiers a traiter et emplacement a mettre les fichiers creer
class Lecture:
    """
    Entrées: 
    Sorties:
    But:
    """
    def lecture_dict(nom_fichier):
        walmart = {} #dictionnaire
        grand_tuple = []
        with open(nom_fichier) as fichier:
            #lignes = fichier.readlines()
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
        return walmart

              
            
             
     
    

    


