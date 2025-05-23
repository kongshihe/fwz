# 微信朋友圈房产营销助手

[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)

一个智能的房产营销助手，帮助您生成专业的朋友圈房产营销内容。

## 功能特点

- 🏠 智能解析房源信息
- 📝 自动生成多种风格的营销文案
- 🗺️ 生成房源位置地图
- 🎨 创建专业的营销图片
- 😊 智能添加表情符号
- 🏷️ 自动添加热门话题标签

## 安装说明

1. 克隆项目到本地：
```bash
git clone https://github.com/yourusername/wechat-moments-assistant.git
cd wechat-moments-assistant
```

2. 安装依赖：
```bash
pip install -r requirements.txt
npm install
```

3. 配置环境变量：
- 复制 `.env.example` 文件为 `.env`
- 填入必要的API密钥和配置信息

## 使用方法

1. 启动服务：
```bash
python marketing_assistant.py
```

2. 输入房源信息，例如：
```
急售！世纪公园旁电梯两房，建面89平中间楼层，满五唯一税费省10万，对口明珠小学，房东置换诚意出售
```

3. 系统将自动生成：
- 房源信息解析结果
- 营销图片
- 位置地图
- 多个文案模板

## 配置说明

在 `config.json` 中可以自定义：
- 文案模板样式
- 图片生成参数
- 地图显示范围
- 表情符号密度
- 必加话题标签

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 许可证

本项目采用 ISC 许可证。