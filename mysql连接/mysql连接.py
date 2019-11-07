


# 导入pymysql模块
import  pymysql
import  json
import  decimal
####################针对Decimal类型转换#######################################
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)
# 使用：
# data = json.dumps(数据, cls=DecimalEncoder,ensure_ascii=False)
# with open('omo_pe_question_path.json', 'w', encoding="utf-8") as f:
#     f.write(data)
###########################################################

# 连接database
# conn = pymysql.connect(host=“你的数据库地址”, user=“用户名”,password=“密码”,database=“数据库名”,charset=“utf8”)
db = pymysql.connect(host='39.107.26.185', user='xieyalong',password='xieyalong',database='omo_military',charset='utf8',port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql = "select * from omo_resource;"
sql = "select * from omo_military_user;"
sql = "select * from omo_pe_question_path;"


results=[]
columns= []
try:
    print("-------------执行sql-------------")
    # 执行sql语句
    cur.execute(sql)
    # 获取查询的所有记录
    results = cur.fetchall()
    #获取表字段
    fields = cur.description
    # # print(results)
    # data = json.dumps(results, cls=DecimalEncoder,ensure_ascii=False)
    # print(data)
    # with open('omo_pe_question_path.json', 'w', encoding="utf-8") as f:
    #     f.write(data)

    # 定义字段名的列表
    for item in fields:
        columns.append(item[0])
    # print('字段名称=',columns,'元组=',item)


    # 遍历结果
    # for row in results:
    #     id = row[0]
    #     name = row[1]
    #     password = row[2]
    #     print(id, name, password)
    listData=[]
    # 遍历每行
    for row in results:
        # (54016, 1637, '3,5,7,8,9', 0, 204, 0, '', 0, 2, 1553841940, 1553841940, '')
        # print('每行的数据',row)
        i=0
        # 定义Python 字典
        map = {}
        #遍历没列
        for item in row:
            map[columns[i]]=item
            i=i+1
        # print(map)
        listData.append(map)

    jsonData = json.dumps(listData, cls=DecimalEncoder, ensure_ascii=False)
    print(jsonData)
    with open('omo_pe_question_path.json', 'w', encoding="utf-8") as f:
        f.write(jsonData)
except Exception as e:
    raise e
finally:
    db.close()  # 关闭连接

def runQql():
    pass


def setData():
    pass


