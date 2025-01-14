from typing import Final

from database import create_tables
from database.models import *

pokemon_stats: Final[dict[str, dict[str, tuple[str, ...] | int]]] = {
    "Articuno": {
        "hp": 90,
        "atk": 85,
        "def": 100,
        "sp.atk": 95,
        "sp.def": 125,
        "speed": 85,
        "types": ("ice", "flying")
    },
    "Blaziken": {
        "hp": 80,
        "atk": 120,
        "def": 70,
        "sp.atk": 110,
        "sp.def": 70,
        "speed": 80,
        "types": ("fire", "fighting")
    },
    "Charizard": {
        "hp": 78,
        "atk": 84,
        "def": 78,
        "sp.atk": 109,
        "sp.def": 85,
        "speed": 100,
        "types": ("fire", "flying")
    },
    "Dragonite": {
        "hp": 91,
        "atk": 134,
        "def": 95,
        "sp.atk": 100,
        "sp.def": 100,
        "speed": 80,
        "types": ("dragon", "flying")
    },
    "Gardevoir": {
        "hp": 68,
        "atk": 65,
        "def": 65,
        "sp.atk": 125,
        "sp.def": 115,
        "speed": 80,
        "types": ("psychic", "fairy")
    },
    "Gengar": {
        "hp": 60,
        "atk": 65,
        "def": 60,
        "sp.atk": 130,
        "sp.def": 75,
        "speed": 110,
        "types": ("ghost", "poison")
    },
    "Groudon": {
        "hp": 100,
        "atk": 150,
        "def": 140,
        "sp.atk": 100,
        "sp.def": 90,
        "speed": 90,
        "types": ("ground",)
    },
    "Gyarados": {
        "hp": 95,
        "atk": 125,
        "def": 79,
        "sp.atk": 60,
        "sp.def": 100,
        "speed": 81,
        "types": ("water", "flying")
    },
    "Kyogre": {
        "hp": 100,
        "atk": 100,
        "def": 90,
        "sp.atk": 150,
        "sp.def": 140,
        "speed": 90,
        "types": ("water",)
    },
    "Lapras": {
        "hp": 130,
        "atk": 85,
        "def": 80,
        "sp.atk": 85,
        "sp.def": 95,
        "speed": 60,
        "types": ("water", "ice")
    },
    "Lucario": {
        "hp": 70,
        "atk": 110,
        "def": 70,
        "sp.atk": 115,
        "sp.def": 70,
        "speed": 90,
        "types": ("fighting", "steel")
    },
    "Lugia": {
        "hp": 106,
        "atk": 90,
        "def": 130,
        "sp.atk": 90,
        "sp.def": 154,
        "speed": 110,
        "types": ("psychic", "flying")
    },
    "Machamp": {
        "hp": 90,
        "atk": 130,
        "def": 80,
        "sp.atk": 65,
        "sp.def": 85,
        "speed": 55,
        "types": ("fighting",)
    },
    "Mew": {
        "hp": 100,
        "atk": 100,
        "def": 100,
        "sp.atk": 100,
        "sp.def": 100,
        "speed": 100,
        "types": ("psychic",)
    },
    "Mewtwo": {
        "hp": 106,
        "atk": 110,
        "def": 90,
        "sp.atk": 154,
        "sp.def": 90,
        "speed": 130,
        "types": ("psychic",)
    },
    "Moltres": {
        "hp": 90,
        "atk": 100,
        "def": 90,
        "sp.atk": 100,
        "sp.def": 125,
        "speed": 90,
        "types": ("fire", "flying")
    },
    "Pikachu": {
        "hp": 45,
        "atk": 80,
        "def": 50,
        "sp.atk": 75,
        "sp.def": 60,
        "speed": 120,
        "types": ("electric",)
    },
    "Rayquaza": {
        "hp": 105,
        "atk": 150,
        "def": 90,
        "sp.atk": 150,
        "sp.def": 90,
        "speed": 95,
        "types": ("dragon", "flyng")
    },
    "Sceptile": {
        "hp": 70,
        "atk": 85,
        "def": 65,
        "sp.atk": 105,
        "sp.def": 85,
        "speed": 120,
        "types": ("grass",)
    },
    "Swampert": {
        "hp": 100,
        "atk": 110,
        "def": 90,
        "sp.atk": 85,
        "sp.def": 90,
        "speed": 60,
        "types": ("water", "ground")
    },
    "Zapdos": {
        "hp": 90,
        "atk": 90,
        "def": 85,
        "sp.atk": 125,
        "sp.def": 90,
        "speed": 100,
        "types": ("electric", "flying")
    }
}

def insert_data():
    create_tables()

    for pokemon_name, stats in zip(pokemon_stats.keys(), pokemon_stats.values()):
        ts = []

        for t in stats["types"]:
            ts.append(PokemonType.get_or_create(name=t)[0])

        stats_db = PokemonStats.create(
            hp=stats["hp"],
            atk=stats["atk"],
            defence=stats["def"],
            atk_speed=stats["sp.atk"],
            defence_speed=stats["sp.def"],
            speed=stats["speed"]
        )

        pokemon_db = Pokemon.create(
            name=pokemon_name,
            stats=stats_db,
        )

        for t in ts:
            PokemonToTypes.create(
                pokemon=pokemon_db,
                type=t,
            )

        print(f"Pokemon {pokemon_name} added!")


insert_data()
