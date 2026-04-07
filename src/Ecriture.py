"""
    But: Écrire dans des fichiers en fonction de l'information voulant être écrite et de l'emplacement voulu du fichier
"""
class Ecriture:
    """
    Entrées: info, emplacement
    Sorties: Aucune
    But: Écrire par-dessus le fichier ce qui correspond à la varaible info à l'emplacement fichier
    """
    @staticmethod
    def ecrire(info, emplacement):
        try:
            with open(emplacement, "w") as fichier: # w signifie ecrire par dessus fichier
                for ligne in info:
                    fichier.write(f"{ligne} \n")
        except PermissionError:
            print("Erreur pas de permission pour ecrire dans ce fichier") # controle limiter
        except Exception: # Laisse passer keyboardInterrupt
            print("Erreur inattendu lors de l'écriture, veuillez reporter ce problème: {e}")


