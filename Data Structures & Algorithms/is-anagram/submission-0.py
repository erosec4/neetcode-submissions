class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ### CHECK FOR EQUAL LENGTHS FIRST. DISQUALIFY IF NOT ###
        if len(s) != len(t):
            return False

        charDict = {}
        for char in s:
            if char in charDict:
                charDict[char] += 1
            else:
                charDict[char] = 1
        
        for char in t:
            if char not in charDict:
                return False
            else:
                if charDict[char] < 1:
                    return False
                else:
                    charDict[char] -= 1
        return True

        # Go through s, store each char : occurrences in dict
        # Go through t, check if char in dict and value >= 1
        # Then: -1 from # occurrences for that char
        # Else: False
        # True if make it through t
        