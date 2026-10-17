
from collections import deque

# =====================================
# 1. 輸入區（Input）
# =====================================

while True:
    try:
        n = int(input())
    except EOFError:
        break

    operations = []

    for _ in range(n):
        command, value = map(int, input().split())
        operations.append((command, value))


    # =====================================
    # 2. 核心邏輯區（Logic）
    # =====================================

    stack = []
    queue = deque()
    priority_queue = []

    is_stack = True
    is_queue = True
    is_priority_queue = True

    for command, value in operations:

        if command == 1:
            # 加入元素
            stack.append(value)
            queue.append(value)
            priority_queue.append(value)

        elif command == 2:

            # Stack：後進先出（LIFO）
            if not stack:
                is_stack = False
            else:
                if stack.pop() != value:
                    is_stack = False

            # Queue：先進先出（FIFO）
            if not queue:
                is_queue = False
            else:
                if queue.popleft() != value:
                    is_queue = False

            # Priority Queue：最大值優先
            if not priority_queue:
                is_priority_queue = False
            else:
                largest = max(priority_queue)
                priority_queue.remove(largest)

                if largest != value:
                    is_priority_queue = False


    # 判斷還有哪些資料結構符合
    possible = []

    if is_stack:
        possible.append("stack")

    if is_queue:
        possible.append("queue")

    if is_priority_queue:
        possible.append("priority queue")


    # =====================================
    # 3. 輸出區（Output）
    # =====================================

    if len(possible) == 0:
        print("impossible")

    elif len(possible) > 1:
        print("not sure")

    else:
        print(possible[0])
