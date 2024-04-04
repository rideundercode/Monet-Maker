# Groupe de brahim_y 1010476

README.md

## Étape 2: Salé Vador Dali

Ce script Python permet d'améliorer l'isolation des contours des images en appliquant un flou gaussien.

### Dépendances

Ce script utilise les bibliothèques suivantes :

- `cv2` (OpenCV) : Utilisée pour le traitement d'images, notamment pour appliquer le flou gaussien et détecter les contours.

### Approche

L'approche de ce script consiste à prendre en compte l'entrée de l'utilisateur pour décider d'appliquer un flou gaussien ou non, et avec quelle intensité. Ensuite, il utilise la bibliothèque OpenCV pour appliquer le flou gaussien à l'image et détecter les contours améliorés.

Cela permet de gérer les détails excessifs dans les images, améliorant ainsi la qualité des contours détectés.

### Utilisation du programme

Pour utiliser le programme, exécutez le fichier `sale_vador_dali.py` en lui passant le chemin d'accès complet à l'image que vous souhaitez traiter en tant qu'argument. Par exemple :

```bash
python sale_vador_dali.py chemin/vers/votre_image.jpg
```

Le programme détectera les contours de l'image spécifiée, les affichera en noir sur un fond blanc et attendra que vous appuyiez sur une touche `esc` pour fermer la fenêtre.

Assurez-vous d'avoir installé les dépendances et d'avoir fourni le chemin d'accès correct à l'image lors de l'exécution du programme. Si le fichier image n'existe pas ou est corrompu, le programme affichera un message d'erreur approprié.

N'hésitez pas à utiliser ce script pour détecter les contours d'autres images en spécifiant simplement leur chemin lors de l'exécution du script.
