class Solution(object):
    def replaceElements(self, arr):
        if len(arr) > 0:
            new_arr = [0]*len(arr)
            max_from_seen=-1
            for i in range(len(arr)-1,-1,-1):
                if arr[i]>max_from_seen:
                    max_from_seen= arr[i]
                new_arr[i-1]=max_from_seen
            new_arr[len(arr)-1]=-1
            return new_arr
        return arr
