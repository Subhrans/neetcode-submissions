class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)
        if s_length != t_length:
            return False
        s_set = set(s)
        t_set = set(t)
        if s_set != t_set:
            return False

        s_dict = dict()
        t_dict = dict()
        for string in s_set:
            s_dict[string]=s.count(string)
            t_dict[string] = t.count(string)
        if s_dict == t_dict:
            return True
        return False
