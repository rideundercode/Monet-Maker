# Groupe de brahim_y 1010476

README.md

## Étape 4: Renoir et Blanc - Dessin des Contours d'une Image

Ce script Python permet de créer un dessin artistique des contours d'une image en utilisant des techniques de détection de contours et l'approche du plus proche voisin.

### Dépendances

Ce script utilise les bibliothèques suivantes :

- `OpenCV` (cv2) : Une bibliothèque d'apprentissage automatique utilisée pour le traitement d'image.
- `NumPy` : Une bibliothèque Python pour le calcul numérique, utilisée pour les opérations sur les données des pixels.
- `Pillow`` (PIL) : Une bibliothèque de traitement d'images en Python, utilisée pour capturer l'image finale.
- `Turtle Graphics` : Une bibliothèque graphique pour créer l'interface de dessin.

### Approche

1. **Prétraitement de l'image :** Application d'un flou gaussien pour lisser l'image (optionnel).
2. **Détection des contours :** Utilisation de l'algorithme de détection de contours de Canny.
3. **Dessin des contours :** Utilisation de l'approche du plus proche voisin pour dessiner les contours de l'image.
4. **Affichage et Enregistrement :** L'image finale peut être affichée et enregistrée sur le disque.

### Utilisation du programme

Pour utiliser le programme, exécutez le fichier `renoir_blanc.py` en lui passant le chemin d'accès complet à l'image que vous souhaitez traiter en tant qu'argument. Par exemple :

```bash
python renoir_blanc.py licorne.png
```

##### Instructions :

1. Le programme demandera si vous souhaitez appliquer un flou à l'image. Répondez par "Oui" ou "Non".
   - Si vous choisissez "Oui", le programme demandera ensuite l'intensité du flou (un nombre entier positif).
   - Si vous choisissez "Non", l'image sera utilisée telle quelle sans flou.
2. Ensuite, spécifiez la vitesse de l'animation (un nombre entier positif) pour le dessin des contours. Cette valeur déterminera la rapidité avec laquelle l'animation est générée.

Assurez-vous d'avoir installé les dépendances `pip install -r requirements.txt` et de fournir le chemin d'accès correct à l'image lors de l'exécution du programme. Si le fichier image n'existe pas ou est corrompu, le programme affichera un message d'erreur approprié.

N'hésitez pas à utiliser ce script pour créer des animations de contours pour d'autres images en spécifiant simplement leur chemin lors de l'exécution du script.
