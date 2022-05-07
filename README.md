# FastAPI / PostgresQL / Masonite ORM Starter

This project serves as a starter project for FastAPI usecases. The project utlizes PostgresQL as the database, and Masonite-ORM as the database manager.

## Setup

Follow the below steps to start the project.

### Create a `.env` file

1. `touch .env`
2. Populate your env file with the following:

   ```
   SECRET_KEY=supersecret
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_SERVER=db
   POSTGRES_PORT=5432
   POSTGRES_DB=postgres
   LOG_QUERIES=true
   ```

### Install project requirements

I recommend using venv, conda, or your favorite virtual environment library for python.

```
conda create -n masonite python=3.8
conda activate masonite
pip install -r requirements.txt
```

### Migrate the database

`masonite-orm migrate`

### Seed the database

`masonite-orm seed:run Database`

## Run Server

`uvicorn api.main:app --reload`

## API Docs

`http://localhost:8000/docs`
