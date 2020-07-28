# rock paper scissors
# we simulate a rock,paper,scissors game with different probability distributions
# over actions.
# the game is proven to have a nash equilibrium under mixed strategy setting (uniform over actions)
from enum import Enum
import random

class Action(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

ACTIONS = [Action.ROCK,Action.PAPER,Action.SCISSORS]

class Strategy(Enum):
    FIXED = 1
    MIXED = 2

def payoff(act1,act2):  
    if (act1,act2) == (Action.ROCK,Action.PAPER):
        return (-1,1)
    elif (act1,act2) == (Action.PAPER,Action.ROCK):
        return (1,-1)
    elif (act1,act2) == (Action.PAPER,Action.SCISSORS):
        return (-1,1)
    elif (act1,act2) == (Action.SCISSORS,Action.PAPER):
        return (1,-1)
    elif (act1,act2) == (Action.SCISSORS,Action.ROCK):
        return (-1,1)
    elif (act1,act2) == (Action.ROCK,Action.SCISSORS):
        return (1,-1)
    else :
        return (0,0)
def payoff2(turnout):  
    if turnout == (Action.ROCK,Action.PAPER):
        return (-1,1)
    elif turnout == (Action.PAPER,Action.ROCK):
        return (1,-1)
    elif turnout == (Action.PAPER,Action.SCISSORS):
        return (-1,1)
    elif turnout == (Action.SCISSORS,Action.PAPER):
        return (1,-1)
    elif turnout == (Action.SCISSORS,Action.ROCK):
        return (-1,1)
    elif turnout == (Action.ROCK,Action.SCISSORS):
        return (1,-1)
    else :
        return (0,0)


class Player:
    def __init__(self,strategy,start):
        self.actions = []
        self.payoff = 0
        self.start = start
        self.strategy = strategy
    
    def tally(self):
        return self.payoff

    def turn(self):
        if self.strategy == Strategy.FIXED :
            return self.start
        else :
            return random.sample(ACTIONS,1)[0]
  
    def add_action(self,action):
       self.actions.append(action)
    def add_payoff(self,payoff):
        self.payoff += payoff
    
    
def play(player1,player2):
        p1 = player1.turn()
        p2 = player2.turn()
        print((p1,p2))
    
        player1.add_action(p1)
        player2.add_action(p2)
    
        p1Score,p2Score = payoff2((p1,p2))
    
        player1.add_payoff(p1Score)
        player2.add_payoff(p2Score)

           
if __name__ == '__main__':
    

    runs = 10 
    # python sample returns a list
    fixedAction = random.sample(ACTIONS,1)[0]
    fixedPlayer = Player(Strategy.FIXED,fixedAction)
    mixedPlayer = Player(Strategy.MIXED,Action.ROCK)


    for i in range(runs):
       play(fixedPlayer,mixedPlayer) 
    print("Fixed vs Mixed strategy players {} runs",runs)
    print("Fixed Player Tally : {}".format(fixedPlayer.tally()))
    print("Mixed Player Tally : {}".format(mixedPlayer.tally()))
    
