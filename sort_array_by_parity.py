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

    def solution2(self, A: List[int]) -> List[int]:
        start=0
        end=len(A)-1
        
        while start<end:
            if A[start]%2==0:
                start+=1
            else:#swap with the end pointer
                A[end], A[start]=A[start], A[end]
                end-=1
        return A
