import math
import heapq

# Функція прима для побудови мінімального каркасу в повнозв'язному графі (на площині)
def prim(points):
    n = len(points)  # Кількість точок
    used = [False] * n  # Масив для позначення використаних вершин
    min_edge = [float('inf')] * n  # Мінімальна вага ребра до кожної вершини
    min_edge[0] = 0.0  # Починаємо з вершини 0
    heap = [(0.0, 0)]  # Купа: (вага ребра, номер вершини)
    total_weight = 0.0  # Підсумкова вага каркасу

    # Основний цикл алгоритму Прима
    while heap:
        cost, u = heapq.heappop(heap)  # Беремо вершину з найменшим ребром
        if used[u]:
            continue
        used[u] = True  # Позначаємо як використану
        total_weight += cost  # Додаємо вартість ребра до результату

        # Оновлюємо ваги ребер для сусідів
        for v in range(n):
            if not used[v]:
                dist = math.hypot(points[u][0] - points[v][0], points[u][1] - points[v][1])  # Евклідова відстань
                if dist < min_edge[v]:
                    min_edge[v] = dist
                    heapq.heappush(heap, (dist, v))  # Додаємо нову вагу ребра в купу

    return total_weight

# Зчитуємо кількість точок
n = int(input())

# Зчитуємо координати точок
points = [tuple(map(int, input().split())) for _ in range(n)]

# Обчислюємо довжину мінімального остового дерева і виводимо результат з точністю до 5 знаків
print(f"{prim(points):.5f}")
