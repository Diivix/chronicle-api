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

### Initialize Database

```bash
# Build and run custom MSSQL Docker image with SQL Tools installed.
docker build -t mssql-2019-tools -f resources/mssql/Dockerfile .
docker run --name mssql-2019-tools -d -p 1433:1433 -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=StrongP^ssword" -e "MSSQL_PID=Express" mssql-2019-tools

# Open an interactive shell with database container.
docker exec -it mssql-2019-tools /bin/bash

# Example SQL query using MSSQL Tools
sqlcmd -C -S localhost -U sa -P StrongP^ssword -d chronicle -y 20 -Q "SELECT * FROM [user];"

# Initialize (and seed database for development)
poetry run python3 init_db.py
```

### Run App

1. Start the MSSQL database. See [MS SQL with Tools](#MS-SQL-with-Tools)

2. Start the application.

```bash
poetry shell

# Ensure the VS Code python version is using our Poetry Virtual Environment. Check bottom right.
# This is required for intellisense to work properly.

poetry install

poetry run python3 run.py

# Swagger Docs
http://localhost:8000/docs
```

## Resources

### Offline Docs

For offline FastAPI and SQLModel docs:

```bash
docker build -t docs-offline -f resources/offline-docs/Dockerfile .
docker run --name docs-offline -d -p 8010:8010 -p 8020:8020 docs-offline
```
