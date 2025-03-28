import importlib
import os
from app.models.base_model import Base
from app.repository.database import engine


def run_migrations():
    """
    Simple function to create all database tables based on the imported models.
    In a production system, you would use a tool like Alembic for migrations.
    """
    # Ensure all models are imported so they're registered with Base
    models_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models")
    for file in os.listdir(models_dir):
        if file.endswith(".py") and file != "__init__.py" and file != "base_model.py":
            module_name = file[:-3]  # Remove .py extension
            importlib.import_module(f"app.models.{module_name}")

    # Create all tables
    Base.metadata.create_all(bind=engine)
