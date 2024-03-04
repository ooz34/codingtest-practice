from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
       
    while len(prices)>1:
        current_price = prices.popleft()
        s = 0
        
        for price in prices:
            s += 1
            if current_price > price:
                break
        answer.append(s)
    
    answer.append(0)
    return answer      