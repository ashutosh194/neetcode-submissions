class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_len = len(s)
        if s_len == 1:
            return True
        i = 0
        j = s_len-1
        s = s.lower()
        print(s_len)
        while i <= j :
            print((s[i],s[j]))
            if s[i] == " " or not self.alphaNum(s[i]):
                i += 1
                continue
            if s[j] == " " or not self.alphaNum(s[j]) :
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
               
            
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))




        