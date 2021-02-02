import weapon
import random


class Player:
    """A player class with all necessary attributes to intialize a player object"""

    def __init__(self, name: str, health: int, might: int, magic: int, mana: int, defense: int, gold: int):
        """Initializes a player class with the values given to it"""
        self._name = name  # the players name
        self._health = health  # the players maximum health
        self._cur_health = health  # the players current health
        self._might = might  # the players attack power
        self._magic = magic  # the players magic attack power
        self._mana = mana  # the players maximum ability to cast spells
        self._cur_mana = mana  # the players current ability to cast spells
        self._defense = defense  # the players defense
        self._gold = gold  # the players purchasing power
        self._weapon = None  # the players current equipped weapon

    def __str__(self):
        """allows for easy printing of the player object, for testing purposes"""
        s = ''
        s += 'Name: ' + self._name + '\n'
        s += 'Max Health: ' + str(self._health) + '\n'
        s += 'Current Health: ' + str(self._cur_health) + '\n'
        s += 'Might: ' + str(self._might) + '\n'
        s += 'Magic: ' + str(self._magic) + '\n'
        s += 'Max Mana: ' + str(self._mana) + '\n'
        s += 'Current Mana: ' + str(self._mana) + '\n'
        s += 'Defense: ' + str(self._defense) + '\n'
        s += 'Gold: ' + str(self._gold) + '\n'
        s += 'Equipped Weapon: ' + self._weapon.get_name() + '\n'
        return s

    def get_name(self):
        """returns the players name"""
        return self._name

    def get_max_health(self):
        """returns the players max health"""
        return self._health

    def set_max_health(self, hp: int):
        """takes a new health value and changes the max health of the player to it"""
        self._health = hp
        return

    def get_cur_health(self):
        """returns the players current health"""
        return self._cur_health

    def change_health(self, hp: int):
        """hurts or heals the player for the given amount, returns False if health drops below 0, returns True otherwise
        """
        self._cur_health += hp
        if self._cur_health < 0:
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

    def get_might(self):
        """returns the might value for the player"""
        return self._might

    def set_might(self, new: int):
        """takes a new might value and sets the players might to that value"""
        self._might = new
        return

    def get_magic(self):
        """returns the magic value for the player"""
        return self._magic

    def set_magic(self, new: int):
        """takes a new magic value and sets the players magic to that value"""
        self._magic = new
        return

    def get_mana(self):
        """returns the max mana value for the player"""
        return self._mana

    def set_mana(self, new: int):
        """takes a new value and sets the mana for the player to that value"""
        self._mana = new
        return

    def get_cur_mana(self):
        """returns the current mana value for the player"""
        return self._cur_mana

    def change_mana(self, amt: int):
        """takes a value and changes the mana by that amount"""
        self._cur_mana += amt
        if self._cur_mana < 0:
            self._cur_mana = 0
        elif self._cur_mana > self._mana:
            self._cur_mana = self._mana
        return

    def get_def(self):
        """returns the defense value for the player"""
        return self._defense

    def set_def(self, new: int):
        """takes a new value and sets the defense value to that amount"""
        self._defense = new
        return

    def get_gold(self):
        """returns the amount of gold the player has"""
        return self._gold

    def change_gold(self, amt: int):
        """takes an amount and changes the players gold by that amount"""
        self._gold += amt
        return

    def get_weapon(self):
        """returns the current equipped weapon the player has"""
        return self._weapon

    def set_weapon(self, new: weapon.Weapon):
        """takes a new weapon and equips the player with that weapon"""
        self._weapon = new
        return

    def attack(self):
        """uses the players might and the equipped weapon to generate an amount of damage"""
        dam = random.randint(self._weapon.get_low(),self._weapon.get_high())
        dam += self._might
        return dam
