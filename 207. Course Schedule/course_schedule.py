"""
Problem : 207. Course Schedule
Difficulty: Medium
Topics   : Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
Runtime  : 3
Memory   : 21356000
Language : python3
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        

        # 0 = never visited
        # 1 = currently exploring
        # 2 = already explored
        state = [0] * numCourses
    
        def dfs(course):

            # We came back to a course we're already exploring.
            # This means there's a cycle.
            if state[course] == 1:
                return False

            # We've already checked this course before.
            # No need to check again.
            if state[course] == 2:
                return True

            # Start exploring this course.
            state[course] = 1

            # Check every course that depends on this one.
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False

            # Finished exploring this course.
            state[course] = 2

            return True

        for course in range(numCourses):
                if not dfs(course):
                    return False

        return True
