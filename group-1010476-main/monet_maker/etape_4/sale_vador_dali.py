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
