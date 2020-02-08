info = """
===========
请选择操作
1. 查询余额
2. 存款
3. 取款
4. 退出
===========
"""

result = 999999999
number = 0

while number != 4:
    number = int(input(info))
    if number ==1:
        print('您当前所在账户余额为：',result)
    elif number ==2:
        money = int(input('请输入存款金额：'))
        result += money
    elif number ==3:
        require = int(input('请输入取款金额：'))
        if require > result:
            print('您当前所在账户余额不足！')
        else:
            result -= require
            print('您当前所在的账户已经取出', require, '元！')
    else:
        print('已退出！')
        break