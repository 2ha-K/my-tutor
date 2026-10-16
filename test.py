#輸入值區域
k = int(input())
a = input()

#因為不管大小寫都要轉成0或1，所以先將字串轉成0或1的list
ori = []
for c in a:
    if c>='A' and c<='Z':
        ori.append(0)
    elif c>='a' and c<='z':
        ori.append(1)
print(ori)

#將連續的0或1分段，並計算每段的長度
seg = []
num = ori[0]
count = 0
for i in ori:
    if i == num:
        count += 1
    else:
        seg.append(count)
        num = i
        count = 1
seg.append(count)
print(seg)


# 1.我觀察到的是只要是有k或者連續是k的話+或前後大於k那就是一組。最後我們來看哪一組最大
# 2.先找到所有的k片段
k_seg = []
isStart = True
start = 0
end = 0
for i in range(1, len(seg)):
    if isStart:
        if seg[i-1]==k:
            start = i-1
            isStart = False
    if not isStart:
        if seg[i]!=k:
            end = i-1
            isStart = True
            k_seg.append((start,end))
        elif i == len(seg)-1:
            end = i
            k_seg.append((start,end))

print(k_seg)

#3. 算出每個片段延伸後的值取最大
length = 0
for start, end in k_seg:
    num = end-start+1
    ori_length = num*k
    if start>0 and seg[start-1]>=k:
        ori_length+=k
    if end < len(seg)-1 and seg[end+1]>=k:
        ori_length+=k
    length = max(ori_length, length)

print(length)
             



