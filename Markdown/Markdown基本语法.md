# Markdown基本语法

## 作者：ShuHang2

[![build](https://github.com/Anduin2017/HowToCook/actions/workflows/build.yml/badge.svg)](https://github.com/ShuHang2/ShuHang2.github.io)

## [返回主页](../README.md)

# Markdown编辑器

1. Typora（非常好用）
2. VsCode插件
    1. Markdown All in One（也挺好用、不过只有双屏展示）
    2. Markdown Preview Enhanced

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

使用空白行将一行或多行文本进行分隔，不要用空格（spaces）或制表符（ tabs）缩进段落。

如果缩进四个字符（tabs）就会变成**代码块**

```
I really like using Markdown.

I think I'll use it to format all of my documents from now on.

	Code Block
```

### 效果

I really like using Markdown.

I think I'll use it to format all of my documents from now on.

    Code Block

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
唯一的缺点就是图片的大小不可控，它默认是100%铺满你的屏幕，想要调整要使用HTML中的图片标签
### 格式
```
![随便起名字](本地相对路径、结对路径、两页链接)

![tu](../Att/pp.jpeg)

# HTML图片标签
<img src="./Att/pp.jpeg" alt="BiliBili" width="150" height=auto>
```

### 效果

![tu](../img/pp.jpeg)

#### HTML图片标签
<img src="../Att/pp.jpeg" alt="BiliBili" width="150px" height=auto>

# 给图片添加超链接

因为MarkDown文件支持插入部分HTML标签，因此我们可以使用锚标签来进行实现点击图片进行跳转超链接

```
<a href="https://space.bilibili.com/85119525?spm_id_from=333.1007.0.0">
<img src="../Att/pp.jpeg" alt="BiliBili" width="150" height=auto>
</a>
```
<a href="https://space.bilibili.com/85119525?spm_id_from=333.1007.0.0">
<img src="../Att/pp.jpeg" alt="BiliBili" width="150" height=auto>
</a>

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

***
下面是**脚注语法**的脚注

