
#!/usr/bin/python
def displayPathtoPrincess(n, grid):
    xp = yp = 0
    xm=ym=(n)//2
    if grid[0][n - 1] == 'p':
        xp = 0
        yp = n - 1
    elif grid[n - 1][0] == 'p':
        xp = n - 1
        yp = 0
    elif grid[n - 1][n - 1] == 'p':
        xp = yp = n - 1

    
    aly=xm-xp
    alx=ym-yp
    if aly<0:
        for i in range(abs(aly)):
            print("DOWN")
    else:
        for i in range(abs(aly)):
            print("UP")

    if alx < 0:
        for i in range(abs(alx)):
            print("RIGHT")
    else:
        for i in range(abs(alx)):
            print("LEFT")


# print all the moves here
m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())



displayPathtoPrincess(m, grid)
