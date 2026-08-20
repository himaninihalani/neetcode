class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        n = len(people)
        people.sort()
        heavy=n-1
        light=0
        while light<=heavy:
            if people[light]+people[heavy]<=limit:
                boats+=1
                light+=1
                heavy-=1
            else:
                boats+=1
                heavy-=1
        return boats        