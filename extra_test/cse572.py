import json

with open("preprocess_dataset.jsonl", encoding="utf-8") as f:
    data = [json.loads(line) for line in f]

# 第一筆資料的所有頂層欄位
print(data[0].keys())
print("Number of fields:", len(data[0]))

# 整個 Dataset 出現過的所有頂層欄位
all_fields = set()

for item in data:
    all_fields.update(item.keys())

print("All fields:", sorted(all_fields))
print("Total unique fields:", len(all_fields))
print(data[0]["commit_to_review"].keys())