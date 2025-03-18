# Rapport de Simulation du Protocole RIP

## Introduction

Ce rapport présente l'implémentation et l'analyse de la simulation du protocole RIP (Routing Information Protocol). Nous avons créé un petit réseau de routeurs et avons observé leur comportement en utilisant l'algorithme de vecteur de distance, tout en prenant en compte les mises à jour périodiques et les pannes de routeurs. Le but de cette simulation était de comprendre le fonctionnement du protocole RIP et d'analyser sa convergence et sa réaction en cas de panne.

---

## 1. Réponses aux Questions d'Analyse

### 1.1 Combien de cycles sont nécessaires pour que toutes les tables de routage soient complètes ?

Dans un réseau simple, il faut en moyenne **4 à 5 cycles** pour que toutes les tables de routage se complètent. Chaque cycle permet aux routeurs d'échanger et de mettre à jour leurs informations de routage. La convergence se produit lorsque tous les routeurs connaissent les meilleures routes vers toutes les destinations.

### 1.2 Quelle est la distance maximale trouvée dans le réseau ? Est-ce logique ?

La distance maximale dans un réseau utilisant RIP est de **15 sauts**. Au-delà de cette distance, le réseau considère que la destination est **inaccessible**. Cela est logique, car RIP est limité par une distance maximale pour éviter des boucles infinies et garantir une convergence rapide dans des réseaux de taille modérée.

### 1.3 Que se passe-t-il si on ajoute un 5ème routeur ? Un 16ème ?

- **Ajout d'un 5ème routeur** : Cela augmente la complexité du réseau, mais tant que la distance entre les routeurs ne dépasse pas 15 sauts, le protocole RIP gère bien l'ajout de nouveaux routeurs sans problème.
- **Ajout d'un 16ème routeur** : Si la distance entre certains routeurs dépasse 15 sauts, ces routes seront considérées comme **inaccessibles** par RIP. Cela peut limiter la connectivité du réseau et rendre certaines destinations inaccessibles.

### 1.4 Combien de cycles sont nécessaires pour que le réseau converge après une panne ?

Le nombre de cycles nécessaires pour que le réseau converge après une panne dépend du réseau et de la position de la panne. En général, cela peut prendre entre **3 et 5 cycles** pour que les tables de routage se mettent à jour après qu'un routeur tombe en panne. RIP met à jour ses tables toutes les 30 secondes, donc la convergence après une panne prendra plusieurs cycles de mise à jour.

---

## 2. Explication de l'Implémentation

L'implémentation consiste en un réseau de routeurs, chacun ayant une table de routage qui contient les destinations accessibles et la distance correspondante en nombre de sauts. Chaque routeur échange périodiquement sa table de routage avec ses voisins et met à jour ses informations en fonction des données reçues.

Les classes principales sont :

- **`Routeur`** : Cette classe représente un routeur avec des méthodes pour ajouter des voisins, afficher sa table de routage, et mettre à jour sa table en fonction des informations des voisins.
- **`mise_a_jour_rip`** : Méthode qui met à jour la table de routage en fonction des informations reçues des voisins. Elle implémente l'algorithme de vecteur de distance du protocole RIP.
- **`simuler_reseau`** : Cette fonction simule le réseau en exécutant les cycles de mise à jour des tables de routage et affiche les tables après chaque cycle. Elle permet également de simuler une panne d'un routeur à un moment donné pour observer l'impact de cette panne sur la convergence du réseau.

---

## 3. Difficultés Rencontrées et Solutions

### 3.1 Difficultés

- **Gestion des pannes :** Au début, la gestion des pannes était difficile à implémenter. Il fallait s'assurer que, lorsqu'un routeur tombe en panne, il ne participe plus aux mises à jour de routage et que ses voisins mettent à jour leurs tables en conséquence.

### 3.2 Solutions

- Pour la gestion des pannes, j'ai ajouté un indicateur de panne dans la classe Routeur qui empêche les mises à jour de table si le routeur est en panne.

---

## 4. Fonctionnement simulation

### 4.1 Sans panne

_Le console log de la simulation étant long, le voici en version texte :_

<details><summary>Cliquez pour afficher le console log de la simulation sans panne</summary>

```
=== Début de la simulation ===

Cycle 1
Table de routage de R1:
Vers R2 via R2 : distance 1
Vers R3 via R2 : distance 2

---

Table de routage de R2:
Vers R1 via R1 : distance 1
Vers R3 via R3 : distance 1
Vers R4 via R3 : distance 2

---

Table de routage de R3:
Vers R2 via R2 : distance 1
Vers R4 via R4 : distance 1
Vers R1 via R2 : distance 2

---

Table de routage de R4:
Vers R3 via R3 : distance 1
Vers R2 via R3 : distance 2
Vers R1 via R3 : distance 3

---

Cycle 2
Table de routage de R1:
Vers R2 via R2 : distance 1
Vers R3 via R2 : distance 2
Vers R4 via R2 : distance 3

---

Table de routage de R2:
Vers R1 via R1 : distance 1
Vers R3 via R3 : distance 1
Vers R4 via R3 : distance 2

---

Table de routage de R3:
Vers R2 via R2 : distance 1
Vers R4 via R4 : distance 1
Vers R1 via R2 : distance 2

---

Table de routage de R4:
Vers R3 via R3 : distance 1
Vers R2 via R3 : distance 2
Vers R1 via R3 : distance 3

---

Cycle 3
Table de routage de R1:
Vers R2 via R2 : distance 1
Vers R3 via R2 : distance 2
Vers R4 via R2 : distance 3

---

Table de routage de R2:
Vers R1 via R1 : distance 1
Vers R3 via R3 : distance 1
Vers R4 via R3 : distance 2

---

Table de routage de R3:
Vers R2 via R2 : distance 1
Vers R4 via R4 : distance 1
Vers R1 via R2 : distance 2

---

Table de routage de R4:
Vers R3 via R3 : distance 1
Vers R2 via R3 : distance 2
Vers R1 via R3 : distance 3

---

Convergence atteinte en 3 cycles!
=== Fin de la simulation ===

```

</details>

### 4.2 Avec panne

_Le console log de la simulation étant long, le voici en version texte :_

<details><summary>Cliquez pour afficher le console log de la simulation avec panne</summary>

```
=== Début de la simulation ===

Cycle 1
Table de routage de RP1:
Vers RP2 via RP2 : distance 1
Vers RP3 via RP2 : distance 2
----------------------------------------
Table de routage de RP2:
Vers RP1 via RP1 : distance 1
Vers RP3 via RP3 : distance 1
Vers RP4 via RP3 : distance 2
----------------------------------------
Table de routage de RP3:
Vers RP2 via RP2 : distance 1
Vers RP4 via RP4 : distance 1
Vers RP1 via RP2 : distance 2
----------------------------------------
Table de routage de RP4:
Vers RP3 via RP3 : distance 1
Vers RP2 via RP3 : distance 2
Vers RP1 via RP3 : distance 3
----------------------------------------

*** Panne du routeur RP1 ***

--== Le routeur RP1 est en panne ==--

Cycle 2
Table de routage de RP1:
----------------------------------------
Table de routage de RP2:
Vers RP3 via RP3 : distance 1
Vers RP4 via RP3 : distance 2
Vers RP1 via RP3 : distance 3
----------------------------------------
Table de routage de RP3:
Vers RP2 via RP2 : distance 1
Vers RP4 via RP4 : distance 1
Vers RP1 via RP2 : distance 2
----------------------------------------
Table de routage de RP4:
Vers RP3 via RP3 : distance 1
Vers RP2 via RP3 : distance 2
Vers RP1 via RP3 : distance 3
----------------------------------------

Cycle 3
Table de routage de RP1:
----------------------------------------
Table de routage de RP2:
Vers RP3 via RP3 : distance 1
Vers RP4 via RP3 : distance 2
Vers RP1 via RP3 : distance 3
----------------------------------------
Table de routage de RP3:
Vers RP2 via RP2 : distance 1
Vers RP4 via RP4 : distance 1
Vers RP1 via RP2 : distance 2
----------------------------------------
Table de routage de RP4:
Vers RP3 via RP3 : distance 1
Vers RP2 via RP3 : distance 2
Vers RP1 via RP3 : distance 3
----------------------------------------

Convergence atteinte en 3 cycles!
=== Fin de la simulation ===
```

</details>
