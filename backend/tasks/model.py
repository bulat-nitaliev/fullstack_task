from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from infrastructure import Base



class Tasks(Base):
    title: Mapped[str] = mapped_column(String(300))
    completed: Mapped[bool]