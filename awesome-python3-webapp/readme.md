[TOC]

# 概述
目标是一个Blog网站，包含日志、用户和评论3大部分

# 环境

## Python版本
要求: Python 3.x
实际: Mac环境是3.6
> 查看Python版本的命令`$ Python3 --version`

## 数据库版本
要求: MySql 5.x
实际: Mac环境是Community5.7
> 查看是否成功安装MySql`在系统设置中有MySQL图标`

## 需要的第三方库
1. aiohttp(异步框架)
   > 安装命令`$ pip3 install aiohttp`
2. jinja2(前端模板引擎)
   > 安装命令`$ pip3 install jinja2`
3. aiomysql(异步数据库驱动)
   > 安装命令`$ pip3 install aiomysql`

## 项目目录
```
awesome-python3-webapp/  <-- 根目录
|
+- backup/               <-- 备份目录
|
+- conf/                 <-- 配置文件
|
+- dist/                 <-- 打包目录
|
+- www/                  <-- Web目录，存放.py文件
|  |
|  +- static/            <-- 存放静态文件
|  |
|  +- templates/         <-- 存放模板文件
|
+- ios/                  <-- 存放iOS App工程
|
+- LICENSE               <-- 代码LICENSE
```

## 开发工具
Visual Studio Code for Mac
