import ast
import pymongo
import requests
import json



def createConn(client, database, collection):
    myclient = pymongo.MongoClient(client)
    mydb = myclient[database]
    mycol = mydb[collection]
    return mycol


db1 = requests.get('http://siddhiartjewellery.true-order.com/WebReporter/api/v1/items', headers={'Content-Type': ''
                                                                                                                 'application/json;charset=UTF-8',
                                                                                                 'X-Auth-Token': '20D48FEA0700964D5FF5A51519F925D464D862798609188500AB67277A82E796FE7A104D6C57DDAB'})
data1=db1.json()['items']

db2 = createConn("mongodb://prabjyot:PiPcJp8UTf6K@localhost:27017/siddhiart", "siddhiart", "items")

print(db2.find())
for i in db2.find():
    print(i)