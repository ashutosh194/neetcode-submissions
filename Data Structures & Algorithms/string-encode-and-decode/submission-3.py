class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        str_len = 0
        for item in strs:
            str_len = len(item)
            res = res + str(str_len)+"#"+item
        # print(res)
        return res
    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            lst.append(s[i:j])
            i = j
        return lst