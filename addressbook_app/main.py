from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/addresses/", response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db=db, address=address)

@app.put("/addresses/{address_id}", response_model=schemas.Address)
def update_address(address_id: int, latitude:float, longitude:float, db: Session = Depends(get_db)):
    return crud.update_address(db=db, address_id=address_id, latitude=latitude, longitude=longitude)

@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    return crud.delete_address(db=db, address_id=address_id)

@app.get("/addresses/", response_model=List[schemas.Address])
def read_addresses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_addresses(db, skip=skip, limit=limit)
    return users

@app.get("/addresses/{address_id}", response_model=schemas.Address)
def read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@app.get("/search_addresses/", response_model=List[schemas.Address])
def search_addresses(given_latitude: float, given_longitude: float, given_distance_km: float,\
                   db: Session = Depends(get_db)):
    within_addresses = crud.search_address(db, given_latitude, given_longitude, given_distance_km)
    return within_addresses