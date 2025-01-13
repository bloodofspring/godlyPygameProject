from typing import Final

pokemon_stats: Final[dict[str, dict[str, tuple[str, ...] | int]]] = {
    "Charizard": {
        "hp": 78,
        "atk": 84,
        "def": 78,
        "sp.atk": 109,
        "sp.def": 85,
        "speed": 100,
        "types": ("huj",),
    },
    "Rayquaza": {
        "hp": 105,
        "atk": 150,
        "def": 90,
        "sp.atk": 150,
        "sp.def": 90,
        "speed": 95,
        "types": ("huj",)
    },
    "Mewtwo": {
        "hp": 106,
        "atk": 110,
        "def": 90,
        "sp.atk": 154,
        "sp.def": 90,
        "speed": 130,
        "types": ("huj",)
    },
    "Mew": {
        "hp": 100,
        "atk": 100,
        "def": 100,
        "sp.atk": 100,
        "sp.def": 100,
        "speed": 100,
        "types": ("huj",)
    },
}
