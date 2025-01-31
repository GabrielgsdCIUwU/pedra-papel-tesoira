import random
from enum import IntEnum


class GameAction(IntEnum):

    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class GameResult(IntEnum):
    VICTORY = 0
    DEFEAT = 1
    TIE = 2


Victories = {
    GameAction.ROCK: GameAction.PAPER,
    GameAction.PAPER: GameAction.SCISSORS,
    GameAction.SCISSORS: GameAction.ROCK
}
class Game():

    def __init__(self):
        self.last_game_result = -1
        self.computer_what_action_choose = 0

    def assess_game(self, user_action, computer_action):

        if user_action == computer_action:
            return GameResult.TIE
        elif computer_action == Victories[user_action]:
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


    def get_user_action(self):
        game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
        game_choices_str = ", ".join(game_choices)
        user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
        user_action = GameAction(user_selection)

        return user_action


    def is_user_want_play(self):
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'y'


    def play(self):

        while True:
            user_action = self.get_user_action()

            computer_action = self.get_computer_action()
            self.last_game_result = self.assess_game(user_action, computer_action)

            if not self.is_user_want_play():
                break


if __name__ == "__main__":
    Game().play()
