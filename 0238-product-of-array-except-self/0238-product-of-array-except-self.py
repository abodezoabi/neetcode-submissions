class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,postfix = len(nums)*[1], len(nums)*[1]
        i,j =0,0

        for i in range(len(nums)):
            if i==0:
                prefix[i]=nums[i]
            else:
                prefix[i] = prefix[i-1]*nums[i]

        for j in range(len(nums)-1,0,-1):
            if j==len(nums)-1:
                postfix[j] = nums[j]
            else:
                postfix[j] = postfix[j+1] * nums[j]
        ans=[]

        for k in range (len(nums)):
            if k-1<0:
                ans.append(1*postfix[k+1])
            elif k+1>=len(nums):
                ans.append(prefix[k-1]*1)
            else:
                ans.append(prefix[k-1]*postfix[k+1])
        return ans


        




