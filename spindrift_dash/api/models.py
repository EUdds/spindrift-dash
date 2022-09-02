from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class Flavor(Base):
    __tablename__ = "flavors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), index=True)
    _ingredients = Column(String(64), index=True)
    calories = Column(Integer, index=True)
    total_fat = Column(Integer, index=True)
    saturated_fat = Column(Integer, index=True)
    carbohydrates = Column(Integer, index=True)
    sugars = Column(Integer, index=True)
    protein = Column(Integer, index=True)
    spiked = Column(Boolean, index=True)
    
    @property
    def ingredients(self):
        return self._ingredients.split(",")

    @ingredients.setter
    def ingredients(self, ingredients):
        self._ingredients = ",".join(ingredients)

class Drink(Base):
    __tablename__ = "drinks"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    flavor = relationship("Flavor")
    flavor_id = Column(Integer, ForeignKey("flavors.id"), index=True)


