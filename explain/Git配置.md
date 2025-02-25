1.在vscode使用Git服务
# git设置HTTP代理指令：
```bash
git config --global http.proxy http://127.0.0.1:10809  
```
`http://` +`本地ip` + `http端口`(默认10809)
http端口=socks端口+1
# 测试是否成功

```bash
curl -x http://127.0.0.1:10809 http://ifconfig.me   #访问ifconfig.me
curl -x http://127.0.0.1:10809 http://ifconfig.co   #访问ifconfig.co
```