class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        right = 0
        mpp = {}
        res = 0
        for right in range(n):
            if s[right] not in mpp:
                mpp[s[right]] = 0
            mpp[s[right]] += 1
            window_size = right-left+1
            while window_size - max(mpp.values()) > k:
                mpp[s[left]] -= 1
                left += 1
                window_size = right-left+1
            res = max(res,window_size)
            
        return res

        
            
            
                
