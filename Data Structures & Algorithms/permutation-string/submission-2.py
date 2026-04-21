class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        store = []
        s1 = list(s1)
        l = 0
        r = 0

        while r < len(s2):
            if len(store) == len(s1):
                store.pop(0)
                l += 1

            store.append(s2[r])

            if sorted(s1) == sorted(store):
                return True
            r += 1

        return False