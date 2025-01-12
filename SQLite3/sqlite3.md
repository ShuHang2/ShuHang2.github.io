# Sqlite3

## 作者：ShuHang2

[![build](https://github.com/Anduin2017/HowToCook/actions/workflows/build.yml/badge.svg)](https://github.com/ShuHang2/ShuHang2.github.io)

## [返回主页](../README.md)

## 介绍

sqlite是一个**精简**关系型数据库，无需配置

## 安装

官网：[Sqlite3](https://www.sqlite.org/index.html)

下载地址：[sqlite3 download](https://www.sqlite.org/download.html)

根据你使用的平台选择你要使用的版本

比如：windows平台选择`Precompiled Binaries for Windows`,下载两个安装包

* `32-bit DLL (x86) for SQLite version 3.46.1.`或`64-bit DLL (x64) for SQLite version 3.46.1.`
* `A bundle of command-line tools for managing SQLite database files, including the command-line shell program, the sqldiff.exe program, and the sqlite3_analyzer.exe program. 64-bit.`

将解压的文件放到你安装应用的文件夹下比如`D:\SQLite`中

```cmd
├─sqldiff.exe 
├─sqlite3.def 
├─sqlite3.dll 
├─sqlite3.exe 
└─sqlite3_analyzer.exe 
```

将`D:\SQLite`添加到`PATH`环境变量

## 启动

1. 打开`cmd`
2. 输入`sqlite3`
