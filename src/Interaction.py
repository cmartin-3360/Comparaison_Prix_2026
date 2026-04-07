import os
import tkinter
import tkinter.filedialog as fd

"""
    But: Interagir avec l'utilisateur de façon a savoir quelles fichiers veulent être lire et l'emplacement voulu de l'analyse
"""
class Interaction:
    tkt_root = None

    """
    Entrées: premier_deuxieme
    Sorties: chemin(String)
    But: Donner un chemin à utiliser en lecture
    """
    @staticmethod
    def interagir_lecture(premier_deuxieme):
        type_usage = str("")
        if premier_deuxieme == "premier":
            type_usage += "la première lecture"
        elif premier_deuxieme == "deuxieme":
            type_usage += "la deuxième lecture"
        else:
            type_usage += "lecture"

        etat = Interaction.__selectionner_etat(type_usage)

        count = 0
        emplacement = ""
        while not os.path.isfile(emplacement):
            if count > 0:
                print("Il semble y avoir eu un problème: Veuillez réessayer")
            elif count > 20:
                break # sortir boucle apres 20 essaies si emplacement encore
            count += 1
            match etat:
                case 1: # Ajustable
                    message = "="*60 + "\n"
                    message += "Déplacer la fenêtre de VS code et celles en arrières jusqu'à ce que vous voyez l'explorateur de fichier avec une entente spéciale"
                    message += "\n" + "Selectionner le {premier_deuxieme} fichier voulant être comparer et appuyer sur save"
                    print(message)
                    emplacement = Interaction.__chercher_fichier_tkinter(premier_deuxieme)
                    if not Interaction.__est_excel_csv(emplacement):
                        print("Le fichier choisi n'est pas du type excel ou csv, veuillez réessayer")
                        emplacement = ""
                case 2: # Démontrable
                    
                    if premier_deuxieme == "premier":
                        emplacement = "assets/walmart_prices.csv"
                    else: # Normalement deuxieme, mais veut avoir un par defaut defaut
                        emplacement = "assets/Costco_Product_Catalog.xlsx"
                    print(f"Le programme va utiliser le fichier par défaut dans l'emplacement du projet: {emplacement}")
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
        etat = Interaction.__selectionner_etat("l'écriture")
        count = 0
        emplacement = ""
        while not Interaction.__dossier_exist(os.path.dirname(emplacement)):
            if count > 0:
                print("Il semble y avoir eu un problème: Veuillez réessayer")
            elif count > 20:
                break # sortir boucle apres 20 essaies si emplacement encore
            count += 1
            match etat:
                case 1: # Ajustable
                    message = "="*60 + "\n"
                    message += "Déplacer la fenêtre de VS code et celles en arrières jusqu'à ce que vous voyez l'explorateur de fichier avec une entente spéciale"
                    message += "\n" + "Avec le sélecteur, vous pouvez changez le type de dossier possible entre CSV et Excel"
                    message += "\n" + "Selectionner le nom du dossier et appuyer sur Select folder"
                    print(message)
                    emplacement_dossier = Interaction.__creation_dossier_tkinter()
                    nom_fichier = str(input("Entrez le nom souhaitez du fichier text comprenant l'analyse(sans .txt): "))
                    emplacement = Interaction.__creation_fichier(nom_fichier, emplacement_dossier)
                case 2: # Démontrable
                    print("Le fichier d'analyse sera créé dans le dossier 'data' du projet avec le nom 'demo.txt'")
                    emplacement_actuel = os.path.dirname(os.path.abspath(__file__))
                    emplacement_projet = os.path.dirname(emplacement_actuel)
                    emplacement_data = os.path.join(emplacement_projet, "data")
                    emplacement = Interaction.__creation_fichier("demo", emplacement_data)
                case _:
                    return "invalide" # NOTE: Pourrait etre utiliser pour revenir/sortir
        return emplacement

    """
    Entrées: emplacement
    Sorties: boolean(True ou False)
    But: Déterminer si le type de fichier est valide pour le programme
    """
    @staticmethod
    def __est_excel_csv(emplacement): # Méthode static et "privée"
        if ".xlsx" in emplacement:
            return True
        elif ".csv" in emplacement:
            return True
        else:
            return False

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
        mise_en_contexte = "Vous pouvez procéder dans ses deux mode différents:"
        etat_un = "1. AJUSTABLE: Possibilité de suivre d'autres instructions du terminal pour personaliser l'expérience"
        etat_deux = "2: DÉMONTRABLE: Voir ce que le programme peut faire avec les fichiers par défaut"
        instructions = f"Inscrivez le mode voulant être utilisé, soit 1 soit 2, pour {type_usage}:"
        contenu_message = (mise_en_contexte, etat_un, etat_deux, instructions)
        message += formattage
        for ligne in contenu_message:
            message += saut_ligne + ligne

        etat = int(input(message)) # Demande à l'utilisateur quel est l'état désirer

        while not Interaction.__etat_est_valide(etat):
            print("="*60 + "\n" + "Votre mode est invalide assurez vous d'inscrire 1 ou 2" + "\n")
            etat = int(input(message)) # NOTE: Boucle pourrais etre infinie, mais pas mal simple davoir un etat valide
        return etat

    """
    Entrées: emplacement_fichier (String)
    Sorties: boolean(True ou False)
    But: Valider l'existence du fichier
    """
    @staticmethod
    def __dossier_exist(emplacement_fichier):
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
        emplacement_fichier = fd.askopenfilename(
            title= f"Sélectionner le {premier_deuxieme} fichier voulant être comparer",
            filetypes= [("CSV", "*.csv"), ("Excel", "*.xlsx")]
        )
        Interaction.__detruire_tkt()
        return emplacement_fichier

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
    Entrées: nom_fichier(sous le format nom), emplacement_voulu
    Sorties: String, qui représente le nom complet de l'emplacement du fichier à utiliser
    But: Créer nom_fichier dans l'emplacement par défaut étant le "data" du projet
    """
    @staticmethod
    def __creation_fichier(nom_fichier, emplacement_dossier): # Méthode static et "privée"
        try:
            os.makedirs(emplacement_dossier, exist_ok=True) # Créer le dossier si n'existe pas déjà
        except PermissionError:
            print("Aucune permission pour écrire dans ce fichier")
        except:
            print("Une erreur inattendu lors de l'intéraction s'est produite, veuillez reporter le problème.")
        return os.path.join(emplacement_dossier, f"{nom_fichier}.txt") # Le dir du fichier qui se fait reellement creer dans ECRITURE