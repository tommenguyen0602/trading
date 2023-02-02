import MetaTrader5 as mt5
import random 
import matplotlib.pyplot as plt
import time


#variable
INIT_BALANCE = 5000
INIT_RISK = 0.01
class sim_result:
    lifetime = 0
    profit = 0
    highest_profit = 0
    lowest_profit = 0
def one_sim_after_n_trades(INIT_BALANCE, INIT_RISK,NUMBER_OF_TRADES):
    balance = INIT_BALANCE
    bet= INIT_BALANCE * INIT_RISK
    history = []
    history.append(balance)
    while 1:
        win_or_loss = random.randint(0,1)
        if win_or_loss == 0: #LOSS
            #calculate next bet
            #check if next bet is over the risk threshold 
            #take the loss and reset bet else double the risk and reroll
            if (bet * 2 > balance/10):
                balance = balance - bet
                bet = balance * INIT_RISK
            else:
                bet = bet * 2
            NUMBER_OF_TRADES -= 1
        else: #WIN
            balance = balance + bet
            #reset bet
            bet = balance * INIT_RISK
            NUMBER_OF_TRADES -= 1
            history.append(balance)
        if NUMBER_OF_TRADES == 0:
            break
    return history
def one_sim_until_reach_n_drawdown(INIT_BALANCE, INIT_RISK,DRAWDOWN):
    return 0  
one_sim= one_sim_after_n_trades(INIT_BALANCE, INIT_RISK, 111)
multiple_sim = []
NUMBER_OF_SIM = 1111
while (NUMBER_OF_SIM!= 0):
    multiple_sim.append(one_sim_after_n_trades(INIT_BALANCE, INIT_RISK, 1111).pop())
    NUMBER_OF_SIM-=1
plt.plot(multiple_sim,'o')
plt.show()