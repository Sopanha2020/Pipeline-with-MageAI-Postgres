import os
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path
from dotenv import load_dotenv

# Load environment variables from .env (if present)
load_dotenv()

@data_exporter
def export_commune_data(df: DataFrame, **kwargs) -> None:
    """
    Exporte les données vers PostgreSQL avec gestion d'erreurs.
    """
    # Get configuration file path
    config_path = path.join(get_repo_path(), 'io_config.yaml')

    # Vérification du fichier de configuration
    if not path.exists(config_path):
        raise FileNotFoundError(f"❌ Le fichier de configuration n'existe pas : {config_path}")

    try:
        config_profile = 'MyConfigProfile'
        schema_name = os.getenv('POSTGRES_SCHEMA', 'public')  # Default to 'public' if not found
        table_name = 'communes_france'

        # Log connection attempt
        print(f"🔄 Tentative de connexion à PostgreSQL avec le profil : {config_profile}")

        # Open PostgreSQL connection
        with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
            loader.export(
                df,
                schema_name,
                table_name,
                index=False,
                if_exists='replace',
            )
            print(f"✅ Données exportées avec succès dans {schema_name}.{table_name}")

    except KeyError as e:
        print(f"❌ Erreur de configuration : {e}")
        print("🔍 Vérifiez que votre fichier io_config.yaml contient une section 'MyConfigProfile'.")
        raise
    except Exception as e:
        print(f"❌ Erreur lors de l'export : {e}")
        print("🔍 Vérifiez vos paramètres de connexion et assurez-vous que PostgreSQL est accessible.")
        raise
