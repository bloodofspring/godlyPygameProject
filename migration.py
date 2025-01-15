from playhouse.migrate import *
from database import db


def start_migration():
    migrator = SqliteMigrator(db)

    with db.transaction():
        migrate(
            migrator.rename_column("PokemonStats", "special_defence", "special_defense"),  # table, old_name, new_name
            migrator.rename_column("PokemonStats", "defence", "defense"),
        )

        print("migration finished!")


start_migration()
