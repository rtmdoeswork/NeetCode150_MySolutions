class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 1
        l = 0
        store = set()

        if len(s) < 1:
            return 0
        if len(s) < 2:
            return 1

        store.add(s[0])
        max_store = 0

        while r < len(s):
            while s[r] in store:
                store.remove(s[l])
                l += 1
            store.add(s[r])
            r += 1
            max_store = max(max_store, len(store))

        return max_store