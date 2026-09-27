class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for words in strs:
            # 1. Sort the characters of the word to create a unique signature
            key = "".join(sorted(words)) 
            
            # 2. Group the original word under its sorted key
            if key in groups:
                groups[key].append(words)
            else:
                groups[key] = [words]
                
        # 3. Return a list of all the grouped anagrams
        return list(groups.values())
