def getWays(n, c):
    # Write your code here
    l =[0]*(n+1)
    l[0] = 1
    for coin in c:
        for amount in range(1, len(l)):
            if coin <= amount:
                l[amount] += l[amount-coin]
    return l[n]


print(getWays(12, [1,2,5]))