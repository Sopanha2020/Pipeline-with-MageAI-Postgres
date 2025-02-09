# ☁️ Projet - Building Pipeline avec MageAI/Postgres (Windows)

Dans ce projet, nous allons apprendre à créer un pipeline en utilisant les "blocs" de MageAI.

---

## 🎯 Objectifs

- ✅ **Récupérer** des données avec le bloc **Data Loader**.
- ✅ **Formater** ces données via le bloc **Transformer**.
- ✅ **Insérer** les données formatées dans une base de données avec le bloc **Data Exporter**.

---

## 🚀 Étapes

### 1️⃣ Définir les Objectifs du Pipeline
- Pourquoi ce pipeline est-il nécessaire ?
- Quels résultats ou transformations sont attendus ?

### 2️⃣ Identifier les Sources de Données
- Bases de données, fichiers CSV, API, data lakes, etc.
- Faut-il agréger plusieurs sources ?

### 3️⃣ Définir le Format des Données
- Base de données structurée ou non structurée ?
- Quelles sont les tables ?
- Un nettoyage est-il nécessaire ?

### 4️⃣ Définir la Fréquence des Mises à Jour
- Périodique (horaire, journalier) ou événementiel ?

### 5️⃣ Identifier les Parties Prenantes
- Qui sont les utilisateurs des données ?
- Besoins en **dashboarding** ou **reporting** ?

---

## ⚠️ Guide de Dépannage

### 1️⃣ Problèmes d'Encodage
- Vérifiez l'encodage dans le **Data Loader**.
- Testez **utf-8**, **latin1**, **iso-8859-1**.
- Ajoutez des **prints** pour inspecter les données.

### 2️⃣ Erreurs PostgreSQL
- Vérifiez la présence de `MyConfigProfile`.
- Assurez-vous que **PostgreSQL est accessible** :
  - 🔍 **Docker est-il lancé ?**
  - 🔍 **Les ports sont-ils corrects ?**
  - 🔍 **Les identifiants sont-ils valides ?**

---
## 🚀 Instructions pour démarrer le projet
### 💪 Prérequis

    ✔️ **Windows 10/11 avec WSL2 activé**
    ✔️ [Docker Desktop](https://www.docker.com/products/docker-desktop/)
    ✔️ [Visual Studio Code](https://code.visualstudio.com/) (recommandé)
    ✔️ Extension Docker pour VSCode
    ✔️ **Git installé**

---

### 🔧 Installation et Configuration

#### 1️⃣ Nettoyage de Docker (si nécessaire)

```bash
# Arrêter et nettoyer Docker
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker volume prune
docker system prune -a
```
⚠️ **Attention** : `docker system prune -a` supprime toutes les images non utilisées.

#### 2️⃣ Configuration de l'Environnement Python

```bash
# Créer un environnement virtuel
python -m venv docker_mage

# Activer l'environnement virtuel (PowerShell Windows)
.\docker_mage\Scripts\activate
```

#### 3️⃣ Cloner le Repository

```bash
git clone https://github.com/Sopanha2020/Pipeline-with-MageAI-Postgres.git
```

---

### 📂 Structure des Fichiers

```
Pipeline-with-MageAI-Postgres/
│
├── .env                  # Variables d'environnement
├── docker-compose.yml    # Configuration Docker Compose
├── Dockerfile            # Instructions de build de l'image
├── io_config.yaml        # Configuration Mage AI
├── requirements.txt      # Dépendances Python
└── README_Windows.md     # Ce fichier
```

---

### 🚀 Démarrage des Conteneurs

```bash
cd Pipeline-with-MageAI-Postgres

docker compose build
docker compose up
```
📌 **Pour exécuter en arrière-plan :**
```bash
docker compose up -d
```

---

### ✅ Vérification de l'Installation

1️⃣ **Ouvrir Docker Desktop** et vérifier les conteneurs :
   - `[PROJECT_NAME]_mageai`
   - `[PROJECT_NAME]_postgres`

2️⃣ **Accéder à Mage AI**
   - 🔗 `http://localhost:6789`

---

### 🛑 Arrêt des Conteneurs

```bash
docker compose down
```

---

### 🔄 Commandes Utiles

```bash
# Voir les logs
docker compose logs

# Voir les logs d'un conteneur spécifique
docker compose logs mageai
docker compose logs postgres

# Redémarrer les conteneurs
docker compose restart

# Reconstruire les images et redémarrer
docker compose up --build
```

---

### 🔍 Résolution des Problèmes

#### 🚫 Les conteneurs ne démarrent pas
1. **Docker Desktop est-il lancé ?**
2. **Les ports 6789 et 5432 sont-ils libres ?**
3. **Vérifier les logs** : `docker compose logs`

#### ⚠️ Erreur "Port is already allocated"
```bash
# Trouver le processus utilisant le port
netstat -ano | findstr "6789"
netstat -ano | findstr "5432"

# Arrêter le processus
Taskkill /PID [PID] /F
```

#### 🔑 Problèmes de Permissions (Windows)
1. **Donner les droits à Docker Desktop sur votre dossier.**
2. **Exécuter PowerShell en mode Administrateur.**

---

### 📌 Support et Conseils

1. **Vérifier les logs Docker.**
2. **S'assurer que tous les fichiers de configuration sont corrects.**
3. **Docker Desktop doit avoir assez de ressources (RAM, CPU, disque).**
4. **Ne pas modifier les fichiers de configuration en cours d'exécution.**
5. **Docker Desktop doit être mis à jour.**

---

### 📚 Ressources Additionnelles

📌 [Documentation Mage AI](https://docs.mage.ai/)
📌 [Documentation Docker](https://docs.docker.com/)
📌 [Documentation PostgreSQL](https://www.postgresql.org/docs/)

---

