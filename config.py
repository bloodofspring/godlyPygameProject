from typing import Final

test_mode: Final[bool] = True  # pass true if you want to switch on test mode
version: Final[str] = "1.1.1"  # version num.

DATABASE_NAME: Final[str] = f"database v{version} {'[test_version]' if test_mode else ''}".strip()
