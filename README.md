# ScanFidel
[![CI ScanFidel](https://github.com/Alex-hexa/devops-tp-alexandre-mulard/actions/workflows/ci.yml/badge.svg)](https://github.com/Alex-hexa/devops-tp-alexandre-mulard/actions/workflows/ci.yml)

Cette application est une web app de gestion de cartes de fidélité. Elle permet de scanner des cartes de fidélité et de les stocker dans une base de données. L'utilisateur peut voir les cartes scannées et les nommer comme il le souhaite.

## Stack
- **Frontend :** HTML / JS / CSS (Nginx)
- **Backend :** Python / Flask
- **Base de données :** Supabase
- **DevOps :** Docker, Render, GitHub Actions

## Lancer le projet

### 1. Configuration initiale
Avant de lancer le projet, il faut créer le fichier d'environnement et y renseigner vos identifiants de base de données :
```bash
cp .env.example .env
```

### 2. Démarrage (Environnement de dev)
```bash
docker compose up --build api-dev web
```

### 3. Démarrage (Environnement de prod)
```bash
docker compose up --build api-prod web
```

### 4. Accès
- **Interface web (local) :** http://localhost:8080
- **Statut de l'API (déploiement Render) :** https://scanfidel-api.onrender.com/health

## Tester
Pour exécuter les tests automatisés et générer le rapport de couverture, utilisez la commande suivante :
```bash
npm run test:coverage
```

## Architecture
Toute la documentation technique, la stratégie DevOps et l'analyse des risques sont détaillées dans le répertoire dédié :
[Consulter la documentation (docs/)](./docs/)

## Auteur 
Alexandre Mulard