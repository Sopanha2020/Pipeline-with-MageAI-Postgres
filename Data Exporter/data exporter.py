from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path

@data_exporter
def export_commune_data(df: DataFrame, **kwargs) -> None:
    """
    Exporte les données vers PostgreSQL avec gestion d'erreurs
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    
    # Vérification du fichier de configuration
    if not path.exists(config_path):
        raise FileNotFoundError(f"Le fichier de configuration n'existe pas : {config_path}")
    
    try:
        config_profile = 'MyConfigProfile'
        schema_name = 'public'
        table_name = 'communes_france'

        with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
            loader.export(
                df,
                schema_name,
                table_name,
                index=False,
                if_exists='replace',
            )
            print(f"Données exportées avec succès dans {schema_name}.{table_name}")
            
    except KeyError as e:
        print(f"Erreur de configuration : {e}")
        print("Vérifiez que votre fichier io_config.yaml contient une section 'MyConfigProfile'")
        raise
    except Exception as e:
        print(f"Erreur lors de l'export : {e}")
        print("Vérifiez vos paramètres de connexion et que PostgreSQL est accessible")
        raise