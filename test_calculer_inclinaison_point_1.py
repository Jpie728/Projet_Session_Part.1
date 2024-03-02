from transformation_geometrique import calculer_inclinaison_point
def test_calculer_inclinaison_point_1():
    """
    Teste la fonction calculer_inclinaison_point avec les valeurs fournies.
    """
    point = (2, 4)
    angle = 5
    direction = 'x'
    resultat_attendu = (2.35, 4.0)
    resultat_obtenu = calculer_inclinaison_point(point, angle, direction)
    assert resultat_obtenu == resultat_attendu, f"Échec du test : {resultat_obtenu} != {resultat_attendu}"

if _name_ == "_main_":
    # Exécuter le test unitaire
    test_calculer_inclinaison_point_1()
    print("Test réussi!")