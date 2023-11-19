#!/usr/bin/env python

import re
import sys
from pathlib import Path


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent.parent))

from custom_components.hon.const import APPLIANCES
from custom_components.hon.binary_sensor import BINARY_SENSORS
from custom_components.hon.button import BUTTONS
from custom_components.hon.climate import CLIMATES
from custom_components.hon.fan import FANS
from custom_components.hon.light import LIGHTS
from custom_components.hon.lock import LOCKS
from custom_components.hon.number import NUMBERS
from custom_components.hon.select import SELECTS
from custom_components.hon.sensor import SENSORS
from custom_components.hon.switch import (
    SWITCHES,
    HonControlSwitchEntityDescription,
    HonSwitchEntityDescription,
)

ENTITY_CATEGORY_SORT = ["control", "config", "sensor"]

entities = {
    "binary_sensor": BINARY_SENSORS,
    "button": BUTTONS,
    "climate": CLIMATES,
    "fan": FANS,
    "light": LIGHTS,
    "lock": LOCKS,
    "number": NUMBERS,
    "select": SELECTS,
    "sensor": SENSORS,
    "switch": SWITCHES,
}

result = {}
for entity_type, appliances in entities.items():
    for appliance, data in appliances.items():
        for entity in data:
            if isinstance(entity, HonControlSwitchEntityDescription):
                key = f"{entity.turn_on_key}` / `{entity.turn_off_key}"
            else:
                key = entity.key
            attributes = (key, entity.name, entity.icon, entity_type)
            category = (
                "control"
                if entity.key.startswith("settings")
                or isinstance(entity, HonSwitchEntityDescription)
                or isinstance(entity, HonControlSwitchEntityDescription)
                or entity_type in ["button", "climate", "lock", "light", "fan"]
                else "sensor"
            )
            result.setdefault(appliance, {}).setdefault(
                entity.entity_category or category, []
            ).append(attributes)
text = ""
for appliance, categories in sorted(result.items()):
    text += f"\n### {APPLIANCES[appliance]}\n"
    categories = {k: categories[k] for k in ENTITY_CATEGORY_SORT if k in categories}
    for category, data in categories.items():
        text += f"#### {str(category).capitalize()}s\n"
        text += "| Name | Icon | Entity | Key |\n"
        text += "| --- | --- | --- | --- |\n"
        for key, name, icon, entity_type in sorted(data, key=lambda d: d[1]):
            icon = f"`{icon.replace('mdi:', '')}`" if icon else ""
            text += f"| {name} | {icon} | `{entity_type}` | `{key}` |\n"

with open(Path(__file__).parent.parent / "README.md", "r") as file:
    readme = file.read()
readme = re.sub(
    "(## Appliance Features\n)(?:.|\\s)+?([^#]## |\\Z)",
    f"\\1{text}\\2",
    readme,
    re.DOTALL,
)
entities = sum(len(x) for cat in result.values() for x in cat.values())
readme = re.sub("badge/Entities-\\d+", f"badge/Entities-{entities}", readme)
with open(Path(__file__).parent.parent / "README.md", "w") as file:
    file.write(readme)
