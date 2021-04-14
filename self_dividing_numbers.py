class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for i in range(left, right+1):

            possible=True
            if i>=10:
                if not '0' in str(i):
                    for c in str(i):
                        if i%int(c)!=0:
                            possible=False
                            break
                elif '0' in str(i):
                    possible=False
            if possible:
                ans.append(i)

        return ans
    # one liner
    def selfDividingNumbers2(self, left: int, right: int) -> List[int]:
        
        return [i for i in range(left, right+1) if all([int(j) and i%int(j)==0 for j in str(i)])]
    
        
