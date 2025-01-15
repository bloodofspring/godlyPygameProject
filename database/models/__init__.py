from .attacks import PokemonAttack
from .pokemon import PokemonStats, Pokemon, PokemonToTypes, PokemonToAttacks
from .pokemonType import PokemonType, PokemonTypeInteraction

active_models = [
    PokemonStats,
    Pokemon,
    PokemonToTypes,

    PokemonType,
    PokemonTypeInteraction,
    PokemonToAttacks,

    PokemonAttack,
]
