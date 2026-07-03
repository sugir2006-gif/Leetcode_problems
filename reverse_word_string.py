class Solution:
    def reverseWords(self, s):
        s1= s.split()
        s2=s1[::-1]
        s3=" ".join(s2)
        return s3