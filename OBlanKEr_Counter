total = 0

while True:
    try:
        div = int(input("你的除数是什么？"))
        if div == 0:
            print("除数不能为0！")
            continue
        break
    except ValueError:
        print("请输入数字！")

while True:
    check_ans = input("请问你的被除数是否有几个数的相加？请回答是或否")
    if check_ans in ["是", "否"]:
        break
    print("请回答是或否！！！！！！！！！！！")

if check_ans == "是":
    while True:
        try:
            count = int(input("请问有几个数？"))
            if count == 0:
                print("个数不能为0！！！")
                continue
            break
        except ValueError:
            print("请输入数字！")

    for _ in range(count):
        while True:
            try:
                score = int(input("输入你的数字"))
                break
            except ValueError:
                print("请输入数字！")
        total += score

else:
    while True:
        try:
            score_01 = int(input("输入你的数字"))
            total += score_01
            break
        except ValueError:
            print("请输入数字！！！！！！！")

print("最终值为", total / div)
