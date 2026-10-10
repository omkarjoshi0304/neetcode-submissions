class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def childerns(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])
                digit = str((int(lock[i]) - 1 + 10) % 10 )
                res.append(lock[:i] + digit + lock[i + 1:])
            return res
            
        queue = deque()
        queue.append(["0000" , 0])
        visit = set(deadends)

        while queue:
            lock , turns = queue.popleft()

            if lock == target:
                return turns

            for child in childerns(lock):
                if child not in visit:
                    visit.add(child)
                    queue.append([child, turns + 1])
        return - 1
                    
