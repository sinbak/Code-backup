from maze import Maze

# """
#     [과제 3]
#         mazerunner.py 파일의 shortest_path() 함수를 완성하시오.
#         이 파일 안에서 함수를 더 만들어도 괜찮지만, 주어진 함수의 매개변수는 건드리지 말 것
#         maze.py, mazetester.py는 건드리지 말 것
    
#     [올바른 경로valid path란?]
#         (1, 1) 로 시작하지 않거나,
#         (HEIGHT, WIDTH) 로 끝나지 않거나,
#         이동 방향이 상하좌우 네 방향이 아니거나
#         벽'#'이 포함된 경로는 유효하지 않은 경로 invalid path
        
#     [경로 길이]
#         편의상 "경로에 포함된 좌표 개수"로 정의함
        
#     [제출]
#         mazerunner.py
        
#     [채점기준]
#         invalid path이면 0점
#         경로 길이가 최적해의 100%면 만점, (100+x)% 이면 점수는 (100-x)%
#         즉, 경로 길이가 최적해의 두 배 이상이면 0점
        
#         **웹에서 검색한 결과를 참고해서 작성한 경우 출처를 적어 둘 것
#         평가에는 반영되지 않으나, 출처 표기 없이 유사한 코드가 발견되면 0점
# """

# # 이 함수를 먼저 만들어보는 걸 추천함
# # def shortest_path_length(maze):
# # #     # maze에서 (1, 1)에서 (maze2.height, maze2.width)까지 가는 최단 경로의 "길이"를 리턴(정수)
# # #     # 이동 방향은 상/하/좌/우 네 방향 (대각선x)
# # #     # 갈 수 있는 경로가 없으면 -1을 리턴한다.
# # #     # return -1
# #     path = shortest_path(maze)

# #     if path:
# #         return len(path)
# #     else:
#         # return -1
direct_x = [0,1,0,-1] #상하좌우
direct_y = [-1,0,1,0]

def backTrack(maze,wx,hy):
    visits_T = []
    visits_T.append((hy,wx))
    visit = maze[hy][wx]

    while True:
        for dn in range(0,4):
            x = wx + direct_x[dn]
            y = hy + direct_y[dn]
            if maze[y][x] == maze[hy][wx]-1:
                # visits_L.append([x,y])
                visits_T.append((y,x))
                wx = x
                hy = y
                visit = maze[y][x]
                # print(visit)
                break
            if visit == 1:
                # visits_L.reverse()
                visits_T.reverse()
                return visits_T
def shortest_path(maze):
        # maze에서 (1, 1)에서 (maze.height, maze.width)까지 가는 "최단 경로"를 리턴
        # 이동 방향은 상/하/좌/우 네 방향 (대각선x)
        # 경로는 2-tuple의 리스트로 만든다(예: [(1,1), (1, 2), (2, 2), ...]
        # 갈 수 있는 경로가 없으면 []를 리턴한다.
        start_x = 1
        start_y = 1
        copymaze = []
        a = maze.height+2
        for i in range(a):
           copymaze.append(maze.maze[i].copy())
        #    print(copymaze)
        queue = []
        queue.append([start_x,start_y]) #시작지점
        copymaze[1][1]=1
        while (len(queue) > 0):
            start_x,start_y = queue.pop(0)
            for dn in range(0,4):
                x = start_x+direct_x[dn]
                y = start_y+direct_y[dn]
                copymaze[start_y][start_x]
                if y== maze.height and x == maze.width: #도착지라면
                    x = maze.width
                    y = maze.height
                    copymaze[y][x] = copymaze[start_y][start_x]+1
                    # print(maze.maze)
                    return backTrack(copymaze,x,y)

                elif copymaze[y][x] ==' ': #길일 때
                        copymaze[y][x] = copymaze[start_y][start_x]+1
                        queue.append([x,y])
        return [] #출
#참고 : https://ehpub.co.kr/%EB%AF%B8%EB%A1%9C%EC%97%90-%EB%AC%BC%EC%9D%84-%EC%8F%9F%EC%95%84-%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C%EB%A5%BC-%EA%B5%AC%ED%95%B4%EC%9A%94-bfs-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%BD%94/