from peewee import CharField, ForeignKeyField, FloatField

from database.models.base import BaseModel


class PokemonType(BaseModel):
    name = CharField()


class PokemonTypeInteraction(BaseModel):
    first = ForeignKeyField(PokemonType, backref="interacts_on")
    second = ForeignKeyField(PokemonType, backref="interacts_on")
    k = FloatField()
