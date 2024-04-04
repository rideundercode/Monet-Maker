# Groupe de brahim_y 1010476

README.md

## Étape 3: Zhang GUI - Animation des Contours d'Image

Ce script Python utilise la bibliothèque Turtle pour créer une animation dessinant les contours d'une image au fur et à mesure. Avant de dessiner les contours, l'image est traitée avec l'étape précédente, "Salé Vador Dali", pour améliorer l'isolation des contours en appliquant un flou gaussien.

### Dépendances

Ce script utilise les bibliothèques suivantes :

- `Turtle` : Utilisé pour créer une animation graphique des contours. Turtle est une bibliothèque graphique simple à manipuler, adaptée à ce projet d'animation pixel par pixel.

- `PIL` (Python Imaging Library) : Utilisé pour capturer l'animation et générer l'image finale. Cette bibliothèque permet de sauvegarder l'animation créée avec Turtle en tant qu'image.

### Approche

1. **Normalisation des Coordonnées :** Les coordonnées des pixels sont normalisées pour les adapter à l'écran Turtle, garantissant un rendu précis des contours à l'échelle de la fenêtre graphique.

2. **Animation des Contours :** Chaque pixel du tableau des contours est parcouru, et si le pixel est noir (représentant un contour), il est dessiné à l'écran Turtle. L'algorithme parcourt ainsi l'image pixel par pixel, dessinant les contours au fur et à mesure.

3. **Animation en Temps Réel :** Pendant le dessin des contours, l'animation est mise à jour après un certain nombre de pixels dessinés, contrôlé par la variable vitesse_dessin. Cela permet un affichage en temps réel à l'écran, offrant une meilleure expérience visuelle à l'utilisateur.

4. **Capture de l'Animation :** Une fois l'animation terminée, elle est capturée à l'aide de la bibliothèque Pillow (PIL). Cela génère une image finale haute résolution représentant les contours dessinés à l'écran.

### Utilisation du programme

Pour utiliser le programme, exécutez le fichier `zhang_gui.py` en lui passant le chemin d'accès complet à l'image que vous souhaitez traiter en tant qu'argument. Par exemple :

```bash
python zhang_gui.py licorne.png
```

Le programme demandera d'abord si vous souhaitez appliquer un flou gaussien à l'image. Si oui, il vous demandera ensuite l'intensité du flou. Ensuite, vous pouvez spécifier la vitesse de l'animation. Lorsque le programme est exécuté, il affiche les contours de l'image spécifiée en noir sur un fond blanc et attend que vous appuyiez sur une touche pour fermer la fenêtre.

Assurez-vous d'avoir installé les dépendances `pip install -r requirements.txt` et de fournir le chemin d'accès correct à l'image lors de l'exécution du programme. Si le fichier image n'existe pas ou est corrompu, le programme affichera un message d'erreur approprié.

N'hésitez pas à utiliser ce script pour créer des animations de contours pour d'autres images en spécifiant simplement leur chemin lors de l'exécution du script.
