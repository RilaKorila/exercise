# if there are many possible courses, we have to return any of courses.
# if we detect a cycle, atop algorithm immediately return an empty list.

class Solution:
    def findOrder(self, numCourse: int, prerequisites: List[List[int]]) -> List[int]:
        #build adjacency list of prerequisites
        prereq = { c: [] for c in range(numCourse)}

        for crs, pre in prerequisites :
            prereq[crs].append(pre)
        
        # a course has 3 possible states
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added cycle
        # unvisited -> crs not added to output or cycle
        output = []
        visit, cycle  = set(), set()

        # input -> crs: int
        # output -> boolean  
        def dfs(crs):
            # detect a cycle
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            # check all prerequisites of crs
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output