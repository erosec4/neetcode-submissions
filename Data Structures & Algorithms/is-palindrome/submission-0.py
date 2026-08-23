class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Pointer from end and pointer from start
        i = 0
        j = len(s) - 1
        s = s.lower()
        alpha = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        while i < j:
            if s[i] in alpha and s[j] in alpha:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            else:
                if s[i] not in alpha:
                    i += 1
                if s[j] not in alpha:
                    j -= 1
            
        return True
        