#多继承

# class father1():
#       def have(self):
#             print("父级有的东西")

# class father2():
#       def money(self):
#             print("父级有的东西2")           
# class son(father1,father2):
#       pass
       
# john = son()  #两个父级都调用

#如果两个父级有同样的东西，调用的是第一个里面的，优先继承第一个类

# class father1():
#       def have(self):
#             print("父级有的东西")

# class father2():
#       def have(self):
#             print("父级有的东西2")           
# class son(father1,father2):
#       pass
       
# john = son()
# john.have()

#可以一层套一层继承

# class grandfather():
#       def yeye(self):
#             print("爷爷有的东西")
# class father1(grandfather):
#       def have(self):
#             print("父级有的东西")

# class father2(grandfather):
#       def yiu(self):
#             print("父级有的东西2")    

# class son(father1,father2):
#       pass
       
# john = son()
# john.yeye()

#儿子层只能先在父级层找，找不到才去爷爷层找

# class grandfather():
#       def yeye(self):
#             print("爷爷有的东西")
# class father1(grandfather):
#       def yeye(self):
#             print("父级有的东西")
   
# class son(father1):
#       pass
       
# john = son()
# john.yeye()

# 第一个父级没有，会找第二个父级，没有的话再找爷爷级

# class grandfather():
#       def yeye(self):
#             print("爷爷有的东西")
# class father1(grandfather):
#       pass

# class father2(grandfather):
#       def yeye(self):
#             print("父级有的东西2")    

# class son(father1,father2):
#       pass
       
# john = son()
# john.yeye()

#python3继承顺序
# 新式类的继承方式是：先找最亲的爸爸（括号里面第一个继承的类），然后再去找第二个爸爸（括号里面第二个继承的类），
#当爸爸类都找不到的时候，找第一个爸爸的父类


#类里面的方法不能相互调用，单现在讲一个方法可以相互调用
#类的命名方式和方法命名方式不一样，类的命名方式，多个单词把首字母大写， 方法的是单词中间用下划线；


# class PlusNum:
#     def plus_int(self,a,b):
#         a = int(a)
#         b = int(b)
#         return a+b

#     def plus_float(self,a,b):
#         a = float(a)
#         b = float(b)
#         return a+b
    
#     def plus_all(self,a,b,c,d):
#         return self.plus_int(a,b)+self.plus_float(c,d)  #参数名字可以变，但是个数不能变

# num = PlusNum()
# # print(num.plus_int(3,4))
# # print(num.plus_float(2.1,3.4))
# print(num.plus_all(1,2,3.3,4.3))

# 如下例子：
# class Act:

#     @classmethod   #表示类的方法
#     def use(cls):  #加上了上面的，此处变为cls，是class的缩写
#         print("www")

# Act.use()

#类方法不仅可以被类调用，还可以被对象调用

# class Run:
    
#     @staticmethod  #类的静态方法，不传对象也不传类，既不属于类做的事情，也不属于对象做的事情，但可以被类和对象调用
#     def have_breakfast(): #静态方法括号为空，是针对于cls和self方法用的，可以传自己的参数如a，b等，
#         print('eat eggs')

# r = Run
# r.have_breakfast()  #被对象调用

# Run.have_breakfast() #被类调用


#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————-
# Python 实例方法、类方法、静态方法的区别与作用
# Python中至少有三种比较常见的方法类型，即实例方法，类方法、静态方法。它们是如何定义的呢？如何调用的呢？它们又有何区别和作用呢？且看下文。

# 首先，这三种方法都定义在类中。下面我先简单说一下怎么定义和调用的。（PS：实例对象的权限最大。）

# 实例方法

#     定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；

#     调用：只能由实例对象调用。

# 类方法

#     定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；

#     调用：实例对象和类对象都可以调用。

# 静态方法

#     定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；

#     调用：实例对象和类对象都可以调用。

# 实例方法
# 简而言之，实例方法就是类的实例能够使用的方法。这里不做过多解释。

# 类方法
# 使用装饰器@classmethod。

# 原则上，类方法是将类本身作为对象进行操作的方法。假设有个方法，且这个方法在逻辑上采用类本身作为对象来调用更合理，那么这个方法就可以定义为类方法。另外，如果需要继承，也可以定义为类方法。

# 如下场景：

# 假设我有一个学生类和一个班级类，想要实现的功能为：
#     执行班级人数增加的操作、获得班级的总人数；
#     学生类继承自班级类，每实例化一个学生，班级人数都能增加；
#     最后，我想定义一些学生，获得班级中的总人数。

# 思考：这个问题用类方法做比较合适，为什么？因为我实例化的是学生，但是如果我从学生这一个实例中获得班级总人数，在逻辑上显然是不合理的。同时，如果想要获得班级总人数，如果生成一个班级的实例也是没有必要的。

# 复制代码
# class ClassTest(object):
#     __num = 0

#     @classmethod
#     def addNum(cls):
#         cls.__num += 1

#     @classmethod
#     def getNum(cls):
#         return cls.__num

#     # 这里我用到魔术方法__new__，主要是为了在创建实例的时候调用累加方法。
#     def __new__(self):
#         ClassTest.addNum()
#         return super(ClassTest, self).__new__(self)


# class Student(ClassTest):
#     def __init__(self):
#         self.name = ''

# a = Student()
# b = Student()
# print(ClassTest.getNum())
# 复制代码
# 静态方法
# 使用装饰器@staticmethod。

# 静态方法是类中的函数，不需要实例。静态方法主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，不会涉及到类中的属性和方法的操作。可以理解为，静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于使用和维护。

# 譬如，我想定义一个关于时间操作的类，其中有一个获取当前时间的函数。

# 复制代码
# import time

# class TimeTest(object):
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second

#     @staticmethod
#     def showTime():
#         return time.strftime("%H:%M:%S", time.localtime())


# print(TimeTest.showTime())
# t = TimeTest(2, 10, 10)
# nowTime = t.showTime()
# print(nowTime)
# 复制代码
# 如上，使用了静态方法（函数），然而方法体中并没使用（也不能使用）类或实例的属性（或方法）。若要获得当前时间的字符串时，并不一定需要实例化对象，此时对于静态方法而言，所在类更像是一种名称空间。

# 其实，我们也可以在类外面写一个同样的函数来做这些事，但是这样做就打乱了逻辑关系，也会导致以后代码维护困难。

# 以上就是我对Python的实例方法，类方法和静态方法之间的区别和作用的简要阐述。
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


import re
import requests
import json


# response = requests.get('http://news.baidu.com')  #用这个方法访问百度新闻
# print(response) #打印获取的是状态码
# content = response.text
# print(content)   #打印获取整个的网页内容

# with open('duban.json','w',encoding='utf-8') as file:  #把网页内容写到文件中
#     file.write(content)


##############################################拓展：
# file = open('duban.json','r',encoding='utf-8') #读取这个文件
# a = file.read()
# # pattern = re.compile(r'新闻')
# # pattern = re.compile(r'\d{1,10}')  #找到所有数字匹配，下标从一位到10位数字
# # pattern = re.compile(r'\d{1,}')  #左边不输入，代表从0开始，右边不输入，最大随便出现  取出这个文件中的所有数字
# # pattern = re.compile(r'\d+') #跟上面的[1,]效果是一样的
# # pattern = re.compile(r'\w') #把数字、字母、下划线、汉字都打印出来了
# # pattern = re.compile(r'\w+') #把数字、字母、下划线、汉字都打印连在一起
# # pattern = re.compile(r'\W+') #除掉数字、字母、下划线和汉字剩下的东西（大写的W）
# # pattern = re.compile(r'\D+') #非数字的一切内容
# pattern = re.compile(r'\w*') #表示匹配0此或者多次，等于[0,]
# result = pattern.findall(a)  #找到这个文件中所有的“新闻”字样
# print(result)

# file.close()  #打开文件记得关闭



# file = open('duban.json','r',encoding='utf-8') #读取这个文件
# a = file.read()
# a2 = 'song.lu@errc.com,song lu@errcxcom,song!lu@errc1com'
# # pattern = re.compile(r'song.lu@errc.com') #因为‘。’导致都匹配上了
# # pattern = re.compile(r'.') #'.'能匹配所有的东西，代表匹配所有
# pattern = re.compile(r'song\.lu@errc\.com') #在点前面加上反斜杠，就能完全匹配
# result = pattern.findall(a2)  
# print(result)

# file.close()  #打开文件记得关闭

# 比如匹配所有邮箱
# file = open('duban.json','r',encoding='utf-8') #读取这个文件
# a = file.read()
# a2 = 'song.lu@errc.com,928@qq.com,sswdou@aliyun.com'

# # pattern = re.compile(r'.+@\w+\.com') #匹配所有邮箱,但是打印出来的是一组字符串，需要分开打印，用下面方法
# # pattern = re.compile(r'\w+.\w+@\w+\.com')  #正常情况只要后面的\w+@\w+\.com（正常的邮箱正则表达式）即可，但是因为此题前面有个点
# result = pattern.findall(a2)  
# print(result)

# file.close()  #打开文件记得关闭


# # 题目：chuxinhong@hit.com，只要匹配@hit
# file = open('duban.json','r',encoding='utf-8') #读取这个文件
# a = file.read()
# a2 = 'chuxinhong@hit.edu.cn.cf.aa.ee.dd'
# # pattern = re.compile(r'@.+\.')  #正则表达式默认贪婪模式，尽可能多的匹配点，会匹配到最后一个，如何避免呢。前面加个问号即可，如下：
# pattern = re.compile(r'@.+?\.')  #正则表达式的点的懒惰模式，问号是解除贪婪模式变为懒惰模式
# result = pattern.findall(a2)  
# print(result)

# file.close()  #打开文件记得关闭

# file = open('duban.json','r',encoding='utf-8') #读取这个文件
# a = file.read()
# a2 = '<HtMl>hello</hTmL>'   #网页,要把hello匹配出来
# pattern = re.compile(r'<[Hh][Tt][Mm][Ll]>hello</[Hh][Tt][Mm][Ll]>')  #中括号里面是你可以匹配的对象
# result = pattern.findall(a2) 
# print(result)

# file.close()  #打开文件记得关闭

# .*? 代表啥意思=====代表万能表达式。  
# \d 换成中括号可以用[0123456789] 或者[0-9] 如\d{,2}可以写成[012]
#\w 字母数字_    也可以写成[a-zA-Z0-9_]
# \W 非数字字母_
# \d 数字
# \D 非数字
# . 所有
# + 匹配一次或多次等于{1,}
# {1,4} 匹配一次到4次
# {,4} 匹配至多四次
# {1,} 匹配至少一次
# ? 解除贪婪模式，接在次数的正则表达式后面使用
# * 表示匹配0次或多次，等于{0,}




file = open('duban.json','r',encoding='utf-8') #读取这个文件
a = file.read()
a2 = 'song.lu@errc.com,song lu@errcx.com,song!lu@errc.com'
pattern = re.compile(r'@(.*?)\.com')  #万能表达式需要告诉在哪里结束
result = pattern.findall(a2)  
print(result)

file.close()  #打开文件记得关闭

###################################################拓展：
# import json  #json仅限于拿接口数据，content拿所有格式
# import requests



# response = requests.get('http://news.baidu.com')  #用这个方法访问百度新闻
# # print(str(response.text))  #类型是字符串类型
# # print(str(response.content)) #用concent会生成字节流，前面有个b，加上“encoding=‘utf-8’”就可以了
# print(response.json)   #类型是字典类型