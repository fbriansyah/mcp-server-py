from utils.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column

class TransferAccount(Base):
  __tablename__ = "transfer_account"

  uuid = Column(String(36), primary_key=True)
  bank_code = Column(String(5))
  bank_name = Column(String(50))
  account_no = Column(String(50))
  account_name = Column(String(100))

class TransferConfig(Base):
  __tablename__ = "transfer_config"

  uuid = Column(String(36), primary_key=True)
  priority = Column(Integer)
  transfer_type = Column(String(50))
  bank_account_uuid = Column(String(36), ForeignKey("transfer_account.uuid"))
  account: Mapped["TransferAccount"] = relationship("TransferAccount")
  is_active = Column(Boolean)
  deleted_at = Column(DateTime)

  def __repr__(self):
    return f"<TransferConfig(uuid={self.uuid}, priority={self.priority}, transfer_type={self.transfer_type}, bank_name={self.account.bank_name}, bank_code={self.account.bank_code})>"
