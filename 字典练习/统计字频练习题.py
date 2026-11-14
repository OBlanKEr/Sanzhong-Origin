#统计字频练习题
text = input("输入一句话")#输入原字符串

counts = {}#创建空字典

for ch in text:
    counts[ch] = counts.get(ch,0) + 1#计数，每遇到一个相同字就加1

print("每一个字出现的次数：")
for ch,num in counts.items():
    print(f"{ch}：{num}次")