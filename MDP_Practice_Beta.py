import random
import numpy as np

# 필드, 0 = 이동 가능 구역, 1 = 에이전트 위치, 2 = 골 지점

# 크기
size = 14

field = np.zeros((size, size))
# size * size 필드 생성

# 최적 경로를 정하기 위해서
optimal_route = np.zeros((size, size))

# 필드 초기화
for i in range(1, len(field)) :
    for k in range(len(field)) :
        field[i][k] = 0
# 골라인 생성
for i in range(len(field)) :
    field[0][i] = 2

# 체크 시점에 상태별 에이전트의 존재 확률 확인용
count_field = np.zeros((size, size))

# 각 상태마다 보상 저장
field_rew = np.zeros((size, size))

for i in range(len(field)) :
    field_rew[len(field) - 1][i] = -13

for i in range(1, len(field) - 1) :
    # # 벽이 연속적으로 나타나지 않게 정의
    # walls = []
    # while len(walls) < 2:
    #     wall = random.randint(0, 13)
    #     if (wall + 1) in walls or (wall - 1) in walls :
    #         continue
    #     walls.append(wall)

    walls = []
    wall = i + (i % 5)

    if wall >= len(field) :
        wall -= len(field)
    walls.append(wall)
    print(walls)
    # 벽이 있는 상태의 보상을 -15로 지정
    for k in range(len(field)) :
            # 각 상태별 보상 지정
            field_rew[i][k] = (-14) + (len(field) - i)

    for k in walls :
         field_rew[i][k] = -15

    for k in walls:
        field[i][k] = 7



# 에이전트 클래스. 위치 초기화, 이동 함수
class agent():
    def __init__(self):  # 생성자, # 필드의 가장 아랫 부분중 가운데 위치에 에이전트 생성

        self.x = len(field) // 2
        self.y = len(field) - 1

        field[self.y][self.x] = 1

    def reset(self):  # 첫번째 시도 이후, 에이전트 위치 초기화
        self.x = len(field) // 2
        self.y = len(field) - 1

    def decision_move(self):

        selecting = []

        selecting.append(field_rew[self.y - 1][self.x]) # 에이전트 상

        if (self.x + 1) != len(field) : # 에이전트 우
            selecting.append(field_rew[self.y][self.x + 1])
        else :
            selecting.append(field_rew[self.y][self.x])

        if not((self.x - 1) < 0) : # 에이전트 좌
            selecting.append(field_rew[self.y][self.x - 1])
        else :
            selecting.append(field_rew[self.y][self.x])

        selecting.append(-14) # 에이전트 하

        choose = selecting.index(max(selecting)) + 1

        # 10%의 확률로 에이전트가 원하지 않는 곳으로 이동
        if random.random() < 0.2:
            while True:
                ran = random.randint(1, 4)
                # 랜덤하게 이동하게 하기 위해 기존의 방향과 다르게 하기 위해 반복
                if ran != choose:
                    choose = ran
                    break

        return choose


    def move(self):  # 에이전트 이동
        # 1 : 북 2: 동 3: 서 4: 남

        step = self.decision_move()

        # 4방향 이동에 대한 구현

        # 북쪽으로 이동
        if step == 1 :
            if not (field[self.y - 1][self.x] == 7):
                self.y -= 1

        # 동쪽으로 이동
        elif step == 2 :
            if not ((self.x + 1) >= len(field)):
                if not(field[self.y][self.x + 1] == 7) :
                    self.x += 1

        # 서쪽으로 이동
        elif step == 3 :
            if not ((self.x - 1) < 0):
                if not(field[self.y][self.x - 1] == 7) :
                    self.x -= 1

        # 남쪽으로 이동
        elif step == 4 :
            if not ((self.y + 1) >= len(field)):
                if not (field[self.y + 1][self.x]) :
                    self.y += 1


    # 에이전트가 골 지점에 도착할 경우
    def check_finish(self) -> bool :
        if field[self.y][self.x] == 2 :
            count_field[self.y][self.x] += 1
            return True
        else :
            return False




def main() :

    array = []
    count = 5000

    ag = agent()
    for _ in range(count) :
        for _ in range(12) :
            ag.move()
            if ag.check_finish() :
                break
        count_field[ag.y][ag.x] += 1
        ag.reset()

    for i in range(len(field)) :
        array2 = []
        for k in range(len(field)) :
            array2.append(round(count_field[i][k] / count * 100, 2))

        array.append(array2)
    for i in array :
        print(i)

    print(count_field)

    print(field)


    print(array[7][7])
    print(count_field[7][7])

if __name__ == '__main__' :
    main()

    # 개선사항 1, 클린 코드 2, 벽이 가로 막혀진 경우 탈출 불가

