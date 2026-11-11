class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        #solution 1 
        ans=[]

        for i in range(len(matrix[0])):
            temp = []

            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            
            ans.append(temp)

        return ans

            
