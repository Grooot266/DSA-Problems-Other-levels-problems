#Grooot266 #Two Pointer sol
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        answer=[]

        while left <= right :
            if abs(nums[left]) > abs(nums[right]):
                answer.append(nums[left] ** 2)
                left +=1
            else:
                answer.append(nums[right] ** 2)
                right-=1
        answer.reverse()
        return answer


