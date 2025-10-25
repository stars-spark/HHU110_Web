from sqlalchemy import Column, Integer, String, Text, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(Text, default="")
    cover_url = Column(String(500), default="")

class Discipline(Base):
    __tablename__ = "discipline"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    intro = Column(Text, default="")
    icon = Column(String(200), default="")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    role = Column(String(20), default="user")
    created_at = Column(DateTime, default=datetime.utcnow)

class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    content = Column(Text, nullable=False)
    likes = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User")

def get_engine(db_path="sqlite:///hhu110.db"):
    return create_engine(db_path, echo=False, future=True)

def get_session(db_path="sqlite:///hhu110.db"):
    engine = get_engine(db_path)
    Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return Session(), engine
