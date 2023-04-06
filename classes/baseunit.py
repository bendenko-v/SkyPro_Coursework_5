from abc import ABC, abstractmethod

from classes.units import UnitClass
from classes.equipment import Weapon, Armor


class BaseUnit(ABC):
    """
    Base Unit Class
    """

    def __init__(self, name: str, unit_class: UnitClass):
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon: Weapon
        self.armor: Armor
        self._is_skill_used = False

    @property
    def health_points(self) -> float:
        """
        Returns unit HP
        """
        return self.hp

    @property
    def stamina_points(self) -> float:
        """
        Returns unit Stamina
        """
        return self.stamina

    def equip_weapon(self, weapon: Weapon) -> None:
        """
        Equip Weapon to Hero
        """
        self.weapon = weapon

    def equip_armor(self, armor: Armor) -> None:
        """
        Equip Armor to Hero
        """
        self.armor = armor

    def _count_damage(self, target) -> float | None:
        """
        Calculates the damage the user will deal to an enemy or vice versa.
        If the hero has enough stamina to use the weapon -> calculate damage
        Reduce the hero's stamina
        If the enemy has enough stamina to use the armor -> calculate defence
        Reduce the enemy's stamina
        Use get_damage() method to reduce enemy's HP
        or return None if the hero's stamina is not enough
        """
        if self.stamina_points < self.weapon.stamina_per_hit:
            return None

        damage = round(self.weapon.damage * self.unit_class.attack, 1)
        self.stamina = round(self.stamina_points - self.weapon.stamina_per_hit, 1)

        if target.stamina_points >= target.armor.stamina_per_turn:
            defence = round(target.armor.defence * target.unit_class.armor, 1)
            target.stamina = round(target.stamina_points - target.armor.stamina_per_turn, 1)
        else:
            defence = 0

        damage = round(damage - defence, 1)
        target.get_damage(damage)
        return damage

    def get_damage(self, damage: float) -> None:
        """
        Hero gets a damage
        Args:
            damage: damage points
        """
        # TODO получение урона целью
        #      присваиваем новое значение для аттрибута self.hp
        if damage > 0:
            if self.hp - damage >= 0:
                self.hp = round(self.hp - damage, 1)
            else:
                self.hp = 0

    @abstractmethod
    def hit(self, target) -> str:
        pass

    def use_skill(self, target) -> str:
        """
        Hero uses a skill

        Args:
            target: BaseUnit, who is trying to use the skill

        Returns:
            the result of use (or info that the skill was used)
        """
        """
        метод использования умения.
        если умение уже использовано возвращаем строку
        Навык использован
        Если же умение не использовано тогда выполняем функцию
        self.unit_class.skill.use(user=self, target=target)
        и уже эта функция вернем нам строку которая характеризует выполнение умения
        """
        if self._is_skill_used:
            return '🌀 The skill has already been used!<br>'

        return self.unit_class.skill.use(user=self, target=target)
