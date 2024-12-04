from collections import deque

class Arbre:
    def __init__(self, valeur):
        self.gauche = None
        self.droite = None
        
        self.valeur = valeur
    
    def taille(self):
        taille = 0
        if self is None:
            return 0
        if self.gauche is not None:
            taille += self.gauche.taille()
        
        if self.droite is not None:
            taille += self.droite.taille()

        return taille+1
    
    def profondeur(self):
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
        if self is not None:print(self.valeur)
        if self.gauche: self.gauche.parcours_prefixe()
        if self.droite: self.droite.parcours_prefixe()            

    def parcours_infixe(self):
        if self.gauche: self.gauche.parcours_infixe()
        if self is not None: print(self.valeur)
        if self.droite: self.droite.parcours_infixe()

    def parcours_postfixe(self):
        if self.gauche: self.gauche.parcours_postfixe()
        if self.droite: self.droite.parcours_postfixe()
        if self is not None: print(self.valeur)
            
    def parcours_largeur(self):
        if self is None: return
        
        file = deque([self])
        while file:
            noeud = file.popleft()
            print(noeud.valeur)
            if noeud.gauche: file.append(noeud.gauche)
            if noeud.droite: file.append(noeud.droite)