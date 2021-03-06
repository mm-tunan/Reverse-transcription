###逆转录浓度计算

while 1:
    try:
        print("-----试用于逆转录20 ul体系，且酶的浓度为5x-----")
        reverse_system = int(input("反转录体系ul"))
        enzyme1 = int(input("gDNA去除酶体积："))
        enzyme2 = int(input("逆转录酶体积："))
        a = int(input("结果保留几位小数："))
        M = float(input("需要多少ng："))
        print("提示：浓度输入0，可以重新回到保留小数和需要ng输入界面！")
    except ValueError:
        print("请输入数字")
    else:
        while 1:
            try:
                n = float(input("浓度（ng/ul）："))
            except ValueError:
                print("请输入数字")
            else:
                if n > 0:
                    out = round(M/n,a)
                    solution = reverse_system - enzyme1 - enzyme2
                    if out > solution:
                        print("RNA浓度太低")
                    else:
                        print(f"RNA体积：{out}")
                        print(f"水：{solution-out}")
                else:
                    break