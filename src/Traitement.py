
class Traitement:
    @staticmethod
    def _plus_petit(chiffre_a, chiffre_b):
        if not isinstance(chiffre_a, (int, float)) or not isinstance(chiffre_b, (int, float)):
            raise TypeError("Les deux paramètres doivent être des nombres.")
        return chiffre_a if chiffre_a <= chiffre_b else chiffre_b

    @staticmethod
    def _item_valide(dictionnaire, mot_chercher):
        if not isinstance(dictionnaire, dict):
            raise TypeError("Le premier argument doit être un dictionnaire.")
        if not isinstance(mot_chercher, str):
            raise TypeError("Le terme de recherche doit être une chaîne de caractères.")

        recherche = mot_chercher.lower().strip()
        prix_trouves = [prix for item, prix in dictionnaire.items() if recherche in str(item).lower()]

        if not prix_trouves:
            return -1
        return min(prix_trouves)

    @staticmethod
    def _dire(dictionnaires, mot_chercher):
        if not isinstance(dictionnaires, (list, tuple)):
            raise TypeError("Le premier argument doit être une liste ou un tuple de dictionnaires.")

        prix_minimum = None
        for dictionnaire in dictionnaires:
            prix = Traitement._item_valide(dictionnaire, mot_chercher)
            if prix != -1:
                prix_minimum = prix if prix_minimum is None else Traitement._plus_petit(prix_minimum, prix)

        if prix_minimum is None:
            return f"Aucun produit trouvé pour '{mot_chercher}'."
        return f"Le prix le plus bas pour '{mot_chercher}' est {prix_minimum:.2f}$"

    @staticmethod
    def traiter(dictionnaires):
        if not isinstance(dictionnaires, (list, tuple)):
            raise TypeError("Le paramètre doit être un tuple ou une liste de dictionnaires.")

        resultat = []
        while True:
            mot_chercher = input("Entrez le nom du produit à rechercher (ou 'exit' pour terminer) : ").strip()
            if mot_chercher.lower() == 'exit':
                break
            if not mot_chercher:
                print("Veuillez entrer un terme de recherche valide.")
                continue

            texte = Traitement._dire(dictionnaires, mot_chercher)
            print(texte)
            resultat.append(texte)

        return resultat
