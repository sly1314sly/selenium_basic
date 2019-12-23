
import unittest
from ddt import ddt,data,file_data,unpack

def get_nums():
    return [["xiaoming","123456"], ["xiaohong","123"], ["xiaozhang",'1234']]

@ddt
class TestDDT(unittest.TestCase):
    
    @data(*get_nums())
    @unpack
    def test_case3(self,username,password):
        print(username,"-----", password,"------")


    # @data({'username':'xxxxxx1','password':'12345','repass':'1231','email':'12321@11.com'},{'username':'xxxxxx2','password':'12345','repass':'1231','email':'12321@11.com'},{'username':'xxxxxx3','password':'12345','repass':'1231','email':'12321@11.com'})
    # def test_case1(self,value):
    #     # data = {username:'xxxxxx',password:'12345',repass:'1231',email:'12321@11.com'}
    #     print('-----------',value['username'])
    #     print('-----------',value['password'])
    #     print('-----------',value['repass'])

    # @file_data('test_demo_data.json')
    # def test_case2(self,start,end,value):
    #     print("-----",start,end,value,"----")


    


if __name__ == "__main__":
    unittest.main(verbosity=2)

