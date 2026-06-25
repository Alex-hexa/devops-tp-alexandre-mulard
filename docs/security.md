# Sécurité du Projet ScanFidel

## Configuration GitHub Security
*(Preuve de l'activation de Dependabot et Secret Scanning)*
![Configuration Advanced Security (1/3)](./images/Securité%20GitHub%201:3.png)
![Configuration Advanced Security (2/3)](./images/Securité%20GitHub%202:3.png)
![Configuration Advanced Security (3/3)](./images/Securité%20GitHub%203:3.png)

---

## Risques DevOps

### R1 Clé Supabase (SUPABASE_KEY) exposée dans le dépôt public
**Probabilité :** Moyenne
**Impact :** Critique (Accès total à la base de données, corruption ou fuite des données des cartes de fidélité).
**Action :** Utilisation stricte du fichier `.env` (exclu via `.gitignore`), scan automatique des secrets par GitHub (Secret Scanning) et utilisation de GitHub Secrets pour la CI/CD.

### R2 Indisponibilité de la base de données distante (Supabase)
**Probabilité :** Faible
**Impact :** Élevé (L'API Flask ne peut plus sauvegarder ni récupérer les cartes scannées).
**Action :** Gestion des exceptions dans les routes Flask pour renvoyer une erreur 500 propre, et healthcheck configuré dans le `docker-compose.yml`.

### R3 Faille de sécurité critique dans une dépendance Python (ex: Flask, Supabase-py)
**Probabilité :** Moyenne
**Impact :** Élevé (Vulnérabilité de l'API face aux attaques web).
**Action :** Activation de *Dependabot alerts* et *Dependabot security updates* sur GitHub pour surveiller le `requirements.txt` et proposer des Pull Requests correctives automatiques.

### R4 Panne du pipeline d'intégration continue (CI)
**Probabilité :** Moyenne
**Impact :** Modéré (Empêche la validation du code et le déploiement, mais ne casse pas la production actuelle).
**Action :** Tests automatisés lancés à chaque "push" et "pull_request" sur les branches principales. Blocage des fusions (merges) si le pipeline est rouge.

### R5 Surface d'attaque trop large sur les conteneurs Docker
**Probabilité :** Faible
**Impact :** Élevé (Un attaquant pourrait exploiter une faille de l'OS du conteneur).
**Action :** Utilisation d'images Docker minimalistes et optimisées (`python:3.11-slim` pour le backend et `nginx:alpine` pour le frontend) afin de réduire drastiquement le nombre de paquets vulnérables embarqués.