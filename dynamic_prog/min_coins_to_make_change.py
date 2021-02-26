# input: n=non-negative integer representing target amount
#        denoms = array of distinct positive integers representing coin denominations
# output: minimum number of coins to make change for the target amount using given coin denominations (unlimited repetitions) 
       
def minNumberOfCoinsForChange(n, denoms):
    minCoins = [float("inf")]*(n+1)
    minCoins[0] = 0
    for coin in denoms:
        if coin > n:
            continue
        for target in range(coin, n+1):
            newCount = minCoins[target - coin] + 1
            if newCount < minCoins[target]:
                minCoins[target] = newCount
    
    if(minCoins[n] == float("inf")):
        return -1
    else:
        return minCoins[n]


def main():
    solution = minNumberOfCoinsForChange(n=5, denoms=[1,5,10,25])
    print(solution)


if __name__=='__main__':
    main()
