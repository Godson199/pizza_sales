from database.db import engine, Base
from models.db_models import User, Order

Base.metadata.create_all(bind=engine)