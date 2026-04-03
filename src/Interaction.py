import os

class InteractionEnvironment:
    def exploring():
        # linux: Example output on Linux: '/home/username'
        # Example output on Windows: 'C:\\Users\\username'
        home_dir = os.path.expanduser('~')
        return home_dir

    def user_input(reponse = "Entrer une reponse : "):
        chemin = input(reponse)
        if os.path.exists(chemin):
            return chemin
        else:           
            print("Le chemin n'existe pas.")
            return None
        
    @staticmethod
    def lire_fichier():
        nom_fichier_un = input("Entrez le nom du premier fichier (avec extension .xlsx ou .csv) : ")
        nom_fichier_deux = input("Entrez le nom du deuxième fichier (avec extension .xlsx ou .csv) : ")
        return nom_fichier_un, nom_fichier_deux