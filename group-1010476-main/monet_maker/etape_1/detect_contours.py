import cv2
import numpy as np
import sys
import os


def detecter_contours(image):
    # Conversion en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Réduction du bruit avec un flou gaussien
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Calcul des gradients d'intensité
    gradient_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    gradient_direction = np.arctan2(gradient_y, gradient_x)

    # Définition des seuils d'hystérésis
    mean_gray = np.mean(gray)
    threshold1 = int(max(0, 0.7 * mean_gray))
    threshold2 = int(min(255, 1.3 * mean_gray))

    # Appliquer l'algorithme Canny pour détecter les contours
    edges = cv2.Canny(blurred, threshold1, threshold2)

    # Inverse binary thresholding pour afficher les contours en noir sur un fond blanc
    ret, thresholded = cv2.threshold(edges, 128, 255, cv2.THRESH_BINARY_INV)

    # Affichage des contours
    cv2.imshow("Contours", thresholded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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

    detecter_contours(image)


if __name__ == "__main__":
    main()
