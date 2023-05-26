# run



```
docker run -d \
  -v $PWD/config.json:/config.json \
  -v $PWD/get_ip.sh:/get_ip.sh \
  --network host \
  newfuture/ddns
```

由于ddns的容器内比较精简，所以没有curl等命令。
这点要注意，如果是编写的脚步。可能得自己Dockerfile编译容器。





#### 配置参数表

| key    | type               | required | default     | description       | tips                                                         |
| ------ | ------------------ | -------- | ----------- | ----------------- | ------------------------------------------------------------ |
| id     | string             | √        | 无          | api 访问 ID       | Cloudflare 为邮箱(使用 Token 时留空) HE.net 可留空           |
| token  | string             | √        | 无          | api 授权 token    | 部分平台叫 secret key , **反馈粘贴时删除**                   |
| dns    | string             | No       | `"dnspod"`  | dns 服务商        | 阿里 DNS 为`alidns`, Cloudflare 为 `cloudflare`, dns.com 为 `dnscom`, DNSPOD 国内为 `dnspod`, DNSPOD 国际版为 `dnspod_com`, HE.net 为`he`, 华为 DNS 为`huaweidns`, 自定义回调为`callback` |
| ipv4   | array              | No       | `[]`        | ipv4 域名列表     | 为`[]`时,不会获取和更新 IPv4 地址                            |
| ipv6   | array              | No       | `[]`        | ipv6 域名列表     | 为`[]`时,不会获取和更新 IPv6 地址                            |
| index4 | string\|int\|array | No       | `"default"` | ipv4 获取方式     | 可设置`网卡`,`内网`,`公网`,`正则`等方式                      |
| index6 | string\|int\|array | No       | `"default"` | ipv6 获取方式     | 可设置`网卡`,`内网`,`公网`,`正则`等方式                      |
| ttl    | number             | No       | `null`      | DNS 解析 TTL 时间 | 不设置采用 DNS 默认策略                                      |
| proxy  | string             | No       | 无          | http 代理`;`分割  | 多代理逐个尝试直到成功,`DIRECT`为直连                        |
| debug  | bool               | No       | `false`     | 是否开启调试      | 运行异常时,打开调试输出,方便诊断错误                         |
| cache  | string\|bool       | No       | `true`      | 是否缓存记录      | 正常情况打开避免频繁更新,默认位置为临时目录下`ddns.cache`, 也可以指定一个具体文件实现自定义文件缓存位置 |

#### index4 和 index6 参数说明

- 数字(`0`,`1`,`2`,`3`等): 第 i 个网卡 ip
- 字符串`"default"`(或者无此项): 系统访问外网默认 IP
- 字符串`"public"`: 使用公网 ip(使用公网 API 查询,url 的简化模式)
- 字符串`"url:xxx"`: 打开 URL `xxx`(如:`"url:http://ip.sb"`),从返回的数据提取 IP 地址
- 字符串字符串"regex:xxx" 正则表达(如"regex:192.*"): 提取ifconfig/ipconfig中与之匹配的首个 IP 地址,注意 json 转义(\要写成\\)
"192.*"表示 192 开头的所有 ip
如果想匹配10.00.xxxx应该写成"regex:10\\.00\\..\*"("\\"json 转义成\)
- 字符串`"cmd:xxxx"`: 执行命令`xxxx`的 stdout 输出结果作为目标 IP
- 字符串`"shell:xxx"`: 使用系统 shell 运行`xxx`,并把结果 stdout 作为目标 IP
- `false`: 强制禁止更新 ipv4 或 ipv6 的 DNS 解析
- 列表：依次执行列表中的index规则，并将最先获得的结果作为目标 IP
  - 例如`["public", "172.*"]`将先查询公网API，未获取到IP后再从本地寻找172开头的IP

