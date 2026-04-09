class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_words = {}
        t_words = {}

        s = s
        t = t

        return sorted(s) == sorted(t)