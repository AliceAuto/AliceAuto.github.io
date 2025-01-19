money=5000
name=str(input())
def chaxun():
    print(f"当前余额为：{money}")
def cunkuan():
    print("请输入你需要存款的金额")
    qian=int(input())
    global money
    money=money+qian
    print(f"当前余额为：{money}")
def qukuan():
    print("请输入你需要去除的金额")
    qian=int(input())
    global money
    money=money-qian
    print(f"当前余额为:{money}")
def caidan():
    choice=int(input())
    while True:
        if choice ==1:
            chaxun()
            break
        elif  choice== 2:
            cunkuan()
            break
        elif  choice ==3:
            qukuan()
            break
        else:
            continue
caidan()




