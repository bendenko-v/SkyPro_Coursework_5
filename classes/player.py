from classes.baseunit import BaseUnit


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        Player unit hit action

        Args:
            target: The enemy who gets hit

        Returns:
            the result of hit action
        """
        damage = self._count_damage(target)

        if damage is None:
            return f"🟡 {self.name} tried to use the {self.weapon.name}, he didn't have enough stamina.<br>"

        if damage > 0:
            return f"⚔ {self.name} used the {self.weapon.name} breaks through {target.armor.name} " \
                   f"and deals {damage} damage!<br>"
        else:
            return f"⛔ {self.name} used the {self.weapon.name}, but the {target.armor.name} blocked it!<br>"
