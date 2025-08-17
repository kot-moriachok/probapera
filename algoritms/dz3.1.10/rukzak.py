def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

#Проверяем функцию на работоспособность

weights = [1, 2, 3]
values = [6, 10, 12]
capacity = 5
print("Рюкзак", knapsack(weights, values, capacity))  # Ожидаемый результат: 22

def lcs_length(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

#Проверяем
str1 = "abcde"
str2 = "ace"
print("LCS функция:",lcs_length(str1, str2))

def count_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n]

#проверяем
n = 4
print("Коинт", count_partitions(n))  # Ожидаемый результат: 5
# Разбиения: 4; 3+1; 2+2; 2+1+1; 1+1+1+1


def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] =  dist[i][k] + dist[k][j]
    return dist

#проверяем
graph = [
    [0, 3, float('inf'), 7],
    [8,0 , 2, float('inf')],
    [5, float('inf'),0 , 1],
    [2, float('inf'), float('inf'), ]
]
dist = floyd_warshall(graph)
for row in dist:
    print("Флойд:" , row)
