from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    #출발 지점과 도착 지점 사이의 거리를 포함하기 위해  `stops` 리스트에 0(출발점)과 `distance`(도착점)를 추가
    stops = [0] + stops + [distance]
    num_refills = 0 #주유 횟수
    current_position = 0 # 현재 위치를 가리키는 인덱스 
    
    while current_position < len(stops) - 1:
        last_position = current_position #현재 위치를 저장 
        
        #다음 위치를 찾음: 현재 위치에서 최대 주행 거리 내에 있는 가장 먼 주유소로 이동
        while (current_position < len(stops) - 1 and 
            stops[current_position + 1] - stops[last_position] <= tank):
            current_position += 1
            
        #현재 위치에서 이동할 수 없는 경우, 목적지에 도달할 수 없음
        if current_position == last_position:
            return -1
        
        #도착하지 않았고. 이동한 위치가 출발 지점이 아닌 경우 주유 횟수 추가
        if current_position < len(stops) -1:
            num_refills += 1
        
    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
