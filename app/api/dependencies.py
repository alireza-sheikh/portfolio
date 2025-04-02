from fastapi import Depends
from sqlalchemy.orm import Session

from app.repository.database import get_db


# Define db dependency - this is the correct format
db_dependency = Depends(get_db)
