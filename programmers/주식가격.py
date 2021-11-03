def solution(prices):
    time_check = [0 for _ in range(len(prices))]
    stack_price = []
    stack_index = []
    
    for index in range(len(prices)-1):
        now_price = prices[index]
        if stack_price:
            
            while stack_price and now_price < stack_price[-1]:
                stack_price.pop()
                stack_index.pop()
                
            stack_price.append(now_price)
            stack_index.append(index)
        else:
            stack_price.append(now_price)
            stack_index.append(index)
            
        for i in stack_index:
            time_check[i] += 1
        
    
    return time_check
