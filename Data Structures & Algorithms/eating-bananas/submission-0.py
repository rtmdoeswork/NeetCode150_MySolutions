class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        holder = 0 
        n = 0

        while l <= r:
            m = (r + l) // 2

            while n < len(piles):
                holder += math.ceil(piles[n] / m)
                n += 1
            n = 0

            if holder > h:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1
            
            holder = 0
        return res