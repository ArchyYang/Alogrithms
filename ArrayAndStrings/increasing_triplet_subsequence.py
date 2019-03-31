'''
Given an unsorted array return whether an increasing 
subsequence of length 3 exists or not in the array.

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
'''

def increasingTriplet(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    a = b = None
    for n in nums:
        if a is None or a >= n:
            a = n
        elif b is None or b >= n:
            b = n
        else:
            return True
    return False