class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}

        for c in t:
            count_t[c] = count_t.get (c , 0) + 1
        have , need = 0 , len(count_t)

        res , res_win = [-1 , -1 ], float('infinity')

        l = 0
        window = {}
        for r in range (len(s)):
            window[s[r]] = window.get(s[r] , 0) + 1

            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1

            while  have == need:

                if (r - l + 1) < res_win:
                    res_win = r - l + 1
                    res = [l , r]

                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l , r = res
        return s[l : r + 1] if res_win != float("infinity") else ""


                

