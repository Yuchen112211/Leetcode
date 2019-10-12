def coinChange(coins, amount):
    cnt = 0
    while amount != 0:
        if coins == []:
            return -1
        max_coin = coins[-1]
        coins = coins[:-1]
        left = amount % max_coin
        if len(coins) == 0 and amount/max_coin == 0 and left != 0:
            print left
            return -1
        cnt += (amount/max_coin)
        amount = left
    return cnt


if __name__ == '__main__':
    coins = [186,419,83,408]
    print coinChange(coins,6249)