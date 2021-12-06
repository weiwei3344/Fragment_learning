# HTML标签

## 1、HTML语法规范

### 1.1 基本语法概述

1. HTML标签是由尖括号包围的关键词，例如`<html>`

2. HTML标签通常是承兑出现的，例如`<html>`和`</html>`。我们称为双标签。标签对中的第一个标签是开始标签，第二个标签是结束标签

3. 有些特殊的标签必须是单个标签（极少情况下，例如`<br>`）,我们称为单标签

### 1.2 标签关系

双标签关系可以分为两类:<span style="color:red">包含关系和并列关系</span>

<span style="color: blue">包含关系</span>

```html
<head>
    <title></title>
</head>
```

<span style="color: blue">并列关系</span>

``` html
<head>
</head>
<body>
</body>
```

<span style="color: blue">单标签</span> （还有一些input，自定义标签）

``` html
<br />
```

##  2、HTML基本结构标签

### 2.1 第一个HTML

​	每一个网页都会有一个基本的结构标签（也称为骨架标签），页面内容也是在这些基本标签上书写

| 标签名            | 定义       | 说明                                                     |
| ----------------- | ---------- | -------------------------------------------------------- |
| `<html></html>`   | HTML标签   | 页面中最大的标签，我们称为根标签                         |
| `<head></head>`   | 文档的头部 | 在head标签中我们必须设置的标签是title标签                |
| `<title></title>` | 文档的标题 | 页面拥有一个属于自己的网页标题                           |
| `<body></body>`   | 文档的主体 | 元素包含文档的所有内容，页面内容基本上都是放在body里面的 |

> 第一个网页
>

```html
<html>
    <head>
        <title></title>
    </head>
    <body>
        
    </body>
</html>
```

**看图说话**

![基本结构标签](C:\Users\weiwei\AppData\Roaming\Typora\typora-user-images\image-20211130211638253.png)

## 3、网页开发工具

### 3.1 文档类型声明标签

​	`<!DOCTYPE html>`文档类型声明，**作用**：告诉浏览器使用哪种HTML版本来显示网页

```html
<!DOCTYPE html>
```

​	这句代码的意思是:**当前页面采用的是HTML5版本来显示网页**

**注意**：

1. `<!DOCTYPE>`声明位于文档中的最前面的位置，处于`<html>`标签之前

2. `<!DOCTYPE>`不是一个HTML标签，他就是文档类型的声明标签

### 3.2 lang语言种类

​	用来定义当前文档显示的语言

1. en定义语言为英语

2. zh-CN定义语言为中文

​	简单来说，定义为en就是英文网页，定义zh-CN就是中文网页

​	其实对于文档显示来说，定义成en的文档也可以显示中文，定义zh-CN的文档也可以显示英文，这个属性对于浏览器和搜索引擎还是很有作用的

### 3.3 字符集

​	字符集（Character set）是多个字符的集合。以便计算机能够识别和存储各种文字。

​	在`<head>`标签内，可以通过`<meta>`标签的<span style="color:red">charset</span>属性来规定HTML文档应该使用哪种字符编码

<meta charset="UTF-8">

​	charset常用的值有： GB2312、BIG5、GBK和UTF-8，其中<span style="color:red">UTF-8</span>也被称为万国码，基本包含了全世界所有国家需要用到的字符。

​	**<span style="color:red">注意</span>**：上面语法是必须要写的代码，否则可能会引起乱码的情况。一般情况下，统一使用“UTF-8”编码，尽量写成标准的“UTF-8”，不要写成“utf8”或者“UTF8”
