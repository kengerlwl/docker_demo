#coding=utf-8
#coding=gbk
import os, re
import requests
import time

# 要留下就返回true
def is_none(s):
    if s:
        return True
    else:
        return False


# execute command, and return the output
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


def send_msg(msg):
    # url = 'http://110.40.204.239:5700/send_group_msg?group_id={}&message={}'.format(
    #     '590020444',
    #     msg
    # )
    print(msg)
    url = 'http://127.0.0.1:5700/send_private_msg?user_id={}&message={}'.format(
        '2892211452',
        msg
    )
    rsp = requests.get(url)
    print("发送消息结果" + rsp.text)



if __name__ == '__main__':
    all_listen_username = {"testuser", "prk"}
    online_users = {}
    while True:

        # 针对每一个用户都进行检测
        for listen_username in all_listen_username:
            cmd = "w | grep {}".format(listen_username)
            result = execCmd(cmd)
            # print(result)
            result = result.split('\n')
            online_tty = {} # 当前在线终端
            all_msgs = ""
            for i in result:

                try:
                    # 字符串划分
                    i = list(filter(is_none, i.split(' ')))
                    # print(i)
                    username = i[0]
                    id = i[1]
                    
                    date = i[3]

                    # 用人和时间做key值
                    key = date + " " + username

                    online_tty[key] = 1
                    
                    # 剔除掉非目标用户
                    if username != listen_username:
                        continue

                    # 不在，通知并且添加到在线用户
                    if key not in online_users:
                        online_users[key] = {
                            "username":username,
                            "date":date
                        }
                        all_msgs = all_msgs + "{} 于 {} 登录了服务器\n".format(username, date)
    
                except Exception as e:
                    # print(e)
                    pass

            if all_msgs:
                send_msg(all_msgs)


            # 清理掉不在线的终端
            del_key = []

            # 累计的所有终端。减去当前的终端数目，就是下线数目
            for user_key in online_users:
                # print(user_key, online_tty, user_key not in online_tty)
                if user_key not in online_tty:
                    # print("{} 终端已经下线".format(online_users[user_key]))
                    del_key.append(user_key)
            # print(online_tty, online_users, del_key)
            for user_key in del_key:
                online_users.__delitem__(user_key)
                del_msg = "{} 用户已经下线".format(user_key)
                send_msg(del_msg)
        # print(online_users)
        time.sleep(5)
        all_msgs = ""