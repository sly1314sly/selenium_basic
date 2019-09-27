#一
#  def login(a,b=10):    #提供默认参数
#     print(a+b)
# login(1)


#二
# 1、
# def login(username,password,count=0):
#     if username == 'qwe' and password == '123':
#         count += 1
#         print(count)
#     else:
#         print(count)

# login('qwe','123')   #只输入前面两个值
# login('qwe','123',13)    #输入后面的值
# login('qwe','123','13')    #类型不一致，报错
# login(13,'qwe','123')    #顺序不一致，虽然没有报错，调用的是else后面的

# 2、
# def get_info(name,age):
#     print('我叫%s，我今年%d岁了'%(name,age))

# get_info(13,'qwe')    #顺序不一致，类型不一致，报错
# 如何让不报错，可以这样写
# get_info(age=12,name="小明")  #要么都给，要么都不给

#三
# 1、
# def get_infos(*args):   # *号代表你传进来的东西是一个元祖，给多少变量，统统转换为元祖，不定长参数
#     print(args)

# get_infos(1,2,45,'123','qwe',[3,4,56,67],{'a':1,'b':2})

# 2、
# def get_infos(*args):
#     for i in args:    #把args中的值一个一个取出来
#         print(i)

# get_infos(1,2,45,'123','qwe',[3,4,56,67],{'a':1,'b':2})


# 3、
# def get_infos(*args):
#     print(args[-1])     #传进来的参数只想要其中哪个参数，这个是最后一个参数

# get_infos(1,2,45,'123','qwe',[3,4,56,67],{'a':1,'b':2})

#练习题
# 1、多种收费项目需要报销，餐饮费，机票费、住宿费、会议费、门票费，我要报住宿费和机票费，john要报名餐饮费、会议费、门票费，求所报费用的总和。


# def for_payment(*fee):
#     sum = 0   * 如果定义在外面，就有可能被别人调用
#     for i in fee:
#         sum += i
#     print('您的所有报销费用，一共是：',sum,'元')

# for_payment(200,450,600)


# 2、加一个要求，如果传进来的不是整数和小数的，就忽略掉，只取整数和小数
# def for_payment(*fee):
#     sum = 0
#     for i in fee:
#         if type(i) == int or type(i) == float:
#             sum += i
#     print('您的所有报销费用，一共是：',sum,'元')

# for_payment('wwww',450,600.67,{1,2,3})



#3、题目：往一个函数里不断输入，每次调用的函数里面存到一个文档里面，即终端写的东西都到保持到文档里面
# def Word(args):
#     with open(r'/Users/songluyao/Documents/PYTHON_LESSON/a.txt','w') as f:
#         f.write(args)

# Word(input('输入单词：')) 



# 四、try的使用
## 一旦try块的代码报错就执行except块的代码

# try:
#     pass    #要捕捉的对象，比如哪些代码觉得异常，放在try里
# except expression as identifier:    #处理异常  except后面接的是异常，as是异常带的参数 去掉except后面的都没有问题
#     pass  #pass只是占位的，什么事都不干


#1、如：
# try:
#     a = 2/0
# except:
#     print('出现异常')

# 2、如：打开一个文件，并且写‘aaa’，如果文件异常了，就把aaa打印出来
# a = 'aaa'
# try:
#     with open(r'/Users/songluyao/Documents/PYTHON_LESSON/a.txt','w') as f:
#          f.write(a)
# except:
#     print(a)



# 3、尝试看代码的错误信息
# try:
#     a = 'qrtghh'
#     print(b)
# except ZeroDivisionError:   #except后面接了报错名字，就只会按照相应的去报异常，如果不在此里面，就会在终端报错
#     print('除数不能为0')
# except NameError:
#     print('名字没有定义')


# dict = {'a':1,2}   #SyntaxError: invalid syntax 一般缩进有问题，会报这个错误，某个字符不符合规定，也报错误

# dict = {'a':1,[12,24]:2}  #ypeError: unhashable type: 'list'   表示类型错误


#报错原理：当try代码块某一行报错时，直接进入excert中对应执行（语法错误不好捕捉）
# try:
#     dict = {'a':1,[12,24]:2}
#     a = 1/0     
#     with open(r'/Users/songluyao/Documents/PYTHON_LESSON/a.txt‘,'r') as f:
#          f.write(a)

#     def suibian(a,c,d):
#         xxxxxxxx
#         return "dfsdgdsg"
#     suibian(1,2,3)
#     input('dfsdf')

# except ZeroDivisionError:
#     print('除数不能为零')
# except NameError:
#     print('名字没定义')
# except IOError:
#     print('IOerror')
# except KeyboardInterrupt:
#     print('输入异常')
# except TypeError:
#     print('类型错误')

  #如何在异常后面加参数
# try:
#     dict = {'a':1,[12,24]:2}
# except TypeError as e:    #先捕获类型，再拿到参数 ，e是随便取的  如果是python2，直接把as改为逗号即可
#     print('类型错误',e)


# 五、try  else
# try:    
#     pass
# except expression as identifier:
#     pass
# else:       #表示try运行正常，没有报错，进入这里面
#     pass


#如：
# try:
#     a=1/1
#     #a=1/0
# except:
#     print('出错了')
# else:
#     print('运行正常')

# 题目：执行一个输入算法，如果输入中断了，就打印错误'输入中断'，如果正常退出，将输入的内容打印出来
# try:    #ctrl+c  中断输入，mac中是control+c
#     a = input()
# except:
#     print('输入中断')
# else:
#     print(a)

# 拓展：
# try:
#     input()
# except:
#     print('打印中断')
# else:
#     print('打印正常')
# finally:
#     print(233333)   #表示无论上面输入什么，最后都执行此处信息

# try:
#     pass
# except expression as identifier:
#     pass
# else:
#     pass
# finally:
#     pass


# &&&&&&&
# try:
#     pass
# except expression as identifier:
#     pass
# finally:
#     pass


# try:
#     pass
# finally:
#     pass


#六、import 导入

#pip install requests #装一个requests包
# import requests  #安装完就可以导入这个包了，如果没有，就会报错的
# import re



# import keyword  #导入一个包
# print(keyword.kwlist)

# from keyword import kwlist  #从某某中导入某一个方法，与上面的那个导入方式不一样，单结果一样，各有利弊
# print(kwlist)

# from keyword import *  # *号代表所有的方法

# import requests
# # print(help(requests)) #打印查看有哪些方法
# response = requests.get('http://www.baidu.com')  #用这个方法访问百度
# print(response.text)   #打印获取整个的网页内容



# 七、面向对象
# 把一个抽象的对象变成一个实体，叫实例化

#第一种
class Student:   #定义一个学生类
    number = 1234
    name = ''
    pont = 0

    def study(self):
          print('我在学习')

    def ask(self):
          print('我在问问题')

    def think(self):
          print('我在思考')

john = Student()
john.study()
john.name = 'john' #调用该方法
#在类里面，一定要加self


#第二种
class Student:   #定义一个学生类 
    def __init__(self,name,age,gender):  #类的内置方法，预定义函数，在类里面传参数，就是让这个参数变成这个类的属性，
        self.name = name  #selef把传进来的参数变成它的属性
        self.age = age
        self.gender = gender

#在某个方法前面加上双下划线，代表是这个的私有方法；init默认在每个类里面都有，如果想传参数给整个类作为属性，一定要在init里面传

    def study(self):
          print('我在学习')

    def ask(self):
          print('我在问问题')

    def think(self):
          print('我在思考')

john = Student('john',23,'male')
john.ask()
john.name = 'john' #调用该方法
#在类里面，一定要加self

#问题：区别？
#init没有写，传参里面没有写东西，为什么也不报错？ 
#因为init在实例化的时候会被调用，如果不传参，可以不用写
#在方法里面传参，不影响其他的，其他的方法不会调用，但是在init里面的，其他的方法都会调用

#题目
#1、定义一个类，OperateList,实例化，为他写一些方法，查询方法,查询这个list、修改方法、删除方法

class OperateList:
      def quety(self,list1): #查询list1
            print(list1)
      def change(self,list1,list2):#把list2添加到list1中
            list2.append(list1)
            print(list2)
      def shanchu(self,list1):  #删除list中的下标为2的值
            list1.pop(2)
            print(list1)

s = OperateList()
s.quety([1,2,3,45,6777])
s.change([1,2,'aa'],7)
s.shanchu([3,4,52,6,7])

##########

#题目二，定义一个类叫乘法表，类里面只有一个方法，方法名字叫做乘法，传几就是1成几结束 

class Chengfabiao:
      def chengfa(self,s):
          for i in range(1,s+1):
             for j in range(1,i+1):
                print('%d*%d=%d'%(i,j,i*j),end='\t')
             print()

a = Chengfabiao()

a.chengfa(7)


# 题目三、三个数，判断是不是三角形、判断是不是等腰、等边、直角三角形？
class Sanjiaoxing:  

    def __init__(self,a,b,c): 
        self.a = a
        self.b = b
        self.c = c

    def sanjiaoxing(self):
        a = self.a
        b = self.b
        c = self.c     
        if a+b>c and a+c>b and b+c>a and a!=0 and b!=0 and c!=0:
             print("是三角形")
        else:
               print("不是三角形")

    def dengbiansj(self):
        a = self.a
        b = self.b
        c = self.c
        if a+b>c and a+c>b and b+c>a and a!=0 and b!=0 and c!=0: 
            if a==b or a==c or b==c and a!=0:
                print("是等腰三角形")
            else:
                print("不是等腰三角形")

    def zhijiao(self):
        a = self.a
        b = self.b
        c = self.c  
        if a**2+b**2==c**2 or a**2+c**2==b**2  or b**2+c**2==a**2 and a!=0 and b!=0 and c!=0:
            print("是直角三角形")
        else:
            print("不是直角三角形")

john = Sanjiaoxing(3,4,5)
john.sanjiaoxing()
john.dengbiansj()
john.zhijiao()




#继承
# 什么是继承，儿子继承爸爸的方法， 如果儿子有同名方法，会先调用儿子自己的，然后再调用爸爸的
class father():
      def have(self):
            print("父级有的东西")
class son(father):
      pass
       
john = son()
john.have()

# # 复习
# def login(a,b):
#     print(a,b)


# #单*号传入的是元祖
# def fee(*args):
#     for i in args:
#         print(i)

# fee(1,2,34,'qqqq')


# #双*号传入的是字典
# def fed(**kw):
#     print(kw)

# fed(a=1,b=2,c='sdada')   #必须有等于号 有等于号才能传入进去

# try:        异常
#       pass
# except:
#       pass
# else：
#     pass
# finally：
#     pass


# #如何安装一个包
#   #在终端直接运行pip install xxxxxxxx

# #如何导入一个包
#   #import request
#   from requests import get #从包里导入一个方法
# from requests import *  #从包里导入所有方法
# a = get("......")

#class 类

#   只要在类里面  self一定不能少
#调用的时候 括号不能少