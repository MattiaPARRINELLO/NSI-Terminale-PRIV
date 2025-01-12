from manim import *

class GraphTraversal(Scene):
    def construct(self):
        # Définir les positions des sommets
        positions = {
            'A': [-3, 2, 0], 'B': [3, 2, 0],
            'C': [-3, -1, 0], 'D': [3, -1, 0],
            'E': [-4, -3, 0], 'F': [4, -3, 0]
        }

        # Définir les sommets et arêtes
        vertices = {v: Dot(positions[v], radius=0.2, color=BLUE) for v in positions}
        labels = {v: Text(v).next_to(vertices[v], UP) for v in vertices}
        edges = [
            ('A', 'B'), ('A', 'C'), ('A', 'D'),
            ('B', 'D'), ('C', 'D'), ('C', 'E'),
            ('E', 'F'), ('D', 'F')
        ]

        # Créer les arêtes (clé ordonnée pour éviter les erreurs)
        edge_lines = {
            tuple(sorted((u, v))): Line(vertices[u].get_center(), vertices[v].get_center(), color=GRAY)
            for u, v in edges
        }

        # Ajouter les sommets et les arêtes à la scène
        self.play(*[Create(edge_lines[e]) for e in edge_lines])
        self.play(*[Create(vertices[v]) for v in vertices], *[Write(labels[v]) for v in labels])

        # Ajouter une liste du parcours en bas de l'image
        traversal_text = Text("Parcours :").to_edge(DOWN)
        traversal_list = Text("").next_to(traversal_text, RIGHT)
        self.play(Write(traversal_text), Write(traversal_list))

        # Définir la structure du graphe pour le parcours
        graph = {
            'A': ['B', 'C', 'D'],
            'B': ['A', 'D'],
            'C': ['A', 'D', 'E'],
            'D': ['A', 'B', 'C', 'F'],
            'E': ['C', 'F'],
            'F': ['D', 'E']
        }

        # Animation pour le parcours DFS
        visited = []
        stack = ['A']
        tree_edges = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                self.play(vertices[current].animate.set_color(GREEN))
                
                # Mettre à jour la liste des sommets visités
                updated_text = ", ".join(visited)
                new_traversal_list = Text(updated_text).next_to(traversal_text, RIGHT)
                self.play(Transform(traversal_list, new_traversal_list))
                traversal_list = new_traversal_list

                # Récupérer les voisins non visités
                neighbors = [n for n in graph[current] if n not in visited]
                for neighbor in neighbors:
                    stack.append(neighbor)
                    tree_edges.append(tuple(sorted((current, neighbor))))  # Utiliser une clé ordonnée
                
                # Créer les animations pour les arêtes
                edge_animations = [
                    edge_lines[tuple(sorted((current, n)))].animate.set_color(GREEN)
                    for n in neighbors
                ]
                
                # Jouer les animations si elles existent
                if edge_animations:
                    self.play(*edge_animations)

        self.wait(2)
