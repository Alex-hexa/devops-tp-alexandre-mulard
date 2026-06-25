# ScanFidel
[![CI ScanFidel](https://github.com/Alex-hexa/devops-tp-alexandre-mulard/actions/workflows/ci.yml/badge.svg)](https://github.com/Alex-hexa/devops-tp-alexandre-mulard/actions/workflows/ci.yml)

Cette application est une web app de gestion de cartes de fidélité. Elle permet de scanner des cartes de fidélité et de les stocker dans une base de données. L'utilisateur voit les cartes scanner et les nommer comme il veut.

## Stack

- Supabase
- Python
- Docker

## Lancer le projet

### Pour l'environnement de dev
```bash
docker compose up --build api-dev web
```

### Pour l'environnement de prod
```bash
docker compose up --build api-prod web
```

### Pour accéder au site (Render)
```bash
https://scanfidel-api.onrender.com/health
```

## Tester

## Architecture

```bash
cd docs/
```

## Auteur 

Alexandre Mulard