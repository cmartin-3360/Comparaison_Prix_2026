import os
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
                fichier.write(info)
                fichier.write("\n")
        except PermissionError:
            print("Erreur pas de permission pour ecrire dans ce fichier") # controle limiter
        except:
            print("Erreur inattendu lors de l'écriture, veuillez reporter le problème.")


