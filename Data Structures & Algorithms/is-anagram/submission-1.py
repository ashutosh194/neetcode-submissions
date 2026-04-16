class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        dict1 = {}
        dict2 = {}
        for i in s:
            if i in dict1:
                dict1[i]  = dict1[i] +1
            else:
                dict1[i] = 1

        for i in t:
            if i in dict2:
                dict2[i] = dict2[i] + 1
            else:
                dict2[i] = 1

        for key,value in dict1.items():
            if key not in dict2 or dict2[key] != value:
                return False
        return True     