from datetime import datetime

from sqlalchemy import Column, Integer, BigInteger, String, Text, DateTime

from app.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    telegram_user_id = Column(BigInteger, index=True)
    document_name = Column(String(255))
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
