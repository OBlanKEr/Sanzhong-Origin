__version__ = "0.1.0"

Knowledge_history = ("《战争与和平法》奠定了国际法的基础")
knowledge_philosophy = ("哲学不能为具体科学提供解决方法")

print("=========Hello,this is OBlanKEr Knowledge Engine.=========")
print("=========by OBLanKEr=========")
start = input("按1开始学习")
if start == "1" :
    if start == "1":
        print("历史按1，哲学按2，要加资料请乱按")
        while True:
            try:
                search = int(input("要什么？或者要加什么？"))
                if search == 1 :
                    print("找到了")
                    print(Knowledge_history)
                if search == 2 :
                    print("找到了")
                    print(knowledge_philosophy)
                if search not in {1,2} :
                    print("似乎没有")
            except ValueError:
                check = input("要加资料？是就按1，不是随便按")
                if check == "1" :
                    knowledge_addition_01 = input("输入资料")
                    print("输入成功")
                    Name_Knowledge_addition_01 = input("给资料加一个名字")
                    print("资料添加完成")
                    break

    if start == "1":
        print(f"历史按1，哲学按2，{Name_Knowledge_addition_01}按3，要加资料请乱按")
        while True:
            try:
                search = int(input("要什么？或者要加什么？"))
                if search == 1 :
                    print("找到了")
                    print(Knowledge_history)
                if search == 2 :
                    print("找到了")
                    print(knowledge_philosophy)
                if search == 3:
                    print("找到了")
                    print(knowledge_addition_01)
                if search not in {1,2,3} :
                    print("似乎没有")
            except ValueError:
                check = input("要加资料？是就按1，不是随便按")
                if check == "1" :
                    knowledge_addition_02 = input("输入资料")
                    print("输入成功")
                    Name_Knowledge_addition_02 = input("给资料加一个名字")
                    print("资料添加完成")
                    break

    if start == "1":
        print(f"历史按1，哲学按2，{Name_Knowledge_addition_01}按3，{Name_Knowledge_addition_02}按4，要加资料请乱按")
        while True:
            try:
                search = int(input("要什么？或者要加什么？"))
                if search == 1 :
                    print("找到了")
                    print(Knowledge_history)
                if search == 2 :
                    print("找到了")
                    print(knowledge_philosophy)
                if search == 3:
                    print("找到了")
                    print(knowledge_addition_01)
                if search == 4 :
                    print("找到了")
                    print(knowledge_addition_02)
                if search not in {1,2,3,4} :
                    print("似乎没有")
            except ValueError:
                check = input("要加资料？是就按1，不是随便按")
                if check == "1" :
                    knowledge_addition_03 = input("输入资料")
                    print("输入成功")
                    Name_Knowledge_addition_03 = input("给资料加一个名字")
                    print("资料添加完成")
                    break
else :
    print("不学吗？那依你")
