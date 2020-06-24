#!/home/user/venv/bin
# -*- coding: utf-8 -*-
# Part of the Henry project. Do not use as standalone.
# Refer to the project documentation for authorship and licencing information.

"""Translators to convert from DTO to DB and back
"""
from typing import Any
from functools import singledispatch

from infrastructure import dtos
from infrastructure import models


@singledispatch
def from_dto(dto: Any) -> Any:
    raise NotImplementedError


@from_dto.register
def user_from_dto(dto: dtos.UserIn) -> models.User:
    return models.User(name=dto.name)


@from_dto.register
def account_from_dto(dto: dtos.AccountIn) -> models.Account:
    return models.Account(title=dto.title, description=dto.description)


@singledispatch
def to_dto(model: Any) -> Any:
    raise NotImplementedError


@to_dto.register
def user_to_dto(model: models.User) -> dtos.UserOut:
    return dtos.UserOut.from_orm(model)


@to_dto.register
def account_to_dto(model: models.Account) -> dtos.AccountOut:
    return dtos.AccountOut.from_orm(model)
