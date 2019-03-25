import tkinter

# 窗体设置
calculator = tkinter.Tk()
calculator.title("软件工程---计算器")
calculator.minsize(280, 410)
calculator.maxsize(280, 410)

# 全局变量
his_val = ''
ans_val = ''
show_his = ''
show_ans = ''
ans_temp_num = ''
ans_temp_sign = ''
flag_point = True

# 历史纪录
display_his = tkinter.StringVar()
display_his.set(show_his)

# 结果显示
display_ans = tkinter.StringVar()
display_ans.set(0)

# --显示历史纪录
laber1 = tkinter.Label(calculator, font=('微软雅黑', 20), bg='#94d6da', bd='9', fg='#828282', anchor='se',textvariable=display_his)
laber1.place(x=0, y=0, width=280, height=60)

# --显示答案
label2 = tkinter.Label(calculator, font=('微软雅黑', 20), bg='#94d6da', bd='9', fg='white', anchor='se',textvariable=display_ans)
label2.place(x=0, y=60, width=280, height=72)

# ---------按钮
btn_his = tkinter.Button(calculator, text='', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
btn_his.place(x=0, y=135, width=280, height=0)

# 第一行

btn_c = tkinter.Button(calculator, text='AC', font=('微软雅黑', 20), fg=('#feaf17'), bd=0.5, command=lambda: pressC())
btn_c.place(x=5, y=135, width=105, height=50)

btn_remove = tkinter.Button(calculator, text='←', font=('微软雅黑', 20), fg=('#feaf17'), bd=0.5, command=lambda: pressRM())
btn_remove.place(x=115, y=135, width=50, height=50)

btn_chu = tkinter.Button(calculator, text='/', font=('微软雅黑', 20), fg=('#94d6da'), bd=0.5,command=lambda: pressCompute('/'))
btn_chu.place(x=170, y=135, width=50, height=50)

btn_zk = tkinter.Button(calculator, text='(', font=('微软雅黑', 20), fg=('#94d6da'), bd=0.5,command=lambda: press_('('))
btn_zk.place(x=225, y=135, width=50, height=50)

# 第二行

btn_7 = tkinter.Button(calculator, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('7'))
btn_7.place(x=5, y=190, width=50, height=50)

btn_8 = tkinter.Button(calculator, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('8'))
btn_8.place(x=60, y=190, width=50, height=50)

btn_9 = tkinter.Button(calculator, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('9'))
btn_9.place(x=115, y=190, width=50, height=50)

btn_che = tkinter.Button(calculator, text='*', font=('微软雅黑', 20), fg=('#94d6da'), bd=0.5, command=lambda: pressCompute('*'))
btn_che.place(x=170, y=190, width=50, height=50)

btn_yk = tkinter.Button(calculator, text=')', font=('微软雅黑', 20), fg=('#94d6da'), bd=0.5, command=lambda: press_(')'))
btn_yk.place(x=225, y=190, width=50, height=50)

# 第三行

btn_4 = tkinter.Button(calculator, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('4'))
btn_4.place(x=5, y=245, width=50, height=50)

btn_5 = tkinter.Button(calculator, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('5'))
btn_5.place(x=60, y=245, width=50, height=50)

btn_6 = tkinter.Button(calculator, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('6'))
btn_6.place(x=115, y=245, width=50, height=50)

btn_jian = tkinter.Button(calculator, text='-', font=('微软雅黑', 20), fg=('#94d6da'), bd=0.5,command=lambda: pressCompute('-'))
btn_jian.place(x=170, y=245, width=50, height=50)

btn_point = tkinter.Button(calculator, text='.', font=('微软雅黑', 20), fg=('#94d6da'), bd=0.5,command=lambda: pressPoint())
btn_point.place(x=225, y=245, width=50, height=50)

# 第四行

btn_1 = tkinter.Button(calculator, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('1'))
btn_1.place(x=5, y=300, width=50, height=50)

btn_2 = tkinter.Button(calculator, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('2'))
btn_2.place(x=60, y=300, width=50, height=50)

btn_3 = tkinter.Button(calculator, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('3'))
btn_3.place(x=115, y=300, width=50, height=50)

btn_jia = tkinter.Button(calculator, text='+', font=('微软雅黑', 20), fg=('#94d6da'), bd=0.5,command=lambda: pressCompute('+'))
btn_jia.place(x=170, y=300, width=50, height=50)

btn_dy = tkinter.Button(calculator, text='=', font=('微软雅黑', 20),bg='#feaf17', fg=('#4F4F4F'), bd=0.5, command=lambda: pressAns())
btn_dy.place(x=225, y=300, width=50, height=105)

# 第五行

btn_0 = tkinter.Button(calculator, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('0'))
btn_0.place(x=5, y=355, width=160, height=50)

btn_cf = tkinter.Button(calculator, text='^', font=('微软雅黑', 20), fg=('#94d6da'), bd=0.5,command=lambda: pressCompute('**'))
btn_cf.place(x=170, y=355, width=50, height=50)



# 字符串转换
def pressChange(str):

    temp = ''
    len_str = len(str)

    i = 0
    while i < len_str:


        if str[i] == '*' and i + 1 < len(str) and str[i + 1] == '*':
            temp = temp + '^'
            i = i + 1
        else:
            temp = temp + str[i]

        i = i + 1

    return temp


# 数字函数
def pressNum(num):  # 设置一个数字函数 判断是否按下数字 并获取数字将数字写在显示版上

    global show_his
    global show_ans
    global his_val
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point

    # 将ans_val 和 ans_temp_sign 合并，
    if ans_temp_sign != '':
        ans_val = ans_val + ans_temp_sign
        ans_temp_sign = ''

    if ans_val == '0':
        ans_val = ''

    if ans_temp_num == '' and len(ans_val) > 0 and ans_val[-1] != '.' and ans_val[-1] < '0' and ans_val[-1] > '9':
        ans_temp_num = '0'

    if ans_temp_num == '0' and num == '0' and flag_point:
        ans_temp_num = '0'
    elif ans_temp_num == '0' and num != '0' and flag_point:
        ans_temp_num = num
    else:
        ans_temp_num = ans_temp_num + num

    show_ans = pressChange(ans_val + ans_temp_num)
    display_ans.set(show_ans)

# 括号空格
def press_(sign):

    global show_his
    global show_ans
    global his_val
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point
    ans_val = ans_val + ans_temp_sign + ans_temp_num
    ans_temp_sign = ''
    ans_temp_num = ''
    ans_val = ans_val + sign


    show_ans = pressChange(ans_val)
    display_ans.set(show_ans)


# 运算符号
def pressCompute(sign):
    global show_his
    global show_ans
    global his_val
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point
    flag_point = True

    # 初始前缀 -
    if ans_val == '' and ans_temp_num==''and sign == '-':
        ans_val = '-'
        display_ans.set(ans_val)
        return

    # 合并
    if ans_temp_num != '':
        ans_val = ans_val + ans_temp_num
        ans_temp_num = ''

    if ans_val == '':
        ans_val = '0'

    if sign == '+' or sign == '/' or sign == '*' or sign == '**' or (sign == '-' and (ans_temp_sign == '' or ans_temp_sign == '+')):
        ans_temp_sign = sign
    elif sign == '-' and ans_temp_sign[-1] != '-' and ans_temp_sign[-1] != '+':
        ans_temp_sign = ans_temp_sign + sign

    show_ans = pressChange(ans_val + ans_temp_sign)
    display_ans.set(show_ans)


# 处理小数点
def pressPoint():
    global show_his
    global show_ans
    global his_val
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point

    if flag_point == True:

        flag_point = False

        ans_val = ans_val + ans_temp_num + ans_temp_sign
        ans_temp_num = ''
        ans_temp_sign = ''
        if ans_val == '' or ans_val[-1] == '+' or ans_val[-1] == '-' or ans_val[-1] == '*' or ans_val[-1] == '/' or (len(ans_val)>=2 and ans_val[-1]=='*' and ans_val[-2]=='*'):
            ans_val = ans_val + '0.'
        else:
            ans_val = ans_val + '.'

        show_ans = pressChange(ans_val)
        display_ans.set(show_ans)


# 左移
def pressRM():
    global show_his
    global show_ans
    global his_val
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point

    ans_val = ans_val + ans_temp_sign + ans_temp_num
    ans_temp_num = ''
    ans_temp_sign = ''
    flag_point = True

    ans_val = str(ans_val)
    if len(ans_val) > 0:
        ans_val = ans_val[0:-1]
    else:
        return
    show_ans = pressChange(ans_val)
    display_ans.set(show_ans)

    for i in range(len(ans_val) - 1, -1, -1):
        if ans_val[i] == '.':
            flag_point = False
        if ans_val[i] == '+' or ans_val[i] == '-' or ans_val[i] == '*' or ans_val[i] == '/' or (len(ans_val) >= 2 and ans_val[-1] == '*' and ans_val[-2] == '*'):
            break


# 清除
def pressC():
    global show_his
    global show_ans
    global his_val
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point
    show_ans = ''
    show_his = ''
    his_val = ''
    ans_val = ''
    ans_temp_num = ''
    ans_temp_sign = ''
    flag_point = True
    # 历史纪录

    display_his.set('')
    # 结果显示
    display_ans.set(0)


# 等于
def pressAns():
    global show_his
    global show_ans
    global his_val
    global ans_val
    global ans_temp_num
    global ans_temp_sign
    global flag_point

    his_val = ans_val + ans_temp_num + ans_temp_sign


    try:
        #print(str(ans_val + ans_temp_num) + '___________')
        ans = eval(str(ans_val + ans_temp_num))

    except SyntaxError or IndexError or TypeError:
        ans_val = ''
        ans_temp_num = ''
        ans_temp_sign = ''
        flag_point = True
        # 历史纪录
        show_his = pressChange(his_val)
        display_his.set(show_his)
        # 结果显示
        display_ans.set("FORMAT ERROR")
        return
    except TypeError:
        ans_val = ''
        ans_temp_num = ''
        ans_temp_sign = ''
        flag_point = True
        # 历史纪录
        show_his = pressChange(his_val)
        display_his.set(show_his)
        # 结果显示
        display_ans.set("FORMAT ERROR")
        return
    except ZeroDivisionError:
        ans_val = ''
        ans_temp_num = ''
        ans_temp_sign = ''
        flag_point = True
        # 历史纪录
        show_his = pressChange(his_val)
        display_his.set(show_his)
        # 结果显示
        display_ans.set("VALUE ERROR")
        return


    else:
        ans = round(ans, 10)
        show_his = pressChange(his_val)
        display_his.set(show_his)
        display_ans.set(str('=' + str(ans)))

        show_ans = ''
        show_his = ''
        his_val = ''
        ans_val = ''
        ans_temp_num = ''
        ans_temp_sign = ''
        flag_point = True




if __name__ == '__main__':
    calculator.mainloop()
