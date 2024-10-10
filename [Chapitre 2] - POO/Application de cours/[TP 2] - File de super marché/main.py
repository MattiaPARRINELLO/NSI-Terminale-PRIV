from file import File
from client import Client
from caisse import Caisse

#
# TP 2 du chapitre 2 (p44)
# Un supermarché à plusieurs caisses
#

from random import random
from math import exp, factorial

#
# Insérer ou importer ici la classe File
#

#
# Insérer ou importer ici la classe Client
#

#
# Insérer ou importer ici la classe Caisse
#

#
# Classe auxiliaire pour calculer les distributions aléatoires.
# Il n'est pas nécessaire de lire ni de comprendre ce code.
#
class Distribution:
    """ Cette classe représente une distribution de probabilité """
    def poisson(self, lambda_, n=5):
        """ Calcule la fonction de repartition de la Loi de Poisson pour lambda donne et k = 1 a n """
        self.cdf = [0.0] * n
        cumul = 0
        for k in range(n):
            p = lambda_**k * exp(-lambda_) / factorial(k)
            cumul += p
            self.cdf[k] = cumul
        return self

    def exp(self, mu, n=50):
        """ Calcule la fonction de repartition de la Loi Exponentielle pour mu donne et k = 1 a n """
        self.cdf = [1 - exp(-mu * k) for k in range(n)]
        return self
    
    def get(self):
        """ Donne une valeur aleatoire en fonction de la fonction de repartition """
        p = random()
        for i in range(len(self.cdf)):
            if self.cdf[i] > p:
                return i
        return len(self.cdf)

#
# Classe qui pilote la simulation
#
class Simulation:
    def __init__(self, flux_moyen, nb_moyen_articles):
        # initialise les distributions de probabilité selon les paramètres
        # Ces distributions sont utilisées seulement dans les méthodes nb_arrivees et nb_articles
        self.poisson_distr = Distribution().poisson(flux_moyen)
        self.exp_distr = Distribution().exp(1.0/nb_moyen_articles)

    def nb_arrivees(self):
        """ Retourne le nombre d'arrivees pendant un pas de temps.
            On utilise des arrivees poissonniennes.
        """
        return 1 + self.poisson_distr.get()
    
    def nb_articles(self):
        """ Retourne le nombre d'articles d'un client qui arrive a la file d'attente.
            Ce nombre suit une loi exponentielle.
        """
        return 1 + self.exp_distr.get() # au moins un article
    
    def simuler(self, n):
        """ Démarre la simulation et exécute n pas. """
        # Créer la file d'attente
        self.file = File()

        # Créer le caissier en lui passant la file d'attente
        self.caissier = Caisse(self.file)

        # Faire n pas de simulation
        for horloge in range(n):
            print('-- Horloge: '+str(horloge))
            self.pas(horloge)

    def pas(self, horloge):
        caisse = Caisse(File())
        nbClients = self.nb_arrivees()
        print('Arrivée de '+str(nbClients)+' clients')
        for _ in range(nbClients):
            self.file.enfiler(Client(self.nb_articles()))
            caisse.nouveau_client(self.nb_articles())   
            
        print('File: '+str(self.file))
        self.caissier.pas()
        #
        # À COMPLÉTER
        #   - obtenir le nombre de nouveaux clients
        #   - ajouter chaque nouveau client à la file avec son nombre d'articles
        #   - faire travailler le caissier
        #

# Lancer une simulation
sim = Simulation(0.3, 8)
sim.simuler(100)      