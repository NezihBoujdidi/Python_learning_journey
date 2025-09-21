class Solution(object):
    def maxProduct(self, n):
        list = []
        max = 0
        while n // 10 != 0:
            list.append(n%10)
            n = n // 10
        list.append(n)
        for i in range(len(list)-1):
            for j in range(i+1,len(list)):
                if list[i]*list[j] > max:
                    max = list[i]*list[j]     
        return max
