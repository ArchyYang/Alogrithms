'''

Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.

'''

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    max_length = 0
    local_max_substring = ""
    length = len(s)
    for i in range(length):
        index = local_max_substring.find(s[i])
        if index > -1:
            if len(local_max_substring) > max_length:
                max_length = len(local_max_substring)
            local_max_substring = local_max_substring[index+1:] 
        local_max_substring = local_max_substring + s[i]
    if local_max_substring and len(local_max_substring) > max_length:
        max_length = len(local_max_substring)
    return max_length