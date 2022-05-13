class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_k = 1
        right_k = max(piles) # 最大就是堆中最大
        while left_k < right_k:
            mid_k = int(left_k + (right_k-left_k)/2)
            if self.costTime(piles, mid_k) <= h: # 要最小,所以取左边的
                right_k = mid_k
            elif self.costTime(piles, mid_k) > h:
                left_k = mid_k + 1
        return left_k

    def costTime(self, piles, k):
        sum = 0
        for n in piles:
            if k >= n:
                sum += 1
            else:
                sum += math.ceil(n/k*1.0)
        return sum

