
import pandas


class Traitement:
    """
    les entrees sont(a,b )
    """
    @staticmethod
    def plus_bas_prix(a, b):
        if a > b:
            return b
        elif a < b:
            return a
        else:
            return a
    @staticmethod
    def article_rechercher(mainstring, substring):
        if substring in mainstring:
            print (f"'{mainstring}' contains '{substring}'")

        
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
    @staticmethod
    def item_valide(item, price):
        if not isinstance(item, str):
            raise TypeError("L'élément doit être une chaîne de caractères.")
        if not isinstance(price, (int, float)):
            raise TypeError("Le prix doit être un nombre.")
        if price < 0:
            raise ValueError("Le prix ne peut pas être négatif.")

def traiter(csv_dict, excel_dict, search_term):
    matching_items = {}
    for item, price in csv_dict.items():
        if search_term.lower() in item.lower():
            matching_items[item] = price
    for item, price in excel_dict.items():
        if search_term.lower() in item.lower():
            matching_items[item] = price

    if not matching_items:
        print("No matching products found.")
        return None, None

    cheapest_item = min(matching_items, key=matching_items.get)
    cheapest_price = matching_items[cheapest_item]
    
    print(f"The cheapest matching product is: '{cheapest_item}' at ${cheapest_price:.2f}")
    return cheapest_item, cheapest_price



    

