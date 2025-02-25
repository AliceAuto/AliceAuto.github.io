---
layout: post
---
# 如何参与贡献?
>### 1.安装python3以上的解释器

>### 2:安装上git

>### 3:安装vscode以及一些插件
>
>**Chinese (Simplified) Language Pack for Visual Studio Code**![alt text](image-2.png)
>**Auto Run command:**![alt text](image.png)
>**Competitive Programming Helper:**![alt text](image-1.png)
>**Drawio Preview:**![alt text](image-3.png)
>**Markdown All in One:**![alt text](image-4.png)
>**Markdown Previed Enhanced:**![alt text](image-5.png)
>**Markdown PDF:**![alt text](image-6.png)
>**Paste Image:**![alt text](image-7.png)
>**HTML Preview:**![alt text](image-8.png)
>**HTML CSS Support:**![alt text](image-9.png)

>### 4:为git进行配置
> 
>在vscode使用Git服务
> # git设置HTTP代理指令：
> ```bash
> git config --global http.proxy http://127.0.0.1:10809  
> ```
> `http://` +`本地ip` + `http端口`(默认10809,具体看你的VPN的全局代理端口配置文件)
> http端口=socks端口+1
> # 测试是否成功
> 
> ```bash
> curl -x http://127.0.0.1:10809 http://ifconfig.me   #访问ifconfig.me
> curl -x http://127.0.0.1:10809 http://ifconfig.co   #访问ifconfig.co
> ```



><div style="color:red"> else<strong>(平替git方案)</strong>: 使用Github desktop进行远程控制</div>

>### 5:Fork AliceAuto.github.io仓库
> 在vscode中通过url克隆远程仓库到本地


>### 6:进行工作区功能测试

>### 7:提交PR

>### 8:等待管理员审核

> 额外<bar><strong>
以CodeSpace文件夹打开新窗口，在这个窗口中配置每个人的代码环境，如编译链脚本配置
</strong>

>### 教程:
> <video src="URL" controls="controls" style="width: 100%"></video> 