#!/home/user/venv/bin
# -*- coding: utf-8 -*-
# Part of the Henry project. Do not use as standalone.
# Refer to the project documentation for authorship and licencing information.

"""Defines the DTO (Data Transfer Objects).
    These DTOs handle interaction between the DB and API.
"""

from __future__ import annotations

from typing import List
from typing import ForwardRef

from pydantic import BaseModel


class AccountBase(BaseModel):
    """Common for both DTOs."""

    title: str
    description: str = None

    class Config:
        orm_mode = True


class AccountIn(AccountBase):
    """DTO From API to DB."""

    class Config:
        orm_mode = False


class AccountOut(AccountBase):
    """DTO From DB to API."""

    aid: int


class UserBase(BaseModel):
    """Common for both DTOs."""

    name: str

    class Config:
        orm_mode = True


class UserIn(UserBase):
    """DTO From API to DB."""

    class Config:
        orm_mode = False


class UserOut(UserBase):
    """DTO From DB to API."""

    uid: int
    accounts: List[AccountOut]


class AccountOwnerBase(BaseModel):
    """Common for both DTOs."""

    aid: int
    uid: int
    shares: int

    class Config:
        orm_mode = True


class AccountOwnerIn(AccountOwnerBase):
    """DTO From API to DB."""

    class Config:
        orm_mode = False


class AccountOwnerOut(AccountOwnerBase):
    """DTO From DB to API."""

    owner: UserBase
    account: AccountBase
