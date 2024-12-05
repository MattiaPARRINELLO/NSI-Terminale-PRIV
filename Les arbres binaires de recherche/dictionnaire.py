class DicoABR:
    """
    Classe représentant un dictionnaire sous forme d'arbre binaire de recherche (ABR).
    Chaque nœud de l'arbre contient un mot et sa définition.
    """        
    def __init__(self, mot, definition):
        """
        Initialise un nœud de l'arbre avec un mot et sa définition.
        Args:
            mot (str): Le mot à stocker dans le nœud.
            definition (str): La définition du mot.
        """
        self.mot = mot
        self.definition = definition
        self.gauche = None
        self.droite = None

    def inserer(self, mot, definition):
        """
        Insère un nouveau mot et sa définition dans l'arbre.
        Si le mot existe déjà, met à jour sa définition.
        Args:
            mot (str): Le mot à insérer.
            definition (str): La définition du mot.
        """
        if mot < self.mot:
            if self.gauche is None:
                self.gauche = DicoABR(mot, definition)
            else:
                self.gauche.inserer(mot, definition)
        elif mot > self.mot:
            if self.droite is None:
                self.droite = DicoABR(mot, definition)
            else:
                self.droite.inserer(mot, definition)
        else:
            self.definition = definition

    def rechercher(self, mot):
        """
        Recherche la définition d'un mot dans l'arbre.
        Args:
            mot (str): Le mot à rechercher.
        Returns:
            str: La définition du mot si trouvé, sinon None.
        """
        if mot < self.mot:
            if self.gauche is None:
                return None
            return self.gauche.rechercher(mot)
        elif mot > self.mot:
            if self.droite is None:
                return None
            return self.droite.rechercher(mot)
        else:
            return self.definition
    
    def afficher(self):
        """
        Affiche tous les mots et leurs définitions dans l'arbre par ordre alphabétique.
        """
        if self.gauche is not None:
            self.gauche.afficher()
        print(self.mot, ":", self.definition)
        if self.droite is not None:
            self.droite.afficher()

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères du nœud.
        Returns:
            str: Le mot et sa définition sous forme de chaîne de caractères.
        """
        return self.mot + " : " + self.definition

    def __len__(self):
        """
        Retourne le nombre de nœuds dans l'arbre.
        Returns:
            int: Le nombre de nœuds dans l'arbre.
        """
        if self.gauche is None and self.droite is None:
            return 1
        nb_gauche = 0 if self.gauche is None else len(self.gauche)
        nb_droite = 0 if self.droite is None else len(self.droite)
        return nb_gauche + nb_droite + 1
    
    def supprimer (self, mot):
        """
        Supprime un mot de l'arbre.
        Args:
            mot (str): Le mot à supprimer.
        Returns:
            DicoABR: Le nœud mis à jour après suppression.
        """
        if mot < self.mot:
            if self.gauche is not None:
                self.gauche = self.gauche.supprimer(mot)
        elif mot > self.mot:
            if self.droite is not None:
                self.droite = self.droite.supprimer(mot)
        else:
            if self.gauche is None:
                return self.droite
            if self.droite is None:
                return self.gauche
    