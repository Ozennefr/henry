#!/home/user/venv/bin python
# -*- coding: utf-8 -*-
# Part of the Henry project. Do not use as standalone.
# Refer to the project documentation for authorship and licencing information.

"""Setting up SQL Alchemy and PG
"""

import sqlalchemy
import pydantic
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class DbConfig(pydantic.BaseSettings):
    user: str
    password: str
    db: str
    host: str
    port: int = 5432

    @property
    def dsn(self):
        return (
            f"postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"
        )

    class Config:
        env_prefix = "POSTGRES_"
        case_sensitive = False


conf = DbConfig()


engine = sqlalchemy.create_engine(conf.dsn)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
