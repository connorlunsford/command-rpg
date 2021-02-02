class Weapon:
    """A weapon class to be equipped by the player"""

    def __init__(self,name: str,dam_low: int,dam_high: int,speed: int,crit: int):
        """creates a weapon class with the values given to it"""
        self._name = name           # the name of the weapon
        self._dam_low = dam_low     # the lowest possible base damage the weapon could do
        self._dam_high = dam_high   # the highest possible base damage the weapon could do
        self._speed = speed         # how fast the weapon is
        self._crit = crit          # the % chance the weapon will hit a critical

    def __str__(self):
        """prints out the weapon in a readable manner"""
        s = ''
        s+= 'Name: ' + self._name + '\n'
        s+= 'Damage Range: ' + str(self._dam_low) + ' - ' + str(self._dam_high) + '\n'
        s+= 'Speed: ' + str(self._speed) + '\n'
        s+= 'Critical Chance: ' + str(self._crit) + '\n'

    def get_name(self):
        """returns the name of the weapon"""
        return self._name

    def get_low(self):
        """returns the lower bound of the weapon damage"""
        return self._dam_low

    def get_high(self):
        """returns the upper bound of the weapon damage"""
        return self._dam_high

    def get_speed(self):
        """returns the weapons speed"""
        return self._speed

    def get_crit(self):
        """returns the weapons crit chance"""
        return self._crit