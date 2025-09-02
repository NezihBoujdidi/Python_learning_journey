class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        current=[]
        for i in range(numRows):
            current=[1]*(i+1)
            if result != [] and result[i-1] :
                for j in range(1,i): 
                    current[j]=result[i-1][j-1]+result[i-1][j]
            result.append(current)
        return result
