import turtle
import cv2
import sys
import os
import numpy as np
from PIL import ImageGrab

from detect_contours import detecter_contours
from sale_vador_dali import appliquer_flou


def normalize_coordinates(x, y, width, height):
    normalized_x = x - width // 2
    normalized_y = height // 2 - y
    return normalized_x, normalized_y


def dessiner_contours(image_contours, vitesse_dessin):
    height, width = image_contours.shape

    screen = turtle.Screen()
    screen.setup(width, height)
    screen._root.attributes("-topmost", True)
    screen.tracer(0)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.shape("blank")

    # Parcourir les pixels de l'image et dessiner le contour
    for y in range(height):
        for x in range(width):
            if image_contours[y, x] == 0:  # Si le pixel est noir (contour)
                normalized_x, normalized_y = normalize_coordinates(x, y, width, height)
                t.goto(normalized_x, normalized_y)
                t.dot(1.5, "black")

                if (x + y) % vitesse_dessin == 0:
                    screen.update()  # Mettre à jour l'écran après avoir dessiné 'draw_speed' pixels

    screen.update()
    canvas = screen.getcanvas()
    dessin_contours = ImageGrab.grab(
        (
            canvas.winfo_rootx(),
            canvas.winfo_rooty(),
            canvas.winfo_rootx() + canvas.winfo_width(),
            canvas.winfo_rooty() + canvas.winfo_height(),
        )
    )

    turtle.done()
    return dessin_contours


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
    image_flou = appliquer_flou(image, blur_intensity)
    contours = detecter_contours(image_flou)
    while True:
        try:
            vitesse_animation = int(input("Vitesse de l'animation (entier positif) : "))
            if vitesse_animation >= 0:
                break
            else:
                print("La vitesse de l'animation doit être comprise entier positif.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    # Ajustez cette valeur en fonction de la vitesse souhaitée
    image_dessiner_contours = dessiner_contours(contours, vitesse_animation)
    image_dessiner_contours.show()


if __name__ == "__main__":
    main()
