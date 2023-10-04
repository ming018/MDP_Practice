import random
import numpy as np

# 필드, 0 = 이동 가능 구역, 1 = 에이전트 위치, 2 = 골 지점
field = [[2, 0, 0, 0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [2, 0, 0, 0, 0, 0, 0, 0, 2]]


count_field = np.zeros((len(field), len(field)))

# 사전에 정의된 최적 경로 5 목표지점, 6 에이전트 위치
optimal_route = [[5, 2, 2, 2, 2, 1, 1, 1, 5],
                 [4, 2, 4, 2, 4, 1, 4, 1, 4],
                 [4, 4, 2, 4, 2, 4, 1, 4, 4],
                 [4, 2, 4, 2, 4, 1, 4, 1, 4],
                 [4, 4, 2, 4, 6, 3, 1, 3, 3],
                 [3, 2, 3, 2, 2, 1, 3, 1, 3],
                 [3, 3, 2, 3, 3, 3, 1, 3, 3],
                 [3, 2, 3, 2, 2, 1, 3, 1, 3],
                 [5, 2, 2, 2, 1, 1, 1, 1, 5]]

# 에이전트 클래스. 위치 초기화, 이동 함수
class agent():
    def __init__(self):  # 생성자, 필드 중앙에 위치
        self.x = len(field) // 2
        self.y = len(field) // 2

    def reset(self):  # 첫번째 시도 이후, 에이전트 위치 초기화
        self.x = len(field) // 2
        self.y = len(field) // 2

    def decision_move(self):
        move = optimal_route[self.y][self.x]

        # 30%의 확률로 사전에 정의된 최적경로를 이탈함
        if random.random() < 0.1:
            while True:
                m_ = random.randint(1, 4)
                # 랜덤하게 이동하게 하기 위해 기존의 방향과 다르게 하기 위해 반복
                if m_ != move:
                    move = m_
                    break

        if move == 6 :
            move = random.randint(1, 4)
        return move


    def move(self):  # 에이전트 이동
        # 1 : 동, 2 : 서, 3 : 남, 4 : 북

        step = self.decision_move()

        # 동서남북 이동에 대한 구현

        # 동쪽으로 이동
        if step == 1 :
            if not ((self.x + 1) >= len(field)):
                self.x += 1

        # 서쪽으로 이동
        elif step == 2 :
            if not ((self.x - 1) < 0):
                self.x -= 1

        # 남쪽으로 이동
        elif step == 3 :
            if not ((self.y + 1) >= len(field)):
                self.y += 1

        # 북쪽으로 이동
        elif step == 4 :
            if not ((self.y - 1) < 0):
                self.y -= 1

        # count_field[self.y][self.x] += 1


    # 에이전트가 골 지점에 도착할 경우
    def check_finish(self) -> bool :
        if field[self.y][self.x] == 2 :
            return True
        else :
            return False




def main() :
    ag = agent()

    for i in range(1000) :
        for _ in range(7) :
            ag.move()



        count_field[ag.y][ag.x] += 1

        ag.reset()

    # count_field[0][0] = 0
    # count_field[0][len(count_field) - 1] = 0
    # count_field[len(count_field) - 1][0] = 0
    # count_field[len(count_field) - 1][len(count_field) - 1] = 0

    count_field[len(count_field) // 2][len(count_field) // 2] = -1
    print(count_field)



main()
