from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        def dfs(blanket, path, cnt, sum_value):
            # print(f'dfs{blanket, path, cnt, sum_value}')
            if len(path) == 2*n:
                result.append(path)

            else:
                if sum_value == 0:
                    if cnt >0:
                        dfs("(", path+"(", cnt-1, sum_value +1)

                elif sum_value > 0:
                    if cnt>0:
                        dfs("(", path+"(", cnt-1, sum_value +1)
                        dfs(")", path+")", cnt, sum_value -1)
                    else:
                        dfs(")", path+")", cnt, sum_value -1)
                else:
                    return
                
        dfs("(", "(", n-1, 1)
        # print(result)
        return result