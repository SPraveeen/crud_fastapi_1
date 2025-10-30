from pydantic import BaseModel
class BookBase(BaseModel):
    title:str
    author:str
    description:str
    year:int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id:int

    class config:
        # orm_mode=True #for pydantic version < 2.0
        from_attribute=True #version >2.0
        