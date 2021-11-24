class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        The median is the middle number in a sorted, ascending or descending, 
        list of numbers and can be more descriptive of that data set than the average.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import numpy as np
        
        #merge the array and sort it.
        num = np.sort(nums1 + nums2)
        
        #Find the Length of the merged array to find it's median
        length = len(num)
        median = int(length//2)
        
        #if even, array would have 2 middle numbers. 
        #median would be mid of sum of middle numbers 
        if (length % 2) == 0:
            result = (num[median-1]+num[median])/2.0
        else:
            #if odd, array would have just one number, hence that would the median.
            result = float(num[median])
        return result        