
class ABR:
    def __init__(self, valeur):
        self.gauche = None
        self.droite = None
        
        self.valeur = valeur
    
    def rechercher(self, valeur):
        if self is None or self.valeur == valeur:
            return self is not None 
        
        if valeur < self.valeur:
            if self.gauche is None:
                return False
            return self.gauche.rechercher(valeur)
        else:
            if self.droite is None:
                return False
            return self.droite.rechcercher(valeur)
        
    def inserer(self, valeur):
        if self is None:
            return ABR(valeur)
        
        if valeur < self.valeur:
            self.gauche = self.gauche.inserer(valeur) if self.gauche else ABR(valeur)
        else:
            self.droite = self.droite.inserer(valeur) if self.gauche else ABR(valeur)
        return self
        
