class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        prereqs = { i: [] for i in range(numCourses) }
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        visited, cycleDet = set(), set()
        res = []

        def dfs(course):
            if course in cycleDet:
                return False
            if course in visited:
                return True
            
            cycleDet.add(course)

            for neighbor in prereqs[course]:
                if not dfs(neighbor):
                    return False
            
            cycleDet.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res