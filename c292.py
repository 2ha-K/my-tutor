
# =====================================
# 1. 輸入區（Input）
# =====================================

n = int(input())
direction = int(input())

# 建立二維陣列
grid = []

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)


# =====================================
# 2. 核心邏輯區（Logic）
# =====================================

# 四個方向：左、上、右、下
# direction: 0=左, 1=上, 2=右, 3=下
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

# 從陣列正中央開始
r = n // 2
c = n // 2

# 儲存走訪結果
result = [str(grid[r][c])]

# 每個方向要走幾步
steps = 1

# 總共要走訪 n*n 個位置
while len(result) < n * n:

    # 每兩個方向使用相同的移動步數
    for _ in range(2):

        # 沿著目前方向移動 steps 步
        for _ in range(steps):

            # 更新 row、column
            r += dr[direction]
            c += dc[direction]

            # 走出範圍代表邏輯有錯
            assert 0 <= r < n and 0 <= c < n, "超出陣列範圍"
            
            # 確認位置在陣列範圍內
            result.append(str(grid[r][c]))

            # 全部走訪完成
            if len(result) == n * n:
                break

        # 順時針轉向
        direction = (direction + 1) % 4

        if len(result) == n * n:
            break

    # 每走完兩個方向，步數 +1
    steps += 1


# =====================================
# 3. 輸出區（Output）
# =====================================

print("".join(result))
