class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        totals = list()
        last = 0
        for el in nums:
            li.append(el+last)
            last += el
        return totals

        

        