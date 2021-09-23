#https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = [(0, 'a')]
        lib = {0: 'a'}
        while q:
            cur = q.pop(0)        
            nei = graph[cur[0]]
            if len(nei) == 0:
                if len(graph) > 1:
                    q.append((cur[0]+1, cur[1]))
            for node in nei:
                if node in lib:
                    #case 1: node has same marking as cur
                    if cur[1] == lib[node]:
                        return False
                    #case 2: node has different marking as cur
                else:
                    # node not in lib, add it to the lib and q, with opposite marking from cur
                    if cur[1] == 'a':
                        lib[node] = 'b'
                        q.append((node,'b'))
                    else: 
                        lib[node] = 'a'
                        q.append((node,'a'))

        return True
            
            
                
            
            