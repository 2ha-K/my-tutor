#輸入區域
#如果過於忘記我們可以把題目複製上方便對照
"""
r= row, c=column, m=選取操作的數字
"""
r, c, m = map(int, input().split())
#建立我們的矩陣
matrics = []
for i in range(r):
    column = list(map(int, input().split()))
    matrics.append(column)
# print(matrics) #確認矩陣正確

#建立選取操作樣式
"""
只是要依序取出 / 拆給變數 → map() 就夠了。
之後還要 [0]、sort、反覆操作 → 轉成 list(map(...))。
"""
operations = list(map(int, input().split()))


#建議:每個def都可以分開先測試再組合

#使用def將問題拆開
#建立顛倒的方式，如果題目沒有要求的話創立新的矩陣來接收往往比較簡單
def opposite(matrics):
    new_matirc = []
    new_matirc = matrics[::-1]

    return new_matirc


# #建立旋轉方式，抽取每個row的第一個塞入new矩陣
def span(matrics):
    global c
    global r
    new_matirc = []
    for i in range(c):
        new_row = []
        for j in range(r):
            new_row.append(matrics[j][i])
        new_matirc.append(new_row[::-1])
    temp = r
    r = c
    c = temp
    return new_matirc
# print(span(matrics))
        
#操作
for operation in operations:
    if operation == 1:
        matrics = opposite(matrics)
    elif operation ==0:
        matrics = span(matrics)

#列印
print(r, c)
for row in matrics:
    print(" ".join(map(str, row)))

