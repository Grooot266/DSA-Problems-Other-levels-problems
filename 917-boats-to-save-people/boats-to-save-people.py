class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # Two Pointer solution
        people.sort()
        lt=0
        rt=len(people)-1
        bt=0
        while lt <= rt :
            if people[lt]+people[rt]<=limit:
                lt+=1
                rt-=1
            else:
                rt-=1
            bt +=1
        return bt

