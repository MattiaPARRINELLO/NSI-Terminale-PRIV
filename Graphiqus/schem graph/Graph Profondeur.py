from manim import *

class GraphTraversal(Scene):
    def construct(self):
        # --- TITRE ---
        text = Text("Parcours Graphe Profondeur").scale(1.5).set_color_by_gradient(BLUE, GREEN)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))
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

        # Définir la structure du graphe pour les parcours
        graph = {
            'A': ['B', 'C', 'D'],
            'B': ['A', 'D'],
            'C': ['A', 'D', 'E'],
            'D': ['A', 'B', 'C', 'F'],
            'E': ['C', 'F'],
            'F': ['D', 'E']
        }

        # Fonction d'affichage dynamique de la liste de parcours
        def update_traversal_list(visited, title):
            traversal_list = Text(", ".join(visited)).to_edge(DOWN)
            self.play(Write(traversal_list))
            traversal_text = None
            return traversal_text, traversal_list

        # --- PARCOURS EN PROFONDEUR (DFS) ---
        visited_dfs = []
        stack = ["A"]
        traversal_text, traversal_list = update_traversal_list([], "DFS Parcours :")

        while stack:
            current = stack.pop()
            if current not in visited_dfs:
                visited_dfs.append(current)
                self.play(vertices[current].animate.set_color(GREEN), Circumscribe(vertices[current], color=GREEN, buff=1))

                # Mettre à jour la liste des sommets visités
                new_traversal_list = Text(", ".join(visited_dfs)).to_edge(DOWN) 
                self.play(FadeOut(traversal_list), Write(new_traversal_list))
                traversal_list = new_traversal_list

                # Ajouter les voisins non visités à la pile
                neighbors = [n for n in graph[current] if n not in visited_dfs]
                for neighbor in neighbors:
                    stack.append(neighbor)

        self.wait(1)

        # --- RÉINITIALISATION ---
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.wait(1)


        # ----------------- PARCOURS EN LARGEUR (BFS) -----------------
        # --- TITRE ---
        text = Text("Parcours Graphe Largeur").scale(1.5).set_color_by_gradient(BLUE, GREEN)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))

        # --- Initialisation ---
        # Position des sommets
        positions = {
            'A': [-3, 2, 0], 'B': [3, 2, 0],
            'C': [-3, -1, 0], 'D': [3, -1, 0],
            'E': [-4, -3, 0], 'F': [4, -3, 0]
        }        

        # Sommets et arêtes
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

        # Définir la structure du graphe pour les parcours
        graph = {
            'A': ['B', 'C', 'D'],
            'B': ['A', 'D'],
            'C': ['A', 'D', 'E'],
            'D': ['A', 'B', 'C', 'F'],
            'E': ['C', 'F'],
            'F': ['D', 'E']
        }

        # Fonction d'affichage dynamique de la liste de parcours
        def update_traversal_list(visited, title):
            traversal_list = Text(", ".join(visited)).to_edge(DOWN)
            self.play(Write(traversal_list))
            traversal_text = None
            return traversal_text, traversal_list
        
        # --- PARCOURS EN LARGEUR (BFS) ---
        visited_bfs = []
        queue = ["A"]
        traversal_text, traversal_list = update_traversal_list([], "BFS Parcours :")

        while queue:
            current = queue.pop(0)
            if current not in visited_bfs:
                visited_bfs.append(current)
                self.play(vertices[current].animate.set_color(GREEN), Circumscribe(vertices[current], color=GREEN, buff=1))

                # Mettre à jour la liste des sommets visités
                new_traversal_list = Text(", ".join(visited_bfs)).to_edge(DOWN)
                self.play(FadeOut(traversal_list), Write(new_traversal_list))
                traversal_list = new_traversal_list

                # Ajouter les voisins non visités à la file
                neighbors = [n for n in graph[current] if n not in visited_bfs]
                for neighbor in neighbors:
                    queue.append(neighbor)

        self.wait(1)

        
            



       
