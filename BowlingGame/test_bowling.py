import pytest
from bowling import BowlingGame

@pytest.fixture   
def game():
    return BowlingGame()

def roll_many(game, rolls, pins):
    for _ in range(rolls):
        game.roll(pins)

def roll_spare(game):
    game.roll(5)
    game.roll(5)

def roll_strike(game):
    game.roll(10)

#======= Actual Tests ========
def test_gutter_game(game):
    roll_many(game, 20, 0)
    assert game.score() == 0

def test_all_ones(game):
    roll_many(game, 20, 1)
    assert game.score() == 20

def test_one_spare(game):
    roll_spare(game)
    game.roll(3)
    roll_many(game, 17, 0)
    assert game.score() == 16

def test_one_strike(game):
    roll_strike(game)
    game.roll(3)
    game.roll(4)
    roll_many(game, 16, 0)
    assert game.score() == 24

def test_perfect_game(game):
    for _ in range(12):
        game.roll(10)
    assert game.score() == 300
    
def test_all_spares(game):
    for _ in range(10):
        roll_spare(game)
    game.roll(5)
    assert game.score() == 150
