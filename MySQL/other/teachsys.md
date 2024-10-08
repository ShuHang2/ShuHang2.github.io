# teachsys

[![build](https://github.com/Anduin2017/HowToCook/actions/workflows/build.yml/badge.svg)](https://github.com/ShuHang2/ShuHang2.github.io)

# [返回目录](MySQL.MD)

## Student 结构

| 名称  | 数据类型  | 是否可为 NULL | 是否为键 | 默认值 | 描述 |
| ----- | --------- | ------------- | -------- | ------ | ---- |
| sno   | Char (5)  | 否            | 是       |        | 学号 |
| sname | Char (20) | 否            | 否       |        | 姓名 |
| ssex  | Char (2)  | 否            | 否       | 男     | 性别 |
| sage  | tinyint   | 否            | 否       |        | 年龄 |
| sdept | Char (10) | 是            | 否       |        | 系别 |

### Student样本数据

| Sno | Sname | Ssex | Sage | Sdept |
| --- | --- | --- | --- | --- |
| 03001 | 李勇 | 男 | 20 | CS |
| 04001 | 刘晨 | 女 | 19 | IS |
| 04002 | 张立 | 男 | 19 | IS |
| 06001 | 张天 | 男 | 18 | CS |
| 07001 | 王敏 | 女 | 18 | MA |

## SC 结构

| Col Name | Data Type | NULL | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| sno | Char (5) | n | Primary |  | 学号 |
| sname | Char (20) | n |  |  | 姓名 |
| ssex | Char (2) | n |  | 男 | 性别 |
| sage | tinyint | n |  |  | 年龄 |
| sdept | Char (10) | y |  |  | 系别 |

### SC样本数据

| Sno   | Cno  | Grade |
| ----- | ---- | ----- |
| 03001 | 3001 | 95    |
| 03001 | 3007 | 93    |
| 03001 | 3008 | 90    |
| 03001 | 3009 | 87    |
| 03001 | 7001 | 92    |
| 04001 | 3001 | 88    |
| 04001 | 3009 | 89    |
| 04001 | 7001 | 87    |
| 04002 | 3007 | 85 |
| 04002 | 3008 | 87 |
| 04002 | 7001 | 78 |
| 06001 | 3007 | 87 |
| 06001 | 3008 | 88 |
| 06001 | 3009 | NULL |
| 06001 | 7001 | 92 |
| 07001 | 7001 | 94 |

## course 结构

| Col Name | Data Type | NULL | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| sno | Char (5) | n | Primary |  | 学号 |
| cno | Char (4) | n | Primary |  | 课程号 |
| grade | tinyint | y |  |  | 成绩 |

### course样本数据

| 编号 | 课程名称 | 对应编号 | 学分 |
| --- | --- | --- | --- |
| 3001 | 程序设计语言 | 3009 | 3 |
| 3007 | 数据库   | 3008 | 3   |
| 3008 | 数据结构 | 3001 | 3   |
| 3009 | 数据处理 |      | 3   |
| 7001 | 数学     |      | 6   |
