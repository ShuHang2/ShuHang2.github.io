# 基本资料

项目名称：Markdown基本语法

Github地址: [ShuHang2-Github](https://github.com/ShuHang2/ShuHang2.github.io)

## [返回主页](../README.md)

# 标题编号

### 格式

```
# h1
## h2
### h3
#### h4
##### h5
```

### 效果

# h1

## h2
### h3
#### h4
##### h5

# 段落语法

### 格式

使用空白行将一行或多行文本进行分隔，不要用空格（spaces）或制表符（ tabs）缩进段落

```
I really like using Markdown.

I think I'll use it to format all of my documents from now on.
```

### 效果

I really like using Markdown.

I think I'll use it to format all of my documents from now on.

# 强调语法

斜体、粗体、同时粗体和斜体、删除线

### 格式

```
*斜体*  **粗体**  ***同时粗体和斜体***
~~删除线~~
```

### 效果

*斜体*  **粗体**  ***同时粗体和斜体***

~~删除线~~

# 分隔线语法

使用三个或多个星号 (`***`)、破折号 (`---`) 或下划线 (`___`) 

### 格式

```
***
---
___
```

### 效果

***
---
___

# 列表语法

可以将多个条目组织成有序或无序列表.

## 有序列表

### 格式

```
* First item
* Second item
* Third item
* Fourth item
```

### 效果

1. First item
2. Second item
3. Third item
4. Fourth item

## 无序列表

### 格式

```
- First item
- Second item
- Third item
- Fourth item
```

### 效果

- First item
- Second item
- Third item
- Fourth item

# 任务列表语法

### 格式

```
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```

### 效果

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

# 超链接语法

点击跳转

### 格式

```
[shuhang2的笔记](https://shuhang2.github.io/)
```

### 效果

[shuhang2的笔记](https://shuhang2.github.io/)

# 图片插入语法

### 格式

![随便起名字](本地相对路径、结对路径、两页链接)

```
![随便起名字](./img/1.png)
```

### 效果

![tu](../Att/pp.jpeg)

# 代码语法

一个或多个反引号

### 格式

````
`圆周率`
```
3.1415926
```
````

### 效果

`圆周率`

```
3.1415926
```

# 表格语法

三个或多个连字符（`---`）创建每列的标题，并使用管道（`|`）分隔每列

### 格式

```
| 名字 | 年龄 |
| ---- | ---- |
| 张三 | 18   |
```

### 效果

| 名字 | 年龄 |
| ---- | ---- |
| 张三 | 18   |

## 对齐

通过在标题行中的连字符的左侧，右侧或两侧添加冒号（`:`），将列中的文本对齐到左侧，右侧或中心。

### 格式

```
| 名字 | 年龄 | 性别 |
| :--: | :--- | ---: |
| 张三 | 18   |   男 |
```

### 效果

| 名字 | 年龄 | 性别 |
| :--: | :--- | ---: |
| 张三 | 18   |   男 |

# 脚注

在方括号（`[^1]`）内添加插入符号和标识符。标识符可以是数字或单词

在括号内使用另一个插入符号和数字添加脚注，并用冒号和文本（`[^1]: My footnote.`）

### 格式

```
Here's a simple footnote,[^1] and here's a longer one.[^2]


[^1]: This is the first footnote.
[^2]: dfadfaadfa
```

### 效果

Here's a simple footnote,[^1] and here's a longer one.[^2]

[^1]: This is the first footnote.

[^2]: dfadfaadfa

# 引用语法

创建块引用，请在段落前添加一个 `>` 符号。使用的比较少，一般都直接用代码块

### 格式

```
> Dorothy followed her through many of the beautiful rooms in her castle.
```

### 效果

> Dorothy followed her through many of the beautiful rooms in her castle.
