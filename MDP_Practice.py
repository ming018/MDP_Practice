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

        if move == 6:
            move = random.randint(1, 4)
        return move

    def move(self):  # 에이전트 이동
        # 1 : 동, 2 : 서, 3 : 남, 4 : 북

        step = self.decision_move()

        # 동서남북 이동에 대한 구현

        # 동쪽으로 이동
        if step == 1:
            if not ((self.x + 1) >= len(field)):
                self.x += 1

        # 서쪽으로 이동
        elif step == 2:
            if not ((self.x - 1) < 0):
                self.x -= 1

        # 남쪽으로 이동
        elif step == 3:
            if not ((self.y + 1) >= len(field)):
                self.y += 1

        # 북쪽으로 이동
        elif step == 4:
            if not ((self.y - 1) < 0):
                self.y -= 1

        # count_field[self.y][self.x] += 1

    # 에이전트가 골 지점에 도착할 경우
    def check_finish(self) -> bool:
        if field[self.y][self.x] == 2:
            return True
        else:
            return False


def main():
    ag = agent()

    count = 5000

    for i in range(count):
        for _ in range(7):
            ag.move()

        count_field[ag.y][ag.x] += 1

        ag.reset()

    # 각 상태를 % 형태로 변경
    for i in range(len(count_field)):
        for k in range(len(count_field)):
            count_field[i][k] = count_field[i][k] / count * 100

    count_field[len(count_field) // 2][len(count_field) // 2] = -1

    print(count_field)


main()

# import random
#
# # 필드, 0 = 이동 가능 구역, 1 = 에이전트 위치, 2 = 골 지점
# field = [[2, 0, 0, 0, 0, 0, 0, 0, 2],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 1, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [2, 0, 0, 0, 0, 0, 0, 0, 2]]
#
# # 보상
# rew1 = -0.9
# rew2 = -0.7
# rew3 = -0.5
# rew4 = -0.3
# rew5 = -0.1
#
# # 사전에 정의된 최적 경로 5 목표지점, 6 에이전트 위치
# optimal_route = [[5, 2, 2, 2, 2, 1, 1, 1, 5],
#                  [4, 2, 4, 2, 4, 1, 4, 1, 4],
#                  [4, 4, 2, 4, 2, 4, 1, 4, 4],
#                  [4, 2, 4, 2, 4, 1, 4, 1, 4],
#                  [4, 4, 2, 4, 6, 3, 1, 3, 3],
#                  [3, 2, 3, 2, 2, 1, 3, 1, 3],
#                  [3, 3, 2, 3, 3, 3, 1, 3, 3],
#                  [3, 2, 3, 2, 2, 1, 3, 1, 3],
#                  [5, 2, 2, 2, 1, 1, 1, 1, 5]]
#
# # 각 필드별 보상 구조
# field_rew = [[0, rew4, rew2, rew1, rew3, rew4, rew1, rew2, 0],
#              [rew5, rew3, rew4, rew2, rew4, rew5, rew2, rew1, rew4],
#              [rew2, rew5, rew5, rew3, rew1, rew2, rew3, rew2, rew5],
#              [rew3, rew4, rew1, rew4, rew5, rew4, rew5, rew5, rew1],
#              [rew4, rew1, rew3, rew5, -1, rew5, rew1, rew3, rew2],
#              [rew1, rew2, rew5, rew2, rew2, rew3, rew4, rew1, rew3],
#              [rew2, rew5, rew2, rew1, rew3, rew2, rew3, rew4, rew5],
#              [rew3, rew2, rew3, rew3, rew4, rew1, rew5, rew5, rew2],
#              [0, rew1, rew4, rew5, rew2, rew5, rew2, rew1, 0]]
#
# field = [[2, 0, 0, 0, 0, 0, 0, 0, 2],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 8, 1, 8, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [2, 0, 0, 0, 0, 0, 0, 0, 2]]
#
#
#
#
# # 에이전트 클래스. 위치 초기화, 이동 함수
# class agent():
#     def __init__(self):  # 생성자, 필드 중앙에 위치
#         self.x = len(field_rew) // 2
#         self.y = len(field_rew) // 2
#         field[self.y][self.x] = 1
#
#     def set(self):  # 첫번째 시도 이후, 에이전트 위치 초기화
#         field[self.y][self.x] = 1
#
#     def decision_append(self):
#
#         move_decision = []
#
#         if not ((ag.x + 1) >= len(field_rew)):  # 에이전트 동쪽 방향 보상 추가
#             move_decision.append(field_rew[ag.y][ag.x + 1])
#         else:
#             move_decision.append(field_rew[ag.y][ag.x])
#
#         if ag.x != 0:  # 에이전트 서쪽 방향 보상 추가
#             move_decision.append(field_rew[ag.y][ag.x - 1])
#         else:
#             move_decision.append(field_rew[ag.y][ag.x])
#
#         if not ((ag.y + 1) >= len(field_rew)):  # 에이전트 남쪽 방향 보상 추가
#             move_decision.append(field_rew[ag.y + 1][ag.x])
#         else:
#             move_decision.append(field_rew[ag.y][ag.x])
#
#         if ag.y != 0:  # 에이전트 북쪽 방향 보상 추가
#             move_decision.append(field_rew[ag.y - 1][ag.x])
#         else:
#             move_decision.append(field_rew[ag.y][ag.x])
#
#         print('move_decision : ', move_decision)
#         # 동서남북 방향으로 보상값을 추가 하고, 그 추가된 값 중 가장 큰 값의 방향을 리턴
#         return move_decision.index(max(move_decision)) + 1
#
#     def move(self):  # 에이전트 이동
#         # 1 : 동, 2 : 서, 3 : 남, 4 : 북
#
#         m = self.decision_append()
#         m_ = 0
#
#         rand = random.random()
#         print(rand)
#         # 30%의 확률로 에이전트의 동서남북 방향중 보상이 가장큰 방향의 이동을 변경
#         if rand < 0.0:
#             print('m이 변경됌')
#             while True:
#                 m_ = random.randint(1, 4)
#                 # 랜덤하게 이동하게 하기 위해 기존의 방향과 다르게 하기 위해 반복
#                 if m_ != m:
#                     m = m_
#                     break
#
#         # 동서남북 이동에 대한 구현
#
#         print('m : ', m, 'm_ : ', m_)
#
#         field[self.y][self.x] = 3
#
#         # 동쪽으로 이동
#         if m == 1 :
#             if not ((self.x + 1) >= len(field_rew)):
#                 self.x += 1
#
#         # 서쪽으로 이동
#         elif m == 2 :
#             if not ((self.x - 1) < 0):
#                 self.x -= 1
#
#         # 남쪽으로 이동
#         elif m == 3 :
#             if not ((self.y + 1) >= len(field_rew)):
#                 self.y += 1
#
#         # 북쪽으로 이동
#         elif m == 4 :
#             if not ((self.y - 1) < 0):
#                 self.y -= 1
#
#         field[self.y][self.x] = 1
#
#
#
# ag = agent()
# print(ag.x, ag.y)
# for i in range(len(field)):
#     print(field[i])
#
# for k in range(10):
#     print('--------------------------------------')
#     print((k + 1), '번째 실행')
#     ag.move()
#     print(ag.x, ag.y)
#     for i in range(len(field)):
#         print(field[i])
#
# # 보상이 높은 곳을 70%의 확률로 이동을 구현
