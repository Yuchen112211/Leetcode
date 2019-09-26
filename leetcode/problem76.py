class Solution(object):

    def minWindow(self, s, t):
        length_t = len(t)
        left = right = 0
        t_dict = {}
        s_dict = {}
        string_min = s
        for i in t:
            t_dict[i] = t.count(i)
            s_dict[i] = s.count(i)
            if t_dict[i] > s_dict[i]:
                return ''

        while left <= len(s) - len(t):
            signal = 0
            while max(t_dict.values()) > 0:
                if right >= len(s):
                    signal = 1
                    break
                if s[right] in t:
                    t_dict[s[right]] -= 1
                right += 1
            if signal:
                return string_min
            if len(string_min) > right - left:
                string_min = s[left:right]
            if s[left] in t:
                t_dict[s[left]] += 1
            left += 1
        return string_min

if __name__ == '__main__':
    S = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print S.minWindow(s,t)