# 輸入區域
# APCS 題目已明確規定輸入限制，不需要額外檢查
n = int(input())
scores = []

for _ in range(n):
    score = input().split()
    total = sum(map(int, score[2:]))
    score.append(total)
    scores.append(score)


# 邏輯區域

# 方法一：使用 Lambda
# 總分由高到低，總分相同時座號由小到大
scores.sort(key=lambda x: (-x[-1], int(x[0])))

# 方法二：使用 Function
# def mySort(x):
#     return (-x[-1], int(x[0]))
#
# scores.sort(key=mySort)


# 計算排名
rank = 1

for i in range(n):
    if i > 0 and scores[i][-1] != scores[i-1][-2]:
        rank = i + 1

    scores[i].append(rank)


# 輸出區域
for score in scores:
    print(" ".join(map(str, score)))