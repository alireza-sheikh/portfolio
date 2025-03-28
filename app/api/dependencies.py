from app.repository.database import get_db

# We can re-export the dependency directly
db_dependency = get_db
