import networkx as nx
import matplotlib.pyplot as plt

class Graph_dict:
    def __init__(self):
        self.graph = {}
    
    def ajouter_sommet(self, s):
        if s not in self.graph:
            self.graph[s] = []
    
    def ajouter_arete(self, s1, s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        if s2 not in self.graph[s1]:
            self.graph[s1].append(s2)
            self.graph[s2].append(s1)

    def arete(self, s1, s2):
        return s2 in self.graph[s1]
    
    def supprimer_arete(self, s1, s2):
        if self.arete(s1, s2):
            self.graph[s1].remove(s2)
            self.graph[s2].remove(s1)

    def sommets(self):
        return list(self.graph.keys())
    
    def voisins(self, s):
        return self.graph[s]
    
    def __str__(self):
        G = nx.Graph()
        for s in self.sommets():
            G.add_node(s)
            for v in self.voisins(s):
                G.add_edge(s, v)
        nx.draw(G, with_labels=True)
        plt.show()


def exemple():
    g = Graph_dict()
    g.ajouter_arete("A","B")
    g.ajouter_arete("A","D")
    g.ajouter_arete("B","C")
    g.ajouter_arete("D","B")
    g.ajouter_arete("D","C")

    print("Sommets du graphe:",g.sommets())
    print("Voisins de A:",g.voisins("A"))
    print("Voisins de B:",g.voisins("B"))
    g.supprimer_arete("B","D")
    print("Voisins de B:",g.voisins("B"))
    print(g)



def Exo2():
    h = Graph_dict()
    h.ajouter_arete("b","a")
    h.ajouter_arete("a","c")
    h.ajouter_arete("c","d")
    h.ajouter_arete("b","d")
    h.ajouter_arete("d", "e")
    h.ajouter_arete("b","e")
    h.ajouter_arete("e","g")
    h.ajouter_arete("g","f")
    h.ajouter_arete("e","f")
    h.ajouter_arete("g","h")
    print(h)



# Ecrire des fonctions qui renvoient:

# 1. l'ordre d'un graphe passé en paramètre
# 2. le nombre d'arêtes d'un graphe passé en paramètre
# 3. le degré d'un sommet passé en paramètre
# 4. le sommet de plus haut degré et le degré associé d'un graphe passé en paramètre
    

def ordre(graph):
    return len(graph.sommets())

def nb_aretes(graph):
    nb = 0
    for i in g.sommets():
        nb += len(graph.voisins(i))
    return nb//2

def degre(graph,sommet):
    return len(graph.voisins(sommet))

def plus_haut_degre(graph):
    degMax = 0
    sommet = graph.sommet()[0]
    for sommetItt in graph.sommet():
        if degre(graph,sommetItt) > degMax:
            degMax = degre(graph, sommetItt)
            sommet = sommetItt
    return (sommet, degMax)




class Graph_mat:
    def __init__(self,n : int):
        self.n = n
        self.adj = [[0]*n for _ in range(n)]
    
    def ajouter_arete(self, s1, s2):
        self.adj[s1][s2] = 1
        self.adj[s2][s1] = 1

    def supprimer_arete(self, s1, s2):
        self.adj[s1][s2] = 0
        self.adj[s2][s1] = 0
    
    def arete(self, s1, s2):
        return (self.ajd[s1][s2] == 1)
    
    def voisins(self, s):
        list_voisins = []
        for t in range(self.n):
            if self.adj[s][t] == 1:
                list_voisins.append(t)
        return list_voisins
    
    def __str__(self):
        G = nx.Graph()
        for s1 in range(self.n):
            for s2 in self.voisins(s1):
                G.add_edge(s1,s2)
        nx.draw(G, with_labels=True, node_color="skyblue")
        plt.show()
        return ""



g = Graph_mat(4)
g.ajouter_arete(0,1)
g.ajouter_arete(0,3)
g.ajouter_arete(1,2)
g.ajouter_arete(3,1)
print(g)



