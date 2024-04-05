# mongo从安装到使用

## 下载安装

进入官网：网址 选择版本和系统

怕麻烦的话选择安装包下载，

图片

如果不想爆掉C盘就选择压缩包

解压后手动在根目录下创建data和log两个文件夹

配置环境变量，添加mongoDB的bin路径，比如我的就是：D:\mongoDB_Install\mongodb-win32-x86_64-windows-7.0.7\bin

图片

在data目录里创建一个db文件夹

进入bin目录输入cmd

图片

输入命令：mongod --dbpath D:\mongoDB_Install\mongodb-win32-x86_64-windows-7.0.7\data\db

把D:\mongoDB_Install\mongodb-win32-x86_64-windows-7.0.7\data\db换成你的路径；

回车之后就会有很多东西：

图片

之后打开浏览器输入：http://localhost:27017/

就会有这些东西：

图片

这样安装就是成功了

在前面打开的cmd窗口 CTRL+C结束进程；

## 不需要进入bin目录启动mongo的篇日志方法：

在data目录下创建log文件夹；

在安装根目录即bin同级目录下创建文件：[mongo](https://so.csdn.net/so/search?q=mongo&spm=1001.2101.3001.7020).config

随便一个文本编辑器打开并添加内容：

图片：配置文件

其中D:\mongoDB_Install\mongodb-win32-x86_64-windows-7.0.7改为你的安装路径；

以管理员身份运行cmd并进入bin目录；
图片

输入：mongod -dbpath "D:\mongoDB_Install\mongodb-win32-x86_64-windows-7.0.7\data\db" -logpath "D:\mongoDB_Install\mongodb-win32-x86_64-windows-7.0.7\data\log\mongo.log" -install -serviceName "MongoDB"

其中"D:\mongoDB_Install\mongodb-win32-x86_64-windows-7.0.7\data\db"和

"D:\mongoDB_Install\mongodb-win32-x86_64-windows-7.0.7\data\log\mongo.log"为你的路径

"MongoDB"为服务名;

完了以后启动服务:net start MongoDB

关闭服务:net stop MongoDB

从任务管理器进入服务找到MongoDB(快键m),选择打开服后再次找到MongDB(快键m)或者**win + r** -> 输入 **services.msc**

编辑其属性中的启动类型为手动应用确定;

## **安装MongoDB Compass**

网址:[MongoDB Compass Download (GUI) | MongoDB](https://www.mongodb.com/try/download/atlascli)

选择(stable)稳定版本,系统以及安装方式自选,我选择为windows10 64位(Zip)版解压即用

exe或者msi版本也可以

最后打开连接就可以,我这里换了主题对眼睛好:

图片

## csv数据导入

新建库:use 库名

新建集合:db.createCollection ("集合名")

导入csv数据

图片



## 创建python项目操作mongoDB查询等



## 学习并且使用chart.js库进行数据可视化

官方文档:[Chart.js | Open source HTML5 Charts for your website (chartjs.org)](https://www.chartjs.org/)

## 在web页打开实现可视化和查询操作

说起思路，先说我的博客站是用php+mysql构建的，在自定义页面的时候我就发现在html中竟然可以直接写php代码，然后我就在想，我用python写好各个需求的函数在填入html中怎样？结果一了解还真有这个库PyScrip

使用css美化web,怎么绘制有咩的css?



问题处理：

图片：

![](G:\my_file\王老师作业_mongoDB应用\城市名的api查询错误排除.png)

```python
# 成功解决问题的关键!!!
response = jsonify(data)
response.headers.add('Access-Control-Allow-Origin', '*')  # 添加允许所有域名的头信息
```



第二api访问错误的问题：

图片

解决办法

```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

一些错误处理：挖坑踩坑埋坑
