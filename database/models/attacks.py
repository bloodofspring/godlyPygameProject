from peewee import CharField, ForeignKeyField, IntegerField

from database.models.pokemonType import PokemonType
from database.models.base import BaseModel


class PokemonAttack(BaseModel):
    name = CharField()
    type = ForeignKeyField(PokemonType)
    category = CharField()
    power = IntegerField()
    accuracy = IntegerField()
