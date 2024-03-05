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


Base.metadata.create_all(bind=engine)
