from peewee import IntegerField, ForeignKeyField, CharField

from database.models.attacks import PokemonAttack
from database.models.base import BaseModel
from database.models.pokemonType import PokemonType


class PokemonStats(BaseModel):
    hp = IntegerField()
    attack = IntegerField()
    defense = IntegerField()
    special_attack = IntegerField()
    special_defense = IntegerField()
    speed = IntegerField()


class Pokemon(BaseModel):
    name = CharField()
    stats = ForeignKeyField(PokemonStats, backref="pokemon")


class PokemonToTypes(BaseModel):
    pokemon = ForeignKeyField(Pokemon, backref="types")
    type = ForeignKeyField(PokemonType, backref="pokemons")


class PokemonToAttacks(BaseModel):
    pokemon = ForeignKeyField(Pokemon, backref="attacks")
    attack = ForeignKeyField(PokemonAttack, backref="pokemons")
