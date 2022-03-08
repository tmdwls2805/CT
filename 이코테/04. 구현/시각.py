#삼중 나생문이면 그냥 끝남
h = int(input())
count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 이거는 그냥 문자열에 3이 존재한다면 count하게 하는 것임(간단)
            # 초반엔 int형을 list안에 넣어서 다 character 단위로 쪼개서 3이 존재하면 count하게 하려고 짜려했으나 미치도록 비효율적이라 다시 생각해보니
            # 문자열 사용하면 됐음...
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)