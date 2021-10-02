"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Intuition: use a sliding window by 2 indices, i and j. If current char is in the dictionary, we let i jump to 1 index next to its last occurence.  
Time: N
Space: N
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        #mp stores the char itself as key and (current index+1) for each character's value 
        mp = {}
        i = 0 
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j], i])
            
            ans = max(ans, j-i+1)
            mp[s[j]] = j+1

        return ans



"""
Solution 2
"""

def lengthOfLongestSubstring(self, s: str) -> int:
    longest, start, dicts= 0, -1, {}
    for i, value in enumerate(s):
        if value in dicts and dicts[value] > start:
            start = dicts[value]
        elif i-start > longest:
            longest = i - start
        dicts[value] = i
        
    return longest