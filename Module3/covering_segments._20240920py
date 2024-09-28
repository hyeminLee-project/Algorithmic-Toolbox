from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    #선분을 오른쪽 끝을 기준으로 오름차순 정렬
    segments.sort(key=lambda s: s.end)
    points = []
    
    #현재 선택된 점
    current_point = None
    
    for segment in segments:
    # 현재 선택된 점이 해당 선분을 커버하지 못하는 경우
        if current_point is None or current_point < segment.start:
            # 새로운 점을 선택 (선분의 오른쪽 끝점)
            current_point = segment.end
            points.append(current_point)
    
    return points
    
    points = []
    # write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
