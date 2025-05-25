from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from utils.database import Base

# Example model
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    signup_date = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"