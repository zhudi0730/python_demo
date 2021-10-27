
from ctypes import *
import os, sqlite3
import json

db_file = os.path.join(os.path.dirname('__file__'), 'sqlite.db')

"""python计算sqlite数据库中的数据count"""
if __name__ == '__main__':
    # pDll = CDLL("./fanucDll01.dll")
    #
    # ########## 指定 函数的参数类型 #################
    # pDll.init.argtypes = [c_char_p]
    # # 第一个参数
    # arg1 = c_char_p(bytes("192.168.3.9", 'utf-8'))
    # arg2 = c_char_p(bytes("R201", 'utf-8'))
    # ########## 指定 函数的返回类型 #################
    # pDll.collectData.restype = c_char_p
    #
    # ########### 调用动态链接库函数 ##################
    # # pDll.init(b'192.168.3.9', b'R201')
    #
    # pDll.init(arg1, arg2)
    # for i in range(0, 100):
    #     # print(str(i))
    #     res = pDll.collectData().decode()
    #
    # #打印返回结果
    #     print(res) #返回的是utf-8编码的数据，需要解码
    # # print(res)
    #     item = [i for i in res.split()]
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select count(*) from current_real_time')
    cur_num =cursor.fetchone()
    print(cur_num[0])