"""
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        em_to_name = {}
        
        for account in accounts:
            name = account[0]
            for em in account[1:]:
                graph[account[1]].add(em)
                graph[em].add(account[1])
                em_to_name[em] = name
        visited = set()
        res = []
        for key in graph:
            if not key in visited:
                visited.add(key)
                stack = [key]
                sub_result = []
                while stack:
                    node = stack.pop()
                    sub_result.append(node)
                    for nei in graph[node]:
                        if not nei in visited:
                            visited.add(nei)
                            stack.append(nei)
                res.append([em_to_name[key]] + sorted(sub_result))
        return res