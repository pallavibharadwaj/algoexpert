# input: n=non-negative integer representing target amount
#        denoms = array of distinct positive integers representing coin denominations
# output: number of ways to make change for the target amount using given coin denominations (unlimited repetitions) 
       
def numberOfWaysToMakeChange(n, denoms):
    if not n:   # base case
        return 1    # no denoms for n=0
    ways = [0]*(n+1)
    ways[0] = 1
    
    for coin in denoms:
        if coin > n:
            break
        for i in range(coin, len(ways)):
            ways[i] += ways[i-coin]
    return ways[n]


def main():
    solution = numberOfWaysToMakeChange(n=5, denoms=[1,5,10,25])
    print(solution)


if __name__=='__main__':
    main()
