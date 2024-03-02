class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt  = 0
        words = s.rstrip()
        
        for i in range(len(words)-1, -1, -1):
            if words[i] != ' ':
                cnt += 1
            else:
                return cnt
        
        return cnt
