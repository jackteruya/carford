from sqlalchemy import Column, String, DATE, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

from infra.db import Base
from utils.constants import ColorCar, ModelCar


class Cars(Base):
    """Cars Model"""

    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, name='id', unique=True, index=True)
    name = Column(String(64), name='name', nullable=False)
    color = Column(String(64), name='color', nullable=False)
    model = Column(String(64), name='model', nullable=False)
    owner_id = Column(Integer, ForeignKey("onwers.id"), name='owner_id', nullable=False)
    owner = relationship("Owners")

    def __repr__(self):
        return f'Car: [id={self.id}, name={self.name}]'
