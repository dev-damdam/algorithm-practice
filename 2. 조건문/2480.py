#같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
#같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
#모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

dice1, dice2, dice3 = map(int, input().split())

reward = 0

if dice1 == dice2 and dice1 == dice3 and dice2 == dice3 :
    reward = 10000 + dice1 * 1000
else :
    if dice1 == dice2 or dice1 == dice3 :
        reward  = 1000 + dice1 * 100
    elif dice2 == dice3 :
         reward  = 1000 + dice2 * 100
    else :
        tmpLst = [dice1, dice2, dice3]
        tmpLst.sort(reverse=True)
        maxValue = tmpLst[0]
        reward = maxValue * 100

print(reward)