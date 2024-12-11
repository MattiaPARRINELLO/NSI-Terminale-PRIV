# Réponses aux questions


## 1. La propriété fondamentale des ABR
#### Exercice 1
1. Cet arbre est valide car il respecte bien la regle donnée ci dessus. $$3<5<8$$ $$1<3$$  $$6<8<9$$
2. 
    a. 2
    b. Aucune 

## 2. Algotithme fondamentaux 
### 2.1 Recherche guidée 
1. 
    a. 14: 8 -> 10 -> 14 (trouvé)
    b. 4: 9 -> 3 -> 6 -> Fin arbre (Non trouvé)
2. `Voir fichier Fondamentaux.py` 
### 2.2 Insertion guidée
1. Insertion de 4:
```
       8
      / \
     3   10
    / \    \
   1   6    14
      /
     4
```
Apres 9:

```
       8
      / \
     3   10
    / \  /  \
   1   6 9   14
      /
     4
```
Après 2 :
```
       8
      / \
     3   10
    / \  /  \
   1   6 9   14
  /   /
 2   4
```

2.  Pour 4 : 
    - 4 < 8 : aller à gauche
    - 4 > 3 : aller à droite
    - 4 < 6 : aller à gauche
    - Place trouvée !

    Pour 9 :
    - 9 > 8 : aller à droite
    - 9 < 10 : aller à gauche
    - Place trouvée !

    Pour 2 :
    - 2 < 8 : aller à gauche
    - 2 < 3 : aller à gauche
    - 2 > 1 : aller à droite
    - Place trouvée !

3. `Voir fichier Fondamentaux.py`

### 2.3 Exercice de synthèse 
1. Insertion de 5:
```
    5
```
Chemin parcouru: -
Nombre de comparaisons: 0

2. Insertion de 3:
```
    5
 /
3
```
Chemin parcouru: 5 -> gauche
Nombre de comparaisons: 1

3. Insertion de 7:
```
    5
 / \
3   7
```
Chemin parcouru: 5 -> droite
Nombre de comparaisons: 1

4. Insertion de 1:
```
    5
 / \
3   7
/
1
```
Chemin parcouru: 5 -> gauche -> 3 -> gauche
Nombre de comparaisons: 2

5. Insertion de 4:
```
    5
 / \
3   7
/ \
1   4
```
Chemin parcouru: 5 -> gauche -> 3 -> droite
Nombre de comparaisons: 2

6. Insertion de 6:
```
    5
 / \
3   7
/ \  /
1   4 6
```
Chemin parcouru: 5 -> droite -> 7 -> gauche
Nombre de comparaisons: 2

7. Insertion de 8:
```
    5
 / \
3   7
/ \  / \
1   4 6  8
```
Chemin parcouru: 5 -> droite -> 7 -> droite
Nombre de comparaisons: 2

8. Recherche de la valeur 6:
Chemin parcouru: 5 -> droite -> 7 -> gauche -> 6 (trouvé)
Nombre de comparaisons: 3

9. Recherche de la valeur 2:
Chemin parcouru: 5 -> gauche -> 3 -> gauche -> 1 -> droite (non trouvé)
Nombre de comparaisons: 4




## 3. Mini Projet : Implémentation d'un dictionnaire
`Voir dictionnaire.py`

