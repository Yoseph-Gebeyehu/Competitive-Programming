class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right, left = len(people) -1 ,0
        boat = 0
        while right >= left:
            if people[right] + people[left] > limit:
                boat += 1
                right -= 1
            elif people[right] + people[left] < limit:
                right -= 1
                left += 1
                boat += 1
            else:
                boat += 1
                right -= 1
                left += 1
        return boat
