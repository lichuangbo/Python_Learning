cal_str = input('输入算式：')
cal_str_rep = cal_str.replace(' ', '')


def is_operator(ch):
    '''
    是否为运算符
    :param ch: char
    :return: True or False
    '''
    operator = ['+', '-', '*', '/', '(', ')', '=']
    if ch in operator:
        return True
    else:
        return False


def getStackPeek(stack):
    if len(stack) == 0:
        return -1
    else:
        return stack[len(stack) - 1]


def getprior(ch):
    '''
    取得operator的优先级
    :param ch: operator
    :return: 对应优先级
    '''
    operator_prio = {'(': 5, '*': 4, '/': 3, '+': 2, '-': 1, ')': 5, '=': 0}
    if ch in operator_prio:
        return operator_prio[ch]
    else:
        return -1


def calculate(a, b, operator):
    '''
    计算
    :param a:int
    :param b:int
    :param operator:operator
    :return: 计算结果
    '''
    result = 0
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a / b
    return result


def instack(str):
    '''
    1 + 2 * 3 =
    数字：
        入数字栈
    非数字(运算符)：
        如果运算符栈空：
            入栈
        如果优先级 > 栈顶优先级：
            入栈
        如果优先级 < 栈顶优先级：
            数字栈弹出俩数，运算符栈弹出栈顶；计算结果放入数字栈
        如果优先级 = 栈顶优先级：
            ()的情况，运算符栈弹栈顶，跳过此次循环读下一字符
    :param str:
    :return:
    '''
    num_stack = []
    oper_stack = []
    for e in str:
        is_oper = is_operator(e)
        if not is_oper:
            temp = int(e)
            num_stack.append(temp)
            continue
        else:
            while True:
                if len(oper_stack) == 0:
                    oper_stack.append(e)
                    break
                if getprior(getStackPeek(oper_stack)) < getprior(e):
                    oper_stack.append(e)
                    break
                elif getprior(getStackPeek(oper_stack)) > getprior(e):
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    op = oper_stack.pop()
                    num_stack.append(calculate(num1, num2, op))
                else:
                    oper_stack.pop()
                    break
    if getStackPeek(oper_stack) == '=':
        return getStackPeek(num_stack)
    # return num_stack, oper_stack


print(instack(cal_str_rep))


