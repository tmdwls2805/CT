n = 1250 # 거스름돈
count = 0 # 동전 개수를 센다
coin_num = [500, 100, 50, 10] # 거스를 돈의 종류를 list값안에 넣는다

# list안의 값 만큼 돌림
for coin in coin_num:
    # count = 0
    count += n // coin # 1260원에서 500원으로 나눈 후 나눈 값을 count에 저장
    n %= coin # 나머지 값 출력
    # print('coin_type : ', coin, 'coin_count : ', count) # 코인의 종류별 개수를 출력

print(count) # 코인의 최소 개수를 출력
# 코인을 종류대로 뽑아보세요.
