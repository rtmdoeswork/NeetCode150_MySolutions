class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = [0] * 26
        window_count = [0] * 26

        for char in s1:
            count_s1[ord(char) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            char_right = s2[r]
            window_count[ord(char_right) - ord('a')] += 1

            if (r - l + 1) > len(s1):
                char_left = s2[l]
                window_count[ord(char_left) - ord('a')] -= 1
                l += 1

            if count_s1 == window_count:
                return True

        return False