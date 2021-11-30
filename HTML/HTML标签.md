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

