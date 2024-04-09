from Inquire_mongo import connect_db, all_phenomena
from Inquire_mongo import all_cityname, \
    query_city_data, query_temperature, \
    query_humidity, query_winddirect, \
    query_updatetime, query_code, all_citycode_and_name
from flask import Flask, jsonify, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

"""
Flask是一个轻量级的Python Web框架，
适用于构建简单的Web应用程序和API。它适合用于小型项目、
原型设计或需要快速搭建的应用。Flask提供了灵活的扩展性，
可以根据需要添加各种功能。
"""

# 查询所有城市
# http://127.0.0.1:5000/get_city_names
@app.route('/get_city_names', methods=['GET'])
def get_city_names():
    city_names = all_cityname()
    response = jsonify(city_names)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify({"city_names": city_names})


# 所有天气统计,绘制柱状图用
# http://127.0.0.1:5000/get_query_phenomena
@app.route('/get_query_phenomena', methods=['GET'])
def get_query_phenomena():
    data = all_phenomena()
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(data)


# http://127.0.0.1:5000/get_city_data/{城市名字}
# http://127.0.0.1:5000/get_city_data/北京
@app.route('/get_city_data/<cityname>', methods=['GET'])
def get_city_data(cityname):
    data = query_city_data(cityname)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(data)


# http://127.0.0.1:5000/get_temperature?cityname={cityname}
# http://127.0.0.1:5000/get_temperature?cityname=北京
@app.route('/get_temperature', methods=['GET'])
def get_temperature():
    cityname = request.args.get('cityname')
    data = query_temperature(cityname)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(data)


# http://127.0.0.1:5000/get_humidity?cityname={city_anme}
# http://127.0.0.1:5000/get_humidity?cityname=北京
@app.route('/get_humidity', methods=['GET'])
def get_humidity():
    cityname = request.args.get('cityname')
    data = query_humidity(cityname)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(data)


# http://127.0.0.1:5000/get_winddirect?cityname={city_anme}
# http://127.0.0.1:5000/get_winddirect?cityname=北京
@app.route('/get_winddirect', methods=['GET'])
def get_winddirect():
    cityname = request.args.get('cityname')
    data = query_winddirect(cityname)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(data)


# http://127.0.0.1:5000/get_updatetime?cityname={city_anme}
# http://127.0.0.1:5000/get_updatetime?cityname=北京
@app.route('/get_updatetime', methods=['GET'])
def get_updatetime():
    cityname = request.args.get('cityname')
    data = query_updatetime(cityname)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(data)


# http://127.0.0.1:5000/get_code?cityname={city_anme}
# http://127.0.0.1:5000/get_code?cityname=北京
@app.route('/get_code', methods=['GET'])
def get_code():
    cityname = request.args.get('cityname')
    data = query_code(cityname)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(data)


# http://127.0.0.1:5000/get_all_citycode_and_name
@app.route('/get_all_citycode_and_name', methods=['GET'])
def get_all_citycode_and_name():
    data = all_citycode_and_name()
    # 成功解决问题的关键!!!
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')  # 添加允许所有域名头信息
    return response


# http://127.0.0.1:5000/weather/
@app.route("/weather/<int:citycode>")
def get_city_weather(citycode):
    collection = connect_db()
    weather_data = collection.find({"citycode": citycode})
    history = []
    for data in weather_data:
        weather = {
            "windspeed": str(data["windspeed"]),
            "airpressure": str(data["airpressure"]),
            "wind": data["wind"],
            "windpower": data["windpower"],
            "winddirect": str(data["winddirect"]),
            "humidity": str(data["humidity"]),
            "temperature": str(data["temperature"]),
            "updatetime": data["updatetime"],
            "phenomena": data["phenomena"]
        }
        history.append(weather)
    result = {"history": history}
    return jsonify(result)


# if __name__ == '__main__':
#     app.run()

if __name__ == '__main__':
    app.run(debug=True)
