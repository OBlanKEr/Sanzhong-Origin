import sys
total = 0

while True:
    try:
        count_sets = int(input ("喂！今天打算练几组？报个数，别磨磨蹭蹭的"))
        if count_sets > 0:
            print(f"行，今天就做着这{count_sets}组吧")
            break
    except ValueError:
        print("*不耐烦地敲了敲剑柄* 喂！你输的是什么鬼东西！老老实实输正整数，听不懂吗？！")

print("小tips：如果做不动就乱敲几个字母或者符号吧")
for i in range(1,count_sets + 1):
    while True:
        try:
            score = int(input(f"*抱着剑，挑了挑眉* 第{i}组，快点！拉了几个？"))
            if score < 0:
                print("做负数是什么鬼？认真点！")
                continue
            if score >= 0 and score <= 6:
                print(f"才{score}个，太少了吧！下一组给我使点劲！")
            else:
                print(f"做了{score}个，勉勉强强吧！")
            total += score
            break
        except ValueError:
            print("*眉头紧皱，一剑劈在旁边的木桩上* 哈？！这就练废了？真没出息！给我滚回去反省！")
            sys.exit()

if total >= count_sets * 8:
    print(f"*凑过来看了一眼你的记录，脸颊微红，别过头去* 哼，一共{total}个……勉强算你及格了吧。别得意，下次给老娘拉30个！")
else:
    print(f"*嫌弃地撇了撇嘴* 才{total}个？就这点力气还叫修行？赶紧给我滚去背单词，别在这浪费时间！")
