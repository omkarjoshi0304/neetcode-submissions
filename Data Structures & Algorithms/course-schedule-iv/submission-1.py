class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        prereqMap = {}
        def dfs(crs):
            if crs not in prereqMap:
                prereqap = set()

                for pre in adj[crs]:
                    prereqap.add(pre)
                    prereqap |= dfs(pre)
                prereqMap[crs] = prereqap
            return prereqMap[crs]
        
        

        for crs in range(numCourses):
            dfs(crs)
        
        res = []

        for u , v in queries:
            res.append(u in prereqMap[v])
        return res
