import pytest
from src.RPS_dict import GameResult, GameAction, Game

@pytest.mark.draw
def test_draw():
    '''
    Partidas con empate
    '''

    assert GameResult.TIE == Game().assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.ROCK)

    assert GameResult.TIE == Game().assess_game(
        user_action=GameAction.SCISSORS, 
        computer_action=GameAction.SCISSORS)

    assert GameResult.TIE == Game().assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.PAPER)

@pytest.mark.rock
def test_ROCK_loses():
    '''
    ROCK pierde con PAPER 
    '''
    assert GameResult.VICTORY == Game().assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.ROCK)

@pytest.mark.rock
def test_ROCK_wins():
    '''
    ROCK gana a SCISSORS
    '''
    assert GameResult.DEFEAT == Game().assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.ROCK)

@pytest.mark.paper
def test_PAPER_loses():
    '''
    PAPER pierde con SCISSORS
    '''
    assert GameResult.VICTORY == Game().assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.PAPER)

@pytest.mark.paper
def test_PAPER_wins():
    '''
    PAPER gana a ROCK
    '''
    assert GameResult.DEFEAT == Game().assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.PAPER)

@pytest.mark.scissors
def test_SCISSORS_loses():
    '''
    SCISSORS pierde con ROCK 
    '''
    assert GameResult.VICTORY == Game().assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SCISSORS)

@pytest.mark.scissors
def test_SCISSORS_wins():
    '''
    SCISSORS gana a PAPER 
    '''
    assert GameResult.DEFEAT == Game().assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SCISSORS)
