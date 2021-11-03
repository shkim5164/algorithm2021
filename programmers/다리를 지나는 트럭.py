from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    time = 0
    sum_bridge = 0 # sum() 함수로 구현하면 테스트 케이스 1개에서 시간 초과가 걸린다.

    while trucks:
        time += 1
        done = bridge.popleft()
        sum_bridge -= done

        if trucks and sum_bridge + trucks[0] <= weight:
            next_truck = trucks.popleft()
            if len(trucks) == 0:
                time += bridge_length
                break
            bridge.append(next_truck)
            sum_bridge += next_truck
        else:
            bridge.append(0)

    return time