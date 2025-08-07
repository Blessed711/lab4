# Функція для знаходження кореня множини (з компресією шляху)
def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

# Функція об’єднання двох множин за рангом
def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u == root_v:
        return False  # Вони вже в одній компоненті — не об’єднуємо (щоб не утворити цикл)
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    else:
        parent[root_v] = root_u
        if rank[root_u] == rank[root_v]:
            rank[root_u] += 1
    return True

# Алгоритм Крускала для пошуку MST
def kruskal(n, edges):
    parent = list(range(n))  # Ініціалізуємо батьківський масив
    rank = [0] * n           # Ініціалізуємо ранги
    edges.sort()             # Сортуємо ребра за вагою
    mst_weight = 0           # Загальна вага MST
    count = 0                # Кількість включених ребер

    for w, u, v in edges:
        if union(parent, rank, u, v):
            mst_weight += w
            count += 1
            if count == n - 1:  # Якщо вже є n - 1 ребро — MST завершено
                break

    return mst_weight

# Зчитування кількості вершин n і кількості ребер m
n, m = map(int, input().split())
edges = []

# Зчитування ребер: (u, v, w), з переходом до 0-індексації
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u - 1, v - 1))  # Важливо: w першим для сортування

# Виведення загальної ваги мінімального остового дерева
print(kruskal(n, edges))
