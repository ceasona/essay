FROM registry.cn-shanghai.aliyuncs.com/alicea/tc:v1

LABEL maintainer="ceasona@qq.com"


RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

# ENV
COPY .bashrc /root/.bashrc

# JAVA
COPY OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u282b08_openj9-0.24.0.tar.gz /root
RUN mkdir /usr/lib/jvm
RUN tar -zxvf /root/OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u282b08_openj9-0.24.0.tar.gz -C /usr/lib/jvm


# HADOOP
COPY hadoop-3.3.1.tar.gz /root/hadoop-3.3.1.tar.gz
RUN tar -zxvf /root/hadoop-3.3.1.tar.gz -C /opt

# HIVE
COPY apache-hive-3.1.2-bin.tar.gz /root/apache-hive-3.1.2-bin.tar.gz
RUN tar -zxvf /root/apache-hive-3.1.2-bin.tar.gz -C /opt

# REMOVE
RUN rm /root/hadoop-3.3.1.tar.gz /root/OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u282b08_openj9-0.24.0.tar.gz
RUN rm /root/apache-hive-3.1.2-bin.tar.gz

# CHOWN
RUN useradd hadoop && mkdir -p /home/hadoop && chown hadoop /home/hadoop  -R
RUN chown hadoop:hadoop -R /opt/hadoop-3.3.1
RUN mkdir -p /data/hadoop/hdfs/name /data/hadoop/hdfs/data1 /data/hadoop/hdfs/data2 /data/hadoop/hdfs/tmp
RUN chown hadoop:hadoop -R /data/hadoop/