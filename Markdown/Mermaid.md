# Mermaid

## 作者：ShuHang2

[![build](https://github.com/Anduin2017/HowToCook/actions/workflows/build.yml/badge.svg)](https://github.com/ShuHang2/ShuHang2.github.io)

## [返回主页](../README.md)

[mermaid官方文档](https://mermaid.nodejs.cn/intro/)

## 常用图标类型

使用方法：

1. 在支持Mermaid的Markdown的软件中，在代码块中输入maermaid代码，再将代码块类型改为mermaid
2. 也可以在官网查看本地、网页部署方法

### 流程图

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

### 思维导图

```mermaid
mindmap
  root((mindmap))
    Origins
      Long history
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectiveness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      id(Pen and paper)
      id[Mermaid]
```

各种形状

1. 正方形 `id[ ]`
2. 椭圆形`id( )`
3. 圆形`id(( ))`
4. 砰`id)) ((`
5. 云`id) (`
6. 六边形`id{{ }}`

### XY图

```mermaid
xychart-beta
    title "Sales Revenue"
    x-axis [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    y-axis "Revenue (in $)" 4000 --> 11000
    bar [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
    line [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
```

### 饼图

```mermaid
pie title Pets adopted by volunteers
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 15

```

## 时间线图

```mermaid
timeline
    title History of Social Media Platform
    2002 : LinkedIn
    2004 : Facebook
         : Google
    2005 : Youtube
    2006 : Twitter
```

### GIT图

```mermaid
gitGraph
   commit
   commit
   branch develop
   commit
   commit
   commit
   checkout main
   commit
   commit
```
