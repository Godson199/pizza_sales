from database.db import Base
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.util import ChoiceType

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(80), unique=True, index=True)
    password = Column(Text, nullable=True)    
    is_active = Column(Boolean, default=False)  # 1 for active, 0 for inactive
    is_superuser = Column(Boolean, default=False)  # 1 for superuser, 0 for regular user    
    order = relationship('Order', back_populates='user')

    def __repr__(self):
        return f"<User {self.username}>"


class Order(Base):
    __tablename__ = "choices"
    ORDER_STATUS = (
        ('PENDING', 'pending'),
        ('IN_PROGRESS', 'in-progress'),
        ('DELIVERED', 'delivered'),
        ('CANCELLED', 'cancelled')
    )

    PIZZA_SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA_LARGE', 'extra-large')
    )   

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    order_status = Column(ChoiceType(ORDER_STATUS), default='PENDING')
    pizza_size = Column(ChoiceType(PIZZA_SIZES), default='MEDIUM')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='orders')

    def __repr__(self):
        return f"<Order {self.id}>"


    
