# # import turtle as t

# # def spiral(sp_len):
# #     if sp_len <= 5:
# #         return
# #     t.forward(sp_len)
# #     t.right(60)
# #     spiral(sp_len - 5)

# # t.speed(0)
# # spiral(200)
# # t.hideturtle()
# # t.done()

# import turtle as t
# def frectal(n):
#     if n <= 5:
#         for i in range(3):
#             # t.forward(n)
#             t.right(120)
#         return
#     next_n = n/2
#     frectal(next_n)
#     t.forward(next_n)
#     frectal(next_n)
#     t.backward(next_n)
#     t.right(60)
#     t.forward(next_n)
#     t.left(60)
#     frectal(next_n)
#     t.right(60)
#     t.backward(next_n)
#     t.left(60)
# t.speed(0)
# frectal(160)
# t.hideturtle()
# t.done()
# # 참고자료 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=mario002&logNo=221450204394

# # import turtle as t


# # def tri(tri_len):

# #     if tri_len <= 10:

# #         for i in range(0, 3):

# #             t.forward(tri_len)

# #             t.right(120)

# #         return

# #     new_len = tri_len / 2

# #     tri(new_len)

# #     t.forward(new_len)

# #     tri(new_len)

# #     t.backward(new_len)

# #     t.right(60)

# #     t.forward(new_len)

# #     t.right(60)

# #     tri(new_len)

# #     t.right(60)

# #     t.backward(new_len)

# #     t.right(60)

 

# # t.speed(0)

# # tri(160)

# # t.hideturtle()

# # t.done()
dx=[ 0,1,0,-1]
dy=[-1,0,1,0]
def BackTracking(maze,ex,ey):
    foots=[]
    foots.append([ex,ey])
    foot = maze[ey][ex]
    while(True):
        for di in range(0,4):
            x = ex + dx[di]
            y = ey + dy[di]
            if(maze[y][x] == foot-1):
                foots.append([x,y])
                ex = x
                ey = y
                foot = maze[y][x]
                break
        if(foot == 1):
            foots.reverse()
            return foots
 
def LoadOfFlood(maze,sx,sy):
    queue = []
    queue.append([sx,sy])
    foot = maze[sy][sx]
    while(len(queue)>0):        
        sx,sy = queue.pop(0)
        foot = maze[sy][sx]
        for di in range(0,4):
           x = sx + dx[di]
           y = sy + dy[di]
           if(maze[y][x]==-2):
               maze[y][x]= foot+1
               return BackTracking(maze,x,y)               
           elif (maze[y][x]==0):
               maze[y][x]= foot+1
               queue.append([x,y])
    return []
    
maze = [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1, 1, 0, 0, 0, 0,-1, 0, 0, 0, 0,-1],
    [-1, 0,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1,-1, 0,-1, 0, 0, 0,-1, 0,-1],
    [-1, 0,-1, 0, 0, 0, 0,-1,-1, 0, 0,-1],
    [-1, 0,-1, 0,-1,-1, 0,-1, 0,-1,-1,-1],
    [-1, 0,-1,-1, 0,-1, 0, 0, 0, 0, 0,-1],
    [-1, 0,-1, 0, 0,-1, 0,-1, 0,-1, 0,-1],
    [-1, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1,-1,-1, 0, 0,-1, 0, 0, 0,-1],
    [-1, 0, 0, 0,-1,-1,-1, 0, 0,-1,-2,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        ]
path = LoadOfFlood(maze,1,1)
print(path)