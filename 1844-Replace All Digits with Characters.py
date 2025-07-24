class Solution(object):
    def replaceDigits(self, s):
        s_new = ""
        for i in range(len(s)):
            if s[i].isdigit():
                prev_char = s_new[-1]
                shifted = chr(ord(prev_char) + int(s[i]))
                s_new += shifted
            else:
                s_new += s[i]
        return s_new