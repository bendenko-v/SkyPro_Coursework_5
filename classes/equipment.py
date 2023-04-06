from dataclasses import dataclass
from random import uniform
import marshmallow_dataclass
import marshmallow
import json

from config import EQUIP_DATA


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    max_damage: float
    min_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    armors: list[Armor]
    weapons: list[Weapon]


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Weapon:
        """
        Returns Weapon object by name
        """
        for weapon in self.equipment.weapons:
            if weapon.name == weapon_name:
                return weapon
        raise NotImplementedError

    def get_armor(self, armor_name) -> Armor:
        """
        Returns Armor object by name
        """
        for armor in self.equipment.armors:
            if armor.name == armor_name:
                return armor
        raise NotImplementedError

    def get_weapons_names(self) -> list[str]:
        """
        Returns a list of available weapon names
        """
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armors_names(self) -> list[str]:
        """
        Returns a list of available armor names
        """
        return [armor.name for armor in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        """
        Loads data from JSON and returns EquipmentData object
        that contains list of Armor objects and list of Weapon objects.
        """
        with open(EQUIP_DATA, 'r', encoding='utf-8') as file:
            data = json.load(file)

        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)

        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
