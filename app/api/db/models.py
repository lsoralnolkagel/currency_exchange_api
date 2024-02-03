import asyncio
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from CEA.app.api.db.database import Base, engine


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    full_name: Mapped[str]
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_models())
