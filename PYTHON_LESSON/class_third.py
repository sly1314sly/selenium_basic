# for循坏

# 打印字符串长度
# str = "wqqwewweiynyihkl"
# print(len(str))

# range 代表一个数字范围，仅限数字
# range(10) #代表从0到9 
# range(1,9) #代表从1到9，8个数，
# range(1,9,2)  #代表从1到9，每两位取值，间隔为2
#
# for i in range(10):
#     print(i)


# str = "ewtnjgiifg"
# for i in range(len(str)):     #对于i而言，在此里面循坏
#     print(str[i])
#

# for i in range(5):
#     print(i)


# for 能对有序的数字结构循坏
# str = "ewtnjgiifg"
# for i in str:
#     print(i)
#

# 题目：想让结果打印出来1，4，9，16，25，36，49，64，81  可以看出是平方
# lis = [1,2,3,4,5,6,7,8,9]
# for i in lis:
#     print(i**2)


# 想让结果打印出来list [1，4，9，16，25，36，49，64，81]
# 思路：对比两个list有什么不同，对比后，对每个元素进行操作，计算
# 第一种方法
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lis2 = []
# for i in lis:
#     s = i**2
#     lis2.append(s)
# print(lis2)

# 第二种方法
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lis2 = [i**2 for i in lis]    #python里面的列表生成式
# print(lis2)

# python列表生成式： ****************
# 1、生成的值在最前面，后面是处理


# 题目：想要生成[1,9,25,49,81]
# 第一种方法：
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lis2 = []
# for i in lis:
#     if i % 2 == 1:
#         s = i**2
#         lis2.append(s)
# print(lis2)

# 第二种方法：（列表生成式）
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lis2 = [i**2 for i in lis if i%2==1]
# print(lis2)




# 看看list的操作:

# array = [1, 2, 5, 3, 6, 8, 4]
# #事实上这里的顺序标识是
# [1, 2, 5, 3, 6, 8, 4]
# (0，1，2，3，4，5，6)
# (-7,-6,-5,-4,-3,-2,-1)
 
# >>> array[0:] #列出0以后的
# [1, 2, 5, 3, 6, 8, 4]
# >>> array[1:] #列出1以后的
# [2, 5, 3, 6, 8, 4]
# >>> array[:-1] #列出-1之前的
# [1, 2, 5, 3, 6, 8]
# >>> array[3:-3] #列出3到-3之间的
# [3]
# 那么两个[::]会是什么那？

# >>> array[::2]
# [1, 5, 6, 4]
# >>> array[2::]
# [5, 3, 6, 8, 4]
# >>> array[::3]
# [1, 3, 4]
# >>> array[::4]
# [1, 6] 
# 假设想让他们颠倒形成reverse函数的效果
# >>> array[::-1]
# [4, 8, 6, 3, 5, 2, 1]
# >>> array[::-2]
# [4, 6, 5, 1]
# range（）在for循环中用法：

# for i in range(4):
#      print(i,'hello')

# 在一些时候也会用range间接的来迭代序列，一般在for循环中使用手动索引才会这样做：


# x = 'python'

# >>>for i in x:
# >>>    print i,
# p y t h o n

# >>>for i in range(len(x)):
# >>>    print x[i],
# p y t h o n


# >>> range(1,5) #代表从1到5(不包括5)
# [1, 2, 3, 4]
# >>> range(1,5,2) #代表从1到5。间隔2(不包括5)
# [1, 3]
# >>> range(5) #代表从0到5(不包括5)
# [0, 1, 2, 3, 4]

# 题目：给三个数6，3,4，组合成不同的三位数，不能重复

# tar = [6,3,4]
# for i in tar:
#     for j in tar:
#         for k in tar:
#             if i !=j  and i != k and j !=k:   #如果这行去掉，就会相等了。 如果有判断，需要把判断写在循环的最里面
#                 print(i*100+j*10+k) 

# 题目：打印奇数的九九乘法表

# for i in range(1,10):
#     for j in range(1,i+1):
#             if i % 2 == 1 and j % 2 == 1: 
#                 print('%d*%d=%d'%(i,j,i*j),end='\t')
#     print()

# for i in range(1,10：2):
#     for j in range(1,i+1):
#                 print('%d*%d=%d'%(i,j,i*j),end='\t')
#     print()


# 题目：九九乘法表   双重循环：外面的掌控里面的
# for i in range(1,10):
#     for j in range(1,i+1):   #内循环  让j在i里面循环  为了能取到i，所以i加1
#         #print(i,'*',j,'=',i*j,end='\t')   #\t是默认空4格
#         print('%d*%d=%d'%(i,j,i*j),end='\t')    #第二种方法： 格式化字符串，前面几个百分号，后面就几个值  先把字符串先写好，
#     print()    #参数没有代表的是（end='\n'） i不变，就不换行


# 第二种
# for i in range(1, 10):
#         for j in range(, 10):  # 内循环  让j在i里面循环  为了能取到i，所以i加1
#             print(i, '*', j, '=', i * j, end='\t')  # \t是默认空4格
#         print()


# 复习后
# 11
# 12 22
# 13 23 33
# 14 24 34 44
# ....
# 19 29 39 49 59 69 79 89 99  #前面这个数字永远小于等于后面这个数字

# for i in range(1,10):  #i就是后面这个数
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(j,i,i*j),end=' ')
#     print()


# 格式化字符串
# print(   '%d*%d=%d'   %    (i,j,i*j)   )   格式化字符串  如果前面变量是字符串，写成%s ，如果是数字%d，如果是小数%f
# 如下：
# print('我叫%s，我今年%d岁了'%('张三',22))





# while循环

# a = 0
# while a < 11:
#     print('hello') #需要把自己的事情先做完，再去加1
#     a+=1

# 题目：a=0，判断当a的平方第一次大于100的时候跳出来，并打印a是多少

# a = 0
# while a**2 <=100:
#     # print(a)  #这个是小于100的值
#     a+=1
# print(a)  #这个是跳出来的值

# 题目：从1加到100的值
#
# a = 1
# sum =0
# while a<=100:
#     sum += a
#     a += 1
# print(sum)


#for和while的区别
# for只能在定好的东西里面循环，但是while的条件是自己定的，更自由一点

# 题目：有一株鲜花，第一天开1朵，第二天再次开两朵，第三天再次开4朵，那么到了第五天总共开了多少朵？
#分析： 1，2，4，8，16  相加为31朵
# 第一种方法
# s = 0
# for i in range(5):
#     i = 2**i     #每天开的朵数
#     s = s+i      #总数
# print(s)

# 第二种方法：
# a = 1   #当前天数对应的鲜花数
# b = 1   #天数
# sum = 0  #每天的鲜花总数
# while b<=5:
#     sum += a  #所有的天数的花朵数
#     a = a*2   #每天的花朵数
#     b += 1    #天数
# print(sum)



# 天数和花数能不能挂钩？





# 第一次超过2000朵，需要多少天？
# a = 1
# b = 0
# sum = 0
# while sum <= 2000:
#     sum += a
#     a = a*2
#     b += 1
# print(b)



# def 定义  2：26

# def name():      #定义函数   定义函数的时候括号里面的是参数

# name()       #调用函数   调用的时候括号里是定义的值
#不调用是不运行的

#如：
# def hello():  上面是空的
#     for i in range(10):
#         print("a")
# hello() 这个也是空的


# def hello(n):  上面有值
#     for i in range(n):
#         print("abc")
# hello(2)  下面也有值


# def login(username,password):
#     if username=='admin' and password=='123':
#         print('登陆成功')
#     else:
#         print('登陆失败')

# login('123','234')






#题目:输入三个数，看能不能组成三角形：

def tux(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        print("能组成三角形")
    else:
        print("不能组成三角形")
tux(0,0,3)



# 如果在def方法中没有给return，那就是表示null，return是给调用方法的人看的，print只是在终端秀一下
def login(username,password):
    if username =='admin' and password =='123':
        print('登陆成功')
        return 0
    else:
        print('登陆失败')
        return -1


a=login('123','234')
print(a)


# 异常
try:
    a = 1/1
    pass#可疑的代码块
except:
    print('error')
    pass#如果可疑的代码块出问题了，我就执行这里面的内容
else:
    print('ok')
    pass#如果可疑的代码块没有报错，我就执行这里面的内容
finally:
    print('必定执行')
    pass#无论try里面的代码有没有报错，最后必定执行finally里面的内容

# 函数里面传多参数的时候怎么办？
#方法一：单*号  用元祖的方法
# def payment(*fee):
#     s = 0
#     for i in fee:
#         s += i
#     print(s)



# tup=(11,23,24,56,90)
# for i in tup:
#     print(i)


# payment(11,23,24,56,90)



# 方法二：双*号 用字典的方法
def payment2(**fee):
#     s = 0
#     for i in fee:
#         s += i
    print(type(fee))

payment2(a = 11,b = 23,c = 24,d = 56,e = 90)




