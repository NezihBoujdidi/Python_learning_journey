class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        used = [False]*len(baskets)  
        for i in range(len(fruits)):
            c=0
            for j in range(len(baskets)):
                if fruits[i]<= baskets[j] and used[j]==False :
                    used[j]= True
                    break
                else:
                    c+=1      
            if c==len(baskets):
                unplaced+=1   
        return unplaced
