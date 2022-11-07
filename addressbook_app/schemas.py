from typing import List, Union

from pydantic import BaseModel

class AddressBase(BaseModel):
    latitude: float
    longitude: float
    
class AddressCreate(AddressBase):
    pass
        
class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True