'''
Given an array of strings, group anagrams together.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]


'''

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	rtn = collections.defaultdict(list)
	for s in strs:
		rtn[tuple(sorted(s))].append(s)
	return list(rtn.values())