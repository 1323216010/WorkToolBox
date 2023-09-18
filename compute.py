
#统计Lead ACK I2C Fail
def getLeadFail(path):
    with open(path,'r') as f:  # 打开 txt 文件
        count_dict = {'Sweep1': 0, 'Sweep2': 0, 'Sweep3': 0}  # 用于统计 Sweep1~3 的计数字典
        Fail_judge = 0  # 判断第一个'Read ACK I2C Fail..'
        temp = 0
        for line in f:  # 逐行读取文件内容
            if temp != 0:
                temp += 1
            if 'Read ACK I2C Fail..' in line:  # 如果当前行包含目标子串
                Fail_judge = 1
                temp = 1
            else:
                if (
                        'Sweep3' in line or 'Sweep2' in line or 'Sweep1' in line) and Fail_judge == 1 and temp == 5:  # 更新最近一行中包含 Sweep1~3 子串的行
                    temp = 0
                    sweep_line = line.strip()  # 获取最近一行中包含 Sweep1~3 子串的行
                    if 'Sweep1 Fail' in sweep_line:  # 判断 Sweep 几
                        count_dict['Sweep1'] += 1  # 计数
                        Fail_judge = 0  # 判断完最近一个置零
                    elif 'Sweep2 Fail' in sweep_line:
                        count_dict['Sweep2'] += 1
                        Fail_judge = 0  # 判断完最近一个置零
                    elif 'Sweep3 Fail' in sweep_line:
                        count_dict['Sweep3'] += 1
                        Fail_judge = 0  # 判断完最近一个置零

    # 打印结果
    print(path, "  ", end="")
    for k, v in count_dict.items():
        print(f'{k}: {v} times', end=" | ")
    print()

#统计HVS ACK I2C Fail
def getHvsFail(path):
    with open(path, 'r') as f:  # 打开 txt 文件
        count_dict = {'Sweep1': 0, 'Sweep2': 0, 'Sweep3': 0}  # 用于统计 Sweep1~3 的计数字典
        Fail_judge = 0  # 判断第一个'Read ACK I2C Fail..'
        for line in f:  # 逐行读取文件内容
            if 'Read ACK I2C Fail..' in line:  # 如果当前行包含目标子串
                Fail_judge = 1
            else:
                if (
                        'Sweep3' in line or 'Sweep2' in line or 'Sweep1' in line) and Fail_judge == 1:  # 更新最近一行中包含 Sweep1~3 子串的行
                    sweep_line = line.strip()  # 获取最近一行中包含 Sweep1~3 子串的行
                    if 'Sweep1 Fail' in sweep_line:  # 判断 Sweep 几
                        count_dict['Sweep1'] += 1  # 计数
                        Fail_judge = 0  # 判断完最近一个置零
                    elif 'Sweep2 Fail' in sweep_line:
                        count_dict['Sweep2'] += 1
                        Fail_judge = 0  # 判断完最近一个置零
                    elif 'Sweep3 Fail' in sweep_line:
                        count_dict['Sweep3'] += 1
                        Fail_judge = 0  # 判断完最近一个置零

    # 打印结果
    print(path, "  ", end="")
    for k, v in count_dict.items():
        print(f'{k}: {v} times', end=" | ")
    print()