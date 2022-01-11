from collections import deque

def solution(cacheSize, cities):
    answer = 0
    lru = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city not in lru:
            answer += 5
        else:
            lru.remove(city)
            answer += 1
        lru.append(city)
    return answer

print( solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))