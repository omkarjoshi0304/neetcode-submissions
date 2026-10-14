class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # adj[course] = list of direct prerequisites
        adj = {i: [] for i in range(numCourses)}
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        # prereq_map maps a course to a Set of ALL its prerequisites (direct + indirect)
        prereq_map = {}

        def dfs(crs):
            # Base Case: Already computed this course's complete prereq set
            if crs in prereq_map:
                return prereq_map[crs]
            
            # Start a new set for the current course
            prereqs = set()
            for p in adj[crs]:
                prereqs.add(p)                   # Add the direct prereq
                prereqs |= dfs(p)                # Union with all indirect prereqs
            
            prereq_map[crs] = prereqs
            return prereqs
        
        # Precompute the prerequisite sets for every single course
        for c in range(numCourses):
            dfs(c)
            
        # Answer each query in O(1) time
        res = []
        for u, v in queries:
            res.append(u in prereq_map[v])
            
        return res