class Traitement:
    @staticmethod
    def plus_bas_prix(a, b):
        if a > b:
            return b
        elif a < b:
            return a
        else:
            return a
        
    @staticmethod
    def creer_list(list):
        if not list:
            raise ValueError("La liste ne peut pas être vide.")
        
        minimum = list[0]
        for e in list:
            minimum = Traitement.plus_bas_prix(minimum, e)
        return minimum
    @staticmethod
    def trier(list):
        return sorted(list)

def traitement():
    fichier = open("kara.csv", "r")
    liste_article = fichier.readline()
    liste_dictionnaire = []
    for article in liste_article:
        article = article.strip().split()
        #if liste_article