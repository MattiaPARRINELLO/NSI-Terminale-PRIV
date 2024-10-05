from random import randint

class Carte():
    def __init__(self, couleur, valeur):
        if valeur not in range(1, 13) or couleur not in ["coeur", "carreau", "trefle", "pique"]:
            raise ValueError("La valeur ou la couleur n'est pas valide")
        else:
            self.couleur = couleur
            self.valeur = valeur
    def nom(self):
        if self.valeur == 1:
            return "As de " + self.couleur
        elif self.valeur == 11:
            return "Valet de " + self.couleur
        elif self.valeur == 12:
            return "Dame de " + self.couleur
        elif self.valeur == 13:
            return "Roi de " + self.couleur
        else:
            return str(self.valeur) + " de " + self.couleur
    


class Paquet():
    def __init__(self):
        self.cartes = []
        for couleur in ["coeur", "carreau", "trefle", "pique"]:
            for valeur in range(1, 14):
                self.cartes.append(Carte(couleur, valeur))
    
    def tirer(self):
        if len(self.cartes) == 0:
            raise ValueError("Il n'y a plus de cartes dans le paquet")
        else:
            return self.cartes.pop(randint(0, len(self.cartes) - 1))
    
        

