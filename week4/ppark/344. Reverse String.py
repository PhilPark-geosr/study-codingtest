class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        l = 0
        r = n-1
        while l < r:
           left = s[l]
           right = s[r]
           s[l], s[r] = right, left 
           l +=1
           r -=1
    
        """
        Do not return anything, modify s in-place instead.
        """