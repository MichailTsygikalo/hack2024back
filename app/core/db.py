from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, DeclarativeMeta, sessionmaker, Session

from app.config import DB_POSTGRES_HOST, DB_POSTGRES_NAME, DB_POSTGRES_PASSWORD, DB_POSTGRES_PORT, DB_POSTGRES_USERNAME

engine = create_engine(f'postgresql+psycopg2://{DB_POSTGRES_USERNAME}:{DB_POSTGRES_PASSWORD}@{DB_POSTGRES_HOST}:{DB_POSTGRES_PORT}/{DB_POSTGRES_NAME}')
Base: DeclarativeMeta = declarative_base()
local_session = sessionmaker(engine, class_=Session, expire_on_commit=False)

def get_session():
    with local_session() as session:
        yield session