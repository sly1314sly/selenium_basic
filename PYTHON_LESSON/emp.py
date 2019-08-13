#一、类和实例的定义
# class Employee:  #定义一个类
    
#     pass

# emp_1 = Employee()  #调用这个类
# emp_2 = Employee()

# print(emp_1) 
# print(emp_2)

# #创建对象，给对象赋值
# emp_1.first='john'  
# emp_1.last='work'
# emp_1.email='john@123.com'
# emp_1.pay=10000

# emp_2.first='mike'
# emp_2.last='little'
# emp_2.email='mike@123.com'
# emp_2.pay=12000

# # 打印这个对象的值
# print(emp_1.first) 
# print(emp_2.first)
 
#每次给对象，每次赋值很麻烦，下面方法，给一个init构造器
###########################################################################################################
 
# class Employee:  #定义一个类
    
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.email = first+'@123.com'   
#         self.pay = pay
    
# emp_1 = Employee('john','work',10000)  #调用这个类
# emp_2 = Employee('mike','little',12000)
    
# print(emp_1) 
# print(emp_2)


# #每次需要需求，这样每次都要写，不够方便 ，用方法去操作
# print('{} {} {} {}'.format(emp_1.first,emp_1.last,emp_1.email,emp_1.pay)) 
# print('{} {} {} {}'.format(emp_2.first,emp_2.last,emp_2.email,emp_2.pay)) 
###########################################################################################################
# class Employee:  #定义一个类
    
#     def __init__(self,first,last,pay): #制作了一个构造器
#         self.first = first
#         self.last = last
#         self.email = first+'@123.com'   
#         self.pay = pay

#     def fullname(self):  #定义了一个方法
#         return('{} {} '.format(self.first,self.last))  


# emp_1 = Employee('john','work',10000)  #调用这个类
# emp_2 = Employee('mike','little',12000)
    
# print(emp_1) 
# print(emp_2)

# #打印的时候直接调用这个方法
# print(emp_1.fullname()) 

###########################################################################################################
# #二、类变量的使用
# class Employee:  #定义一个类
    
#     pay_amount = 1.2 #类的成员变量
#     num_emps =0

#     def __init__(self,first,last,pay): #制作了一个构造器
#         self.first = first
#         self.last = last
#         self.email = first+'@123.com'   
#         self.pay = pay
#         Employee.num_emps+=1
    
#     def fullname(self):  #定义了一个方法
#         return('{} {} '.format(self.first,self.last))  

#     def pay_raise(self):  #定义一个方法
#         self.pay = self.pay * self.pay_amount   #使用类里面的成员变量
    

# print(Employee.num_emps)  

# emp_1 = Employee('john','work',10000)  #调用这个类
# emp_2 = Employee('mike','little',12000)

# print(Employee.num_emps)
# #外面根据不同要求单独改变费率
# emp_1.pay_amount = 2 
# emp_2.pay_amount = 1.4 

# emp_1.pay_raise()
# emp_2.pay_raise()

# print(emp_1.pay) 
# print(emp_2.pay) 
###########################################################################################################
#三、类方法和静态方法
class Employee:  #定义一个类
    

    def __init__(self,first,last,pay): #制作了一个构造器
        self.first = first
        self.last = last
        self.email = first+'@123.com'   
        self.pay = pay

    
    def fullname(self):  #定义了一个方法
        return('{} {} '.format(self.first,self.last))  

    def pay_raise(self):  #定义一个方法
        self.pay = self.pay * self.pay_amount   #使用类里面的成员变量
    
    @classmethod #类的静态方法 调用
    def set_raise_amount(cls,amount):
        cls.pay_amount = amount
    
    # @staticmethod   #类的静态方法 调用

emp_1 = Employee('john','work',10000)  #调用这个类
emp_2 = Employee('mike','little',12000)

#外面根据不同要求改变费率
Employee.set_raise_amount(1.5)

print(emp_1.pay_amount) 
print(emp_2.pay_amount) 