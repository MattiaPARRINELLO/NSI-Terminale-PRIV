
class ABR:
    def __init__(self, valeur):
        """
        Initialise un nœud de l'arbre binaire de recherche.
        Paramètres:
        valeur : La valeur du nœud.
        """

        self.gauche = None
        self.droite = None
        
        self.valeur = valeur
    
    def rechercher(self, valeur):
        """
        Recherche une valeur dans l'arbre binaire de recherche.
        Args:
            valeur (int): La valeur à rechercher dans l'arbre.
        Returns:
            bool: True si la valeur est trouvée dans l'arbre, sinon False.
        """

        if self is None or self.valeur == valeur:
            return self is not None 
        
        if valeur < self.valeur:
            if self.gauche is None:
                return False
            return self.gauche.rechercher(valeur)
        else:
            if self.droite is None:
                return False
            return self.droite.rechercher(valeur)
        
    def inserer(self, valeur):
        """
        Insère une valeur dans l'arbre binaire de recherche (ABR).
        Args:
            valeur: La valeur à insérer dans l'ABR.
        Returns:
            L'ABR mis à jour avec la nouvelle valeur insérée.
        """

        
        if valeur < self.valeur:
            if self.gauche is None:
                self.gauche = ABR(valeur)
            else:
                self.gauche.inserer(valeur)
        else:
            if self.droite is None:
                self.droite = ABR(valeur)
            else:
                self.droite.inserer(valeur)
        return self
        
