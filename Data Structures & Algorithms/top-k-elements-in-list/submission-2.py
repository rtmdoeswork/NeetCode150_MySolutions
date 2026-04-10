class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        holder = {}
        answer = []

        for v in nums:
            if v not in holder:
                holder[v] = 0
            holder[v] += 1

        sorted_items = sorted(holder.items(), key=lambda x: x[1], reverse=True)

        for n in range(k):
            answer.append(sorted_items[n][0])

        return answer