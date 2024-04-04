import cv2
import numpy as np
import sys
import os


def detecter_contours(image, afficher_contours=True):
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
    return thresholded
