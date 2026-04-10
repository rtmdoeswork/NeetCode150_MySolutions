class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        holder = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in holder:
                holder[key] = []
            holder[key].append(word)
        return list(holder.values())