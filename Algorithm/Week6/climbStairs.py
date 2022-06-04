class Solution:
    def climbStairs(self, n: int) -> int:
        # f[i]表示第i阶的时候有多少种方法
        if n==1: return 1
        f=list([0])*(n)
        f[0]=1
        f[1]=2
        for i in range(2,n):
            f[i]=f[i-1]+f[i-2]
        return f[n-1]