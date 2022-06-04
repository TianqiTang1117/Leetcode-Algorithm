class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        #f[i]表示第i个前的最长子序列长度
        #count[i]表示第i个前最大的个数
        n=len(nums)
        max_len=1
        ans=0
        f=list([1])*n
        count=list([1])*n
        f[0]=1
        count[0]=1
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if f[j] + 1 > f[i]: 
                        f[i] = f[j] + 1
                        count[i] = count[j]
                    elif f[j] + 1 == f[i] :
                        count[i] += count[j]  
            if f[i]>max_len:
                max_len=f[i]
        for i in range(n):
            if f[i]==max_len:
                ans+=count[i]
        return ans

