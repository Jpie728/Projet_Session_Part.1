from transformation_geometrique import calculer_reflexion_point
def test_calculer_reflexion_point_2():
    """
    Teste la fonction calculer_reflexion_point avec les valeurs fournies.
    """
    point = (2, 4)
    axe = 'y'
    resultat_attendu = (-2, 4)
    resultat_obtenu = calculer_reflexion_point(point, axe)
    assert resultat_obtenu == resultat_attendu, f"Échec du test 2 : {resultat_obtenu} != {resultat_attendu}"

if _name_ == "_main_":
    # Exécuter le test unitaire
    test_calculer_reflexion_point_2()
    print("Test réussi!")