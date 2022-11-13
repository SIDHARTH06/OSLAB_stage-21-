from collections import defaultdict
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return [i, x.index(v)]
def recursive_solve(i, j, steps, n, m):
    if steps == 0:
        return arr[i][j]
     
    res = 0
    if steps > 0:
        dx = [-2, -1, 1, 2, -2, -1, 1, 2]
        dy = [-1, -2, -2, -1, 1, 2, 2, 1]
        for k in range(0, 8):
            if (dx[k] + i >= 0 and
                dx[k] + i <= n - 1 and
                dy[k] + j >= 0 and
                dy[k] + j <= n - 1):
                if arr[dx[k]+i][dx[k]+j]>=0:
                    arr[dx[k]+i][dx[k]+j]=0
                    print(arr)
                    res = res + recursive_solve(dx[k] + i, dy[k] + j,
                                       steps - 1, n, m)
     
    return res
def solve(i, j, steps, n):
    m = defaultdict(lambda:0)
    return recursive_solve(i, j, steps, n, arr)
t=int(input())
for _ in range(t):
    n=int(input())
    arr=([0]*n)*n
    for i in range(n):
        arr[i]=list(map(int,input().split()))
    b,c=index_2d(arr,-3)
    step=1000
    while(solve(b,c,step,n)!=solve(b,c,step,n)):
        step=step+1
    print(solve(b,c,step,n))
    
    
    

