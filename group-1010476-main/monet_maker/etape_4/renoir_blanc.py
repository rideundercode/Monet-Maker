import turtle
import cv2
import sys
import os
import numpy as np
from PIL import ImageGrab
from detect_contours import detecter_contours
from sale_vador_dali import appliquer_flou
from zhang_gui import normalize_coordinates


def dessiner_contours(image_contours, vitesse_dessin):
    height, width = image_contours.shape
    pixels_a_dessiner = {(x, y) for y in range(height) for x in range(width) if image_contours[y, x] == 0}
    
    screen = turtle.Screen()
    screen.setup(width, height)
    screen._root.attributes("-topmost", True)
    screen.tracer(0)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.shape("blank")

    # Dessiner les contours en suivant l'approche NNS
    if pixels_a_dessiner:
        position_actuelle = pixels_a_dessiner.pop()
        t.goto(normalize_coordinates(position_actuelle[0], position_actuelle[1], width, height))
        t.dot(1.5, "black")

        pixels_dessines = {position_actuelle}

        while pixels_a_dessiner:
            position_suivante = min(pixels_a_dessiner, key=lambda p: (p[0] - position_actuelle[0])**2 + (p[1] - position_actuelle[1])**2)
            t.goto(normalize_coordinates(position_suivante[0], position_suivante[1], width, height))
            t.dot(1.5, "black")
            pixels_dessines.add(position_suivante)
            position_actuelle = position_suivante
            pixels_a_dessiner.discard(position_suivante)

            if len(pixels_dessines) % vitesse_dessin == 0:
                screen.update()  # Mettre à jour l'écran après avoir dessiné 'vitesse_dessin' pixels

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
