# spark

## 环境搭建

准备工作：

1. [JDK](https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK)

   ```
   https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/8/jdk/x64/linux/OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u282b08_openj9-0.24.0.tar.gz
   ```

2. [spark](https://dlcdn.apache.org/spark)

   [https://mirrors.tuna.tsinghua.edu.cn/apache/spark](https://mirrors.tuna.tsinghua.edu.cn/apache/spark)

   ```
   https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
   ```

3. 

- ### local模式

  ```
  # JAVA
  mkdir /usr/lib/jvm
  tar -zxvf /root/OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u282b08_openj9-0.24.0.tar.gz -C /usr/lib/jvm
  
  # SPARK
  tar -zxvf /root/spark-3.2.1-bin-hadoop3.2.tgz -C /opt
  chown -R root spark-3.2.1-bin-hadoop3.2/
  chgrp -R root spark-3.2.1-bin-hadoop3.2/
  
  vim ~/.bashrc
  export JAVA_HOME=/usr/lib/jvm/jdk8u282-b08
  export JRE_HOME=${JAVA_HOME}/jre
  export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
  export PATH=${JAVA_HOME}/bin:/opt/spark-3.2.1-bin-hadoop3.2/bin:$PATH
  
  ```

  [测试](https://spark.apache.org/examples.html)

  ```
  # spark-shell [SparkSubmit]
  
  val text_file = sc.textFile("file:///root/words.txt")
  val counts = text_file.flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_ + _)
  counts.collect
  
  counts.saveAsTextFile("hdfs://...")
  ```

  

- ### standalone [独立集群](https://spark.apache.org/docs/latest/cluster-overview.html)

  ```dockerfile
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
  ```

  ```
  docker run -itd --privileged --hostname node1 --name node1 -P ceasona250/spark:v2.1 init
  docker run -itd --privileged --hostname node2 --name node2 -P ceasona250/spark:v2.1 init
  docker run -itd --privileged --hostname node3 --name node3 -P ceasona250/spark:v2.1 init
  ```

  1. 集群规划

     node1:master

     node2:worker/slave

     node3:worker/slave

  2. 修改works

     进入配置目录，修改配置文件 slaves.template\works.template

     ```
     cp workers.template workers
     vim workers
     node2
     node3
     ```

     

  3. 修改spark-env.sh

     ```
     cp spark-env.sh.template spark-env.sh
     vim spark-env.sh
     
     JAVA_HOME=/usr/lib/jvm/jdk8u282-b08
     HADOOP_CONF_DIR=/opt/hadoop-3.3.1/etc/hadoop
     YARN_CONF_DIR=/opt/hadoop-3.3.1/etc/hadoop
     SPARK_MASTER_HOST=node1
     SPARK_MASTER_PORT=7077
     SPARK_MASTER_WEBUI_PORT=8080
     SPARK_WORKER_CORES=1
     SPARK_WORKER_MEMORY=1g
     
     ```

  4. 配置分发

  5. 启动

     ```
     # sbin目录下
     ./start-all.sh
     
     spark-shell --master spark://node1:7077
     ```

  

- ### standalone-HA集群 高可用模式

  1. zk

     ```
     wget https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0-bin.tar.gz
     tar -zxvf /root/apache-zookeeper-3.8.0-bin.tar.gz -C /opt
     cd /opt/apache-zookeeper-3.8.0-bin/conf
     cp zoo_sample.cfg zoo.cfg
     vim zoo.cfg
     #默认8080与spark冲突
     admin.serverPort=8888
     server.1=172.17.0.2:2888:3888
     server.2=172.17.0.3:2888:3888
     server.3=172.17.0.4:2888:3888
     ```

     分发

     根据 id 和对应的地址分别配置 myid

     ```
     # node1
     vim /tmp/zookeeper/myid
     1
     
     # node2
     vim /tmp/zookeeper/myid
     2
     
     # node3
     vim /tmp/zookeeper/myid
     3
     ```

     启动zk集群 sh zkServer.sh start

  2. 修改spark-env.sh

     ```
     # SPARK_MASTER_HOST=node1
     SPARK_DAEMON_JAVA_OPTS="-Dspark.deploy.recoveryMode=ZOOKEEPER -Dspark.deploy.zookeeper.url=node1:2181,node2:2181,node3:2181 -Dspark.deploy.zookeeper.dir=/spark-ha"
     ```

  3. 启动

     ```
     # node1
     ./start-all.sh
     
     # node2
     ./start-master.sh
     ```

  4. 测试

     ```
     #node1:8080
     URL: spark://node1:7077
     Alive Workers: 2
     Cores in use: 2 Total, 0 Used
     Memory in use: 2.0 GiB Total, 0.0 B Used
     Resources in use:
     Applications: 0 Running, 0 Completed
     Drivers: 0 Running, 0 Completed
     Status: ALIVE
     ```

     ```
     #node2:8080
     URL: spark://node2:7077
     Alive Workers: 0
     Cores in use: 0 Total, 0 Used
     Memory in use: 0.0 B Total, 0.0 B Used
     Resources in use:
     Applications: 0 Running, 0 Completed
     Drivers: 0 Running, 0 Completed
     Status: STANDBY
     ```

     kill node1的master

     ```
     spark-shell --master spark://node1:7077,node2:7077
     ```

     

- ## SparkOnYarn

  1. 配置Yarn

     ```
     /opt/hadoop-3.3.1/etc/hadoop
     vim yarn-site.xml
     ```

     

  2. 配置Spark

     cp spark-defaults.conf.template spark-defaults.conf

     vim spark-defaults.conf

     ```
     spark.eventLog.enabled			true
     spark.eventLog.dir			 hdfs://node1:9000/sparklog
     spark.eventLog.compress		true
     spark.yarn.historyServer.address	node1:18080
     ```

     vim spark-env.sh

     ```
     SPARK_HISTORY_OPTS="-Dspark.history.fs.logDirectory=hdfs://node1:9000/sparklog -Dspark.history.fs.cleaner.enabled=true"
     ```

     创建日志目录

     ```
     hadoop fs -mkdir -p /sparklog
     ```

     修改日志级别 vim log4j.properties

     

     

  3. 配置依赖jar包

     创建存储spark相关jar包

     ```
     hadoop fs -mkdir -p /spark/jars
     ```

     上传jar包

     ```
     hadoop fs -put  /opt/spark-3.2.1-bin-hadoop3.2/jars/* /spark/jars
     ```

     修改 spark-default.conf

     ```
     spark.yarn.jars hdfs://node1:9000/spark/jars/*
     ```

     

  4. 启动

     ```
     SPARK_HOME=/opt/spark-3.2.1-bin-hadoop3.2
     
     ${SPARK_HOME}/bin/spark-submit --master yarn --deploy-mode client --class org.apache.spark.examples.SparkPi ${SPARK_HOME}/examples/jars/spark-examples_2.12-3.2.1.jar 10
     
     ${SPARK_HOME}/bin/spark-submit --master yarn --deploy-mode cluster --class org.apache.spark.examples.SparkPi ${SPARK_HOME}/examples/jars/spark-examples_2.12-3.2.1.jar 10
     ```

     







问题汇总

1. [Error: JAVA_HOME is not set and java could not be found in PATH](https://www.codeleading.com/article/71205967475/)

   shell脚本语法问题

   