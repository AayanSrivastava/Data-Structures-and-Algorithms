from collections import deque

#DFS   use Stack
class Solution:
    def allPathsSourceTarget(self, graph):
        result = []
        stack = [(0, [0])]
        target = len(graph) - 1
        while stack:
            cur,route = stack.pop()
            if cur == target:
                result.append(route)
            else:
                for node in graph[cur]:
                    stack.append((node, route + [node]))
        return result

#BFS     use deque
class Solution:
    def allPathsSourceTarget(self, graph):
        target=len(graph)-1
        ans=[]
        q=deque([(0,[0])])
        while q:
            node,path=q.popleft()
            if node==target:
                ans.append(path)
            else:
                for adjnode in graph[node]:
                    q.append((adjnode, path + [adjnode]))
        return ans