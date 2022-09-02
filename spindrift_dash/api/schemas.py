from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class FlavorBase(BaseModel):
    name: str
    ingredients: List[str]
    calories: int
    total_fat: int
    saturated_fat: int
    carbohydrates: int
    sugars: int
    protein: int

class FlavorCreate(FlavorBase):
    pass

class FlavorUpdate(FlavorBase):
    id: int
    pass

class Flavor(FlavorBase):
    id: int

    class Config:
        orm_mode = True

class DrinkBase(BaseModel):
    date: datetime

class DrinkCreate(DrinkBase):
    flavor_id: int

class Drink(DrinkBase):
    id: int
    flavor: Flavor
    flavor_id: int

    class Config:
        orm_mode = True