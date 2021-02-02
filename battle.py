import player
import monster
import weapon


class Battle:
    """represents a battle between a player and an amount of monsters"""

    def __init__(self, pc: player.Player, monsters: list, gold: int):
        """initializes a battle with a player, a list of monsters, and an amount of gold to win after the battle"""
        self._pc = pc  # the player participating in the battle
        self._monsters = monsters  # the monsters participating in the battle
        self._gold = gold  # the amount of gold you get for winning the battle

    def battle_loop(self):
        """loops through the main phase of the battle"""
        print('Heath: ' + str(self._pc.get_cur_health()) + '/' + str(self._pc.get_max_health()))
        print('Mana: ' + str(self._pc.get_cur_mana()) + '/' + str(self._pc.get_mana()))
        for m in self._monsters:
            print(m.get_name() + ': ' + str(m.get_cur_health()) + '/' + str(m.get_max_health()))
        while pc.get_cur_health() != 0 and mon_list != []:
            i = ''
            while i != '1' and i != '2' and i != '3':
                print('What would you like to do?')
                print('1. Attack with your weapon')
                print('2. Use a spell')
                print('3. Use an item')
                i = input()
                if i != '1' and i != '2' and i != '3':
                    print('Sorry that is not an accepted input')
            # attacking monster
            if i == '1':
                i = '0'
                while int(i) > len(self._monsters) or int(i) < 1:
                    print('What monster do you want to attack?')
                    for m in range(0, len(self._monsters)):
                        print(str(m + 1) + '. ' + self._monsters[m].get_name())
                    i = input()
                    if not i.isdigit():
                        print('Sorry that is not an accepted input')
                        i = '0'
                    else:
                        if int(i) > len(self._monsters) or int(i) < 1:
                            print('Sorry that is not an accepted input')
                            i = '0'
                # determines what monster you are attacking
                mon_to_attack = int(i) - 1
                print(mon_to_attack)
                print(self._monsters[mon_to_attack])
                # first we have to compare the speeds
                pc_speed = self._pc.get_weapon().get_speed()
                # this makes sure you haven't already attacked the monster
                attacked = False
                for m in self._monsters:
                    # if the pc speed is less than the monsters speed and they haven't attacked
                    if pc_speed >= m.get_speed() and not attacked:
                        # damages the monster then checks to see if its dead
                        dam = self._pc.attack()
                        mon_dead = self._monsters[mon_to_attack].take_damage(dam)
                        print('You have attacked ' + self._monsters[mon_to_attack].get_name() +
                              ' for ' + str(dam) + ' damage')
                        # if the monster is dead
                        if not mon_dead:
                            print(self._monsters[mon_to_attack].get_name() + ' has died')
                            self._monsters.remove(self._monsters[mon_to_attack])
                        attacked = True
                    # if statement, because the monster may have died in the last attack
                    if m in self._monsters:
                        mon_dam = m.attack()
                        dead = self._pc.take_damage(mon_dam)
                        print(m.get_name() + ' attacked you for ' + str(mon_dam) + ' damage')
                        # if you have died
                        if not dead:
                            print('Game over, you have died, exiting the game now')
                            return False
                print('Heath: ' + str(self._pc.get_cur_health()) + '/' + str(self._pc.get_max_health()))
                print('Mana: ' + str(self._pc.get_cur_mana()) + '/' + str(self._pc.get_mana()))
                for m in self._monsters:
                    print(m.get_name() + ': ' + str(m.get_cur_health()) + '/' + str(m.get_max_health()))
            # using magic
            elif i == '2':
                print('this does not do anything yet, check back when it is updated')
            # using an item
            elif i == '3':
                print('this does not do anything yet, check back when it is updated')
        print('you have defeated the forces of evil, exiting the game now')
        return True


if __name__ == '__main__':
    wep = weapon.Weapon('Sword', 5, 10, 10, 5)
    pc = player.Player('Test', 50, 2, 2, 50, 3, 100)
    pc.set_weapon(wep)
    mon1 = monster.Monster('Slime01', 20, 3, 5, 2, 10)
    mon2 = monster.Monster('Slime02', 10, 5, 8, 1, 5)
    mon3 = monster.Monster('Slime03', 20, 3, 5, 3, 3)
    mon_list = [mon1, mon2, mon3]
    battle = Battle(pc, mon_list, 500)
    battle.battle_loop()
