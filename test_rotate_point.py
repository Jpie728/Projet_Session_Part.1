from transformation_geometrique import calculer_rotate_point
def test_rotate_point():
    """
    Teste la fonction calculer_rotate_point avec les valeurs fournies.
    """
    point = (2, 4)
    angle = 30
    center = (0, 0)
    resultat_attendu = (-0.27, 4.46)
    resultat_obtenu = calculer_rotate_point(point, angle, center)
    assert resultat_obtenu == resultat_attendu, f"Échec du test : {resultat_obtenu} != {resultat_attendu}"

if _name_ == "_main_":
    # Exécuter le test unitaire
    test_rotate_point()
    print("Test réussi!")