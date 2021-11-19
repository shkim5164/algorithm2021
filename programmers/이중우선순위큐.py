import heapq
from collections import deque
def solution(operations):
    min_heap = []
    max_heap = []
    operations = deque(operations)
    while operations:
        cur_operation = operations.popleft()
        if cur_operation == "D 1":
            if max_heap and min_heap:
                del_num = heapq.heappop(max_heap)
                min_heap.remove(0 - del_num)
        elif cur_operation == "D -1":
            if max_heap and min_heap:
                del_num = heapq.heappop(min_heap)
                max_heap.remove(0 - del_num)
        else:
            split_list = cur_operation.split()
            insert_num = int(split_list[1])
            heapq.heappush(min_heap, insert_num)
            heapq.heappush(max_heap, 0 - insert_num)

    if min_heap and max_heap:
        return [0 - max_heap[0], min_heap[0]]

    return [0,0]