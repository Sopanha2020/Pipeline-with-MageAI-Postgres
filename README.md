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
Si vous voyez des caractères comme "Ã©", "Ã¨", etc. :

- Vérifiez l'encodage dans le Data Loader en premier
- Testez différents encodages (latin1, utf-8, iso-8859-1)
- Utilisez les prints de diagnostic pour voir les données
  
### 2. Erreurs PostgreSQL
Si vous avez des erreurs de connexion :

- Il doit être dans le bon répertoire
- La section 'MyConfigProfile' doit être présente
- Les informations de connexion doivent être correctes

Vérifiez que PostgreSQL est accessible :

- Les services Docker sont-ils lancés ?
- Les ports sont-ils corrects ?
- Les identifiants sont-ils bons ?
