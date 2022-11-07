from sqlalchemy.orm import Session

from . import models, schemas, util

def get_address(db: Session, address_id: int):
    # get a particular address with a given id
    return db.query(models.Address).filter(models.Address.id == address_id).first()

def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    # get all addresses from the database
    return db.query(models.Address).offset(skip).limit(limit).all()

def create_address(db: Session, address: schemas.AddressCreate):
    #create an address with given coordinates
    db_address = models.Address(latitude=address.latitude, longitude=address.longitude)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def update_address(db: Session, address_id: int, latitude: float, longitude: float):
    # get the address item with the given id
    address = db.query(models.Address).get(address_id)
    
    # update address item with the given latitude, longitude (if an item with the given id was found)
    if address:
        address.latitude = latitude
        address.longitude = longitude
        db.commit()
        
    return address

def delete_address(db: Session, address_id: int):
    # get the address item with the given id
    address = db.query(models.Address).get(address_id)
    
    # if address item with given id exists, delete it from the database. Otherwise raise 404 error
    if address:
        db.delete(address)
        db.commit()
        
    return {"ok": True}

def search_address(db: Session, given_latitude: float, given_longitude: float, given_distance_km: float):
    # get all the address from db
    all_addresses = db.query(models.Address).all()
    
    within_addresses = []
    # if address is within given distance from the given address return it
    for address in all_addresses:
        difference_distance = util.get_distance_between_two_coordinates(address.latitude, address.longitude,\
                                given_latitude, given_longitude)
        #print(difference_distance, given_distance_km)
        if difference_distance < given_distance_km:
            within_addresses.append(address)
        
    return within_addresses