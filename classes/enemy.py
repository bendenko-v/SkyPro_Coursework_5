import random

from classes.baseunit import BaseUnit


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        Enemy unit hit action

        Args:
            target: The hero who gets hit

        Returns:
            the result of hit action
        """

        # Random 1/10 chance to use skill
        if not self._is_skill_used:
            skill_chance = random.randint(1, 100)
            if skill_chance < 11:
                return self.use_skill(target)

        damage = self._count_damage(target)

        if not damage:
            return f"🟡 {self.name} tried to use the {self.weapon.name}, but he didn't have enough stamina.<br>"

        if damage > 0:
            return f"⚔ {self.name} used the {self.weapon.name} breaks through {target.armor.name} " \
                   f"and deals {damage} damage!<br>"
        else:
            return f"⛔ {self.name} used the {self.weapon.name}, but the {target.armor.name} blocked it!<br>"
