def coinChange(self, coins: List[int], amount: int) -> int:
        n1=len(coins)
        dp=[[0 for j in range (amount+1)]for i in range(n1+1)]
        for j in range(1,amount+1):
            dp[0][j]=float('inf')
        for j in range(1,amount+1):
            if(j%coins[0]==0):
                dp[1][j]=j//coins[0]
            else:
                dp[1][j]=float('inf')
        for i in range(2,n1+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
                elif coins[i-1]:
                    dp[i][j]=dp[i-1][j]
        if dp[n1][amount]==float('inf'):
            return -1
        else:
            return dp[n1][amount]
