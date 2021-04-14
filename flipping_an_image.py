class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in range(len(image)):
            
            start=0
            end=len(image[r])-1
            while start<end:
                image[r][start], image[r][end]=image[r][end], image[r][start]
                start+=1
                end-=1
            for i in range(len(image[r])):
                image[r][i]=-(~-image[r][i])
        return image
        
    def flipAndInvertImage2(self, image: List[List[int]]) -> List[List[int]]:
#          1^ i does the bitwise exclusive or operation which basically flips a bit from 0 to 1 and vice versa
#           the reversed obviously reverse the row
        return [[1 ^ i for i in reversed(row)] for row in image]
            
        
