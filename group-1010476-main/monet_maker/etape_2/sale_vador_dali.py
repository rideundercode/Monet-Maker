import cv2
import numpy as np
import sys
import os

from detect_contours import detecter_contours


def appliquer_flou(image, intensity):
    # Assurez-vous que intensity est toujours impaire et positive
    intensity = max(intensity, 1)  # Au moins 1
    intensity = (
        intensity + 1 if intensity % 2 == 0 else intensity
    )  # Rendre impaire si nécessaire

    # Appliquer le flou gaussien avec l'intensité spécifiée
    return cv2.GaussianBlur(image, (intensity, intensity), 0)


def main():
    if len(sys.argv) < 2:
        print("Veuillez fournir le chemin d'une image en argument.")
        return

    image_path = sys.argv[1]
    # Vérification de l'existence du fichier image
    if not os.path.isfile(image_path):
        print("Le fichier image n'existe pas.")
        return
    # Charger l'image
    try:
        image = cv2.imread(image_path)
    except FileNotFoundError as e:
        print("Erreur lors de la lecture du fichier image:", str(e))
        return

    # Vérifier si l'image a été chargée correctement
    if image is None:
        raise FileNotFoundError("Le fichier image n'existe pas ou est corrompu.")

    while True:
        apply_blur = input("Appliquer un flou ? (Oui/Non) ").strip().lower()
        if apply_blur == "oui":
            while True:
                try:
                    blur_intensity = int(input("Intensité du flou (entier positif) : "))
                    if blur_intensity >= 0:
                        break
                    else:
                        print("Veuillez entrer un nombre entier positif.")
                except ValueError:
                    print("Veuillez entrer un nombre entier valide.")
            break
        elif apply_blur == "non":
            blur_intensity = 0
            break
        else:
            print("Réponse invalide. Veuillez répondre par 'Oui' ou 'Non'.")
    image = appliquer_flou(image, blur_intensity)
    detecter_contours(image)


if __name__ == "__main__":
    main()
