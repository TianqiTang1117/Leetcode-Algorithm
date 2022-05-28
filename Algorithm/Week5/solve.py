from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        self.m=len(board)
        self.n=len(board[0])
        for j in range(self.n):
            # 第一行
            if board[0][j] == "O":
                self.bfs(board,0, j)
            # 最后一行
            if board[self.m - 1][j] == "O":
                self.bfs(board,self.m - 1, j)
        for i in range(self.m):
            if board[i][0] == "O":
                self.bfs(board,i, 0)
            if board[i][self.n - 1] == "O":
                self.bfs(board,i, self.n - 1)
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"
    
    def bfs(self,board,i,j):
        q=deque()
        q.appendleft((i, j))
        dx=[-1,0,0,1]
        dy=[0,1,-1,0]
        while len(q)>0:
            i,j=q.pop()
            if 0<=i<self.m and 0<=j<self.n and board[i][j]=="O":
                board[i][j]="B"
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if nx < 0 or ny < 0 or nx >= self.m or ny >= self.n:
                        continue
                    q.appendleft((nx,ny))


