class Solution {
    public void moveZeroes(int[] nums) {
        int help=0;
        for (int i=0;i<nums.length;i++){
            if (nums[i]!=0){
                nums[help]=nums[i];
                help+=1;
            }
        }
        for (int i=help;i<nums.length;i++){
            nums[i]=0;
        }
    }
}
