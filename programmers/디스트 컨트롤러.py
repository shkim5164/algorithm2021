import heapq

def solution(jobs):
    time = 0
    start = -1
    total_sum = 0
    cnt = 0

    N_jobs = len(jobs)
    filtered_request = []
    while cnt < len(jobs):
        # 요청 시간이 현재 time 이하 인 것
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(filtered_request, (job[1], job[0]))

        if filtered_request:
            # 소요시간이 제일 작은 것
            smallest = heapq.heappop(filtered_request)
            start = time
            time += smallest[0]
            total_sum += (time - smallest[1])
            cnt += 1
        else:
            time += 1

    return total_sum // len(jobs)
