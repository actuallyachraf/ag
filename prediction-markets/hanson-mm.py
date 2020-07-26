# Hanson's Market Maker
# Author : @actuallyachraf
# Version : 1
# We take two outcomes and simulate a market maker
# with different traders interacting.
# Combobet : http://mason.gmu.edu/~rhanson/combobet.pdf
# Market Scoring Rule : http://mason.gmu.edu/~rhanson/mktscore.pdf
import math


OUTCOME1 = "Trump"
OUTCOME2 = "BIDEN"

MARKET = "WHO WINS THE 2020 ELECTIONS"

# The market maker tracks count of how many shares are outstanding on each side
# Q1 : Total outstanding shares for Outcome 1
# Q2 : Total outstanding shares for Outcome 2

class MarketMaker:
    
    def __init__(self,q1,q2,maxLoss):
        self.Q1 = q1 
        self.Q2 = q2
        self.MAX_LOSS = 100.0



    # cost_function tracks how much money traders have spent purchasing
    # both outcome shares, the market maker choose *b* a parameter
    # that represents max loss value it also represents liquidity in a sense
    def cost_function(self,q1,q2):
        b = self.MAX_LOSS

        return b*math.log(math.exp(q1/b) + math.exp(q2/b))
            
    # quote function basically answers the question how much do I pay 
    # for a quantity of outcome shares.
    # the formula is C(q1*,q2*) - C(q1,q2) at each trader's turn
    # where q* = q1 +/- quantity (+ for buying - for selling)
    # the idea is to quote a price such as the liquity remains in close equilibria
    # with the max loss.
    # the amount can be negative as selling implies receiving quote currency for shares
    # (traders arrive one at a time) 
    def quote_function(self,side,outcome,quantity):
        if side == "BUY" :
            if outcome == OUTCOME1 :
                return self.cost_function(self.Q1 + quantity,self.Q2) - self.cost_function(self.Q1,self.Q2)
            elif outcome == OUTCOME2 :
                return self.cost_function(self.Q1,self.Q2 + quantity) - self.cost_function(self.Q1,self.Q2)
        elif side == "SELL":
            if outcome == OUTCOME1 :
                return self.cost_function(self.Q1-quantity,self.Q2) - self.cost_function(self.Q1,self.Q2)
            elif outcome == OUTCOME2 :
                return self.cost_function(self.Q1,self.Q2-quantity) - self.cost_function(self.Q1,self.Q2)

    # market maker can quote a current price that is entirely dependant on both sides
    # liquidity this only works for infinitesemal quoatity of shares
    def current_price(self,outcome):
        b = self.MAX_LOSS
        if outcome == OUTCOME1:
            return math.exp(self.Q1/b) / (math.exp(self.Q1/b) + math.exp(self.Q2/b))
        elif outcome == OUTCOME2:
            return math.exp(self.Q2/b) / (math.exp(self.Q2/b) + math.exp(self.Q2/b))

def main():
    mm = MarketMaker(0,0,100)
    # firt trade quote price 
    # trader 1 comes wants to buy 10 shares of outcome 1
    trade1 = 10
    quotePrice1 = mm.quote_function("BUY",OUTCOME1,trade1)
    print(' Trader 1 wants to buy 10 shares of outcome 1 he pays {:.3} $'.format(quotePrice1)) 
    Q1 = 50
    Q2 = 10
    mm = MarketMaker(50,10,100)
    # trader 1 comes back to sell his shares 
    # MM now has sold 50 shares of outcome 1 and 10 of outcome 2
    trade2 = 10
    quotePrice2 = mm.quote_function("SELL",OUTCOME1,trade2)
    print(' Trader 2 wants to sell his 10 shares of outcome 2 he gets paid {:.3}$'.format(-quotePrice2))

    mm = MarketMaker(70,30,100)
    currentPrice1 = mm.current_price(OUTCOME1)
    currentPrice2 = mm.current_price(OUTCOME2)
    print(' Current Price for Outcome 1 : {:.3}/SHARE'.format(currentPrice1))
    print(' Current Price for Outcome 2 : {:.3}/SHARE'.format(currentPrice2))
    
    trade3 = 50
    mm = MarketMaker(50,10,100)
    quotePrice3 = mm.quote_function("BUY",OUTCOME1,trade3)
    print(' Price to buy 50 shares of outcome 1 {:.3}$'.format(quotePrice3))

if __name__ == '__main__':
    main()
