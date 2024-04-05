import json
from pymongo import MongoClient

# 连接数据库
def connect_db():
    client = MongoClient('localhost', 27017)
    db = client['tian_qi']
    collection = db['tianQi_data']
    return collection

# 查询某个城市的数据函数
def query_city_data(cityname):
    collection = connect_db()

    projection = {'phenomena': 1,'citycode': 1, 'winddirect': 1, 'humidity': 1, 'temperature': 1, 'updatetime': 1}
    results = collection.find({'cityname': cityname}, projection)

    data = {
        'citycode': [],
        'cityname': [],
        'winddirect': [],
        'humidity': [],
        'temperature': [],
        'updatetime': [],
        'phenomena': []
    }
    data['cityname'].append(cityname)
    data['citycode'].append(int(results[0]['citycode']))
    for result in results:
        # data['citycode'].append(results['citycode'])
        data['phenomena'].append(result['phenomena'])
        data['winddirect'].append(result['winddirect'])
        data['humidity'].append(result['humidity'])
        data['temperature'].append(result['temperature'])
        data['updatetime'].append(result['updatetime'])

    return data

# print(query_city_data('北京'))
# 只保留winddirect字段的数据
# result = query_city_data('北京')
# winddirects = result['winddirect']
# print(winddirects)

# 查询温度的函数
def query_temperature(cityname):
    result = query_city_data(cityname)
    temperature = result['temperature']
    temperature_data = {
        'temperature': temperature
    }
    return temperature_data

# print(query_temperature('北京'))

# 查询指定城市代码
def query_code(cityname):
    result = query_city_data(cityname)
    citycode = result['citycode']
    citycode_data = {
        'citycode': citycode
    }
    return citycode_data

def all_citycode_and_name():
    collection = connect_db()
    data = {'info': []}
    # city_info = collection.find({}, {'citycode': 1, 'cityname': 1, '_id': 0})
    unique_city_info = collection.distinct('citycode')
    for citycode in unique_city_info:
        city = collection.find_one({'citycode': citycode}, {'citycode': 1, 'cityname': 1, '_id': 0})
        data['info'].append(city)

    return data

# print(all_citycode_and_name())
# 查询湿度的函数
def query_humidity(cityname):
    result = query_city_data(cityname)
    humidity = result['humidity']
    humidity_data = {
        'humidity': humidity
    }
    return humidity_data

# print(query_humidity('北京'))

# 查询风级的函数
def query_winddirect(cityname):
    result = query_city_data(cityname)
    winddirect = result['winddirect']
    winddirect_data = {
        'winddirect': winddirect
    }
    return winddirect_data

# print(query_winddirect('北京'))
# 查询更新时间
def query_updatetime(cityname):
    result = query_city_data(cityname)
    updatetime = result['updatetime']
    updatetime_data = {
        'updatetime': updatetime
    }
    return updatetime_data

# print(query_updatetime('北京'))

# 查询所有城市
def all_cityname():
    collection = connect_db()
    # distinct()不重复的元素
    city_names = collection.distinct('cityname')
    return city_names

def all_phenomena():
    collection = connect_db()
    phenomena = collection.find({}, {'phenomena': 1, '_id': 0})  # 返回所有现象，包括重复
    phenomena_list = [doc['phenomena'] for doc in phenomena]
    json_data = json.dumps({"phenomena": phenomena_list})
    return json_data
# print(all_phenomena())