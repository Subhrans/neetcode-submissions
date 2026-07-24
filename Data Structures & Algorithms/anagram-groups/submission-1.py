class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count_ana = {}
        # if len(strs) < 2:
        #     return [strs]
        # for each_str in strs:
        #     str_set = set(each_str)
        #     str_dict = {}
        #     for i in str_set:
        #         str_dict[i]=each_str.count(i)
        #     count_ana[each_str] = str_dict
        # list_ana = []
        # done_items = []

        # keys = list(count_ana.keys())
        # for i in range(len(keys)):
        #     list_a = []
        #     if keys[i] in done_items:
        #         continue
        #     for j in range(i+1, len(keys)):
        #         if count_ana[keys[i]] == count_ana[keys[j]]:
        #             if keys[i] not in list_a:
        #                 list_a.append(keys[i])
        #             list_a.append(keys[j])
        #     if not list_a:
        #         list_a.append(keys[i])
        #     done_items.extend(list_a)
        #     list_ana.append(list_a)
        # return list_ana
        count_ana = {}
        for each_str in strs:
            str_set = set(each_str)
            str_dict = {}
            for i in str_set:
                str_dict[i]=each_str.count(i)
            count_ana[each_str] = str_dict
        list_ana = []
        done_items = []
        for i in range(len(strs)):
            list_a = []
            if strs[i] in done_items:
                continue
            for j in range(i+1, len(strs)):
                if count_ana[strs[i]] == count_ana[strs[j]]:
                    if strs[i] not in list_a:
                        list_a.append(strs[i])
                    list_a.append(strs[j])
            if not list_a:
                list_a.append(strs[i])
            done_items.extend(list_a)
            list_ana.append(list_a)
        return list_ana