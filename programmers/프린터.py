from collections import deque

def solution(priorities, location):
    priorities = deque([ele for ele in enumerate(priorities)])
    answer = 0
    while priorities:
        current_por = priorities.popleft()
        filtered = list(filter(lambda x : x[1] > current_por[1], priorities))
        if filtered :
            priorities.append(current_por)
        else:
            answer += 1
            if current_por[0] == location:
                return answer