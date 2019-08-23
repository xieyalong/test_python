
import  json
import ast

########################
#python类型转json
def toJson(obj):
    return json.dumps(obj,ensure_ascii=False)

########################
#json转list
def josnToList(jsonList):
    return json.loads(jsonList)
########################
#json转map
def josnToDict(jsonDict):
    return json.loads(jsonDict)
########################
#obj转字符串
def toStr(obj):
    return str(obj)
#字符串转map
def strToDict(str):
    return ast.literal_eval(str)
########################
#字符串转map
def strToList(str):
    return ast.literal_eval(str)
#字符串转json
def strToJson(data):
    json.loads(data)
########################
#list转元组
def listToTuple(obj):
    return tuple(obj)
########################
#list元组转map [('Bdpagetype', '1')]
def listTupletoDict(listTuple):
    return dict(listTuple)
########################
#元组转list
def tupleToList(obj):
    return list(obj)