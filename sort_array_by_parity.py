from collections import deque
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        q = deque()
        for num in A:
            if num%2==0:
                q.appendleft(num) #even numbers
            else:
                q.append(num)
                
        return list(q)
