from datetime import datetime
from sqlalchemy.orm import Session

from . import models, schemas

def get_flavor(db: Session, flavor_id: int):
    return db.query(models.Flavor).filter(models.Flavor.id == flavor_id).first()

def get_flavors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Flavor).offset(skip).limit(limit).all()

def create_flavor(db: Session, flavor: schemas.FlavorCreate):
    db_flavor = models.Flavor(**flavor.dict())
    db.add(db_flavor)
    db.commit()
    db.refresh(db_flavor)
    return db_flavor

def update_flavor(db: Session, flavor: schemas.FlavorUpdate):
    db_flavor = db.query(models.Flavor).filter(models.Flavor.id == flavor.id).first()
    db_model = models.Flavor(**db_flavor.dict())
    update_flavor = flavor.dict(exclude_unset=True)
    db_flavor = db_model.copy(update=update_flavor)
    db.commit()
    return db_flavor

def delete_flavor(db: Session, flavor_id: int):
    db_flavor = db.query(models.Flavor).filter(models.Flavor.id == flavor_id).first()
    db.delete(db_flavor)
    db.commit()
    return db_flavor

def get_drink(db: Session, drink_id: int):
    return db.query(models.Drink).filter(models.Drink.id == drink_id).first()

def get_drinks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Drink).offset(skip).limit(limit).all()

def create_drink(db: Session, drink: schemas.DrinkCreate):
    db_drink = models.Drink(**drink.dict())
    db.add(db_drink)
    db.commit()
    db.refresh(db_drink)
    return db_drink

def create_drink_now(db: Session, flavor_id: int):
    db_drink = models.Drink(flavor_id=flavor_id, date=datetime.now())
    db.add(db_drink)
    db.commit()
    db.refresh(db_drink)
    return db_drink