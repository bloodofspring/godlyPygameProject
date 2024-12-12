from peewee import SqliteDatabase
from typing import Final
from config import DATABASE_NAME

db: Final[SqliteDatabase] = SqliteDatabase(DATABASE_NAME)
