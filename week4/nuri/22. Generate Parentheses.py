class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pattern = [')'] * (2*n)
        ret = []
        def helper(n, i, prev):
            if i == n:
                ret.append(''.join(pattern))
                return 
            for j in range(i, i*2+1):
                if j > prev:
                    pattern[j] = '('
                    helper(n, i+1, j)
                    pattern[j] = ')'
        helper(n, 0, -1)
        return ret