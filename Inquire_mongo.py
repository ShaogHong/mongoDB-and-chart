import json
from pymongo import MongoClient

# 全局的MongoClient实例
client = MongoClient('localhost', 27017)
db = client['tian_qi']
collection = db['tianQi_data']

# 连接数据库
def connect_db():
    return collection

# 查询某个城市的数据函数
def query_city_data(cityname):
    collection = connect_db()

    projection = {'phenomena': 1, 'citycode': 1, 'winddirect': 1, 'humidity': 1, 'temperature': 1, 'updatetime': 1}
    results = collection.find({'cityname': cityname}, projection)

    data = {
        'citycode': [int(results[0]['citycode'])],
        'cityname': [cityname],
        'winddirect': [],
        'humidity': [],
        'temperature': [],
        'updatetime': [],
        'phenomena': []
    }

    for result in results:
        data['phenomena'].append(result['phenomena'])
        data['winddirect'].append(result['winddirect'])
        data['humidity'].append(result['humidity'])
        data['temperature'].append(result['temperature'])
        data['updatetime'].append(result['updatetime'])

    return data

# 查询温度的函数
def query_temperature(cityname):
    collection = connect_db()
    projection = {'temperature': 1}
    result = collection.find_one({'cityname': cityname}, projection)
    temperature_data = {
        'temperature': result['temperature']
    }
    return temperature_data

# 查询指定城市代码
def query_code(cityname):
    collection = connect_db()
    projection = {'citycode': 1}
    result = collection.find_one({'cityname': cityname}, projection)
    citycode_data = {
        'citycode': result['citycode']
    }
    return citycode_data

# 查询湿度的函数
def query_humidity(cityname):
    collection = connect_db()
    projection = {'humidity': 1}
    result = collection.find_one({'cityname': cityname}, projection)
    humidity_data = {
        'humidity': result['humidity']
    }
    return humidity_data

# 查询风级的函数
def query_winddirect(cityname):
    collection = connect_db()
    projection = {'winddirect': 1}
    result = collection.find_one({'cityname': cityname}, projection)
    winddirect_data = {
        'winddirect': result['winddirect']
    }
    return winddirect_data

# 查询更新时间
def query_updatetime(cityname):
    collection = connect_db()
    projection = {'updatetime': 1}
    result = collection.find_one({'cityname': cityname}, projection)
    updatetime_data = {
        'updatetime': result['updatetime']
    }
    return updatetime_data

# 查询所有城市
def all_cityname():
    collection = connect_db()
    city_names = collection.distinct('cityname')
    return city_names

# 查询所有现象
def all_phenomena():
    collection = connect_db()
    phenomena = collection.find({}, {'phenomena': 1, '_id': 0})
    phenomena_list = [doc['phenomena'] for doc in phenomena]
    json_data = json.dumps({"phenomena": phenomena_list})
    return json_data

# 查询所有城市代码和名称
def all_citycode_and_name():
    collection = connect_db()
    data = {'info': []}
    unique_city_info = collection.distinct('citycode')
    for citycode in unique_city_info:
        city = collection.find_one({'citycode': citycode}, {'citycode': 1, 'cityname': 1, '_id': 0})
        data['info'].append(city)
    return data