from classes.baseskill import BaseSkill


class FuryPunch(BaseSkill):
    """
    Warrior skill
    """
    _name = 'Fury Punch'
    _stamina = 6.0
    _damage = 11.0


class BackBlow(BaseSkill):
    """
    Thief skill
    """
    _name = 'Back Blow'
    _stamina = 4.0
    _damage = 9.0


class DivinePower(BaseSkill):
    """
    Dwarf skill
    """
    _name = 'Divine Power'
    _stamina = 5.0
    _damage = 10.0
