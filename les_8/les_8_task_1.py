# 1. На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

def hand_count(n):
    nodes = [i for i in range(1, n + 1)]
    edges = []

    for i in nodes:
        for j in range(i + 1, n + 1):
            edges.append((i, j))4

    print(f'Count shakes: {len(edges)}')
    print(f'Pair shakes: {edges}')


n = int(input('Enter hand shakes: '))
hand_count(n)
