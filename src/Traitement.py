
class Traitement:
    """
    les entr/es sont(a,b )
    """
    @staticmethod
    def plus_bas_prix(a, b):
        if a > b:
            return b
        elif a < b:
            return a
        else:
            return a
    def article_rechercher():
        if substring in mainstring:
            print (f"mainstring " contains "substring")

        
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