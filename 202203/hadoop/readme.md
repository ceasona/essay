# HDFS

1. ## 修改hosts文件

   ```
   172.17.0.2 node1
   172.17.0.3  node2
   172.17.0.4 node3
   ```

2. ## hadoop免密登录

   ```
   useradd hadoop
   passwd hadoop
   chown hadoop hadoop/  -R
   
   su hadoop
   ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
   cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
   chmod 0600 ~/.ssh/authorized_keys
   #测试
   ssh localhost(首次需输入yes)
   
   ssh-copy-id -i .ssh/id_rsa hadoop@node1
   ssh-copy-id -i .ssh/id_rsa hadoop@node2
   ssh-copy-id -i .ssh/id_rsa hadoop@node3
   ```

3. ## jdk与hadoop安装

   - [jdk](https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/8/jdk/x64/linux/)

     ```
     https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/8/jdk/x64/linux/OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u282b08_openj9-0.24.0.tar.gz
     ```

   - [hadoop](https://mirrors.sonic.net/apache/hadoop/common/hadoop-3.3.1/)

     ```
     https://mirrors.sonic.net/apache/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
     ```

4. ## 配置hadoop

   - ### hadoop-env.sh

     ```
     export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
     export HADOOP_SSH_OPTS="-p 22"
     ```

   - ### core-site.xml

     ```
     <configuration>
         <property>
             <name>fs.defaultFS</name>
             <value>hdfs://node1:9000</value>
         </property>
     </configuration>
     ```

   - ### hdfs-site.xml

     ```
     <configuration>
         <property>
             <name>dfs.blocksize</name>
             <value>67108864</value>
         </property>
         <property>
             <name>dfs.replication</name>
             <value>2</value>
         </property>
         <property>
             <name>dfs.namenode.handler.count</name>
             <value>20</value>
         </property>
         <property>
             <name>dfs.namenode.name.dir</name>
             <value>/data/hadoop/hdfs/name</value>
         </property>
         <property>
             <name>dfs.datanode.data.dir</name>
             <value>/data/hadoop/hdfs/data1,/data/hadoop/hdfs/data2</value>
         </property>
     </configuration>
     ```

   - ### workers

     ```
     node1
     node2
     node3
     ```

   - ### mapred-site.xml

     ```
     <configuration>
         <property>
             <name>mapreduce.framework.name</name>
             <value>yarn</value>
         </property>
     </configuration>
     ```

   - ### yarn-site.xml

     ```
     <configuration>
         <property>
             <name>yarn.resourcemanager.hostname</name>
             <value>172.17.0.2</value>
         </property>
         <property>
             <name>yarn.resourcemanager.webapp.address</name>
             <value>172.17.0.2:9090</value>
         </property>
         <property>
             <name>yarn.nodemanager.aux-services</name>
             <value>mapreduce_shuffle</value>
         </property>
     </configuration>
     ```

     

5. ## hdfs 集群

   ### hdfs namenode -format

   - ### 主节点

     ```
     # 一次性启动
     start-all.sh
     # 逐个组件启动
     start-dfs.sh
     start-yarn.sh
     
     hdfs --daemon start namenode
     yarn --daemon start resourcemanager
     
     # 一次性停止
     stop-all.sh
     # 逐个组件启动
     stop-dfs.sh
     stop-yarn.sh
     ```

   - ### 从节点

     ```
     hdfs --daemon start datanode
     yarn --daemon start nodemanager
     ```

   - ### 测试

     ```
     hadoop fs -mkdir -p /tmp/test
     hadoop fs -ls /tmp/test
     #上传文件
     hadoop fs -put testboston.csv /tmp/test
     #查看是否上传成功
     hadoop fs -ls /tmp/test
     #下载文件
     hadoop fs -get /tmp/test/testboston.csv /tmp/
     ```

6. ## Hive

   - [安装包](https://archive.apache.org/dist/hive/hive-2.1.0/apache-hive-2.1.0-bin.tar.gz)

     ```
     https://archive.apache.org/dist/hive/hive-3.1.2/
     
     tar -zxvf /root/apache-hive-3.1.2-bin.tar.gz -C /opt
     ```

   - 设置环境变量

     ```
     #Hive Enviroment
     export HIVE_HOME=/opt/apache-hive-3.1.2-bin
     export PATH=$PATH:$HIVE_HOME/bin
     ```

   - 创建hive-site.xml

     ```
     vi hive-site.xml 
     #创建两个对应的目录并赋予读写权限：
     $hadoop fs -mkdir -p /user/hive/warehouse
     $ hadoop fs -mkdir -p /tmp/hive
     $ hadoop fs -chmod -R 777 /user/hive/warehouse
     $ hadoop fs -chmod -R 777 /tmp/hive
     $ hadoop fs -ls /
     ```

   - 配置hive-env.sh文件

     ```
     在/opt/hive-3.2.1/conf下执行该命令
     cp hive-env.sh.template hive-env.sh
     将a、b两个配置添加到hive-env.sh
     （a）配置HADOOP_HOME路径
     export HADOOP_HOME=/opt/hadoop-2.7.2
     （b）配置HIVE_CONF_DIR路径
     export HIVE_CONF_DIR=/opt/apache-hive-3.1.2-bin/conf
     ```

   - JDBC的jar包拷贝在/opt/apache-hive-3.1.2-bin/lib目录下

     https://dev.mysql.com/downloads/file/?id=494887

   - 在/opt/hive-3.2.1/bin目录下执行以下命令

     ```
     schematool -dbType mysql -initSchema
     or  ./schematool -dbType mysql -initSchema
     schematool -dbType mysql -info
     
     ```

   - 测试

     ```
     ./hive
     create table student_test(id INT,name string,age int) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
     load data local inpath '/home/hadoop/student.txt' into table student_test;
     select * from student_test;
     ```

     

7. ## 问题汇总

   - 查看 jps

8. ## 参考

   - [Ubuntu20.04安装Hadoop和Hive](https://blog.csdn.net/weixin_38924500/article/details/106257047?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&utm_relevant_index=2)
   - [hive 学习](https://blog.csdn.net/eases_stone/article/details/80607109)
   - [Hadoop fs常用命令](https://www.jianshu.com/p/b18dc7344cbd)
   - [官方文档](https://hadoop.apache.org/docs/r1.0.4/cn/cluster_setup.html)
   - [HDFS完全分布式集群搭建](https://www.cnblogs.com/williamzheng/p/13043461.html)

