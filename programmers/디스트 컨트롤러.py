import heapq
import math
def solution(jobs):
    time = 0
    total_sum = 0
    # 요청 시간이 현재 time 이하 인 것 
    
    N_jobs = len(jobs)
    
    while jobs:
        request_index = [(jobs[i][0], i) for i in range(len(jobs))]
        # 요청 시간이 현재 time 이하 인 것
        filtered_request_index = list(filter(lambda x : x[0] <= time, request_index))
        heapq.heapify(filtered_request_index)
        
        if filtered_request_index:
            usedtime_list = []
            for filtered_request in filtered_request_index:
                current_job = jobs[filtered_request[1]]
                usedtime_list.append((time + current_job[1] - current_job[0], filtered_request[1]))
            
            # 소요시간이 제일 작은 것
            heapq.heapify(usedtime_list)
            final = usedtime_list[0]
            
            final_index = final[1]
            final_time = jobs[final_index][1]
            final_request = jobs[final_index][0]
            total_sum += (final[0])
            time += final_time
            del jobs[final_index]    
        else:
            final = jobs[0]
            final_request = final[0]
            final_time = final[1]
            total_sum += (time + final_time - final_request)
            time += final_time
            del jobs[0]
        
        
    return math.floor(total_sum / N_jobs)