from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings


# Configure PostgreSQL Database URL
DATABASE_URL = f"postgresql+asyncpg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# Create async SQLAlchemy engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create sessionmaker with async support
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Define the declarative base for SQLAlchemy models
Base = declarative_base()

# Dependency for database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
