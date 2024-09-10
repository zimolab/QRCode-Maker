# QRCode Maker

## 概述

本项目的主要功能是为用户提供二维码生成功能，支持将生成的二维码保存为本地图片文件，支持调整二维码大小、码元颜色、背景色、容错率等参数。
本项目提供了一个简单易用的图形用户界面，方便用户快速调整参数。

> Tip: 同时，本项目还是[`PyGUIAdapter`](https://github.com/zimolab/PyGUIAdapter)的示例项目。
> 开发者可以通过本项目学习如何从零开始构建GUI应用程序。
> 
> 本项目的入口函数在[`main.py`](main.py)文件中，核心代码在[`qrcode_maker`](qrcode_maker/)包下。
> 

## 运行本项目

> `QRCode Maker`项目使用poetry作为依赖管理工具，请确保已安装poetry。

1. 将项目仓库克隆到本地。
```shell
git clone https://github.com/zimolab/QRCodeMaker.git
```

2. 进入项目目录，安装依赖。
```shell
cd QRCode-Makder/
poetry install
```

3. 激活虚拟环境
```shell
poetry shell
```

4. 运行项目
```shell
python main.py
```

## 打包本项目




## 许可证

本项目基于[GPP v3](/LICENSE.txt)许可证进行分发，请遵守相关条款。

