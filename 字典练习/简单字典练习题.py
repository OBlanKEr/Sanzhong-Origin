#练习题
scores = {"何意味":78,
          "合味道":13,
          "意味何":91
}#字典内容

while True:
    check = input("要谁的分数？")
    if check == "退出" :#永远先检查用户有没有元指令，再检查用户需要程序干什么
        print("好的")
        break
    try:
        if check == "add":
            name = input("名字：")
            score = int(input("分数："))
            scores[name] = score#翻译成自然语言：在"scores"这个字典，找到（没有就新建）name然后把score加进去
            print("添加成功，为你打印包ing")
            for key,value in scores.items():#用户输入完之后给出全部字典，方便用户查看已经有了什么内容
                print(f"{key}:{value}分")
                print("打印完成")
                continue#进行完添加模块，记住要continue结束后续代码返回循环开头
    except ValueError:
            print("输入正确分数")

    if check in scores:     #输出
        print(scores[check])#格式

    if check not in scores:
        print("查无此人")
