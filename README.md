# 炒点python不加SQL
### 数据采集和可视化作业:Python+MongoDb+chart.js实现各个城市天气情况的可视化并使用html+css在web中展示
**[最终效果图](./all_img/dome—OK.png)✨**
![](./all_img/dome—OK.png)
**[天气概览图](./all_img/天气概览.png)**
![](./all_img/天气概览.png)

## 项目结构🗂️
### [run_All.py](./run_All.py)
> 如果没有这个，我就需要先执行[allQuery_api.py](./allQuery_api.py)
再打开[index.html](./index.html)，所以就有这个，直接双击执行便可，会自动打开浏览器看到你想看到的东西，要退出的话CTRL+C
> 
### [index.html](./index.html)
> web展示页，div层如图所示
> 
![](./web设计图.png)
### [Inquire_mongo.py](./Inquire_mongo.py)
> 数据获取和规则处理
> 
### [js/chart.js](./jschart.js)
> 可视化的关键，现学现卖;这个项目的语言结构js占90多就是因为这个文件。
> 
### [allQuery_api.py](./allQuery_api.py)
> api的封装，我前面做了很多的查询规则，所以封装了很多api，其实这次作业能用到的就两个api，加上我自己主动添加的两个需求"湿度变化图"和"天气概览"就四个api，我有时间的话会调用这些api试着多做些可视化操作，练习嘛;
> 
## [绿色安装MongoDB看这篇文章🧐](./mongo从安装到使用.md)
自己写的，一步步来一次装好;
## 源数据的导入🛠️
使用MongoDBCompass可视化工具导入csv
给了一个[csv的源数据](./csv源数据/all_cities_weather_data.csv)，需要先将它倒入到mongoDB中去；
```ssh
新建库:use 库名
新建集合:db.createCollection ("集合名")
```
[具体看这里:mongo从安装到使用.md](./mongo从安装到使用.md)

### 在作业过程中遇到的问题和踩过的坑也记录了下来📜
[挖坑踩坑填坑](./挖坑踩坑填坑.md)







