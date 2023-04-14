from classes.baseunit import BaseUnit


class BaseSingleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player: BaseUnit
    enemy: BaseUnit
    game_is_running = False

    def start_game(self, player: BaseUnit, enemy: BaseUnit):
        """
        Starts the game
        """
        self.game_is_running = True
        self.player = player
        self.enemy = enemy

    def stop_game(self) -> str:
        """
        Stop the battle
        Returns:
            text stating that the battle is over
        """
        return self._end_game()

    def _check_players_hp(self) -> str | None:
        """
        Heroes health check
        Returns:
            result of the battle or None
        """
        match (self.player.health_points > 0, self.enemy.health_points > 0):
            case (False, False):
                return 'Nobody left alive!<br>'
            case (True, False):
                return f'{self.player.name} won the battle!<br>'
            case (False, True):
                return f'{self.player.name} lost the battle!<br>'
            case _:
                return None

    def _stamina_regeneration(self) -> None:
        """
        Recoverinvg of stamina for both players
        """
        for hero in (self.player, self.enemy):
            calc_stamina_to_add = round(self.STAMINA_PER_ROUND * hero.unit_class.stamina, 1)
            if hero.stamina + calc_stamina_to_add <= hero.unit_class.max_stamina:
                hero.stamina = round(hero.stamina + calc_stamina_to_add, 1)
            else:
                hero.stamina = hero.unit_class.max_stamina

    def next_turn(self) -> str:
        """
        Enemy hit action
        Checking the health points of both players
        Start the recoverinvg of stamina for both players (if both are alive)

        Returns:
            result of actions and/or "the game is over"
        """
        result = self.enemy.hit(self.player)
        if (battle_result := self._check_players_hp()) is not None:
            return result + battle_result + self._end_game()
        self._stamina_regeneration()
        return result

    def player_hit(self) -> str:
        """
        Player hit action.
        Check if the game is running, the player makes a hit and the move is passed to the enemy

        Returns:
            result of actions or "the game is already over"
        """
        if not self.game_is_running:
            return 'The battle is already over!'

        result = self.player.hit(self.enemy)
        result += self.next_turn()
        return result

    def player_use_skill(self) -> str:
        """
        Player action using a skill

        Returns:
            result of actions or "the game is already over"
        """
        if not self.game_is_running:
            return 'The battle is already over!'

        result = self.player.use_skill(self.enemy)
        result += self.next_turn()
        return result

    def _end_game(self) -> str:
        """
        Clear Arena instance and stop the battle

        Returns:
            result of actions or "the game is already over"
        """
        if not self.game_is_running:
            return 'The battle is already over!'

        self._instances: dict = {}
        self.game_is_running = False
        return 'The battle is over!'
