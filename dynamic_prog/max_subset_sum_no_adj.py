# input: array of positive integers  
# returns: maximum sum of non-adjacent elements when len(array)>0
# returns: 0 when len(array)=0

def maxSubsetSumNoAdjacent(array):
    n = len(array)
    maxSum = [0] * n
    if n==0:
        return 0
    elif n<=2:
        return max(array)
    else:
        maxSum[0]  = array[0]
        maxSum[1] = max(array[0], array[1])
        for i in range(2,n):
            maxSum[i] = max(maxSum[i-1], array[i]+maxSum[i-2])

    return maxSum[n-1]


def main():
    solution = maxSubsetSumNoAdjacent([4, 3, 5, 200, 5, 3])
    print(solution)


if __name__=='__main__':
    main()


