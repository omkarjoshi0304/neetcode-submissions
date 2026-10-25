class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0] )

        output = [intervals[0]]

        for s , e in intervals[1:]:

            lastend = output[-1][1]

            if s <= lastend:
                output[-1][1] = max(e , lastend)
            else:
                output.append([s , e])
        return output