FROM ubuntu

# 设置root用户密码
RUN echo "root:your_password" | chpasswd


# 换源
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list  && \
sed -i s@/security.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list  && \
apt-get clean  && \
apt-get update


RUN echo "==> Install curl and helper tools..."  && \
apt-get update -y                      && \
apt-get install -y  curl


# 配置时间区
RUN apt-get install -y tzdata && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime



# 安装ssh
RUN apt-get  update -y && \
apt-get install -y openssh-server && \
mkdir /run/sshd


# ssh 添加一行允许root登录,以及增加验证方式
RUN sed -i '$a\PermitRootLogin yes' /etc/ssh/sshd_config && \
sed -i '$a\PubkeyAcceptedAlgorithms +ssh-rsa' /etc/ssh/sshd_config && \
sed -i '$a\HostkeyAlgorithms +ssh-rsa' /etc/ssh/sshd_config

# 开启ssh的服务
#RUN /usr/sbin/sshd -D &







WORKDIR /app

RUN mkdir /data

#VOLUME ["/Users/lwl/Documents/GitHub/docker_demo/Ubuntu/data","/data"]

# 复制文件到容器
COPY ./data /data

# ssh 命令
CMD ["/usr/sbin/sshd", "-D"]