from typing import List

from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from infrastructure import crud, models, dtos
from infrastructure.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.post("/users/", response_model=dtos.UserOut)
def create_user(user: dtos.UserIn, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[dtos.UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


@app.get("/users/{user_id}", response_model=dtos.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/accounts/", response_model=dtos.AccountOut)
def create_account(account: dtos.AccountIn, db: Session = Depends(get_db)):
    db_account = crud.get_account_by_title(db, title=account.title)
    if db_account:
        raise HTTPException(status_code=400, detail="title already registered")
    return crud.create_account(db=db, account=account)


@app.get("/accounts/")  # , response_model=List[dtos.AccountOut])
def read_account(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_accounts(db, skip=skip, limit=limit)


@app.get("/accounts/{account_id}", response_model=dtos.AccountOut)
def read_account(account_id: int, db: Session = Depends(get_db)):
    db_account = crud.get_account(db, account_id=account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account
