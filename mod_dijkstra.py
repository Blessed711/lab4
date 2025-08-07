import heapq
from collections import defaultdict

# Функція solve обчислює мінімальні витрати на проїзд з міста 0 до міста n-1
def solve(n, prices, roads):
    # Створюємо список суміжності для графа
    adj = [[] for _ in range(n)]
    for u, v in roads:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    # dist[місто][бак][каністра] — мінімальна ціна, щоб потрапити в такий стан
    dist = [[[float('inf')] * 2 for _ in range(2)] for _ in range(n)]
    dist[0][0][0] = 0  # Починаємо з міста 0, бак порожній, каністри немає

    # Пріоритетна черга: (вартість, місто, бак, каністра)
    heap = [(0, 0, 0, 0)]

    while heap:
        cost, city, fuel, can = heapq.heappop(heap)

        # Якщо ми вже в останньому місті — повертаємо витрати
        if city == n - 1:
            return cost

        # Якщо вже є кращий шлях до цього стану — пропускаємо
        if dist[city][fuel][can] < cost:
            continue

        # Якщо бак порожній — можна купити бензин у бак
        if fuel == 0:
            new_cost = cost + prices[city]
            if new_cost < dist[city][1][can]:
                dist[city][1][can] = new_cost
                heapq.heappush(heap, (new_cost, city, 1, can))

        # Якщо каністри ще немає — можна купити бензин у каністру
        if can == 0:
            new_cost = cost + prices[city]
            if new_cost < dist[city][fuel][1]:
                dist[city][fuel][1] = new_cost
                heapq.heappush(heap, (new_cost, city, fuel, 1))

        # Якщо є каністра і бак порожній — можна перелити
        if can == 1 and fuel == 0:
            if cost < dist[city][1][0]:
                dist[city][1][0] = cost
                heapq.heappush(heap, (cost, city, 1, 0))

        # Якщо бак повний — можна поїхати в сусіднє місто
        if fuel == 1:
            for neighbor in adj[city]:
                if cost < dist[neighbor][0][can]:
                    dist[neighbor][0][can] = cost
                    heapq.heappush(heap, (cost, neighbor, 0, can))

    return -1  # Якщо добратись до останнього міста неможливо

# Зчитуємо кількість міст
n = int(input())

# Зчитуємо ціни на бензин у кожному місті
prices = list(map(int, input().split()))

# Зчитуємо кількість доріг і самі дороги
m = int(input())
roads = [tuple(map(int, input().split())) for _ in range(m)]

# Виводимо результат
print(solve(n, prices, roads))
