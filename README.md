# Chronicle API

An app for logging your D&D adventures!

This app:

- Is the backend API application
- Uses [Poetry](https://python-poetry.org/docs/basic-usage/) for python package managment.
- Uses [FastAPI](https://fastapi.tiangolo.com) for the web API framewaork.
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
poetry run python3 app/main.py

# Swagger Docs
http://localhost:8000/docs
```
