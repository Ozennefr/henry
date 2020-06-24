#!/venv/bin python
# -*- coding: utf-8 -*-
# Part of the Henry project. Do not use as standalone.
# Refer to the project documentation for authorship and licencing information.

"""Model of the tables.
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from infrastructure.db import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    accounts = relationship("AccountOwner", back_populates="owner")


class Account(Base):
    __tablename__ = "accounts"

    aid = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, index=True)

    owners = relationship("AccountOwner", back_populates="account")


class AccountOwner(Base):
    __tablename__ = "accounts_owners"

    owner_id = Column(Integer, ForeignKey("users.uid"), primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.aid"), primary_key=True)
    shares = Column(Integer, default=1)

    owner = relationship("User", back_populates="accounts")
    account = relationship("Account", back_populates="owners")
