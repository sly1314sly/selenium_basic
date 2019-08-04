# ''' 1、小明身高1.75，体重80.5kg，请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖 '''

# high = 1.75
# weight = 80.5




# IT培训业界良心，Uncle.Honey老师，海派清口式讲解“循环+break语句+黑科技”的代码实例
# 游戏1：英雄联盟极地大乱斗版
# from random import choice  # 黑科技
# import time
# LOL_Owned_Person_List = ['卡牌大师', '德玛西亚皇子', '酒桶', '无极剑圣', '诺克萨斯之手', '九尾妖狐']
# while True:
#     press_1 = input('极地大乱斗模式：请按下1重新选择英雄：')
#     if press_1 == '1':
#         print('正在随机选择英雄...')
#         time.sleep(0.3)
#         print('3')
#         time.sleep(1)
#         print('2')
#         time.sleep(1)
#         print('1')
#         time.sleep(1)
#         the_hero = choice(LOL_Owned_Person_List)  # random.choice方法随机选择列表里的一组元素
#         if the_hero == '卡牌大师':
#             print('【{0}】已被选中，极地大乱斗即将在3秒后开启！'.format(the_hero))
#             break
#         else:
#             print('当前选中的是【{0}】，不是【卡牌大师】，请继续- -'.format(the_hero))
#     else:
#         print('亲爱的召唤师，你的英雄已选定，3秒后进入战场！')
#         break

# # 游戏2：王者荣耀版
# from random import choice  # 黑科技
# import time
# KingGlory_Owned_Person_List = ['大乔', '小乔', '孙尚香', '妲己', '不知火舞', '冯提莫', '罗玉凤', '貂蝉', '倪朱紫']
# while True:
#     press_1 = input('女神大乱斗模式：请按下1重新选择你的女神：')
#     if press_1 == '1':
#         print('正在随机选择女神...')
#         time.sleep(0.3)
#         print('3')
#         time.sleep(1)
#         print('2')
#         time.sleep(1)
#         print('1')
#         time.sleep(1)
#         the_hero = choice(KingGlory_Owned_Person_List)  # random.choice方法随机选择列表里的一组元素
#         if the_hero == '罗玉凤':
#             print('【{0}】已被选中，女神大乱斗即将在3秒后开启！女神【{0}】与你同在，祝君好运！'.format(the_hero))
#             break
#         else:
#             print('当前选中的是【{0}】，不是【罗玉凤】，请继续- -'.format(the_hero))
#     else:
#         print('亲爱的召唤师，你的女神已选定，3秒后进入战场！')
#         break

# # 游戏3：《凉凉》抖音网红歌曲联名版
# from random import choice  # 黑科技
# import time
# Songs_List = ['学猫叫', '你还怕大雨吗', '义勇军进行曲', '凉凉', '哈狗帮', '不爱我就拉倒', '演员', '醉赤壁', '一百万个可能', '万紫千红']
# while True:
#     press_1 = input('这里是中国好声音现场：请按下1选择你的神曲：')
#     if press_1 == '1':
#         print('正在随机选择歌曲...')
#         time.sleep(0.3)
#         print('3')
#         time.sleep(1)
#         print('2')
#         time.sleep(1)
#         print('1')
#         time.sleep(1)
#         the_song = choice(Songs_List)  # random.choice方法随机选择列表里的一组元素
#         if the_song == '凉凉':
#             print('【{0}】已被选中，即将在3秒后high爆全场！Wake up！'.format(the_song))
#             break
#         else:
#             print('当前选中的是【{0}】，不是【凉凉】，请继续- -'.format(the_song))
#     else:
#         print('现场的观众，你所点播的歌曲马上开始！')
#         break



#####
# def login(a,b=1):
#     print(a,b)
# login(10)

# def fee(*args):
#     for i in args:
#         print(i)
# fee(1,2,43,5,'aaa')

# def fed(**kw):
#     print(kw)
# fed(a=10,b=20,c='a')


# try:
#     pass
# except:
#     pass


# try:
#     # a=1/0
#     # a = open('a.txt','r')
#     # a.write('fsdfsdfdsf')
#     a = 0
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print('......')
# finally:
#     print("......!")




# # pip install xxxxx

# import requests
# from requests import get
# from requests import *
# a = get('http://www')


# class dict:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c


#     def __query(self):
#         s = self.a + self.b
#         pass
#     def update(self):
#         print('xxxxxxx.')
# # a1 = dict(1,2,3)
# # print(a1.a)

# class newdict(dict):
#     pass
#     # def update(self):
#     #     print('.......')
# dic = newdict(1,2,3)
# dic.update()       



# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(j,i,j*i),end='\t')
#     print()


#转换大小写，  还有一种用字典
# a = 'sfasfv'
# str1 = 'qwertyuiopasdfghjklzxcvbnm'
# str2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'

# def login(username,password):
#     if username =='asd' and password == '123':
#         print('success')
#     else:
#         print('error')

# list1 = ['1','2','3','4']

# lis2 = [int(i)**2 for i in list1]
# print(lis2)