class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i],0) + 1
            dict2[t[i]] = dict2.get(t[i],0) + 1
        



        # for key,value in dict1.items():
        #     if key not in dict2 or dict2[key] != value:
        #         return False
        return dict1 == dict2     