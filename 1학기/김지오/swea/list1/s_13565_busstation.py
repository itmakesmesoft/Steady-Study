T = int(input())

for tc in range(1, T+1):
    K, N, M = map( int, input().split())
    stations = [0]* (N+K+1) #버스정류장 위치표시
    station_numbers = list(map(int, input().split()))
    #station에 위치표시
    for i in range(M):
        stations[station_numbers[i]] = 1

    current_station = 0 #지금 버스가 있는 위치
    charge_times = 0 #충전횟수
    flag =0

    while current_station <= N:
        battery = K
        for t in range(K, 0, -1):
            if stations[current_station+t] == 1:
                current_station += t
                charge_times += 1
                break
                #범위 안에 있으면 충전횟수+1, 지금 역 위치 바꾸기
            # elif current_station+t >= N:
            #     break
            #     #끝까지 가면은 break
            else:
                battery -= 1
                #아니면은 battery에서 1빼고 다시 for문 돌기
            if current_station >= N - K:
                #마지막까지 갈수 있는 station에 도달한경우
                flag = 1
                break
            elif battery == 0:
                #배터리가 떨어진 경우
                flag = 1
                #그동안 온거 초기화하고 0 입력
                charge_times = 0
                break
        if flag:
            break

    print(f'#{tc} {charge_times}')

