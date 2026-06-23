from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)
        this_iteration_not_served = 0
        while sandwiches and this_iteration_not_served <= len(students_queue):
            if students_queue[0] != sandwiches[0]:
                students_queue.append( students_queue.popleft())
                this_iteration_not_served += 1
            else:
                students_queue.popleft()
                sandwiches.pop(0)
                this_iteration_not_served = 0
        return len(students_queue)
        