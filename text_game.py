from random import randint

# constants
MIN_PLAYER_DAMAGE = 10
MAX_PLAYER_DAMAGE = 40
MIN_HEALTH_REGEN = 5
MAX_HEALTH_REGEN = 20
AMOUNT_OF_HEAL_POTIONS = 10


class Game:
    def __init__(self, player_list):
        """
        Class for game logic

        :param player_list: it's the list of Warrior type objects
        :type player_list: list
        """
        self.player_list = player_list
        print('Game started')

    def is_finished(self):
        """
        Checking if game is finished

        Game is over only if one player remained, we check if only one player in player_list(if player killed he got
        deleted from game.player_list).
        If only one player - we print name of last player in player_list and exit from code.
        """
        if len(self.player_list) == 1:
            print(f'Game finished, {self.player_list[0].name} won')
            exit()

    def show_alive_players(self):
        """
        Printing formatted list of players.

        We iterate through enumerate(player_list),create list with f-strings, (number + 1) is index + 1
        of player in player_list, player.name is the name of player with this index, player.health is the hp of
        player with this index.
        result is the list like this ['1. Kosmarik, health: 100','2. shade, health: 77']
        then we join list with newline character and print it.
        """
        print('\n'.join(
            [f'{number + 1}. {player.name}, health:{player.health}' for number, player in enumerate(self.player_list)]))

    def is_dead(self, player):
        """
        Checking if player is dead.

        We check if player.health <= 0.If yes, we delete player from game.player_list, and print '{player.name} is dead'.

        :param player: player is the Warrior class object,which health we are checking.
        :type player: Warrior
        """
        if player.health <= 0:
            self.player_list.remove(player)
            print(f'{player.name} is dead')

    def what_to_do(self, player):
        """
        Deciding what player want to do.

        We ask player what he want to do.
        If them want to attack - we check for valid target and use Warrior method attack.
        If them want to heal - we use Warrior method heal.
        If user doesn't print valid input - we print not valid operation.

        :param player: player is Warrior type object, which do action(heal,attack etc.)
        :type player: Warrior
        """
        operation = input(f'{player.name}, what do you want to do?Heal or attack: \n')
        if operation.lower() == 'attack':
            number_of_target = int(input(f'{player.name}, choose number of player you want to attack: \n'))
            if number_of_target - 1 < len(game.player_list) and number_of_target > 0:
                player.attack(game.player_list[number_of_target - 1])
            else:
                print('Please, write valid number of target.')
        elif operation.lower() == 'heal':
            player.heal()
        else:
            print('Not valid operation.')


class Warrior:
    def __init__(self, name='enemy', health=100):
        """
        Class for players

        :param health: health of player
        :type health: int
        :param name: name of player
        :type name: str
        """
        self.health = health
        self.name = name
        self.heal_potions = AMOUNT_OF_HEAL_POTIONS

    def attack(self, target):
        """
        Do damage to target

        Firstly we check if target != self
        If no, we print "we don't accept self-harming here :)"
        If yes, we randomize damage(min and max player damage are constants)
        and subtract it from target.health. Then we print f-string, in which target.name is the name of target and
        number_of_damage is how many damage we did.
        After that we use Game.is_dead method.

        :param target: Warrior type object,which player is attacking
        :type target: Warrior
        """
        if target != self:
            number_of_damage = randint(MIN_PLAYER_DAMAGE, MAX_PLAYER_DAMAGE)
            target.health -= number_of_damage
            print(f'You attacked {target.name} and did {number_of_damage} damage.')
            game.is_dead(target)
        else:
            print("We don't accept self-harming here :)")

    def heal(self):
        """
        Heal player.

        We check if amount of heal potions > 0.
        If no, we print 'You don't have heal potions'.
        If yes, we randomize amount of health we restore.Then we sum current health and amount of health we restore.
        Also we subtract 1 from heal_potions, because we use 1 potion, and we print f-string.
        """
        if self.heal_potions > 0:
            heal = randint(MIN_HEALTH_REGEN, MAX_HEALTH_REGEN)
            self.health += heal
            self.heal_potions -= 1
            print(f'You drank heal potion and restored {heal} hp.Heal potions left: {self.heal_potions}')
        else:
            print(f"You don't have heal potions left")


if __name__ == '__main__':
    player1 = Warrior(name=input('Player 1, write your nickname please: \n'))
    player2 = Warrior(name=input('Player 2, write your nickname please: \n'))
    list_of_players = [player1, player2]
    game = Game(list_of_players)

    # game cycle
    while True:
        game.show_alive_players()
        for player in game.player_list:
            game.what_to_do(player=player)
        game.is_finished()
