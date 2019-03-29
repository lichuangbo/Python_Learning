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


def pop(stack):
    if len(stack) == 0:
        return 0
    else:
        return stack.pop()


def getprior(ch):
    '''
    取得operator的优先级
    :param ch: operator
    :return: 对应优先级
    '''
    operator_prio = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1, ')': 3, '=': 0}
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


def cal(str):
    '''
    数字：
        入数字栈
    非数字(运算符)：
        如果运算符栈空：
            入栈
        如果栈顶运算符(：
		    如果当前运算符)：
		        弹栈
			否则:
				不用比较当前运算符直接入栈
        否则：
            如果优先级 > 栈顶优先级：
                ）：计算并压栈
                其他：弹栈
            如果优先级 < 栈顶优先级：
                数字栈弹出俩数，运算符栈弹出栈顶；计算结果放入数字栈
            如果优先级 = 栈顶优先级：
                ():弹栈
                +- or */: 计算并压栈
    :param str: string expression
    :return: result
    '''
    num_stack = []
    oper_stack = []
    for e in str:
        is_oper = is_operator(e)
        if not is_oper:
            temp = int(e)
            num_stack.append(temp)
        else:
            while True:
                if len(oper_stack) == 0:
                    oper_stack.append(e)
                if getStackPeek(oper_stack) == '(':
                    if e == ')':
                        oper_stack.pop()
                    else:
                        oper_stack.append(e)
                    break
                else:
                    if getprior(getStackPeek(oper_stack)) < getprior(e):
                        if e == ')':
                            num2 = pop(num_stack)
                            num1 = pop(num_stack)
                            op = pop(oper_stack)
                            num_stack.append(calculate(num1, num2, op))
                        else:
                            oper_stack.append(e)
                            break
                    elif getprior(getStackPeek(oper_stack)) > getprior(e):
                        num2 = pop(num_stack)
                        num1 = pop(num_stack)
                        op = pop(oper_stack)
                        num_stack.append(calculate(num1, num2, op))
                    else:
                        if getStackPeek(oper_stack) == '(':
                            oper_stack.pop()
                            break
                        else:
                            num2 = pop(num_stack)
                            num1 = pop(num_stack)
                            op = pop(oper_stack)
                            num_stack.append(calculate(num1, num2, op))
    result = getStackPeek(num_stack)
    num_stack.clear()
    oper_stack.clear()
    return result


if __name__ == '__main__':
    cal_str = input('输入算式：')
    cal_str_rep = cal_str.replace(' ', '')
    print(cal(cal_str_rep))
'''
测试数据：
3 * (6 - 2 * 2)= 6
(6-3 +(4/5) * (9-2*5/3 + 6 /3*9/4*2 +3 * 5/1 )) - (4*3)/ (6-3*1)= 22.733333333333334
6-3+4/5= 3.8
'''