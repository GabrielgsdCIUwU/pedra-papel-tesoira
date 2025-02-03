import random
from enum import IntEnum
import survey

class GameAction(IntEnum):

    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    LIZARD = 3
    SPOCK = 4

    def get_game_choices():
        return [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    
    def exclude_game_action(*actions_to_exclude):
        return [action for action in GameAction if action not in actions_to_exclude]


class GameResult(IntEnum):
    VICTORY = 0
    DEFEAT = 1
    TIE = 2


class Game():

    def __init__(self):
        self.last_game_result = -1
        self.computer_what_action_choose = 0
        self.victory = {
            GameAction.ROCK: GameAction.exclude_game_action(GameAction.SCISSORS, GameAction.LIZARD),
            GameAction.PAPER: GameAction.exclude_game_action(GameAction.SPOCK, GameAction.ROCK),
            GameAction.SCISSORS: GameAction.exclude_game_action(GameAction.PAPER, GameAction.LIZARD),
            GameAction.LIZARD: GameAction.exclude_game_action(GameAction.SPOCK, GameAction.PAPER),
            GameAction.SPOCK: GameAction.exclude_game_action(GameAction.SCISSORS, GameAction.ROCK)
        }

    def assess_game(self, user_action, computer_action):

        if user_action == computer_action:
            return GameResult.TIE
        elif computer_action in self.victory[user_action]:
            return GameResult.DEFEAT
        else:
            return GameResult.VICTORY



    def get_computer_action(self):

        len_action = len(GameAction)
        options = [option for option in range(len_action)]

        victory = GameResult.VICTORY
        defeat = GameResult.DEFEAT
        if self.last_game_result == victory:
            self.computer_what_action_choose -= 1
        elif self.last_game_result == defeat:
            self.computer_what_action_choose += 1
        else:
            self.computer_what_action_choose = random.choice(options)

        try:
            computer_selection = options[self.computer_what_action_choose % len_action]
        except IndexError:
            computer_selection = GameAction(random.choice(options))

        computer_action = GameAction(computer_selection)

        return computer_action


    def get_color_game_result(self, game_result):
        if game_result == GameResult.VICTORY:
            return survey.colors.basic('green')
        elif game_result == GameResult.DEFEAT:
            return survey.colors.basic('red')
        elif game_result == GameResult.TIE:
            return survey.colors.basic('yellow')

    def play(self):

        while True:

            user_action = survey.routines.select('Selecciona con que quieres jugar: ', options=GameAction.get_game_choices())
           
            computer_action = self.get_computer_action()
            self.last_game_result = self.assess_game(user_action, computer_action)
            
            print(f"Tu elección: {GameAction(user_action).name}")
            print(f"La elección de la computadora: {computer_action.name}")
            survey.printers.text(f'Resultado: {self.get_color_game_result(self.last_game_result)} {self.last_game_result.name} {survey.colors.style('reset')}')
        
            user_want_to_play = survey.routines.inquire('Quieres seguir jugando? ')
            if not user_want_to_play:
                break

if __name__ == "__main__":
    Game().play()
