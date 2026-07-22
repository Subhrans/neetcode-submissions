class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)
        if s_length != t_length:
            return False

        s_set = dict()
        for i in range(s_length):
            if s.count(s[i])!=t.count(s[i]):
                return False
        return True