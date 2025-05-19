from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import os

load_dotenv()

def create_db_with_owner(db_name, host="192.168.5.55", port=7777):
    admin_user = os.getenv("POSTGRES_ADMIN_USER", "postgres")
    admin_password = os.getenv("POSTGRES_ADMIN_PASSWORD", "postgres")
    owner_name = os.getenv("NEW_OWNER_NAME")
    owner_password = os.getenv("NEW_OWNER_PASSWORD")

    try:
        admin_connection_url = f"postgresql://{admin_user}:{admin_password}@{host}:{port}/postgres"
        admin_engine = create_engine(admin_connection_url)

        db_connection_url = f"postgresql://{owner_name}:{owner_password}@{host}:{port}/{db_name}"
        if not database_exists(db_connection_url):
            owner_connection_url = f"postgresql://{admin_user}:{admin_password}@{host}:{port}/postgres"
            owner_engine = create_engine(owner_connection_url)
            with owner_engine.connect() as conn:
                conn.execute(text(f"CREATE USER {owner_name} WITH PASSWORD '{owner_password}';"))
                conn.execute(text(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {owner_name};"))

            create_database(db_connection_url)
            print(f"Database '{db_name}' created successfully with owner '{owner_name}'.")
        else:
            print(f"Database '{db_name}' already exists.")

    except Exception as e:
        print(f"An error occurred: {e}")

create_db_with_owner(db_name="apiproject")