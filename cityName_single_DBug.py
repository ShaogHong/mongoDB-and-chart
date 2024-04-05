# coding: UTF-8
"""
@IDE     ：PyCharm
@Author  ：娄南湘先生
@Date    ：2024/4/5,0005 12:13
"""

"""
    城市名称查询指定的几个字段，包括：风向，风力，湿度，气温，更新时间，天气现象
{"history": [{"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u4e1c\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "9.6", "humidity": "79.0", "temperature": "8.3", "updatetime": "2024-03-27 12:55", "phenomena": "\u9634"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u4e1c\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "10.2", "humidity": "76.0", "temperature": "8.5", "updatetime": "2024-03-27 13:55", "phenomena": "\u9634"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "10.7", "humidity": "75.0", "temperature": "10.0", "updatetime": "2024-03-27 14:55", "phenomena": "\u9634"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u4e1c\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "10.4", "humidity": "85.0", "temperature": "9.1", "updatetime": "2024-03-27 15:55", "phenomena": "\u9634"}, {"windspeed": "9999.0", "airpressure": "0.8", "wind": "\u4e1c\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "11.0", "humidity": "80.0", "temperature": "10.2", "updatetime": "2024-03-27 16:55", "phenomena": "\u5c0f\u96e8"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5357\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "11.1", "humidity": "81.0", "temperature": "10.5", "updatetime": "2024-03-27 17:55", "phenomena": "\u9634"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u4e1c\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "11.0", "humidity": "83.0", "temperature": "10.6", "updatetime": "2024-03-27 18:55", "phenomena": "\u9634"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u4e1c\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "9.8", "humidity": "88.0", "temperature": "8.9", "updatetime": "2024-03-27 19:55", "phenomena": "\u9634"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "9.7", "humidity": "91.0", "temperature": "9.4", "updatetime": "2024-03-27 20:55", "phenomena": "\u9634"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u4e1c\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "10.1", "humidity": "90.0", "temperature": "9.6", "updatetime": "2024-03-27 21:50", "phenomena": "\u9634"}, {"windspeed": "9999.0", "airpressure": "0.4", "wind": "\u4e1c\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "10.0", "humidity": "92.0", "temperature": "9.3", "updatetime": "2024-03-27 22:55", "phenomena": "\u5c0f\u96e8"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u4e1c\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "9.9", "humidity": "92.0", "temperature": "9.6", "updatetime": "2024-03-27 23:55", "phenomena": "\u9634"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5357\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "9.2", "humidity": "94.0", "temperature": "8.7", "updatetime": "2024-03-28 00:55", "phenomena": "\u9634"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "13.4", "humidity": "16.0", "temperature": "10.0", "updatetime": "2024-03-28 01:55", "phenomena": "\u591a\u4e91"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "12.6", "humidity": "14.0", "temperature": "9.2", "updatetime": "2024-03-28 02:55", "phenomena": "\u591a\u4e91"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "11.6", "humidity": "15.0", "temperature": "9.2", "updatetime": "2024-03-28 03:55", "phenomena": "\u591a\u4e91"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "10.6", "humidity": "15.0", "temperature": "7.1", "updatetime": "2024-03-28 04:55", "phenomena": "\u591a\u4e91"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u4e1c\u5317\u98ce", "windpower": "4\u7ea7", "winddirect": "9.5", "humidity": "14.0", "temperature": "4.2", "updatetime": "2024-03-28 05:55", "phenomena": "\u591a\u4e91"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "8.9", "humidity": "13.0", "temperature": "5.4", "updatetime": "2024-03-28 06:55", "phenomena": "\u591a\u4e91"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "9.3", "humidity": "13.0", "temperature": "6.0", "updatetime": "2024-03-28 07:55", "phenomena": "\u6674"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "3\u7ea7", "winddirect": "9.7", "humidity": "11.0", "temperature": "5.5", "updatetime": "2024-03-28 08:55", "phenomena": "\u6674"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "4\u7ea7", "winddirect": "10.9", "humidity": "8.0", "temperature": "5.3", "updatetime": "2024-03-28 09:55", "phenomena": "\u6674"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "\u5fae\u98ce", "winddirect": "12.4", "humidity": "8.0", "temperature": "8.8", "updatetime": "2024-03-28 10:55", "phenomena": "\u6674"}, {"windspeed": "9999.0", "airpressure": "0.0", "wind": "\u897f\u5317\u98ce", "windpower": "3\u7ea7", "winddirect": "13.3", "humidity": "7.0", "temperature": "9.5", "updatetime": "2024-03-28 11:55", "phenomena": "\u6674"}]}

"""

from flask import Flask, jsonify
from flask_cors import CORS

from Inquire_mongo import connect_db

app = Flask(__name__)
CORS(app)


# 查询某个城市的数据函数
#  http://localhost:5000/weather/北京
# http://localhost:5000/weather/%E5%8C%97%E4%BA%AC
@app.route("/weather/<cityname>")
def get_city_weather_name(cityname):
    collection = connect_db()
    weather_data = collection.find({"cityname": cityname})
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


if __name__ == "__main__":
    app.run()
