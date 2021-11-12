import os

from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_PROTOCOL = os.getenv("DB_PROTOCOL")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

engine = sqlalchemy.create_engine(
    url=f"{DB_PROTOCOL}://{DB_USER}:{DB_PASS}@{HOST}:{PORT}/{DB_NAME}"
)

Base = automap_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# reflect: takes a look on the database and generates matching classes
Base.prepare(engine, reflect=True)
