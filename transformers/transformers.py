if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform_commune_data(data, *args, **kwargs):
    """
    Nettoie et formate les données des communes
    """
    df_clean = data.copy()
    
    # Correction d'encodage (si nécessaire après le Data Loader)
    for column in ['nom_commune_complet', 'nom_region']:
        df_clean[column] = df_clean[column].apply(
            lambda x: x.encode('latin1', errors='ignore').decode('utf-8', errors='ignore')
            if isinstance(x, str) else x
        )
    
    # Mise en majuscules des noms de régions
    df_clean['nom_region'] = df_clean['nom_region'].str.upper()
    
    # Sélection des colonnes nécessaires
    df_clean = df_clean[['code_postal', 'nom_commune_complet', 'nom_region']]
    
    return df_clean

@test
def test_transform_output(output, *args) -> None:
    """
    Vérifie la transformation avec diagnostic
    """
    # Affichage pour diagnostic
    print("Exemple de communes :", output['nom_commune_complet'].head())
    print("Exemple de régions :", output['nom_region'].head())
    
    # Vérifications
    assert set(output.columns) == {'code_postal', 'nom_commune_complet', 'nom_region'}, \
           "Colonnes incorrectes"
    assert output['nom_region'].str.isupper().all(), \
           'Certaines régions ne sont pas en majuscules'
    assert not output['nom_commune_complet'].str.contains('Ã').any(), \
           "Problème d'encodage dans les communes"
