class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Could sort and compare, OR

        ### Use array of len 26 (a-z, continuous) instead of hash ###
        # Use array to make a key (w/ ord(), vals are cont.) from str
        # Add to hash map with key:anagrams that match
        # Make a key and add to dict for each str
        # Return anagrams at each key as sublists

        groups = defaultdict(list) # Default list value for missing keys (handles "key error" / looking up a key not in the dict yet)

        for s in strs:
            key = [0] * 26 
            # hash map key:anagrams for each unique key
            for char in s:
                # go through characters in the string to make key
                key[ord(char) - ord("a")] += 1 # ASCII ord(a) = 97, ord(b) = 98, ...

            '''if key in groups:
                groups[key].append(s)
            else:
                groups[key] = s'''
            # ERROR: array can't be a dict key --> make it a tuple (immutable)
            groups[tuple(key)].append(s)
        
        return list(groups.values()) # Return values AS A LIST



        