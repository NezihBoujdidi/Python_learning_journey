# I could just add nums2[j] in nums1[m+j] and use nums1.sort(), but wanted to not use .sort()

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j=0
        while (j!=n and i!= (n+m)):
            if (nums1[i]<=nums2[j]):
                if(i!=m+j):
                    i+=1
                else:
                    nums1[i]=nums2[j]
                    i+=1
                    j+=1
            else:
                for x in range(m+j,i,-1):
                    nums1[x] = nums1[x-1]
                nums1[i] = nums2[j]
                j+=1
                i+=1
            
