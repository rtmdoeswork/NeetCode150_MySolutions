class Solution:

    def encode(self, strs: list[str]) -> str:
        return ''.join(f"{len(word)}#{word}" for word in strs)
            
    def decode(self, s: str) -> list[str]:
        dec_message = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i:j])
            i = j + 1
            dec_message.append(s[i:i+n])
            i += n
        return dec_message