class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prereqMap = { i:[] for i in range(numCourses) }
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if len(prereqMap[course]) == 0:
                return True
            
            visited.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            prereqMap[course] = []
            visited.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


        