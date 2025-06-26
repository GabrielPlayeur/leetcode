class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
         #edges cases:
        if not graph:
            return []

        # build di-graph
        d = {}
        for i in range(len(graph)):
            d[i] = graph[i] # one-way link

        # apply DFS on DAG
        n = len(graph)
        stack = [(0, [0])] # - store noth the (node, and the path leading to it)
        res = []
        while stack:
            node, path = stack.pop()
            # check leaf
            if node == n - 1:
                res.append(path)
            # traverse rest
            for nei in d[node]:
                stack.append((nei, path+[nei]))
        return res
    
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res=[]
        for i in range(len(graph[0])):
            v=graph[0][i]
            path=[0]
            res.extend(self.dfs(graph, v, path))
        return res

    def dfs(self, graph, index, path):
        path.append(index)

        if index==len(graph)-1:
            return [path]

        res=[]
        for i in range(len(graph[index])):
            v=graph[index][i]
            p=self.dfs(graph, v, path.copy())
            res.extend(p)
        return res
