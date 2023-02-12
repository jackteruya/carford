from sqlalchemy import Column, String, DATE, Integer

from infra.db import Base


class Owners(Base):
    """Owners Model"""

    __tablename__ = "onwers"

    id = Column(Integer, primary_key=True, name='id', unique=True, index=True)
    name = Column(String(64), name='name', nullable=False)
    document = Column(String(64), name='document', nullable=False)
    date_of_birth = Column(DATE, name='date_of_birth', nullable=False)

    def __repr__(self):
        return f'Owner: [id={self.id}, name={self.name}]'
