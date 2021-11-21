import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    last_days = deque([])

    for index in range(len(progresses)):
        days = math.ceil((100-progresses[index]) / speeds[index])
        last_days.append(days)

    queue = [last_days.popleft()]
    while last_days:
        cur_days = last_days.popleft()
        if queue[0] >= cur_days:
            queue.append(cur_days)
        else:
            answer.append(len(queue))
            queue = [cur_days]

        if not last_days:
            answer.append(len(queue))

    return answer