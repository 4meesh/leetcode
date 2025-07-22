class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n1=int(a,2)
        n2=int(b,2)
        sum=bin(n1+n2)
        return sum[2:]