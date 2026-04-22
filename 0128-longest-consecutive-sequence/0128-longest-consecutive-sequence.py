class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # regular set over a hasmap
        counts = set(nums)
        longest = 0 
        for count in counts:
            # STARTING POINTS
            if count - 1 not in counts:
                length = 1
                current = count
                while current + 1 in counts:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest