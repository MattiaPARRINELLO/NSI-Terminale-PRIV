from element import Element
class liste_chainee():
    def __init__(self):
        self.premier = None # Premier chainon de la liste

    def est_vide(self): # Vérifier si la liste est vide
        return self.premier == None

    def tete(self): # Retourner la valeur du premier chainon
        if self.premier == None: # Si la liste est vide
            return None
        else: # Sinon
            return self.premier.valeur
        
    def vider(self): # Vider la liste
        self.premier = None

    def retirer_index(self, index): # Retirer un chainon de la liste a partir de son index
        index = int(index)
        if len(self) == 0: # Si la liste est vide
            return None
        if len(self) >= index:
            actuel = self.premier
            if index == 0:
                self.premier = actuel.suivant
            else:
                for i in range(index - 1):
                    actuel = actuel.suivant
                actuel.suivant = actuel.suivant.suivant
        else:
            return None
    
    def retirer_valeur(self, valeur): # Retirer un chainon de la liste a partir de sa valeur
        if len(self) == 0: # Si la liste est vide
            return None
        actuel = self.premier
        if actuel.valeur == valeur:
            self.premier = actuel.suivant
        else:
            while actuel.suivant != None:
                if actuel.suivant.valeur == valeur:
                    actuel.suivant = actuel.suivant.suivant
                    return None
                actuel = actuel.suivant
        return None
    

    def queue(self): # Retourner les valeures de la liste sans la première
        if len(self) <= 1 : # Si la liste est vide
            return None
        else: # Sinon
            actuel = self.premier # On se place sur le premier chainon
            liste = [] # On crée une liste vide
            while actuel.suivant != None: # Tant qu'on n'est pas à la fin de la liste
                liste.append(actuel.valeur) # On ajoute la valeur du chainon à la liste
                actuel = actuel.suivant # On passe au chainon suivant
            liste.append(actuel.valeur) # On ajoute la valeur du dernier chainon à la liste
            liste.pop(0) # On enlève la première valeur

            return liste # On retourne la liste
    
    def fin(self): # Retourner la valeur du dernier chainon
        actuel = self.premier
        while actuel.suivant != None:
            actuel = actuel.suivant
        return actuel.valeur

    def ajouter(self, valeur): # Ajouter un chainon à la fin de la liste
        if len(self) == 0: # Si la liste est vide
            self.premier = Element(valeur) # On crée un chainon
        else: # Sinon
            actuel = self.premier # On se place sur le premier chainon
            while actuel.suivant != None: # Tant qu'on n'est pas à la fin de la liste
                actuel = actuel.suivant # On passe au chainon suivant
            actuel.suivant = Element(valeur) # On crée un chainon à la fin de la liste

    def ajouter_entete(self, valeur): # Ajouter un chainon au début de la liste
        if len(self) == 0: # Si la liste est vide
            self.premier = Element(valeur) # On crée un chainon
        else: # Sinon
            actuel = self.premier # On se place sur le premier chainon
            self.premier = Element(valeur) # On crée un chainon
            self.premier.suivant = actuel # On relie le nouveau chainon au premier chainon

    def ajouter_index(self, valeur, index): # Ajouter un chainon à un index donné
        index = int(index)
        if len(self) == 0: # Si la liste est vide
            self.premier = Element(valeur) # On crée un chainon
        elif len(self) >= index:
            actuel = self.premier
            if index == 0:
                self.premier = Element(valeur)
                self.premier.suivant = actuel
            else:
                for i in range(index - 1):
                    actuel = actuel.suivant
                actuel.suivant = Element(valeur)
                actuel.suivant.suivant = actuel.suivant.suivant
        else:
            return None
        

    def __str__(self): # Afficher la liste
        actuel = self.premier # On se place sur le premier chainon
        chaine = "" # On crée une chaine vide
        if len(self) == 0: # Si la liste est vide
            return "None" # On retourne None
        while actuel != None: # Tant qu'on n'est pas à la fin de la liste
            chaine += str(actuel.valeur) + " -> " # On ajoute la valeur du chainon à la chaine
            actuel = actuel.suivant # On passe au chainon suivant
        return chaine + "None" # On retourne la chaine
    
    def __len__(self): # Retourner la longueur de la liste
        
        actuel = self.premier # On se place sur le premier chainon
        length = 0 # On initialise la longueur à 0
        if actuel == None: # Si la liste est vide
            return 0 # On retourne 0
        while actuel != None: # Tant qu'on n'est pas à la fin de la liste
            length += 1 # On incrémente la longueur
            actuel = actuel.suivant # On passe au chainon suivant
        return length # On retourne la longueur
