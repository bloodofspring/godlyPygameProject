from peewee import IntegerField, ForeignKeyField, CharField

from database.models.base import BaseModel
from database.models.pokemonType import PokemonType


class PokemonStats(BaseModel):
    hp = IntegerField()
    attack = IntegerField()
    defence = IntegerField()  # ToDo: Raname to defense
    special_attack = IntegerField()
    special_defence = IntegerField()  # ToDo: Rename to special_defense
    speed = IntegerField()


class Pokemon(BaseModel):
    name = CharField()
    stats = ForeignKeyField(PokemonStats, backref="pokemon")


class PokemonToTypes(BaseModel):
    pokemon = ForeignKeyField(Pokemon, backref="types")
    type = ForeignKeyField(PokemonType, backref="pokemons")
