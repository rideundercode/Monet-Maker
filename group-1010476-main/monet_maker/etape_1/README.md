# Groupe de brahim_y 1010476

README.md

## Étape 1 : Big Fernand Léger

Ce projet vise à créer un agent capable de peindre un tableau à partir d'une image en utilisant Python. Pour ce faire, l'agent doit être capable de dessiner un sketch du tableau en isolant les contours des différents éléments qui composent l'image. Cette première étape se concentre sur le pré-processing de l'image et le calcul des contours à l'aide de l'algorithme de Canny.

### Installation des dépendances

Avant d'exécuter le programme, assurez-vous d'avoir installé les dépendances nécessaires. Vous pouvez le faire en utilisant le fichier `requirements.txt` fourni avec ce projet. Pour installer les dépendances, exécutez la commande suivante dans votre environnement virtuel ou système Python :

```bash
pip install -r requirements.txt
```

Le fichier `requirements.txt`` contient les dépendances requises pour cette étape, notamment :

### Dépendances

- `OpenCV` (cv2): est une bibliothèque open source pour le traitement d'images et l'apprentissage automatique. Elle est utilisée pour analyser l'image et en isoler les contours.
- `numpy` (np): est une bibliothèque open source pour le calcul scientifique. Elle est utilisée pour traiter les données des images.

### Justification des dépendances

- `opencv-python` : Il s'agit d'une version prête à l'emploi de la bibliothèque OpenCV pour Python. Nous l'utilisons pour les opérations de traitement d'images, telles que la détection de contours avec l'algorithme de Canny et d'autres fonctionnalités avancées.
- `numpy` : Cette bibliothèque est utilisée pour les calculs numériques, tels que les opérations sur les tableaux d'images. Elle est très efficace et largement utilisée dans le domaine du traitement d'images.

Nous utilisons la dépendance `opencv-python` spécifiquement, qui est une version prête à l'emploi d'OpenCV pour Python.

### Approche de détection des contours

La fonction `detecter_contours(image_path)` est le cœur de cette étape. Elle prend en paramètre le chemin de l'image à traiter et effectue les opérations suivantes :

1. **Vérification de l'existence du fichier image :** Avant de charger l'image, l'algorithme vérifie si le fichier image spécifié existe réellement à l'aide de `os.path.isfile()`. Si le fichier n'existe pas, un message d'erreur est affiché et la fonction se termine.

2. **Charger l'image :** L'algorithme charge l'image à partir du chemin spécifié en utilisant la bibliothèque OpenCV (`cv2.imread()`).

3. **Conversion en niveaux de gris :** Pour simplifier le traitement et se concentrer uniquement sur les variations d'intensité, l'image est convertie en niveaux de gris à l'aide de `cv2.cvtColor()`.

4. **Réduction du bruit :** Un filtre de flou gaussien est appliqué à l'image en niveaux de gris (`cv2.GaussianBlur()`) pour réduire le bruit indésirable et les détails superflus.

5. **Calcul des gradients d'intensité :** Les gradients d'intensité en direction x et y sont calculés à l'aide de l'opérateur de Sobel (`cv2.Sobel()`). Ces gradients seront utilisés ultérieurement pour la détection de contours.

6. **Définition des seuils d'hystérésis :** Les seuils d'hystérésis pour l'algorithme de Canny sont définis en fonction de la moyenne des valeurs de gris de l'image.

7. **Détection des contours avec Canny :** L'algorithme de Canny est appliqué à l'image prétraitée pour détecter les contours significatifs (`cv2.Canny()`).

8. **Inverse binary thresholding :** Un seuillage binaire inverse est appliqué aux contours détectés pour les afficher en noir sur un fond blanc.

9. **Affichage des contours :** Les contours détectés sont affichés à l'aide de `cv2.imshow()` pour permettre une vérification visuelle du résultat.

N'oubliez pas de consulter le fichier `requirements.txt` pour les dépendances requises et d'utiliser la commande `pip install -r requirements.txt` pour les installer.

### Utilisation du programme

Pour utiliser le programme, exécutez le fichier `detect_contours.py` en lui passant le chemin d'accès complet à l'image que vous souhaitez traiter en tant qu'argument. Par exemple :

```bash
python detect_contours.py chemin/vers/votre_image.jpg
```

Le programme détectera les contours de l'image spécifiée, les affichera en noir sur un fond blanc et attendra que vous appuyiez sur une touche `esc` pour fermer la fenêtre.

Assurez-vous d'avoir installé les dépendances et d'avoir fourni le chemin d'accès correct à l'image lors de l'exécution du programme. Si le fichier image n'existe pas ou est corrompu, le programme affichera un message d'erreur approprié.

N'hésitez pas à utiliser ce script pour détecter les contours d'autres images en spécifiant simplement leur chemin lors de l'exécution du script.
