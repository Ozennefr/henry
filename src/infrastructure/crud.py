#!/home/user/venv/bin
# -*- coding: utf-8 -*-
# Part of the Henry project. Do not use as standalone.
# Refer to the project documentation for authorship and licencing information.

"""CRUD utilities for the DB.
"""

from sqlalchemy.orm import Session
from infrastructure import models, dtos, translators

### USER
def get_user(db: Session, user_id: int):
    res = db.query(models.User).filter(models.User.uid == user_id).first()
    return translators.to_dto(res)


def get_user_by_name(db: Session, name: str):
    res = db.query(models.User).filter(models.User.name == name).first()
    return translators.to_dto(res)


def get_users(db: Session, skip: int = 0, limit: int = 100):
    res = db.query(models.User).offset(skip).limit(limit).all()
    return (translators.to_dto(res_line) for res_line in res)


def create_user(db: Session, user: dtos.UserIn):
    db_user = translators.from_dto(user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


### ACCOUNT
def get_account(db: Session, account_id: int):
    res = db.query(models.Account).filter(models.Account.aid == account_id).first()
    return translators.to_dto(res)


def get_account_by_title(db: Session, title: str):
    res = db.query(models.Account).filter(models.Account.title == title).first()
    return translators.to_dto(res)


def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    res = db.query(models.Account).offset(skip).limit(limit).all()
    return (translators.to_dto(res_line) for res_line in res)


def create_account(db: Session, account: dtos.AccountIn):
    db_account = translators.from_dto(account)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account
