import random
from enum import IntEnum


class GameAction(IntEnum):

    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def get_game_choices():
        return [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]


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


    def get_user_action(self, user_option_selected):
        
        if user_option_selected in [option.value for option in GameAction]:
            return GameAction(user_option_selected)
        else: 
            return None


    def is_user_want_play(self):
        user_input = input("Quieres seguir jugando? (y/n): ")
        if self.is_input_valid("yon", user_input):
            return user_input.lower() in ['y', 's']
        else:
            print("Invalid input. Valid options: y/n.")
            return self.is_user_want_play()

            
    
    def is_input_valid(self, type_choice, input_user):
        input_user = input_user.lower()
        if type_choice == "yon":
            if input_user not in ['y', 'n', 's']:
                return False
            else:
                return True
            
        elif type_choice == "number":
            try:
                int(input_user)
                return True
            except ValueError:
                return False
    
    def manage_get_user_action(self):
        user_input = input()
        if self.is_input_valid("number", user_input):
                
            return self.get_user_action(int(user_input))
        else:
            print("Invalid input. Need to be a number.")
            return self.manage_get_user_action()
                


    def play(self):

        while True:
            print(f"\n Pick a choice ${", ".join(GameAction.get_game_choices())}")


            user_action = self.manage_get_user_action()
            if user_action in GameAction:
                computer_action = self.get_computer_action()
                self.last_game_result = self.assess_game(user_action, computer_action)
                print(f"Tu elección: {user_action.name}")
                print(f"La elección de la computadora: {computer_action.name}")
                print(f"Resultado: {GameResult(self.last_game_result).name}")
            else:
                print(f"Invalid input. You have to choose {", ".join(GameAction.get_game_choices())} .")
                continue

            if not self.is_user_want_play():
                break
               
            else:
                print("Invalid input. Need to be a number.")
                continue

if __name__ == "__main__":
    Game().play()
