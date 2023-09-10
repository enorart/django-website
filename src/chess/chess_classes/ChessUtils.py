def converted_coordonate(x,y):
    """Convertir les coordonnées des cases de l'échéquier en coordonnées normalisé echec (genre A1)\n
    Paramètres:\n
    x: abscisse de la case (entre 0 et 7)\n
    y: ordonnée de la case (entre 0 et 7)\n
    Retourne:\n
    x_conv: abscisse de la case convertie (a à h)
    y_conv: ordonnée de la case convertie (1 à 8)\n"""
    x_conv= chr(x)+97
    y_conv= 8-y

    return x_conv, y_conv
