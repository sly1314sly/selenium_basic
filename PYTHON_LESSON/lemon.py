'''首先获取当前目录下所有文件，然后做如下处理：
01 文件名去重复
02 选出文件大于10m的
03 获取到文件的md5值，然后利用这个md5值对文件名进行重命名（其中md5代表一个文件属性）
04 打印出最后的符合条件的所有文件名'''


# import os,hashlib
# class get_file():
#     def __init__(self,path):
#         self.path=path
#         """path 通过传入制定路径，获取路径下的所有文件名字返回一个1维列表"""
#         self.file_name=[]
#         for (dirpath, dirnames, filenames) in os.walk(self.path):
#             if  filenames:
#                 self.file_name.append(filenames)
#         self.old_file_name=[]
#         for i in self.file_name:
#             for j in i:
#                 self.old_file_name.append(j)
#         self.old_file_name
#         print("old_file       ",self.old_file_name)

#     def count_file(self,filename):
#         count=0
#         for  i  in self.old_file_name:
#             if filename ==i:
#                 count=count+1
#         return count
#     def getBigFileMD5(self,filepath):
#         """获取文件的md5值，防止因为文件过大而发生读取错误，采用分段读取"""
#         if os.path.isfile(filepath):
#             file_md5 = hashlib.md5()
#             maxbuf = 8192          #设置每次读取的字节数
#             f = open(filepath,'rb')
#             while True:
#                 buf = f.read(maxbuf)  
#                 if not buf:
#                     break          #每次读取设置的字节数大小，直到读完后跳出循环    
#                 file_md5.update(buf)   #用数据中的字节更新哈希对象，重复调用相当于链接起来
#             f.close()      
#             hash = file_md5.hexdigest()
#             return str(hash).upper()
#         return None 

#     def unique_absfile(self):
#         """判断文件名在所有文件的列表中出现的次数，大于1则更改文件名字为md5值，并且保留后缀名字，
#         方法返回处理后的文件名字（绝对路径）的列表"""
#         pathname=[]

#         for (dirpath, dirnames, filenames) in os.walk(self.path):   

#             for filename in filenames: 
#                 if self.count_file(filename)>1: #判断文件名字是否重复
#                     file_first_name=filename.split(".")[0]
#                     file_last_name=filename.split(".")[1] 
#                     path_name=os.path.join(dirpath, filename)  #获取重复文件名字的绝对路径

#                     new_filename=self.getBigFileMD5(path_name)+"."+file_last_name#保证改名后，文件的后缀名字不变
#                     os.path.join(dirpath, new_filename)

#                     new_pathname=os.rename(path_name,new_pathname)
#                     pathname=pathname+[new_pathname ]
#                 else:
#                     pathname=pathname+[os.path.join(dirpath, filename)]
#         return pathname 
#     def file_size(self,condition=10):
#         """调用内部方法self.unique_absfile()，获得去重后的文件名字列表（文件名是绝对路径）"""
#         """获取文件大小，以M为单位"""
#         all_file=self.unique_absfile()
#         file_name=[]
#         for i in   all_file:
#             size = float((os.path.getsize(i)/1024))
#             if size>condition:

#                 if "\\" in i:
#                    file_name.append(i.split("\\")[-1]) 
#                 else:
#                     file_name.append(i.split("/")[-1]) 
#         return file_name





# 镜像星星金字塔
# def mirror_star_pyramid(n):
#     i = 1# 给定初始值
#     star_list1 = []# 存正金字塔每一层元素
#     star_list2 = []# 存倒金字塔每一层元素
#     while i <= n:
#         star_list1.append(' '*((n-i)//2) + '*'*i + ' '*((n-i)//2))
#         # n的奇偶性将决定倒金字塔的元素是跟正金字塔一样还是比正金字塔少一层
#         if n % 2:
#             star_list2.append(' '*((i+1)//2) + '*'*(n-i-1) + ' '*((i+1)//2))
#         else:
#             star_list2 = star_list1[::-1]
#         i += 2
#     for each in star_list1:print(each)
#     for each in star_list2:print(each)

# if __name__ == '__main__':
#     mirror_star_pyramid(5)
#     mirror_star_pyramid(6)
