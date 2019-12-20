#一
import keyword
print(keyword.kwlist)  #打印关键字

#二
a = 'app\nle'  
a2 = r'app\nle'   #加r是防止字符转义的，加r和不加''r是有区别的，如果路径中出现'\t'（python中是空六格的意思）的话 不加r的话\t就会被转义 而加了'r'之后'\t'就能保留原有的样子
print(a)
print(a2)

#三
#打开一个文件，有两种方法
#方法一：
file = open (r'C:\Users\Administrator\Desktop\PYTHON_LESSON\a.txt','r',encoding='utf-8')    #'r,w,a,x'
print(file.read())
file.close()


#方法二：（更简洁）
with open(r'C:\Users\Administrator\Desktop\PYTHON_LESSON\a.txt','r',encoding='utf-8') as file:
    print(file.read())  #read当成整体来读，readline是一行一行的读

#延伸
with open(r'C:\Users\Administrator\Desktop\PYTHON_LESSON\a.txt','r',encoding='utf-8') as file:
    a = file.read()
    print(a)
    res = a.count('a')  #计算文件中a的值有几个，注意：计算出来的是不包括大写的A
    print(res)

with open(r'C:\Users\Administrator\Desktop\PYTHON_LESSON\a.txt','r',encoding='utf-8') as file:
    a = file.read()
    pattern = re.compile(r'python')
    result = re.findall(a) #findall是查找所有的，意思是使用正则表达式去目标字符串匹配
    result = str(result)  #这个方法也行，与上面那个是一样的，string是你要查找的对象，可以更改
    print(result)


# 打开文件两种方法

# file = open(r'/Users/songluyao/Documents/PYTHON_LESSON/a.txt','r')
# print (file.read())
# file.close()

with open(r'/Users/songluyao/Documents/PYTHON_LESSON/a.txt','a') as file:
    file.write('22222ddddd\nqqdfadfaffaafdfafafaff')
    # print(file.read())

# 一些正则表达式的关键词

# w：以写方式打开，
# a：以追加模式打开 (从 EOF 开始, 必要时创建新文件)
# r+：以读写模式打开
# w+：以读写模式打开 (参见 w )
# a+：以读写模式打开 (参见 a )
# rb：以二进制读模式打开
# wb：以二进制写模式打开 (参见 w )
# ab：以二进制追加模式打开 (参见 a )
# rb+：以二进制读写模式打开 (参见 r+ )
# wb+：以二进制读写模式打开 (参见 w+ )
# ab+：以二进制读写模式打开 (参见 a+ )fp.read([size])

#四
# print(help(open))   # 使用help()查看帮助
# help(input)

#五*********************************************************
#if……else  如果，否则  和 elif  或者，再或者
#题目一：

point = 100

if point >= 80 and point <=100:
    print('优秀')
elif point >=60 and point<80:
    print('及格')
elif point >=0 and point<60:
    print('不及格')
else:
    print('非法分数')


a = 1
b = 2
c = 1
if a+b>c and a+c>b and b+c>a:
    print("能组成一个三角形")
else:
    print("不能组成一个三角形")

#题目二：
username = 'admin'
password = '126'
if username == 'admin' and password == '126':
    print('输入正确')
else:
    print('账号或密码错误')

# if username == 'admin' and password == '123':
#     print('输入正确')
# elif username =='admin' and password != '123':
#     print('密码错误')
# else:
#     print('非法输入')



# score = 95

# if score >=90 and score <=100:
#     print('优秀')
#     if score >=95:
#         print('超优秀')
#         if score == 100:
#            print('相当优秀')

# if score >0 and score <= 80:
#     print("及格")


    

# fruit = ['apple','orange','banana','apple']
# fruit.pop()
# print(fruit)


# fruit.extend('watermelon')
# print(fruit)

# number = [2,1,5,53,8,9,23,6,9,8]

# number.sort()
# number.reverse()
# number=number[::-1]
# print(number)


# 大小写转换
# 1、	string1 = “my name is john”  对这句话的首字母进行大写处理，并且把人名都变成大写

# str = "my name is john"
# str = str[0:-4].capitalize()+str[-4:].upper()
# print(str)


# 第二节课上午

# 字符串取值
string = 'hello'
print(string[4])

# 切片  
string = '0123456789'
print(string[0:5])  #能取到第二个参数的前面一位
print(string[:])  #从开始到结尾可以不用写值

# 步长
string = '0123456789'
print(string[::2]) #步长为2，每两位取值，取第一个。
print(string[4::2]) #从下标第四个开始取值，步长为2。

# 字符串的方法
string = '0123456789'
string.join

print(string.count('0'))  #计算字符串中0出现的次数，统计


import re    #导入正则表达式
#re表示regular expression  正则表达式  是匹配用的
string = 'hh0123456789abccdefghijklmnjjq7181910'
pattern = re.compile(r'a')   #pattern其实是一个正则表达式,此句意思是制作一个正则表达式，引号里面是匹配的内容，可以更改
result = re.findall(pattern,string) #findall是查找所有的，意思是使用正则表达式去目标字符串匹配
result = pattern.findall(string)  #这个方法也行，与上面那个是一样的，string是你要查找的对象，可以更改
print(result)  #打印出来的格式一般是list格式

result = str(result)
print(string.count('a'))


# 转换成字符串格式
a = 1
str(a)   #把a转换成字符串
print(type(a))


import re    #导入正则表达式
#re表示regular expression  正则表达式  是匹配用的
string = 'hh0123456789abccdefghijklmnjjq7181910'
pattern = re.compile(r'a')   #pattern其实是一个正则表达式,此句意思是制作一个正则表达式，引号里面是匹配的内容，可以更改
result = re.findall(pattern,string) #findall是查找所有的，意思是使用正则表达式去目标字符串匹配
result = pattern.findall(string)  #这个方法也行，与上面那个是一样的，string是你要查找的对象，可以更改
print(result)  #打印出来的格式一般是list格式

result = str(result)
print(string.count('a'))


string = 'hh0123456789abccdefghijklmnjjq7181910'   
a = string.capitalize()  #首字母大写
a = string.upper()  #所有字母大写
a = string.lower()  #所有字母小写
a = string.islower() #是否全部是小写
a = string.isdigit() # 是否全部是数字
a = string.find('2') #找2第一次出现的地方，find如果找不到返回结果为-1
a = string.index('2') #index找不到会报错

#如果变量出现了多次，以最后一次为准


#列表
list1 = [1,2,'a',"666",a]

fruit = ['apple','banana','orange']
print(fruit[0])
#字符串和list都支持切片
print(fruit[0][1])  #可以把里面的字母取出来 p

#reverse  反向的意思
fruit.reverse()  #将列表倒序排序
fruit.remove('apple')  #删除列表中的一个元素 fruit.remove(string) 只能删除一个,有多个页只能删除第一个，再想删就多写几个
fruit.pop(1) #pop也是删除，里面写的是下标，如果pop为空，默认删除的是最后一个元素，是先进后出的原则（栈），即先插入进去的，最后一个出来。
fruit.append('watermalon') #添加，拼接的意思  添加一个字符串
fruit.append(['a','b','c'])  #添加一个list，默认是把一个list添加进list，后面添加的一个东西当做一个整体添加进去的
fruit.extend('watermalon')  #添加的意思，无论后面是什么，只要能切片，都能切好，添加的一定是一个集合
print(fruit)

list2 = fruit.copy()  #浅复制
#浅复制：单纯把某个地址拿来用，只是拿内存地址

#深复制：不会随着原来的值的改变而改变，是一个全新的对象,不再与原来的对象有任何关联。
import copy
fruit = ['apple','banana','orange']
list3 = copy.deepcopy(fruit)
print(list3)

fruit.clear()  #清空
fruit.index('banana') #查找
fruit.insert(0,'a')  #插入,将a插入到下标0的地方，参数1为下标，参数2为插入的值

# 排序
number = [1,2,3,4,5,12,442,38,64,88,55]
number.sort()  #从小到大排序
number.reverse()   #从小大大排序后反向即可按照从大到小排序
number = number[::-1] #此方法也可以从大到小排序。默认步长为1，倒着走

sor = sorted(number)
print(sor) #此方法是生成了一个新的列表且是排序后的，之前的列表是没有更改的。
#即sort是把原来列表排列了，对原来列表起作用，sorted是把排好的结果放在一个新的list中

#用正则表达式查找列表中的某个字母的总数
import re
fruit = ['apple','banana','orange']
pattern = re.compile(r'a')
res = pattern.findall(fruit)
count = str(res).count('a')
print(count)


#类型转换
s = 'apple'
lis = list(s) #把一个对象转换成list

str() #转化为字符串
list() #转化为列表
int() #转化为数字
float() #转化为小数
tuple() #转换为元祖

#tuple 元祖  元祖也有切片
tup = ('apple','orange','banana')
print(tup[::1])
# tuple本身不能被更改，extend、append、insert方法不行，里面东西是定死的，增删改都不行，可以查询
tup.count('apple') #可以查询
tup.index('apple')

# dict 字典
en_ch = {'apple':'苹果','orange':'橘子','banana':'香蕉'}
#字典里面的东西是一对一对的
print(en_ch['apple']) #打印的是apple后面的值
en_ch.clear #清空字典
en_ch.pop('apple') #删除，给的是key
en_ch.popitem() #随机删除，不需要给值
en_ch.get('banana') #跟print(en_ch['banana']）一样，都是取值，,en_ch.get('banana') 这个没有，提示none，
                    # 如果用print(en_ch['banana']），会提示报错
en_ch.values()  #所有的值
en_ch.keys()   #所有的键
en_ch.items()  #信息一对一对取出来
en_ch.fromkeys()  #生成一个新的字典，可以给一个值，也可以给两个值，一个值报错none，两个值，前面的是key，后面的是值
a = en_ch.fromkeys('asa','s')
print(a)

#延伸
fruit = ['a','erer','eeee','rtgg']
s = ''.join(fruit)
print(s[1])  #此方法是把列表转换成字符串，且里面的各种括号，符号都没有了，如【 ’，如果直接用str会带出这些符号东西


#字典中的值修改
# 先取出来，然后给个新的值
en_ch = {'apple':'苹果','orange':'橘子','banana':'香蕉'}
en_ch['banana'] = 'xiangjiao'
print(en_ch)

#字典中添加值
en_ch = {'apple':'苹果','orange':'橘子','banana':'香蕉'}
en_ch['grape'] = '葡萄'
print(en_ch)