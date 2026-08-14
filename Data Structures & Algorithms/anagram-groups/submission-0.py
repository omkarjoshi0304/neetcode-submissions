import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_dict = collections.defaultdict(list)

        for s in strs:

            count = [0] * 26

            for char in s:

                count[ord(char) - ord('a')] += 1

            count_dict[tuple(count)].append(s)

        return list(count_dict.values())

