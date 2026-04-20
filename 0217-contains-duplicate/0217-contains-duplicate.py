class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i=0
        count = set()
        ans = False
        for num in nums:
            if num in count:
                return True 
            count.add(num)
        return False


    



        