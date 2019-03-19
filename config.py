import os
from pathlib import Path

home = str(Path.home())
CONFIG_DIRECTORY = f"{home}/.betterles/"
CONFIG_LOCATION_MENU = f"{home}/.betterles/config.yml"


def create_config():
    os.makedirs(os.path.dirname(CONFIG_LOCATION_MENU), exist_ok=True)
    if not os.path.isfile(CONFIG_LOCATION_MENU):
        with open(CONFIG_LOCATION_MENU, "w") as f:
            f.write("""# Configure your menus here. Sub folders are supported.
# Plugin names are the same as in the Live plugin browser.
# NOTE: This feature will not function with audio units enabled in Live preferences due to limitations in the Live API.
# Example config:
menu:
  # - Instruments:
  #   - Kontakt
  #   - Addictive Keys
  # - Synths:
  #   - Serum
  # - OTT

""")
