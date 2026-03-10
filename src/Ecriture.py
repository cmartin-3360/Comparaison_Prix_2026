class Ecriture:
    #pass
    """
    Pourrais avoir besoin:
    Entrées: info(String)
    Sorties: Aucune
    But: Initialiser un objet écriture
    def __init__(self, info):
        self.info = info
    """
    def writeFile(info):
        #"a" appends to the end of the file to write and will create the file if it does not exist
        with open("ecriture.txt", "a") as file:
            file.write(info)

    def overwriteFile(info):
        #"x" overwrites an existing file and creates a new one if it doesn't exist
        with open("ecriture.txt", "x") as file:
            file.write(info)

