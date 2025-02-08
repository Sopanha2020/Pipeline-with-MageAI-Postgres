# ☁️ Projet - Building Pipeline with MageAI/Postgres

Dans ce projet, nous verrons comment créer un pipeline en utilisant les "blocs" de MageAI.

## 🎯 Objectifs de ce projet

- ✅ Récupérer des données avec le bloc Data loader.
- ✅ Formater cette donnée via le bloc Transformer.
- ✅ Insérer les données formatées dans une base de données avec le bloc Data exporter.

## 🚀 Étapes nécessaires:

### 1. Bien Définir le ou les objectifs de notre pipeline :
- Pourquoi ce pipeline est-il nécessaire ?
- Quels résultats ou transformations sont attendus ?

### 2. Identification des sources de données :
- Quelles sont les sources de données à utiliser ? Bases de données, fichiers CSV, API, data lakes, etc.
- Aurais-je besoin d'agréger des données provenant de multiples sources ?

### 3. Format des données:
- Comment mes données sont-elles stockées ? Dans une base de données structurée, non structurée ?
- Quelles sont les tables de ma base de données ?
- Un nettoyage des données est-il nécessaire ?

### 4. Fréquence des mises à jour :
- Le pipeline sera-t-il déclenché périodiquement (horaire, journalier) ou en fonction d’un événement ?

### 5. Identification des parties prenantes :
- Qui sont les utilisateurs des données et des résultats du pipeline ?
- Y a-t-il des besoins de dashboarding, de reporting, etc. ?

## ⚠️ Guide de dépannage

### 1. Problèmes d'encodage
Si on voit des caractères comme "Ã©", "Ã¨", etc. :

- Vérifiez l'encodage dans le Data Loader en premier
- Testez différents encodages (latin1, utf-8, iso-8859-1)
- Utilisez les prints de diagnostic pour voir les données
  
### 2. Erreurs PostgreSQL
Si on a des erreurs de connexion :

- Il doit être dans le bon répertoire
- La section 'MyConfigProfile' doit être présente
- Les informations de connexion doivent être correctes

Vérifiez que PostgreSQL est accessible :

- Les services Docker sont-ils lancés ?
- Les ports sont-ils corrects ?
- Les identifiants sont-ils bons ?

# Installation de Mage AI avec Docker et PostgreSQL (WINDOWS !!!!!)

Ce guide vous permettra d'installer et de configurer Mage AI avec PostgreSQL dans un environnement Docker.

## Prérequis

- Windows 10/11 avec WSL2 activé
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé et fonctionnel
- [Visual Studio Code](https://code.visualstudio.com/) (recommandé)
- Extension Docker pour VSCode (recommandée)
- Git installé sur votre machine

## 1. Préparation de l'environnement (Sur VSCode ou sur PowerShell windows, On recommande fortement VSCode)

### 1.1 Nettoyage de Docker (si nécessaire)

Si vous avez déjà travaillé avec Docker, il est recommandé de nettoyer votre environnement :

```bash
# Arrêter tous les conteneurs en cours d'exécution
docker stop $(docker ps -a -q)

# Supprimer tous les conteneurs
docker rm $(docker ps -a -q)

# Supprimer tous les volumes non utilisés
docker volume prune

# Supprimer toutes les images non utilisées
docker system prune -a
```

⚠️ **Attention** : La commande `docker system prune -a` supprimera toutes les images Docker non utilisées. Assurez-vous de ne pas avoir des images importantes que vous souhaitez conserver.

### 1.2 Configuration de l'environnement Python

```bash
# Créer un environnement virtuel
python -m venv docker_mage

# Activer l'environnement virtuel
## Sur Windows (PowerShell)
.\docker_mage\Scripts\activate
```

## 2. Cloner le repository

```bash
# Cloner le repository
git clone https://github.com/WildCodeSchool/data-training-resources.git repo_to_clone

# Accéder au dossier du projet
cd .\repo_to_clone\
```

## 3. Structure des fichiers

Vérifiez que vous avez bien tous les fichiers nécessaires :

```
repo_to_clone/
│
├── .env                  # Variables d'environnement
├── docker-compose.yml    # Configuration Docker Compose
├── Dockerfile           # Instructions de build de l'image
├── io_config.yaml       # Configuration Mage AI
├── requirements.txt     # Dépendances Python
└── README_Windows.md            # Ce fichier
```

## 4. Construction et démarrage des conteneurs

Assurez-vous d'être dans le bon dossier :
```bash
# Vérifier que vous êtes dans le dossier mage-wildcamp
pwd

# Si ce n'est pas le cas, naviguez vers le bon dossier
cd repo_to_clone
```

Ensuite, lancez la construction et le démarrage :
```bash
# Construire les images
docker compose build

# Démarrer les conteneurs
docker compose up
```

Pour exécuter en arrière-plan (mode détaché) :
```bash
docker compose up -d
```
## 5. Vérification de l'installation

1. Ouvrez Docker Desktop et vérifiez que les deux conteneurs sont en cours d'exécution :
   - `[PROJECT_NAME]_mageai`
   - `[PROJECT_NAME]_postgres`

2. Accédez à l'interface Mage AI :
   - Ouvrez votre navigateur
   - Accédez à `http://localhost:6789`

## 6. Arrêt des conteneurs

Pour arrêter les conteneurs :
```bash
# Si en mode détaché
docker compose down

# Si en mode interactif
# Appuyez sur Ctrl+C puis exécutez :
docker compose down
```

## 7. Commandes utiles

```bash
# Voir les logs des conteneurs
docker compose logs

# Voir les logs d'un conteneur spécifique
docker compose logs mageai
docker compose logs postgres

# Redémarrer les conteneurs
docker compose restart

# Reconstruire les images et redémarrer les conteneurs
docker compose up --build
```

## Résolution des problèmes courants

### Les conteneurs ne démarrent pas

1. Vérifiez que Docker Desktop est en cours d'exécution
2. Vérifiez que les ports 6789 et 5432 ne sont pas déjà utilisés
3. Consultez les logs avec `docker compose logs`

### Erreur "port is already allocated"

```bash
# Identifier le processus utilisant le port
netstat -ano | findstr "6789"
netstat -ano | findstr "5432"

# Arrêter le processus (remplacer [PID] par l'ID du processus)
taskkill /PID [PID] /F
```

### Problèmes de permissions

Si vous rencontrez des problèmes de permissions sur Windows :
1. Assurez-vous que Docker Desktop a accès à votre dossier de projet
2. Exécutez PowerShell en tant qu'administrateur

## Support

En cas de problème :
1. Consultez les logs Docker
2. Vérifiez que tous les fichiers de configuration sont correctement formatés
3. Assurez-vous que Docker Desktop dispose de suffisamment de ressources

## Notes importantes

- Ne modifiez pas les fichiers de configuration pendant que les conteneurs sont en cours d'exécution
- Assurez-vous d'avoir suffisamment d'espace disque disponible (minimum 10GB recommandé)
- Gardez Docker Desktop à jour
- En cas de modification des fichiers de configuration, redémarrez les conteneurs

## Ressources additionnelles

- [Documentation officielle de Mage AI](https://docs.mage.ai/)
- [Documentation Docker](https://docs.docker.com/)
- [Documentation PostgreSQL](https://www.postgresql.org/docs/)
