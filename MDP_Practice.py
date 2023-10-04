import random

# 필드, 0 = 이동 가능 구역, 1 = 에이전트 위치, 2 = 골 지점
field = [[2, 0, 0, 0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [2, 0, 0, 0, 0, 0, 0, 0, 2]]

# 보상
rew1 = -0.9
rew2 = -0.7
rew3 = -0.5
rew4 = -0.3
rew5 = -0.1

# 각 필드별 보상 구조
field_rew = [[0, rew4, rew2, rew1, rew3, rew4, rew1, rew2, 0],
             [rew5, rew3, rew4, rew2, rew4, rew5, rew2, rew1, rew4],
             [rew2, rew5, rew5, rew3, rew1, rew2, rew3, rew2, rew5],
             [rew3, rew4, rew1, rew4, rew5, rew4, rew5, rew5, rew1],
             [rew4, rew1, rew3, rew5, -1, rew5, rew1, rew3, rew2],
             [rew1, rew2, rew5, rew2, rew2, rew3, rew4, rew1, rew3],
             [rew2, rew5, rew2, rew1, rew3, rew2, rew3, rew4, rew5],
             [rew3, rew2, rew3, rew3, rew4, rew1, rew5, rew5, rew2],
             [0, rew1, rew4, rew5, rew2, rew5, rew2, rew1, 0]]


# 에이전트 클래스. 위치 초기화, 이동 함수
class agent():
    def __init__(self):  # 생성자, 필드 중앙에 위치
        self.x = len(field_rew) // 2
        self.y = len(field_rew) // 2
        field[self.y][self.x] = 1

    def set(self):  # 첫번째 시도 이후, 에이전트 위치 초기화
        field[self.y][self.x] = 1

    def decision_append(self):

        move_decision = []

        if not ((ag.x + 1) >= len(field_rew)):  # 에이전트 동쪽 방향 보상 추가
            move_decision.append(field_rew[ag.y][ag.x + 1])
        else:
            move_decision.append(field_rew[ag.y][ag.x])

        if ag.x != 0:  # 에이전트 서쪽 방향 보상 추가
            move_decision.append(field_rew[ag.y][ag.x - 1])
        else:
            move_decision.append(field_rew[ag.y][ag.x])

        if not ((ag.y + 1) >= len(field_rew)):  # 에이전트 남쪽 방향 보상 추가
            move_decision.append(field_rew[ag.y + 1][ag.x])
        else:
            move_decision.append(field_rew[ag.y][ag.x])

        if ag.y != 0:  # 에이전트 북쪽 방향 보상 추가
            move_decision.append(field_rew[ag.y - 1][ag.x])
        else:
            move_decision.append(field_rew[ag.y][ag.x])

        print('move_decision : ', move_decision)
        # 동서남북 방향으로 보상값을 추가 하고, 그 추가된 값 중 가장 큰 값의 방향을 리턴
        return move_decision.index(max(move_decision)) + 1

    def move(self):  # 에이전트 이동
        # 1 : 동, 2 : 서, 3 : 남, 4 : 북

        m = self.decision_append()
        m_ = 0

        rand = random.random()
        print(rand)
        # 30%의 확률로 에이전트의 동서남북 방향중 보상이 가장큰 방향의 이동을 변경
        if rand < 0.9:
            while True:
                m_ = random.randint(1, 4)
                # 랜덤하게 이동하게 하기 위해 기존의 방향과 다르게 하기 위해 반복                    m_ = random.randint(1, 4)
                if m_ != m:
                    break

        # 동서남북 이동에 대한 구현

        print('m : ', m, 'm_ : ', m_)

        field[self.y][self.x] = 3

        # 동쪽으로 이동
        if m == 1 or m_ == 1:
            if not ((self.x + 1) >= len(field_rew)):
                self.x += 1

        # 서쪽으로 이동
        if m == 2 or m_ == 2:
            if not ((self.x - 1) < 0):
                self.x -= 1

        # 남쪽으로 이동
        if m == 3 or m_ == 3:
            if not ((self.y + 1) >= len(field_rew)):
                self.y += 1

        # 북쪽으로 이동
        if m == 4 or m_ == 4:
            if not ((self.y - 1) < 0):
                self.y -= 1

        field[self.y][self.x] = 1


ag = agent()
print(ag.x, ag.y)
for i in range(len(field)):
    print(field[i])

for k in range(10):
    print('--------------------------------------')
    print((k + 1), '번째 실행')
    ag.move()
    print(ag.x, ag.y)
    for i in range(len(field)):
        print(field[i])

# 보상이 높은 곳을 70%의 확률로 이동을 구현
