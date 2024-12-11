from collections import deque

class Arbre: 
    """
    Classe représentant un arbre binaire.
    Attributs:
    ----------
    gauche : Arbre
        Sous-arbre gauche.
    droite : Arbre
        Sous-arbre droit.
    valeur : any
        Valeur du noeud.
    Méthodes:
    ---------
    __init__(valeur):
    taille():
    profondeur():
    inserer(valeur):
    inserer_direction(valeur, direction="gauche"):
    parcours_prefixe():
    parcours_infixe():
    parcours_postfixe():
    parcours_largeur():
    est_feuille():
    nombre_feuilles():
    """
    def __init__(self, valeur):
        """
        Initialise un nouveau nœud avec une valeur donnée.
        Args:
            valeur: La valeur à stocker dans le nœud.
        """

        self.gauche = None
        self.droite = None
        
        self.valeur = valeur
    
    def taille(self):
        """
        Calcule la taille de l'arbre binaire.
        La taille de l'arbre est définie comme le nombre total de nœuds dans l'arbre.
        Returns:
            int: La taille de l'arbre binaire.
        """

        taille = 0
        if self is None:
            return 0
        if self.gauche is not None:
            taille += self.gauche.taille()
        
        if self.droite is not None:
            taille += self.droite.taille()

        return taille+1
    
    def profondeur(self):
        """
        Calcule la profondeur de l'arbre binaire.
        La profondeur d'un arbre binaire est définie comme la longueur du chemin le plus long
        de la racine à une feuille. Une feuille est un nœud sans enfants.
        Returns:
            int: La profondeur de l'arbre binaire. Si l'arbre est vide, retourne 0.
        """

        if self is None:
            return 0
        if self.gauche is not None:
            profondeur_gauche = self.gauche.profondeur()
        else:
            profondeur_gauche = 0
        if self.droite is not None:
            profondeur_droite = self.droite.profondeur()
        else:
            profondeur_droite = 0
        return max(profondeur_gauche, profondeur_droite) + 1
    
    def inserer(self, valeur):
        """
        Insère une nouvelle valeur dans l'arbre en respectant l'équilibre des sous-arbres gauche et droit.
        Si le sous-arbre gauche a moins de nœuds ou un nombre égal de nœuds par rapport au sous-arbre droit,
        la nouvelle valeur est insérée dans le sous-arbre gauche. Sinon, elle est insérée dans le sous-arbre droit.
        Args:
            valeur: La valeur à insérer dans l'arbre.
        """

        nouveau_noeud = Arbre(valeur)

        nb_gauche = -1 if self.gauche is None else self.gauche.taille()
        nb_droite = -1 if self.droite is None else self.droite.taille()

        if nb_gauche <= nb_droite:
            ancien_fils = self.gauche

            self.gauche = nouveau_noeud

            nouveau_noeud.gauche = ancien_fils

        else:
            ancien_fils = self.droite

            self.droite = nouveau_noeud

            nouveau_noeud.droite = ancien_fils

    def inserer_direction(self, valeur, direction="gauche"):
        """
        Insère un nouveau noeud dans l'arbre dans la direction spécifiée.
        Args:
            valeur: La valeur du nouveau noeud à insérer.
            direction (str): La direction dans laquelle insérer le nouveau noeud, soit "gauche" soit "droite". 
                             Par défaut, la direction est "gauche".
        Returns:
            str: Un message d'erreur si la direction n'est pas valide.
        Exemple:
            >>> arbre = Arbre(10)
            >>> arbre.inserer_direction(5, "gauche")
            >>> arbre.inserer_direction(15, "droite")
        """

        nouveau_noeud = Arbre(valeur)
        if direction == "gauche":
            ancien_fils = self.gauche
            self.gauche = nouveau_noeud
            
            nouveau_noeud.gauche = ancien_fils
        elif direction == "droite":
            ancien_fils = self.droite
            self.droite = nouveau_noeud
            nouveau_noeud.droite = ancien_fils
        else:
            print("Mauvaise direction")
            return '[ERROR] Not a valid direction'
                
    def parcours_prefixe(self):
        """
        Parcours l'arbre en utilisant l'ordre préfixe (pré-ordre).
        Cette méthode affiche la valeur du nœud courant, puis 
        récursivement les valeurs des sous-arbres gauche et droit.
        Exemple de parcours préfixe:
        - Pour un arbre avec la structure suivante:
              1
             / \
            2   3
           / \
          4   5
        Le parcours préfixe affichera: 1, 2, 4, 5, 3
        """
        
        if self is not None:print(self.valeur)
        if self.gauche: self.gauche.parcours_prefixe()
        if self.droite: self.droite.parcours_prefixe()            

    def parcours_infixe(self):
        """
        Effectue un parcours infixe de l'arbre binaire et affiche les valeurs des nœuds.
        Un parcours infixe visite les nœuds dans l'ordre suivant :
        1. Sous-arbre gauche
        2. Nœud courant
        3. Sous-arbre droit
        Cette méthode affiche les valeurs des nœuds dans l'ordre croissant si l'arbre est un arbre binaire de recherche.
        """

        if self.gauche: self.gauche.parcours_infixe()
        if self is not None: print(self.valeur)
        if self.droite: self.droite.parcours_infixe()

    def parcours_postfixe(self):
        """
        Effectue un parcours postfixé (post-order) de l'arbre binaire.
        Un parcours postfixé visite les nœuds dans l'ordre suivant :
        1. Sous-arbre gauche
        2. Sous-arbre droit
        3. Nœud courant
        Si le nœud courant a un sous-arbre gauche, il appelle récursivement
        la méthode parcours_postfixe sur ce sous-arbre.
        Si le nœud courant a un sous-arbre droit, il appelle récursivement
        la méthode parcours_postfixe sur ce sous-arbre.
        Enfin, il affiche la valeur du nœud courant.
        """
        
        if self.gauche: self.gauche.parcours_postfixe()
        if self.droite: self.droite.parcours_postfixe()
        if self is not None: print(self.valeur)
            
    def parcours_largeur(self):
        """
        Parcours l'arbre en largeur et affiche la valeur de chaque nœud.
        Cette méthode utilise une file (deque) pour parcourir l'arbre en largeur.
        Elle commence par le nœud courant (self) et visite chaque nœud niveau par niveau.
        Pour chaque nœud visité, sa valeur est affichée, puis ses enfants gauche et droit
        sont ajoutés à la file pour être visités à leur tour.
        Returns:
            None
        """

        if self is None: return 
        file = deque([self])
        while file:
            noeud = file.popleft()
            print(noeud.valeur)
            if noeud.gauche: file.append(noeud.gauche)
            if noeud.droite: file.append(noeud.droite)

    def est_feuille(self):
        """
        Vérifie si le nœud est une feuille.
        Une feuille est un nœud qui n'a pas d'enfants, c'est-à-dire ni enfant gauche ni enfant droit.
        Returns:
            bool: True si le nœud est une feuille, False sinon.
        """

        return not self.gauche and not self.droite
    
    def nombre_feuilles(self):
        """
        Calcule le nombre de feuilles dans l'arbre.
        Une feuille est un nœud qui n'a pas d'enfants (ni gauche ni droite).
        Returns:
            int: Le nombre de feuilles dans l'arbre.
        """

        if self is None:
            return 0
        if self.est_feuille():
            return 1
        else:
            nb_gauche = 0 if self.gauche is None else self.gauche.nombre_feuilles()
            nb_droite = 0 if self.droite is None else self.droite.nombre_feuilles()
            return nb_gauche + nb_droite
        
