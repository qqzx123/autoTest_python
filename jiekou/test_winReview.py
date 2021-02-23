import pytest
from jiekou.read_excel import readExcel
import json
from jiekou.model import mynews_like
import allure
from jiekou.do_request import request
# 从excel中读取测试数据
# @allure.story("测试用例 1")

def get_data():
    read=readExcel()
    data = read.read_excelDataDict("用例存放地址",4)
    return data

@pytest.mark.parametrize("data",get_data())  # pytest参数化装饰器，第一个参数写自定义的参数名，第二个参数传取到的数据
# data1 = get_data()
# print(data1)
def test_one(data,get_session,logger):         # 上面的参数名是什么，这里也要写什么,以及需要传入conftest.py里面的函数
    # print(data)
    #从接口中获取数据
    logger.info("["+data["Description"]+"]"+"第"+str(data["casesNumber"])+"条用例开始测试---------------")
    logger.info("读取的数据："+str(data))
    re=request()
    response=re.do_post(data["Interface"],data["Parameters"],data["isMyToken"])
    # response=requests.post(data["Interface"],data["Parameters"],headers=header).text

    # print(response)
    response=json.loads(response)
    # print(type(response))
    num=response["data"]["total"]
    # print(type(num))
    allure.step("接口返回的值为："+str(num))
    # print("接口返回的值为："+str(num))
    logger.info("接口返回的值为："+str(num))

    #从数据库中获取数据
    # db_session=get_session()
    total = get_session.query(mynews_like).filter(mynews_like.remind_user_id == "43222974567417036830",mynews_like.info_type=="0",mynews_like.delete_mark=="0",mynews_like.user_id!="43222974567417036830")
    print(type(total))
    num_fromsql=0
    for obj in total:
        # print(obj.id,obj.user_id,obj.remind_user_id)
        num_fromsql=num_fromsql+1
    # print("从数据库中取得的值为："+str(num_fromsql))
    logger.info("从数据库中取得的值为："+str(num_fromsql))
    #断言
    assert num==num_fromsql

# if __name__ == "__main__":
#     # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
#     pytest.main(['--alluredir', './temp'])
#     # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
#     os.system('allure generate ./temp -o ./report --clean')
