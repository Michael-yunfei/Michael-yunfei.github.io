# Learn Python
# Elements of Programming

import random as rd


rd.seed(555)
stake = 50  # 本金
goal = 100  # 目标
trials = 200  # 人数
bets = 0  # 赌博次数
wins = 0  # 赢的人数

for i in range(trials):
    cash = stake
    while cash > 0 and cash < goal:
        bets = bets + 1
        if rd.random() < 0.45:
            cash = cash + 1
        else:
            cash = cash - 1
    if cash == goal:
        wins = wins + 1

casino_loss = wins * 50
casino_win = (trials-wins) * 50
casino_netprofit = casino_win - casino_loss

print("二百人中有{}人50元去100元回来".format(wins) + "赌场亏了{}元".format(casino_loss))
print("二百人中有{}人50元去0元回来".format(trials-wins) + "赌场赢了{}元".format(casino_win))
print("平均每个人赌博次数为{}".format(bets/trials))
print("赌场净利润{}".format(casino_netprofit))
