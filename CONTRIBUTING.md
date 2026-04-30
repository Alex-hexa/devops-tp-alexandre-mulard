# Guide de Contribution

Pour garantir une collaboration fluide et un déploiement continu stable, merci de respecter les règles suivantes.

## 1. Workflow Git

Nous utilisons un modèle de branchement structuré :

*   **`main`** : La branche de production. Tout code ici doit être stable et fonctionnel. Aucun push direct autorisé.
*   **`develop`** : La branche d'intégration. C'est ici que l'on fusionne les fonctionnalités terminées.
*   **`feature/*`** : Pour chaque nouvelle tâche ou fonctionnalité (ex: `feature/setup-auth`).

## 2. Conventional Commits

Nous suivons strictement la convention **Conventional Commits** pour l'historique Git. Le format est `type(scope): description`.

Types autorisés :
*   `feat:` (nouvelle fonctionnalité)
*   `fix:` (correction de bug)
*   `docs:` (documentation)
*   `test:` (ajout ou modification de tests)
*   `refactor:` (modification du code sans changer le comportement)
*   `ci:` (modification du pipeline de déploiement)
*   `chore:` (maintenance, dépendances, configuration)

*Exemple : `feat(backend): ajout de la route de connexion`*

## 3. Pull Requests

Tout ajout de code doit passer par une Pull Request :

1.  Créer une branche `feature/...` depuis `develop`.
2.  Pousser les modifications sur GitHub.
3.  Ouvrir une Pull Request vers `develop`.
4.  Remplir la description avec les sections : Quoi, Pourquoi, et Comment tester.
5.  Le pipeline CI (tests et linter) doit passer au vert avant toute fusion.