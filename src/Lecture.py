import csv
import xlsx

class Lecture:

    def x():
        nom_ficher = "walmart_prices.csv "


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