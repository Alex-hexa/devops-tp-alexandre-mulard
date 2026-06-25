# Stratégie DevOps - ScanFidel

## 1. Architecture technique cible
L'application ScanFidel repose sur une architecture en trois tiers, conteneurisée pour garantir la portabilité entre les environnements de développement et de production.

    +-------------------+       +--------------------+       +--------------------+
    |   Frontend Web    |       |   Backend API      |       |  Base de Données   |
    |  (Nginx Alpine)   +------>+  (Python / Flask)  +------>+    (Supabase)      |
    | Port: 8080 (80)   | HTTP  | Port: 5001 (5001)  | HTTPS | (PostgreSQL dist.) |
    +-------------------+       +--------------------+       +--------------------+

Le frontend sert des fichiers statiques (HTML, CSS, JS avec html5-qrcode) via Nginx. Le backend est une API REST développée en Python avec Flask, qui utilise le client Supabase pour persister les données des cartes de fidélité dans le cloud.

## 2. Structure du repository
Le dépôt est organisé de manière modulaire pour séparer les responsabilités logiques :
- `backend/` : Contient le code Python (Flask), le `requirements.txt` et le `Dockerfile` multi-étapes (dev/prod).
- `frontend/` : Contient les assets statiques et le `Dockerfile` Nginx.
- `docs/` : Centralise la documentation technique (architecture, sécurité, tests).
- `.github/workflows/` : Héberge la configuration d'intégration continue (`ci.yml`).
Cette séparation permet d'isoler les builds Docker et de maintenir un code propre.

## 3. Workflow Git
L'équipe utilise un workflow basé sur des branches de fonctionnalités (Feature Branching). La branche `main` est protégée et représente l'état stable pour la production. Les développements quotidiens se font sur la branche `developp` (ou des branches `feature/*`). Les fusions vers `main` ou `developp` se font obligatoirement via des Pull Requests (PR) validées par l'intégration continue. Les commits suivent la convention *Conventional Commits* (ex: `feat(api): ...`, `fix(ui): ...`).

Protection de la branche `main` :
![Capture 1](<images/Capture1.png>)
![Capture 2](<images/Capture2.png>)
![Capture 3](<images/Capture3.png>)

## 4. Services Docker prévus
Le fichier `docker-compose.yml` orchestre trois services distincts :
- `api-dev` : Le backend configuré pour le développement (avec rechargement à chaud et `FLASK_DEBUG=1`).
- `api-prod` : Le backend configuré pour la production (utilisant un serveur WSGI comme Gunicorn).
- `web` : Le serveur Nginx servant l'interface utilisateur.
Le `Dockerfile` backend utilise un pattern "multi-stage build" pour séparer l'installation des dépendances du lancement du serveur, optimisant ainsi le poids de l'image.

## 5. Variables d'environnement
La configuration sensible et spécifique à l'environnement est gérée via un fichier `.env` (exclu de Git) et un `.env-example` (versionné). Les variables principales sont :
- `SUPABASE_URL` : L'URL de l'instance Supabase distante.
- `SUPABASE_KEY` : La clé d'authentification de l'API Supabase.
- `FLASK_DEBUG` et `FLASK_ENV` : Variables gérant le mode de lancement du backend.
Ces variables sont injectées dans les conteneurs au moment de l'exécution via Docker Compose.

## 6. Stratégie de tests
La stratégie repose sur des tests automatisés du backend Python. Des tests unitaires vérifieront la logique des routes API (`/api/cards`) en simulant (mockant) le client Supabase pour s'affranchir des appels réseau. L'objectif est de s'assurer que les validations de données (ex: présence du nom et du code) fonctionnent. Le taux de couverture cible est fixé à 60% minimum, calculé via un outil de couverture intégré à la CI.

## 7. Pipeline CI prévu
Le pipeline d'Intégration Continue est géré par GitHub Actions (`ci.yml`) et se déclenche à chaque `push` ou `pull_request` sur `main` et `developp`. Il comprend les étapes suivantes :
1. Récupération du code (Checkout).
2. Configuration des environnements Node.js (pour les outils de linting) et Python.
3. Installation des dépendances avec mise en cache (`npm` et `pip`).
4. Vérification du formatage et de la qualité du code (Linting).
5. Exécution des tests automatisés et génération du rapport de couverture.
6. Vérification du build des images Docker (`docker compose build`).

## 8. Sécurité et secrets
La sécurité est intégrée à plusieurs niveaux : le fichier `.env` contenant les clés Supabase est formellement ignoré par Git. Sur GitHub, la fonctionnalité *Secret Scanning* est activée pour prévenir toute fuite accidentelle. Les alertes *Dependabot* scannent régulièrement `requirements.txt` à la recherche de failles. Enfin, les clés API nécessaires au pipeline CI sont stockées de manière chiffrée dans les *GitHub Secrets*.

## 9. Logs prévus
La collecte des logs repose principalement sur la sortie standard (`stdout` / `stderr`) des conteneurs Docker. Nginx journalisera les requêtes HTTP entrantes (succès et erreurs de chargement du front). Le backend Flask/Gunicorn remontera les erreurs d'exécution, notamment les échecs de connexion à Supabase ou les mauvaises requêtes utilisateur (erreurs 400 et 500). Ces logs seront consultables en local via `docker compose logs`.

## 10. Risques DevOps
Les principaux risques identifiés (détaillés dans `docs/security.md`) incluent la fuite de la clé Supabase, l'indisponibilité du service de base de données distant, les failles dans les paquets Python, et un échec persistant de la CI bloquant les déploiements. Ces risques sont mitigés par nos pratiques de sécurité automatisées et la gestion stricte des variables d'environnement.

## 11. Commandes de lancement
Le projet a été conçu pour être facilement instancié. Les commandes principales sont :
- Copier la configuration : `cp .env-example .env` (puis remplir les clés Supabase).
- Lancement mode Dev : `docker compose up --build api-dev web`
- Lancement mode Prod : `docker compose up --build api-prod web`
L'application web est ensuite accessible sur `http://localhost:8080`.

## 12. Prochaines actions
À court terme, les prochaines étapes consisteront à finaliser le TP avec un déploiement continu via Render. À plus long terme, la mise en place d'une base de données locale sous Docker permettrait de s'affranchir du cloud durant le développement.