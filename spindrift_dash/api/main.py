from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {
        "message": "Yup, that's it"
    }

@app.get("/flavors/", response_model=List[schemas.Flavor])
def get_flavors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_flavors(db=db, skip=skip, limit=limit)

@app.get("/flavors/{flavor_id}", response_model=schemas.Flavor)
def get_flavor(flavor_id: int, db: Session = Depends(get_db)):
    return crud.get_flavor(db=db, flavor_id=flavor_id)

@app.post("/flavors/", response_model=schemas.Flavor)
def create_flavor(flavor: schemas.FlavorCreate, db: Session = Depends(get_db)):
    return crud.create_flavor(db=db, flavor=flavor)

@app.patch("/flavors/{flavor_id}", response_model=schemas.Flavor)
def update_flavor(flavor_id: int, flavor: schemas.FlavorUpdate, db: Session = Depends(get_db)):
    return crud.update_flavor(db=db, flavor_id=flavor_id, flavor=flavor)

@app.delete("/flavors/{flavor_id}")
def delete_flavor(flavor_id: int, db: Session = Depends(get_db)):
    if crud.get_flavor(db=db, flavor_id=flavor_id) is None:
        raise HTTPException(status_code=404, detail="Flavor not found")
    return crud.delete_flavor(db=db, flavor_id=flavor_id)

@app.get("/drinks/", response_model=List[schemas.Drink])
def get_drinks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_drinks(db=db, skip=skip, limit=limit)

@app.get("/drinks/{drink_id}", response_model=schemas.Drink)
def get_drink(drink_id: int, db: Session = Depends(get_db)):
    return crud.get_drink(db=db, drink_id=drink_id)

@app.post("/drinks/", response_model=schemas.Drink)
def create_drink(drink: schemas.DrinkCreate, db: Session = Depends(get_db)):
    return crud.create_drink(db=db, drink=drink)

@app.post("/drinks/now", response_model=schemas.Drink)
def create_drink_now(flavor_id: int, db: Session = Depends(get_db)):
    return crud.create_drink_now(db=db, flavor_id=flavor_id)
