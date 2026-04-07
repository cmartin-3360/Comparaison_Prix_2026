"""
    But: Interagir avec l'utilisateur de façon a savoir quelles fichiers veulent être lire et l'emplacement voulu de l'analyse
"""
class Traitement:
    """
    Entrées: item_prix_un et item_prix_deux (dictionnaires String: float)
    Sorties: resultat (set de String)
    But: Donner des informations traiter en fonction des informations obtenu par l'utilisateur
    """
    @staticmethod
    def traiter(item_prix_un, item_prix_deux):
        resultat = set()
        item_rechercher = str(input("Entrez le nom bref du produit voulant être comparer ou sortir avec la clé `q` pour finir le programme et recevoir l'analyse: "))
        while item_rechercher != "q":
            message, etat = Traitement.__dire(item_prix_un, item_prix_deux, item_rechercher)
            if etat == 1: # Succès de la recherche
                resultat.add(message) # Ajouter le message d'information à la liste de résultat
            item_rechercher = str(input(Traitement.__message_utilisateur(message))) # Afficher le message d'information et redemander une recherche
        return resultat # Donner un set de String

    """
    Entrées: resultat(set de String)
    Sorties: resultat (sans charactére spéciaux)
    But: Nettoyer les résultats de charactére spéciaux pouvant causer des problèmes lors de l'écriture dans le fichier
    """
    @staticmethod
    def __filtrer_resultat(resultat):
        formattage = "\n" +"="*60 + "\n"
        final = "Entrez le nom bref du produit voulant être comparer ou sortir avec la clé `q` pour finir le programme et recevoir l'analyse: "
        message = formattage + aspect + formattage + final
        return message

    """
    Entrées: aspect (String)
    Sorties: message (String formatté)
    But: Uniformisation des informations présenter à l'utilisateur lors du traitement
    """
    @staticmethod
    def __message_utilisateur(aspect):
        formattage = "\n" +"="*60 + "\n"
        final = "Entrez le nom bref du produit voulant être comparer ou sortir avec la clé `q` pour finir le programme et recevoir l'analyse: "
        message = formattage + aspect + formattage + final
        return message
    
    """ 
    Entrées: dictionnaire_un(Dictionnaire), dictionnaire_deux(Dictionnaire), item_rechercher(String)
    Sorties: message (String formatté)
    But: Fournir un état à la recherche ainsi qu'un message en fonction de ce dernier
    """
    # TODO: Commentaires
    @staticmethod
    def __dire(dictionnaire_un, dictionnaire_deux, item_rechercher):
        informations_un = Traitement.__item_present(dictionnaire_un, item_rechercher)
        informations_deux = Traitement.__item_present(dictionnaire_deux, item_rechercher)

        etat_un = Traitement.__etat(informations_un)
        if etat_un == None: # Abandon de la recherche dès le premier fichier si l'état est invalide
            return Traitement.__affiche_item_prix(etat_un, "première"), 0 # Abandon de la recherche

        etat_deux = Traitement.__etat(informations_deux)
        if etat_deux == None: # Abandon de la recherche au deuxième fichier si l'état est invalide
            message = Traitement.__affiche_item_prix(etat_un, "première")
            message += "\n"
            message += Traitement.__affiche_item_prix(etat_deux, "deuxième")
            return message, 0 # Abandon de la recherche

        return Traitement.__affiche_traiter(etat_un, etat_deux), 1 # Succès de la recherche

    """
    Entrées: dictionnaire(Dictionnaire)
    Sorties: Tuple ou None (Représentation de l'état de la recherche)
    But: Donner un état à la recherche en fonction du dictionnaire
    """
    @staticmethod
    def __etat(dictionnaire):
        if not dictionnaire:
            return None # Introuvable, annulation de demande
        if len(dictionnaire) > 1: # Trop d'options
            message = "=" * 60 + "\n"
            message += "Votre recherche a donné plusieurs résultats:  \n"
            count = 1
            for item, prix in dictionnaire.items():
                message += f"{count}. {item}: {prix}$\n"
                count += 1
            message += "Veuillez inscrire le numéro entier(ex: 1) de l'article souhaité, si le numéro est invalide votre demande sera annulé:"
            demande = None
            try:
                demande = int(input(message))
            except Exception:
                print("="*60 + "\n Votre demande est annulée")
                return None # Annulation de demande
            count = 1
            for item, prix in dictionnaire.items():
                if demande == count:
                    return (item, prix)
                count += 1
            return None # Annulation de demande
        else: # Une option
            item, prix = next(iter(dictionnaire.items()))
            return (item, prix) 

    """
    Entrées: dict (Dictionnaire), item_rechercher (String, demande utilisateur)
    Sorties: item_prix(dictionnaires des clé qui corresponde à la requête de l'utilisateur)
    But: Recherche dans le dictionnaire si une de ses clé(item) correspondes à la recherche de l'utilisateur(item)
    """
    @staticmethod
    def __item_present(dict, item_rechercher):
        item_prix = {}
        for item, price in dict.items():
            if str(item_rechercher).lower() in str(item).lower():
                item_prix[item] = price
        return item_prix

    """
    Entrées: tuple, index(String)
    Sorties: String (En foncton de l'état du tuple)
    But: Indiquer à l'utilisateur la raison de l'échec de la comparaison
    """
    @staticmethod
    def __affiche_item_prix(tuple, index):
        if tuple == None:
            return f"Aucun résultat trouvé pour votre {index} fichier fourni." # Donner un message d'erreur pouvant aider l'utilisateur à comprendre le problème
        else:
            item, prix = tuple
            return f"Le prix de {item} pour votre recherche dans le {index} fichier est de {prix}$" # Donner un message d'information pouvant aider l'utilisateur à comprendre le résultat de sa recherche

    """
    Entrées: infos_un(tuple), infos_deux(tuple)
    Sorties: String (Représentant le traitement de la comparaison entre les deux prix)
    But: Retourner l'information de quel prix est le plus bas et de combien, ou si les prix sont égaux
    """
    @staticmethod
    def __affiche_traiter(infos_un, infos_deux):
        item_un = infos_un[0]
        prix_un = infos_un[1]
        item_deux = infos_deux[0]
        prix_deux = infos_deux[1]
        if prix_un > prix_deux:
            return f"Le produit du deuxième fichier: {item_deux} est {prix_deux}$ ce qui est {prix_un - prix_deux:.2f}$ plus économique que le produit du premier fichier, {item_un}, à {prix_un}$"
        elif prix_un < prix_deux:
            return f"Le produit du premier fichier: {item_un} est {prix_un}$ ce qui est {prix_deux - prix_un:.2f}$ plus économique que le produit du deuxième fichier, {item_deux}, à {prix_deux}$"
        else: # Lorsqu'égale
            return f"Les deux produits, soit {item_un} pour le premier fichier et {item_deux} pour le deuxième fichier, ont le même prix de {prix_un}$"
