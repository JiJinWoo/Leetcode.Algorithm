class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result = 0
        seat = sorted(seats)
        student = sorted(students)
        for i in range(len(seats)):
            if seat[i] > student[i]:
                result += seat[i] - student[i]
            else:
                result += student[i] - seat[i]
                
        return result