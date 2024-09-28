#from sys import stdin
#
#
#def points_cover_naive(starts, ends, points):
#    assert len(starts) == len(ends)
#    count = [0] * len(points)
#
#    for index, point in enumerate(points):
#        for start, end in zip(starts, ends):
#            if start <= point <= end:
#                count[index] += 1
#
#    return count
#
#
#if __name__ == '__main__':
#    data = list(map(int, stdin.read().split()))
#    n, m = data[0], data[1]
#    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
#    input_points = data[2 * n + 2:]
#
#    output_count = points_cover_naive(input_starts, input_ends, input_points)
#    print(*output_count)

def points_cover_optimized(starts, ends, points):
    events = []
    result = [0] * len(points)

    # Add segment start and end events
    for start in starts:
        events.append((start, 'L'))
    for end in ends:
        events.append((end, 'R'))

    # Add point events with their original index
    for i, point in enumerate(points):
        events.append((point, 'P', i))

    # Sort events: by value first, then by type ('L' < 'P' < 'R')
    # 'L' (start of a segment) should be processed before 'P' (point) to include segments starting at the point itself.
    # 'P' (point) should be processed before 'R' (end of a segment) to include the segments ending at the point itself.
    events.sort(key=lambda x: (x[0], x[1]))

    current_segments = 0
    
    for event in events:
        if event[1] == 'L':
            # Start of a segment
            current_segments += 1
        elif event[1] == 'R':
            # End of a segment
            current_segments -= 1
        elif event[1] == 'P':
            # A point event
            index = event[2]
            result[index] = current_segments
    
    return result

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    # Call optimized function
    output_count = points_cover_optimized(input_starts, input_ends, input_points)
    print(*output_count)
