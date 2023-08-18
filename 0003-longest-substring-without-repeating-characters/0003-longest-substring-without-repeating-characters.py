class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_length = 0
        start_index = 0
        for i in range(len(s)):
            if s[i] in last_seen.keys():
                if i - start_index > max_length:
                    max_length = i - start_index
                for char in s[start_index : last_seen[s[i]]]:
                    last_seen.pop(char)
                start_index = last_seen[s[i]] + 1
            last_seen[s[i]] = i
            
        if len(s) - start_index > max_length:
            max_length = len(s) - start_index
        
        return max_length
