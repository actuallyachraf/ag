# Automated Market Makers

Automated Market Makers are programmed, algorithmic agents responsible for maintaining open interest
and liquidity in markets.

Whether it's a prediction market or exchange an automated market maker's role is to provide and sustain
liqudity for different actors, with different strategies.

## Constant Product Market Maker

The Constant Product Market Maker or more generally Constant Function Market Maker is an algorithmic
market making model based on a constant scoring rule.

Given two tokens X and Y with respective reserves Rx and Ry the market maker quotes all trades such
as (Rx - Dx) * (Ry - Dy) = k , where Dx and Dy represent the amounts of a given trade.

Let Rx = 500 and Ry = 700 and k = 250 suppose a trader would like to exchange 102 X's 

We have (500 - 102) * (700 - Dy) = 250 <=> 398 * 700 - 398 * Dy = 250 <=> Dy = ((398 * 700) - 250) / 398

The trader receives in exchange of 102 X's 699 Y's setting a price of 0.14 X/Y .

The new liquidity reserves become Rx = 500 + 102 and Ry = 700 - 699.

When another trader comes to exchange and wants to swap 200 Y's in exchange of Dx the same formula repeates

(602 - Dx) * (1 - 200) = 250 <=> 602 * - 199 + 199 * Dx = 250 <=> Dx = (250 - (602 * -199)) / 199 <=> Dx = 602

Setting the new liquidity reserves at Rx = 602 - 602 and Ry = 1 + 200 

Constant Function Market Makers have demonstrated great resilience in [Uniswap](https://uniswap.org) especially since
most price differences are exploited by arbitrageurs who implicitly keep the price up to date with other markets.

You can read more about **CFMM** [here](https://arxiv.org/pdf/2003.10001.pdf).

