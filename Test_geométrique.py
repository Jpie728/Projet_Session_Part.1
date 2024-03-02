# Calculer reflexion point
def calculer_reflexion_point(point, axe):

    x, y = point
    if axe == 'x':
        return x, -y
    elif axe == 'y':
        return -x, y
    else:
        raise ValueError("L'axe de réflexion doit être 'x' ou 'y'.")

# Calculer rotate point

import math

def calculer_rotate_point(point, angle, center=(0, 0)):

    x, y = point
    cx, cy = center

    # Translation pour ramener le centre de rotation à l'origine
    translated_x = x - cx
    translated_y = y - cy

    # Rotation autour de l'origine
    rotated_x = translated_x * math.cos(math.radians(angle)) - translated_y * math.sin(math.radians(angle))
    rotated_y = translated_x * math.sin(math.radians(angle)) + translated_y * math.cos(math.radians(angle))

    # Translation de retour au centre de rotation
    new_x = rotated_x + cx
    new_y = rotated_y + cy

    # Arrondi à deux chiffres après la virgule
    new_x = round(new_x, 2)
    new_y = round(new_y, 2)

    return new_x, new_y

# Calculer inclinaison point

import math

def calculer_inclinaison_point(point, angle, direction):

    x, y = point

    # Convertir l'angle en radians
    angle_radians = math.radians(angle)

    # Calculer la tangente de l'angle
    m = math.tan(angle_radians)

    # Appliquer la transformation d'inclinaison selon la direction
    if direction == 'x':
        new_x = x + m * y
        new_y = y
    elif direction == 'y':
        new_x = x
        new_y = y + m * x
    else:
        raise ValueError("La direction doit être 'x' ou 'y'.")

    # Arrondir les résultats à deux chiffres après la virgule
    new_x = round(new_x, 2)
    new_y = round(new_y, 2)

    return new_x, new_y