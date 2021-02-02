# command-rpg
Command RPG is a simple game made to test my skills with object-oriented design in Python

Run it in the command line using the command:
python3 battle.py

It will initialize a player, a weapon, and 3 monsters for you to do battle with
When the battle is over, if the player or monsters die, it will exit the program

Current Features:
A Battle class - allows you to create and simulate a fight with a player and monsters
  - currently all you can do is pick a monster to attack and attack
  - framework for other skills such as magic and items is implemented but the code for actually using them is not
A Player class - allows you to create a player with a name and stats
A Weapon class - allows you to create a weapon with a given damage amount that can be equipped by a player
A Monster class - allows you to create a monster that will fight a player in a given fight

Planned Features:
Battle System
  - A magic system which allows you to learn new spells and use them at the cost of mana
  - An item system which allows you to heal and harm enemies
Monsters
  - multiple monster types with different stats
  - monsters with multiple attacks
  - monsters that can use magic
  - monsters that choose the best course of action for the situation
Player
  - a character creator that allows you to set your stats
  - a system which allows you to level up your stats depending on what items you have collected
  - an inventory system allowing you to equip different weapons and items
World
  - a full story within the game
  - a game map that you can explore
  - random encounters with monsters within the game world
  - a choice system in text based encounters
  - a money system that allows you to trade with vendors
General
  - a way to save your state and return to it at a later time
  - general reformatting of the interface to be more aesthetically pleasing
