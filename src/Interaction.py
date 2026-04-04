import os
import tkinter
import tkinter.filedialog as fd

class Interaction:
    tkt_root = None
    # TODO: Implémenter un cue qui fait sortir de chacune des while loop via terminal pour eviter les boucles infinies
    # TODO: Implémenter des try catchs
    """
    Entrées: premier_deuxieme
    Sorties: chemin(String)
    But: Donner un chemin à utiliser en lecture
    """
    @staticmethod
    def interagir_lecture(premier_deuxieme):
        type_usage = str("")
        if premier_deuxieme == "premier":
            type_usage += "première lecture"
        elif premier_deuxieme == "deuxieme":
            type_usage += "deuxième lecture"
        else:
            type_usage += "lecture"

        etat = Interaction.__selectionner_etat(type_usage)

        count = 0
        emplacement = ""
        while not Interaction.fichier_exist(emplacement):
            if count > 0:
                print("Il semble y avoir eu un problème: Veuillez réessayer") # TODO: Déterminer si besoin de try-catch et les implémenters si nécessaire
            elif count > 20:
                break # sortir boucle apres 20 essaies si emplacement encore
            count += 1
            match etat:
                case 1: # Interface graphique
                    emplacement = Interaction.__chercher_fichier_tkinter(premier_deuxieme)
                case 2: # Terminal
                    emplacement_donner = str(input(Interaction.__chercher_fichier_os()))
                    emplacement = os.path.expanduser('~') + emplacement_donner
                case 3: # Par defaut
                    if premier_deuxieme == "premier":
                        return "assets/walmart_prices.csv"
                    else: # Normalement deuxieme, mais veut avoir un par defaut defaut
                        return "assets/Costco_Product_Catalog.xlsx"
                case _:
                    return "invalide" # NOTE: Pourrait etre utiliser pour revenir/sortir
        return emplacement

    """
    Entrées: Aucune
    Sorties: chemin
    But: Donner le chemin à utiliser en écriture(en le creant)
    """
    @staticmethod
    def interagir_ecriture():
        #États terminal, gui et default
        etat = Interaction.__selectionner_etat("écriture")
        count = 0
        emplacement = ""
        while not Interaction.dossier_exist(os.path.dirname(emplacement)):
            if count > 0:
                print("Il semble y avoir eu un problème: Veuillez réessayer") # TODO: Déterminer si besoin de try-catch et les implémenters si nécessaire
            elif count > 20:
                break # sortir boucle apres 20 essaies si emplacement encore
            count += 1
            match etat:
                case 1: # Interface graphique
                    emplacement_dossier = Interaction.__creation_dossier_tkinter()
                    nom_fichier = str(input("Entrez le nom souhaitez au fichier qui aura l'analyse(sans .txt): ")) + ".txt"
                    emplacement = os.path.join(emplacement_dossier, nom_fichier)
                    os.makedirs(emplacement_dossier, exist_ok=True) # Créer le dossier si n'existe pas déjà
                case 2: # Terminal
                    emplacement_personel = os.path.expanduser('~') 
                    nom_fichier = str(input("Entrez le nom souhaitez au fichier(Ensuite, vous entreriez le dossier d'enregistrement): "))
                    nom_emplacement = str(input(f"Compléter l'emplacement souhaité pour le fichier(dossier):{emplacement_personel}"))
                    emplacement = Interaction.__creation_fichier_os(emplacement_personel, nom_emplacement, nom_fichier)
                case 3: # Par defaut
                    nom_fichier = str(input("Entrez le nom souhaitez au fichier du fichier qui sera enregistrer dans /data:"))
                    emplacement = Interaction.__creation_fichier_default(nom_fichier)
                case _:
                    return "invalide" # NOTE: Pourrait etre utiliser pour revenir/sortir
        return emplacement

    """
    Entrées: Aucune
    Sorties: tkt_root
    But: Initialiser tkinter pour pouvoir l'utiliser
    """
    @staticmethod
    def __commencer_tkt():
        if Interaction.tkt_root is None: # sécurité
            Interaction.tkt_root = tkinter.Tk() # la main window
            Interaction.tkt_root.withdraw() # Cacher la main window de tkinter
        return Interaction.tkt_root

    """
    Entrées: Aucune
    Sorties: tkt_root
    But: Fermer tkinter lorsque son utlité est terminer(à la fin du programme)
    """
    @staticmethod
    def __detruire_tkt():
        if Interaction.tkt_root is not None:
            Interaction.tkt_root = Interaction.tkt_root.destroy()
            Interaction.tkt_root = None # sécurité
        return Interaction.tkt_root

    """
    Entrées: etat
    Sorties: boolean(True ou False)
    But: Valider si l'état est bon
    """
    @staticmethod
    def __etat_est_valide(etat):
        match etat:
            case 1:
                return True
            case 2:
                return True
            case 3:
                return True
            case __:
                return False
    """
    Entrées: type_usage
    Sorties: message(String)
    But: Fournir un message contenant les instructions pour la sélection d'état
    """
    @staticmethod
    def __selectionner_etat(type_usage): # \n
        message = ""
        formattage = "=" * 60
        saut_ligne = "\n"
        mise_en_contexte = "Vous pouvez procéder dans ses trois mode différents:"
        etat_un = "1: Inscrire le chemin par INTERFACE GRAPHIQUE"
        etat_deux = "2: Inscrire le chemin par TERMINAL"
        etat_trois = "3: Le chemin sera donner par DÉFAUT"
        instructions = f"Inscrivez le chiffre(1, 2 ou 3) représentant le mode voulant être utilisé pour la {type_usage}:"
        contenu_message = (mise_en_contexte, etat_un, etat_deux, etat_trois, instructions)
        message += formattage
        for ligne in contenu_message:
            message += saut_ligne + ligne
        
        etat = int(input(message))
        
        while not Interaction.__etat_est_valide(etat):
            print("="*60 + "\n" + "Votre mode est invalide assurez vous d'inscrire 1, 2 ou 3" + "\n")
            etat = int(input(message)) # NOTE: Boucle pourrais etre infinie, mais pas mal simple davoir un etat valide
        return etat

    """
    Entrées: emplacement_fichier (String)
    Sorties: boolean(True ou False)
    But: Valider l'existence du fichier
    """
    @staticmethod
    def fichier_exist(emplacement_fichier):
        if os.path.isfile(emplacement_fichier):
            return True
        else:
            return False
        
    """
    Entrées: emplacement_fichier (String)
    Sorties: boolean(True ou False)
    But: Valider l'existence du fichier
    """
    @staticmethod
    def dossier_exist(emplacement_fichier):
        if os.path.isdir(emplacement_fichier) and not os.path.isfile(emplacement_fichier):
            return True
        else:
            return False

    """
    Entrées: premier_deuxieme
    Sorties: chemin_fichier (String)
    But: Trouver le chemin complet du fichier voulant être lu avec l'interface de tkinter
    """
    @staticmethod
    def __chercher_fichier_tkinter(premier_deuxieme):
        Interaction.__commencer_tkt()
        chemin_fichier = fd.askopenfilename(
            title= f"Sélectionner le {premier_deuxieme} fichier voulant être comparer",
            filetypes= [("CSV", "*.csv"), ("Excel", "*.xlsx")]
        )
        Interaction.__detruire_tkt()
        return chemin_fichier

    """
    Entrées: Aucune
    Sorties: tkt_root
    But: Afficher le répertoire personnel de l'utilisateur
    """
    @staticmethod
    def __chercher_fichier_os():
        # NOTE: adéquat = csv ou excel ainsi que bien formatté, mais planterais pas ici dans ce cas-la 
        message = ("=" *60) + "\n" + "Veuillez compléter l'emplacement du fichier adéquat(voir readme pour ce qu'adéquat signifie) pour la lecture: "
        home_dir = os.path.expanduser('~') # linux: '/home/username' et Windows: 'C:\\Users\\username'
        message += home_dir # C'est voulu de ne pas ajouter un saut de ligne
        return message

    """
    Entrées: Aucune
    Sorties: chemin_fichier (String)
    But: Créer un fichier à l'emplacement souhaitée par l'utilisateur pour écrire notre analyse avec tkinter
    """
    @staticmethod
    def __creation_dossier_tkinter():
        Interaction.__commencer_tkt()
        chemin_fichier = fd.askdirectory(
            title= f"Sélectionner l'emplacement du dossier pour l'écriture"
        ) # devra surment utiliser fd.askdirectory()
        Interaction.__detruire_tkt()
        return chemin_fichier
    
    """
    Entrées: nom_emplacement, nom_fichier
    Sorties: emplacement_finale (String)
    But: Créer un fichier à l'emplacement souhaitée par l'utilisateur pour écrire notre analyse avec os
    """
    @staticmethod
    def __creation_fichier_os(nom_emplacement, nom_fichier):
        home_dir = os.path.expanduser('~') # linux: '/home/username' et Windows: 'C:\\Users\\username'
        emplacement_voulu = os.path.join(home_dir, nom_emplacement)
        emplacement_finale = os.path.join(emplacement_voulu, f"{nom_fichier}.txt")
        os.makedirs(emplacement_voulu, exist_ok=True)
        return emplacement_finale
    
    """
    Entrées: nom_fichier, sous le format nom
    Sorties: String, qui représente le nom complet de l'emplacement du fichier à utiliser
    But: Créer nom_fichier dans l'emplacement par défaut étant le "data" du projet
    """
    @staticmethod
    def __creation_fichier_default(nom_fichier): # Méthode static et "privée"
        emplacement_actuel = os.path.dirname(os.path.abspath(__file__))
        emplacement_projet = os.path.dirname(emplacement_actuel)
        emplacement_data = os.path.join(emplacement_projet, "data")
        os.makedirs(emplacement_data, exist_ok=True) # threw a permission error
        return os.path.join(emplacement_data, f"{nom_fichier}.txt")