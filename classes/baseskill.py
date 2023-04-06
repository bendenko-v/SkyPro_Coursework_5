from abc import ABC


class BaseSkill(ABC):
    """
    Base Skill Class
    """
    user = NotImplemented
    target = NotImplemented
    _name: str
    _stamina: float
    _damage: float

    @property
    def name(self) -> str:
        return self._name

    @property
    def stamina(self) -> float:
        return self._stamina

    @property
    def damage(self) -> float:
        return self._damage

    def skill_effect(self) -> str:
        """
        Skill effect calculation

        Returns:
            the result of using the skill
        """
        self.user.stamina = round(self.user.stamina_points - self.stamina, 1)

        if self.target.health_points <= self.damage:
            self.target.hp = 0
        else:
            self.target.hp = round(self.target.health_points - self.damage, 1)

        return f'🌀 {self.user.name} used the {self.name} and dealt {self.damage} damage ' \
               f'and {self.user.name} stamina decreased by {self.stamina}.<br>'

    def _is_stamina_enough(self) -> bool:
        """
        Check if hero have enough stamina

        Returns:
            True, if there is enough stamina for the action
        """
        return self.user.stamina_points >= self.stamina

    def use(self, user, target) -> str:
        """
        The hero tries to use his skill

        Args:
            user: BaseUnit, who use the skill
            target: BaseUnit, who gets hit

        Returns:
            the result of using (or not) the skill
        """
        """
        Check if hero have enough stamina
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough():
            self.user._is_skill_used = True
            return self.skill_effect()
        return f"🌀 {self.user.name} tried to use the {self.name}, but he didn't have enough stamina.<br>"
