FROM registry.cn-shanghai.aliyuncs.com/alicea/tc:v1

LABEL maintainer="ceasona@qq.com"


RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

# ENV
ENV JAVA_HOME=/usr/lib/jvm/jdk8u282-b08 \
    JRE_HOME=/usr/lib/jvm/jdk8u282-b08/jre \
    CLASSPATH=.:/usr/lib/jvm/jdk8u282-b08/lib:/usr/lib/jvm/jdk8u282-b08/jre/lib \
    HADOOP_HOME=/opt/hadoop-3.3.1 \
    HADOOP_INSTALL=/opt/hadoop-3.3.1 \
    HADOOP_MAPRED_HOME=/opt/hadoop-3.3.1         \
    HADOOP_COMMON_HOME=/opt/hadoop-3.3.1 \
    HADOOP_HDFS_HOME=/opt/hadoop-3.3.1   \
    YARN_HOME=/opt/hadoop-3.3.1  \
    HADOOP_COMMON_LIB_NATIVE_DIR=/opt/hadoop-3.3.1/lib/native    \
    HADOOP_OPTS="-Djava.library.path=/opt/hadoop-3.3.1/lib/native"   \
    HIVE_HOME=/opt/apache-hive-3.1.2-bin    \
    PATH=/usr/lib/jvm/jdk8u282-b08/bin:/opt/hadoop-3.3.1/sbin:/opt/hadoop-3.3.1/bin:/opt/apache-hive-3.1.2-bin/bin:$PATH

# JAVA
COPY OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u282b08_openj9-0.24.0.tar.gz /root
RUN mkdir /usr/lib/jvm
RUN tar -zxvf /root/OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u282b08_openj9-0.24.0.tar.gz -C /usr/lib/jvm

# SPARK
COPY spark-3.2.1-bin-hadoop3.2.tgz /root/spark-3.2.1-bin-hadoop3.2.tgz
RUN tar -zxvf /root/spark-3.2.1-bin-hadoop3.2.tgz -C /opt

# HADOOP
COPY hadoop-3.3.1.tar.gz /root/hadoop-3.3.1.tar.gz
RUN tar -zxvf /root/hadoop-3.3.1.tar.gz -C /opt

# HIVE
COPY apache-hive-3.1.2-bin.tar.gz /root/apache-hive-3.1.2-bin.tar.gz
RUN tar -zxvf /root/apache-hive-3.1.2-bin.tar.gz -C /opt


# REMOVE
RUN rm /root/*.tgz /root/*.tar.gz

# CHOWN
RUN useradd hadoop && mkdir -p /home/hadoop && chown hadoop /home/hadoop  -R
RUN chown hadoop:hadoop -R /opt/hadoop-3.3.1
RUN mkdir -p /data/hadoop/hdfs/name /data/hadoop/hdfs/data1 /data/hadoop/hdfs/data2 /data/hadoop/hdfs/tmp
RUN chown hadoop:hadoop -R /data/hadoop/
RUN chown hadoop:hadoop -R  /opt/spark-3.2.1-bin-hadoop3.2/

# PORT
EXPOSE 50070
EXPOSE 9870
EXPOSE 8080
EXPOSE 22
EXPOSE 8081
EXPOSE 8030
EXPOSE 8031
EXPOSE 8032
EXPOSE 8088
EXPOSE 4040
EXPOSE 9090
