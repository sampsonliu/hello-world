FROM docker.oa.com:8080/public/centos-7.2:latest

RUN set -x \
    && mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup \
    && curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.cloud.tencent.com/repo/centos7_base.repo \
    && yum clean all \
    && yum makecache \
    && yum -y install java-1.8.0-openjdk maven \
    && yum clean all \
    && rm -rf /tmp/* /var/tmp/* /data/tmp/*

COPY . /data/hello-world

RUN cd /data/hello-world \
    && mkdir -p ~/.m2 \
    && mv settings.xml ~/.m2 \
    && java -version \
    && mvn -version \
    && mvn package \
    && ls target/*.jar \
    && java -version \
    && mvn -version

CMD ["java", "-jar", "/data/hello-world/target/helloworld-1.0-SNAPSHOT.jar"]
