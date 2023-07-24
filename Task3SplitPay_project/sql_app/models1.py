from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database1 import Base


class UserInformation(Base):
    __tablename__ = "user_information"

    user_id = Column(String(30),primary_key=True,index = True)
    unique_genuserid = Column(Integer,autoincrement=True,index=True)
    user_fullname = Column(String(30))
    mail_id = Column(String(30))
    user_display_pic = Column(String(50))
    user_password = Column(String(30))

    #items = relationship("Item", back_populates="owner")

class SplitRecords(Base):
    __tablename__ = "split_records"

    split_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(30))
    initiator_id = Column(String(30))
    amount = Column(Integer)
    payable_by_each = Column(Integer)
    split_amongst_user_ids = Column(String(100))
    
    #owner_id = Column(Integer, ForeignKey("user_information.user_id"))

    #owner = relationship("User", back_populates="items")


def create_transacttableforuser_class(user_id):
    class UserTransactions(Base):
        __tablename__ = user_id+"_transactions"

        user_indept_transaction_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        recipient_id = Column(Integer)
        eq_split_id = Column(Integer)
        sum = Column(Integer)
        status = Column(bool,default=True)

    return UserTransactions

