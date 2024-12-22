from sqlalchemy.orm import Mapped, mapped_column
from .meta_model import Base
from sqlalchemy import  Text

class Request(Base):
    __tablename__ = 'requests'
    
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    user_tg_id : Mapped[str] = mapped_column()
    message : Mapped[str] = mapped_column(Text)
    answer : Mapped[str] = mapped_column(Text)
    