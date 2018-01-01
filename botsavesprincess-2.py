#
def nextMove(n, r, c, a):
    mx = my = px = py = 0

    gotp = gotm = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'm':
                mx = i
                my = j
                gotm = 1
            elif a[i][j] == 'p':
                px = i
                py = j
                gotp = 1
        if gotp == 1 and gotm == 1:
            break
    aly = mx - px
    alx = my - py
    if aly < 0:

        ans="DOWN"
    elif aly==0:
        pass
    else:

        ans="UP"

    if alx < 0:

        ans="RIGHT"
    elif alx==0:
        pass
    else:

        ans="LEFT"


    return ans


n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))
