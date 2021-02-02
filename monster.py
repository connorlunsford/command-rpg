import random

class Monster:
    """Defines a mosnter class"""

    def __init__(self,name: str, health: int,dam_low: int,dam_high: int,defense: int,speed: int):
        """initializes a monster class with the given variables"""
        self._name = name            # the monsters name
        self._health = health       # the monsters max health
        self._cur_health = health   # the monsters current health
        self._dam_low = dam_low     # the monsters lower bound for damage
        self._dam_high = dam_high   # the monster upper bound for damage
        self._defense = defense     # the monsters defense stat
        self._speed = speed         # the monsters speed stat

    def __str__(self):
        """prints the monster in a readable way"""
        s = ''
        s += 'Name: ' + self._name + '\n'
        s += 'Max Health: ' + str(self._health) + '\n'
        s += 'Current Health: ' + str(self._cur_health) + '\n'
        s += 'Damage: ' + str(self._dam_low) + ' - ' + str(self._dam_high) + '\n'
        s += 'Defense: ' + str(self._defense) + '\n'
        s += 'Speed: ' + str(self._speed) + '\n'
        return s

    def get_name(self):
        """returns the monsters name"""
        return self._name

    def get_max_health(self):
        """returns the monsters max health"""
        return self._health

    def get_cur_health(self):
        """returns the monsters current health"""
        return self._cur_health

    def change_health(self,amt:int):
        """takes an amount of health to change, then adds that amount to the health, if the cur_health becomes less
         than 0 it returns false, otherwise it returns True"""
        self._cur_health += amt
        if self._cur_health <= 0:
            return False
        elif self._cur_health > self._health:
            self._cur_health = self._health
        return True

    def take_damage(self,amt:int):
        """takes an amount of damage, and subtracts the amount by the defense of the monster. If cur_health becomes
        less than 0 it returns false, otherwise it returns True"""
        dam = self._defense - amt
        if dam > 0:
            dam = 0
        # in theory the dam will be a negative number
        self._cur_health += dam
        if self._cur_health <= 0:
            return False
        return True

    def get_low(self):
        """returns the low range of the damage"""
        return self._dam_low

    def get_high(self):
        """returns the high range of the damage"""
        return self._dam_high

    def get_def(self):
        """returns the defense of the monster"""
        return self._defense

    def get_speed(self):
        """returns the speed of the monster"""
        return self._speed

    def attack(self):
        """uses the players might and the equipped weapon to generate an amount of damage"""
        dam = random.randint(self.get_low(),self.get_high())
        return dam