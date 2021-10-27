
from ctypes import *
import os, sqlite3
import json

db_file = os.path.join(os.path.dirname('__file__'), 'sqlite.db')

"""python加载json文件demo"""
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
    #     try:
    #         conn = sqlite3.connect(db_file)
    #         cursor = conn.cursor()
    #         cursor.execute('insert into current_hour values (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
    #             item[0], item[1], json.loads(item[4]), json.loads(item[5]), json.loads(item[6]),
    #             json.loads(item[7]), json.loads(item[8]), json.loads(item[9]), json.loads(item[10]),
    #             json.loads(item[11]),
    #             json.loads(item[12]), json.loads(item[13]), json.loads(item[14])))
    #         conn.commit()
    #     except:
    #         print('更新小时数据出错')
    #     finally:
    #         cursor.close()
    #         conn.close()







    json_filename = 'config.json'  # 这是json文件存放的位置
    # # txt_filename = '/home/hjxu/AI_Challenger-master/code_xu/12.02/finnal.txt'  # 这是保存txt文件的位置
    # # file = open(txt_filename, 'w')
    # with open(json_filename, 'r') as f:
    #     pop_data = json.load(f)
    #     print(pop_data)
    #     label_id = pop_data['name']
    #     image_id = pop_data['ip']
    #     print(label_id + " " + image_id)
    #         # file.write(temp + '\n')
    #     # file.close()

    with open(json_filename, 'r') as f:
        config_data = json.load(f)
        collect_time = config_data['collect_time']
        refresh_time = config_data['refresh_time']
        data_num = config_data['data_num']
        res = collect_time + refresh_time + data_num
        print(res)




    # t = range(1, 101)