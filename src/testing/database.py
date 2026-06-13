from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing import AsyncGenerator

engine = create_async_engine(
    "postgresql+asyncpg://postgres:Muhammed4ever@localhost:5432/testing"
)

async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

db = async_session_maker()

async def get_db() -> AsyncGenerator[AsyncGenerator, None]:
    async with async_session_maker as session:
        yield session