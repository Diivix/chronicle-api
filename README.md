# Chronicle API

An app for logging your D&D adventures!

This app:

- Is the backend API application
- Uses [Poetry](https://python-poetry.org/docs/basic-usage/) for python package management.
- Uses [FastAPI](https://fastapi.tiangolo.com) for the web API framework.
- User [SQLModel](https://sqlmodel.tiangolo.com/img/icon-white.svg) for the database framework.
- Uses GitHub Actions for CI/CD and builds into a Docker image.
- Uses Azure:
  - App Service for hosting
  - Cosmos DB for storage
  - Cognitive services
- Uses Apple and Google as auth providers.

## Build and Run

```bash
poetry shell

# Ensure the VS Code python version is using our Poetry Virtual Environment. Check bottom right.
# This is required for intellisense to work properly.

poetry install

poetry run python3 run.py

# Swagger Docs
http://localhost:8000/docs
```

### Database Scripts

```bash
# Seed database for development
poetry run python3 seed_db.py

# Created the database for production
poetry run python3 app/db/database.py
```
