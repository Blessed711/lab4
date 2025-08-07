import heapq
from collections import defaultdict

# Функція для знаходження мінімального часу, щоб дістатись з міста a в місто b
def find_min_time(n, a, b, buses):
    graph = defaultdict(list)  # Створюємо граф у вигляді списку суміжності

    # Заповнюємо граф. Для кожного міста s додаємо маршрут до міста t з відправленням f і прибуттям tf
    for s, t, f, tf in buses:
        graph[s].append((f, t, tf))  # f — час відправлення, tf — час прибуття

    dist = [float('inf')] * (n + 1)  # Масив для збереження мінімального часу до кожного міста
    dist[a] = 0                      # Час до стартового міста дорівнює 0

    heap = [(0, a)]  # Черга з пріоритетами (час, місто), починаємо з міста a

    while heap:
        time, city = heapq.heappop(heap)  # Виймаємо місто з найменшим часом

        if time > dist[city]:
            continue  # Пропускаємо, якщо вже маємо кращий шлях

        # Перебираємо всі рейси з поточного міста
        for dep_time, to, arr_time in graph[city]:
            if dep_time >= time and arr_time < dist[to]:  # Якщо можна сісти на цей автобус
                dist[to] = arr_time
                heapq.heappush(heap, (arr_time, to))  # Додаємо у чергу з новим часом

    # Якщо можна дістатись до міста b — повертаємо час, інакше -1
    return dist[b] if dist[b] != float('inf') else -1


# Зчитування вхідних даних
n = int(input())                          # Кількість міст
a, b = map(int, input().split())          # Стартове та кінцеве місто
r = int(input())                          # Кількість автобусів
buses = [tuple(map(int, input().split())) for _ in range(r)]  # Інформація про автобуси

# Виводимо результат
print(find_min_time(n, a, b, buses))
