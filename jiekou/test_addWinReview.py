import pytest
from jiekou.read_excel import readExcel
from jiekou.do_request import request
# from jiekou.con_mysql import get_session
from jiekou.model import product
import random
import json

def get_data():
    read=readExcel()
    data = read.read_excelDataDict("用例存放地址",1)
    return data

@pytest.fixture(scope="module")
def get_product_and_brand_id(get_session):
    # db_session=get_session()
    product_detail=get_session.query(product).filter(product.delete_mark==0)#获取品牌和产品id
     #封装成这种形式[{"productId":"","brandId":""}]
    product_idList=[]
    for i in product_detail:
        dic={}
        dic["productId"]=i.id
        dic["brandId"]=i.brand_id
        product_idList.append(dic)
    random_num=random.randint(0,len(product_idList)-1)
    product_and_brand_id=product_idList[random_num]
    return product_and_brand_id

@pytest.mark.parametrize("data",get_data())
def test_add_review(data,get_product_and_brand_id,logger):
    logger.info("["+data["Description"]+"]"+"第"+str(data["casesNumber"])+"条用例开始测试---------------")
    # print(data)
    re=request()
    json_para=json.loads(data["Parameters"])
    if json_para["productId"]!="":
        json_para["productId"]=get_product_and_brand_id["productId"]
    if json_para["brandId"]!="":
        json_para["brandId"]=get_product_and_brand_id["brandId"]
    para=json.dumps(json_para)
    logger.info("改造后的参数为："+para)
    # print(para)
    response = re.do_post(data["Interface"],para,data["isMyToken"])
    logger.info("响应结果为："+response)
    json_response=json.loads(response)
    msg=json_response["msg"]
    # print(response)
    # print(type(response))
    assert msg==data["Expect"]
