from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        sets = [(string, ''.join(sorted(string))) for string in strs]
        # {set(a,b,c): ['abc']}
        char_set_map = defaultdict(list)
        for (string, char_set) in sets:
            char_set_map[char_set] = [*char_set_map[char_set], string]
            
        print(char_set_map)
        print(char_set_map.values())
        return char_set_map.values()
    
s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])