# Some courses may have prerequisites
# ex) [[0, 1]]  : we have to take course 0 before taking course 1
# 有向グラフを描く [0, 1] : 0->1, not necessary prerequisites : []
# この時根になるノードはprerequisitesが不要
# DFSで辿っていく-> empty Listにたどり着いたら、can be completed
# After taking course, remove from  prerequisites lists (empty List means "you can take the course")

# Loop = False 

class Solution:
    def canFinish(self, numCourse: int, prerequisites: List[List[int]]) -> bool:
            # すべてのcourseのprerequisitesを[]で初期化 
            preMap = {i: [] for i in range(numCourse)}
            for crs, pre in prerequisites:
                preMap[crs].append(pre)

            # visitSet = all courses along the current DFS pass
            visitSet = set()
            def dfs(crs):
                # if we visited twice
                if crs in visitSet: # = detect Loop = we cant complete prerequisites
                    return False
                if preMap[crs] == []:
                    return True

                visitSet.add(crs)
                for pre in preMap[crs]:
                    if not dfs(pre):
                        return False
                
                visitSet.remove(crs)
                preMap[crs] = []
                return True

            # we have to check all prerequisites of course
            for crs in range(numCourse):
                if not dfs(crs):
                    return False
            return True
