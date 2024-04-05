# yyym-y 的个人网站

## 说明

本网站基于 Jekyll 并且借助 Github Page 进行部署

网站的 UI 设计是以 [Strata-Jekyll-Theme](https://github.com/old-jekyll-templates/Strata-Jekyll-Theme) 为基础, 之后进行了大量自定义设计和修改而成

> 网站展示

![](/assets/basic/main.png)

![](/assets/basic/postImg.png)


## 基于本网站构建自己的网站

你可以将本网站进行修改, 之后部署到本地或者部署到 Github Page 中

部署到 Github Page 的方法见此链接: [创建你的 GitHub Page](https://docs.github.com/zh/pages/getting-started-with-github-pages/creating-a-github-pages-site)

部署到本地的方法较为麻烦已经繁琐, 但也不会太离谱

部署的教程如下 : [本地部署 Jekyll](https://zhuanlan.zhihu.com/p/139567128)

本地部署完 jekyll 环境后, 使用 `bundle` 来安装项目所需要的依赖

```
bundle install
```

之后在项目的根目录执行 `jekyll` 命令即部署成功

```
bundle exec jekyll serve
```


## 二次开发说明

本项目使用 `jekyll`, `Element` 和 `Vue` 联合开发

项目文件结构如下:


```
yyym-y.github.io
├─ 404.html         # 网站 404 时显示的页面
├─ assets           # 静态资源存放路径
├─ css              # 网站 css 文件存储文件夹
├─ fonts            # 字体文件存储文件夹
├─ Gemfile
├─ Gemfile.lock
├─ index.html       # 网站入口页面
├─ js               # 网站所需 js 文件存储文件夹
├─ LICENSE          # 许可证
├─ pdf              # 博客的 pdf
├─ README.md        # 本文件
├─ robots.txt
├─ siteicon.png     # 网站图标(PC)
├─ touch-icon.png   # 网站图标(移动端)
├─ _config.yml      # jekyll 配置文件
├─ _data            # jekyll 数据
├─ _drafts          # jekyll 草稿
├─ _includes
├─ _layouts         # jekyll 布局文件
└─ _posts           # 博客存放的文件夹
```

### 如何添加自己的博客

#### 增加文章元信息

首先准备一个使用 `markdown` 书写的文章, 你可以复制 `_posts/_defaultes.md` 文件中的内容复制到你的文章开头, 如下所示:

> 真正复制的时候不要包含注释 (# 后面的内容为注释)

```
---
layout : post               # 文章采用的 layout 布局, 不需要动
title : ""                  # 这篇文章的标题
githubUrl : ""              # 这篇文章的 github 链接
pdfUrl : "/pdf/"            # 这篇文章的 pdf 文件路径
cover : "/assets/cover/"    # 文章封面
previousUrl : ""            # 上一篇文章的 url
nextUrl : ""                # 下一篇文章的 url
---

# 下面两行用来显示目录(如果没有将没有目录功能)
* awsl
{:toc}

# 这里是你的正文部分
正文...
```

上面的部分为文章的元信息, 有些部分可以省略

> 比如说你没有 github 链接或者 pdf 链接就可以省略
> 没有上一片文章或者下一篇文章都可以省略

#### 文章的命名以及 url

所有的文章都必须放在 `_post` 目录之下, 文章可以在不同的子文件夹中, 建议按类别区分

`jekyll` 解释器对文章的命名格式有限制:

假设我们的文章名字为 `note.md` , 那么我们需要将名字改为 `2024-03-15-note.markdown`

日期默认含义为文件创建日期(也可以随便填), 此时这个文章的 url 为 `2024/03/15/note`

#### 修改主页显示的文章菜单

主页面的菜单为:

![](/assets/basic/main-menu.png)

我们打开下面的文件 `/js/categoryData.js`:

文件的格式如下所示:

```js
export default {
    point_color : "#0bbd87",

    catagoryInfo : [
      { // 第一层信息
        leftInfo : {},
        rightInfo : {}
      },
    ],
    catagoryVis : [
      {leftVis : false, rightVis : false}, // 第一层可见性
      {leftVis : false, rightVis : null} // 第二层可见性
    ],
    catagoryDir : [
      { // 第一层目录
        leftDir : [],
        rightDir : []
      },
    ]
}
```

`catagoryInfo` 中列出了直接展示在主页面的文章目录信息, 包括名字,封面等等

`catagoryDir` 中包含了点击文章目录信息后展示的内容

`catagoryVis` 代表 `catagoryDir` 的可见性, 取值为 `false` , 不存在则为 `null`

