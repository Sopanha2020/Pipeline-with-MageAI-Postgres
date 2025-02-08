import io
import pandas as pd
import requests

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Charge les données avec gestion des erreurs et de l'encodage
    """
    url = 'https://www.data.gouv.fr/fr/datasets/r/dbe8a621-a9c4-4bc3-9cae-be1699c5ff25'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Test de différents encodages
        encodings = ['latin1', 'utf-8', 'iso-8859-1']
        for encoding in encodings:
            try:
                df = pd.read_csv(io.StringIO(response.content.decode(encoding)), sep=',')
                # Vérification rapide de l'encodage
                if not df['nom_commune_complet'].str.contains('Ã').any():
                    return df
            except UnicodeDecodeError:
                continue
        
        # Si aucun encodage n'a fonctionné, utiliser latin1 avec gestion spécifique
        return pd.read_csv(io.StringIO(response.content.decode('latin1')), sep=',')
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erreur lors de la récupération des données : {e}")

@test
def test_output(output, *args) -> None:
    """
    Vérifie la validité des données et l'encodage
    """
    assert output is not None, 'Les données sont vides'
    assert 'nom_commune_complet' in output.columns, 'Colonne nom_commune_complet manquante'
    assert not output['nom_commune_complet'].str.contains('Ã').any(), "Problème d'encodage détecté"
