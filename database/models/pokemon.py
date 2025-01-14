from peewee import IntegerField, ForeignKeyField, CharField

from database.models.base import BaseModel
from database.models.pokemonType import PokemonType


class PokemonStats(BaseModel):
    hp = IntegerField()
    atk = IntegerField()
    defence = IntegerField()
    atk_speed = IntegerField()
    defence_speed = IntegerField()
    speed = IntegerField()


class Pokemon(BaseModel):
    name = CharField()
    stats = ForeignKeyField(PokemonStats, backref="pokemon")


class PokemonToTypes(BaseModel):
    pokemon = ForeignKeyField(Pokemon, backref="types")
    type = ForeignKeyField(PokemonType, backref="pokemons")
