class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 使用bfs
        from collections import defaultdict
        graph = defaultdict(list)
        degree = [0] * numCourses
        # 建图
        for x, y in prerequisites:
            graph[y].append(x)
            degree[x] += 1
        res = []
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        #print(bfs)
        for i in bfs:
            res.append(i)
            for j in graph[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return res if len(res) == numCourses else []
