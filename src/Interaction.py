import os
import tkinter
import tkinter.filedialog as fd

class Interaction:
    tkt_root = None

    """
    Entrées: Aucune
    Sorties: tkt_root
    But: Initialiser tkinter pour pouvoir l'utiliser
    """
    @staticmethod
    def interagir_chemins_lecture():
        #États terminal, gui et default
        return 0
    
    """
    Entrées: Aucune
    Sorties: tkt_root
    But: Initialiser tkinter pour pouvoir l'utiliser
    """
    @staticmethod
    def interagir_chemin_ecriture():
        #États terminal, gui et default
        return 0

    """
    Entrées: Aucune
    Sorties: tkt_root
    But: Initialiser tkinter pour pouvoir l'utiliser
    """
    @staticmethod
    def commencer_tkt():
        global tkt_root
        if tkt_root is None: # sécurité
            tkt_root = tkinter.Tk() # la main window
            tkt_root.withdraw() # Cacher la main window de tkinter
        return tkt_root

    """
    Entrées: Aucune
    Sorties: tkt_root
    But: Fermer tkinter lorsque son utlité est terminer(à la fin du programme)
    """
    @staticmethod
    def detruire_tkt():
        global tkt_root
        tkt_root = tkt_root.destroy()
        tkt_root = None # sécurité
        return tkt_root

    """
    Entrées: chemin_fichier (String)
    Sorties: boolean(True ou False)
    But: Valider l'existence du fichier
    """
    def fichier_exist(chemin_fichier):
        if os.path.isfile(chemin_fichier):
            return True
        else:
            return False

    """
    Entrées: premier_deuxieme
    Sorties: chemin_fichier (String)
    But: Trouver le chemin complet du fichier voulant être lu avec l'interface de tkinter
    """
    def chercher_fichier_tkinter(premier_deuxieme):
        chemin_fichier = fd.askopenfilename(
            title= f"Sélectionner le {premier_deuxieme} fichier voulant être comparer",
            filetypes= [("CSV", "*.csv"), ("Excel", "*.xlsx")]
        )
        return chemin_fichier

    """
    Entrées: Aucune
    Sorties: tkt_root
    But: Afficher le répertoire personnel de l'utilisateur
    """
    def chercher_fichier_os():
        home_dir = os.path.expanduser('~') # linux: '/home/username' et Windows: 'C:\\Users\\username'
        return home_dir

    """
    Entrées: Aucune
    Sorties: chemin_fichier (String)
    But: Créer un fichier à l'emplacement souhaitée par l'utilisateur pour écrire notre analyse avec tkinter
    """
    def creation_fichier_tkinter():
        chemin_fichier = fd.asksaveasfilename(
            title= f"Sélectionner l'emplacement et inscriver le nom du fichier de sortie",
            filetypes= [("Text", "*.txt")]
        ) # devra surment utiliser fd.askdirectory()
        return chemin_fichier
    
    """
    Entrées: nom_emplacement, nom_fichier
    Sorties: emplacement_finale (String)
    But: Créer un fichier à l'emplacement souhaitée par l'utilisateur pour écrire notre analyse avec os
    """
    def creation_fichier_os(nom_emplacement, nom_fichier):
        home_dir = os.path.expanduser('~') # linux: '/home/username' et Windows: 'C:\\Users\\username'
        emplacement_voulu = os.path.join(home_dir, nom_emplacement)
        emplacement_finale = os.path.join(emplacement_voulu, f"{nom_fichier}.txt")
        os.makedirs(emplacement_voulu, exist_ok=True)
        return emplacement_finale
    
    """
    Entrées: nom_fichier, sous le format nom.extension
    Sorties: String, qui représente le nom complet de l'emplacement du fichier à utiliser
    But: Créer nom_fichier dans l'emplacement par défaut étant le "data" du projet
    """
    @staticmethod
    def creation_fichier_default(nom_fichier): # Méthode static et "privée"
        emplacement_actuel = os.path.dirname(os.path.abspath(__file__))
        emplacement_projet = os.path.dirname(emplacement_actuel)
        emplacement_data = os.path.join(emplacement_projet, "data")
        os.makedirs(emplacement_data, exist_ok=True)
        return os.path.join(emplacement_data, nom_fichier)