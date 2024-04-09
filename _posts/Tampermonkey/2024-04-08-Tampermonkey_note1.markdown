---
layout : post
title : "第一个Tampermonkey脚本"
githubUrl : "/404"
pdfUrl : "/404"
cover : "/assets/cover/default.jpg"
previousUrl : ""
nextUrl : ""
---
* awsl
{:toc}

## 初遇 Tampermonkey

某一个夜晚, 在我准备出去吃饭的时候, 浏览器突然蹦出来油猴脚本的更新提示, 虽然不是很想鸟它, 但是不知道怎么就也突然想学油猴脚本了


虽然不是第一次使用油猴脚本, 但是自己也只是在网上找找现成的脚本直接安装, 也是突然就想学习一下具体的语法

一开始在 B 站找了个视频, 发现没有任何屁用, 于是打开浏览器寻找, 结果还真给我找到一个非常不错的教程

教程链接如下 : [油猴开发指南](https://learn.scriptcat.org/)

学习油猴脚本需要有前端编程的经验, 很不巧刚好会前端 ~~~~, 于是便开启了我的脚本之路....


## 油猴脚本概述

所有油猴脚本, 实际上就是一个前端 js 代码植入, 通过这些 js 代码来实现我们的一些功能

一个基本的油猴脚本内容如下所示

```js
// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      2024-04-09
// @description  try to take over the world!
// @author       You
// @match        http://*/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
})();
```

我们主要讲解一下上面的几个注解:

> `@name` : 这个脚本的名字
>
> `@version` : 这个脚本的版本
>
> `@description` : 这个脚本的描述
> 
> `@author` : 这个脚本的作者
>
> `@match` : 这个脚本所适配的网站, 可以有多个, 可以使用通配符 `*`

更多的注解可以查阅官方文档 : [注解官方文档](https://www.tampermonkey.net/documentation.php?ext=dhdg)

> 虽然有些也解释的不明不白....建议不明白直接百度...


## 油猴脚本实践

虽然才看了这么点内容, 但毕竟脚本的核心是 js 代码, 而我对js 代码还算熟悉, 于是直接上手

我早就对 SCNU 的砺儒云课堂非常不满了, 不能保留用户登录信息, 每次登录还挺麻烦的

于是我打算写一个脚本来实现自动化登录

主要的脚本代码如下 : 

```js
// ==UserScript==
// @name         砺儒云课堂自动登录程序
// @namespace    https://moodle.scnu.edu.cn/
// @version      1.0.0
// @description  帮助你自动登录SCNU课程网站-砺儒云课堂
// @author       yyym
// @match        https://moodle.scnu.edu.cn/*
// @match        https://sso.scnu.edu.cn/AccountService/user/login.html
// @match        https://sso.scnu.edu.cn/AccountService/openapi/auth.html*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @require      https://scriptcat.org/lib/513/2.0.0/ElementGetter.js
// @grant        none
// ==/UserScript==


(function() {
    'use strict';
    let username = "username";
    let password = "pwd";

    /* 首先我们需要获取当前网站的 url
    *  因为整个登录过程会跳转到不同的 url, 我希望这个脚本根据不同的 url 来执行不同的逻辑
    *  因为 url 有多个, 所以我也在注解中配置了多个 @match
    */
    let url = window.location.href;
    // 因为网址可能在 ? 带有多个参数, 所以需要过滤掉 ? 后面的参数
    let index = url.lastIndexOf('?');
    if(index != -1) {
        url = url.substring(0, index);
    }

    // 在主登录页面的逻辑, 即砺儒云首页
    if(url == "https://moodle.scnu.edu.cn/") {
        // 通过开发者工具找到对应的 DOM 元素
        let loginButton = document.querySelector(".forgotpass a");
        // if loginButton is null, it mean user has logined
        if(loginButton == null) return;
        loginButton.click(); // js模拟点击跳转
    }
    // 在选择统一身份认证还是游客登录的逻辑, 默认统一身份认证
    if(url == "https://moodle.scnu.edu.cn/login/index.php") {
        // 异步获取 DOM 对象
        elmGetter.get('#ssobtn').then(but => {
            if(but == null) {
                alert("ERROR"); return;
            }
            but.click();
        });
    }
    // 在输入账号密码的逻辑
    if(url == "https://sso.scnu.edu.cn/AccountService/user/login.html") {
        // 如果账号密码错误脚本将在这里被停止
        let msgtext = document.querySelector("#msgtext");
        if(msgtext.innerHTML != "") {
            alert(msgtext.innerHTML);
            return;
        }
        let account_input = document.querySelector("#account");
        let pwd_input = document.querySelector("#password");
        account_input.value = username;
        pwd_input.value = password;
        let but = document.querySelector("#btn-login");
        but.click();
    }
    // 确认登录逻辑
    if(url == "https://sso.scnu.edu.cn/AccountService/openapi/auth.html") {
        let confirm = document.querySelector(".login-check-comfirm a");
        confirm.click();
    }
})();
```

值得注意的是, 我们在一个 `php` 页面执行了异步获取元素的操作

这是因为直接使用 `document.querySelector("...")` 会找不到对象

一般有两种原因, 一个是使用 `iframe` 框架, 一个是在查找元素的时候页面还没有加载

经过排查属于第二种情况, 所以我打算使用 `ElementGetter 库`

`ElementGetter 库` 的使用教程: [ElementGetter 库教程](https://bbs.tampermonkey.net.cn/thread-2726-1-1.html)