from utils.database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import Column, String, ForeignKey, DateTime, Numeric

class Beneficiary(Base):
  __tablename__ = "bt_beneficiary"
  uuid = Column(String(36), primary_key=True)
  account_name = Column(String(100))
  account__no = Column(String(100))

class BankTransfer(Base):
  __tablename__ = "bank_transfer"

  uuid = Column(String(36), primary_key=True)
  beneficiary_id = Column(String(36), ForeignKey("bt_beneficiary.uuid"))
  beneficiary: Mapped["Beneficiary"] = relationship("Beneficiary")
  external_id = Column(String(100))
  amount = Column(String())
  transfer_type = Column(String(50))
  bank_acquirer = Column(String(50))
  remark = Column(String())
  status = Column(String(20))
  created_at = Column(DateTime)

class BTTransaction(Base):
  __tablename__ = "bt_transaction"
  
  uuid = Column(String(36), primary_key=True)
  transfer_order = Column(Numeric)
  bank_transfer_id = Column(String(36), ForeignKey("bank_transfer.uuid"))
  bank_transfer: Mapped["BankTransfer"] = relationship("BankTransfer")
  bank_acquirer = Column(String(50))
  transfer_type = Column(String(50))
  status = Column(String(20))
  created_at = Column(DateTime)
  