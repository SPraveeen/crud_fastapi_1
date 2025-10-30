from models import Book
from sqlalchemy.orm import Session
from schemas import BookCreate

def create_book(db:Session,data:BookCreate):
    book_instance=Book(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance

def get_books(db:Session):
    return db.query(Book).all()

def get_book_by_idd(db:Session,book_id:int):
    return db.query(Book).filter(Book.id==book_id).first()

def update_book(db:Session,book:BookCreate,book_id:int):
    book_querset=db.query(Book).filter(Book.id==book_id).first()
    if book_querset:
        for key,value in book.model_dump().items():
            setattr(book_querset,key,value)
        db.commit()
        db.refresh(book_querset)
    return book_querset

def delete_book(db:Session,id:int):
    book_querset=db.query(Book).filter(Book.id==id).first()
    if book_querset:
        db.delete(book_querset)
        db.commit()
    return book_querset


