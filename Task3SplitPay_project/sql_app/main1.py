from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud1 as crud, models1 as models, schemas1 as schemas
from .database1 import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)  #create tables

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.UserInfoBase)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="User ID Already in Use")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.UserRetrieval])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.UserRetrieval)
def read_user(user_id: str,pw :str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.user_password != pw:
        raise HTTPException(status_code=400, detail="Incorrect Password")
    return db_user






""" 

@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items """
