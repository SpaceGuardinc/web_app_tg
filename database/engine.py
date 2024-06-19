import os
from dotenv import find_dotenv, load_dotenv
from sqlalchemy.ext.asyncio import (AsyncSession,
                                    create_async_engine,
                                    async_sessionmaker)

from typing import Generator
from database.models import Base

load_dotenv(find_dotenv())

engine = create_async_engine(os.getenv('DB_URL'), future=True, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Generator:
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()

# class Database:
#     def __init__(self):
#         self.__engine = create_async_engine(os.getenv('DB_URL'), echo=True)
#         self.__session_maker = async_sessionmaker(
#             bind=self.__engine,
#             class_=AsyncSession,
#             expire_on_commit=False,
#             future=True,
#         )
#
#     async def create_db(self):
#         async with self.__engine.begin() as conn:
#             await conn.run_sync(Base.metadata.create_all)
#
#     async def drop_db(self):
#         async with self.__engine.begin() as conn:
#             await conn.run_sync(Base.metadata.drop_all)
#
#     async def __aenter__(self):
#         self.__session = await self.__session_maker()
#         return self.__session
#
#     async def __aexit__(self, exc_type, exc, tb):
#         await self.__session.close()
#
#     @property
#     async def session_maker(self):
#         return self.__session_maker
