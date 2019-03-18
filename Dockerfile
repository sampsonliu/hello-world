FROM docker.oa.com:8080/public/centos-7.2:latest

RUN set -x \
    && mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup \
    && curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.cloud.tencent.com/repo/centos7_base.repo \
    && yum clean all \
    && yum makecache \
    && yum -y update \
    && yum clean all \
    && rm -rf /tmp/* /var/tmp/* /data/tmp/*

COPY http-server.py /data/test/

CMD ["python", "/data/test/http-server.py"]
