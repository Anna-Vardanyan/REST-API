# **DB-API-project**

## Overview
This project is a REST API built using FastAPI, SQLAlchemy, and Alembic. It supports CRUD operations and advanced SQL queries, along with features like full-text search and JSON fields. The API manages operators, subscribers, and their connections, providing functionality for data filtering, joining, grouping, and conditional updates.

## Features
- CRUD operations for managing operators, subscribers, and connections.
- Advanced SQL queries for filtering, joining, grouping, and conditional updates.
- Full-text search on JSON metadata fields using PostgreSQL GIN indexes.
- Environment-based configuration using a `.env` file.
- Database versioning and migration with Alembic.
- Pagination and sorting for API endpoints.

## Requirements
- Python 3.12
- PostgreSQL (recommended to use a Docker container for ease of setup)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AnnaVardanyann/DB-API-project.git
   cd DB-API-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the environment variables:
   - Create a `.env` file in the root directory.
   - Add the required database connection details:

5. Run the Alembic migrations to initialize the database:
   ```bash
   alembic upgrade head
   ```

6. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## Usage
- Access the API documentation at `http://127.0.0.1:8000/docs`.
