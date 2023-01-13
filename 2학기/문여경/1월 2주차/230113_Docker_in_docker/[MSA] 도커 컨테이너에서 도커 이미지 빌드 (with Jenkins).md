# [MSA] 도커 컨테이너에서 도커 이미지 빌드 (with Jenkins)

## Docker에 Jenkins 컨테이너 띄우기

[jenkins - Official Image | Docker Hub](https://hub.docker.com/_/jenkins)

Ubuntu에 docker pull jenkins 명령어 실행 > 실패 시

docker에서 jenkins 이미지를 받으려고 하면 아래와 같은 에러가 발생한다.

```bash
$ docker pull jenkins
Usingdefault tag: latest
Error responsefrom daemon: manifestfor jenkins:latestnot found: manifest unknown: manifest unknown
```

### 해결

docker hub의 jenkins description을 보면 deprecated 되었다고 안내한다.

![https://blog.kakaocdn.net/dn/AHeSu/btq9gzfMhCo/fMGUec6ENcWwJpThb7LgR1/img.png](https://blog.kakaocdn.net/dn/AHeSu/btq9gzfMhCo/fMGUec6ENcWwJpThb7LgR1/img.png)

This image has been deprecated for over 2 years in favor of the jenkins/jenkins:lts image provided and maintained by the Jenkins Community as part of the project's release process. The images found here have not received updates for over 2 years and will not receive any updates in the future. Remaining tags are here only for historical reasons, none of them are supported and none of them should be used.

**[jenkins/jenkins:lts image](https://hub.docker.com/r/jenkins/jenkins)** 링크를 누르면 새로운 jenkins repository로 안내한다.

LTS를 받으려면 `docker pull jenkins/jenkins:lts-jdk11`최신버전을 받으려면 `docker pull jenkins/jenkins:jdk11` 또는 `docker pull jenkins/jenkins` 을 사용하여 해결할 수 있다.

### Docker에 Jenkins 설치

```bash
docker run -d -p 8080:8080 -v /var/jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -u root --name jenkins jenkins/jenkins:lts-jdk11
```

[localhost](http://localhost):8080으로 접근 > `docker logs jenkins` 명령어로 **admin password**로 확인 후 입력

### Jekins Plugin Manager에서 필요한 플러그인 설치

- GitLab 관련 플러그인, Docker 관련 플러그인 설치

### Jenkins 컨테이너에 접속

```bash
docker exec -it jenkins bash
```

**접속해서 Docker 설치**

```bash
apt-get update && \
apt-get -y install apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     software-properties-common && \
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable" && \
apt-get update && \
apt-get -y install docker-ce
```

```bash
# 추가적으로 docker jenkins에서 host docker 접근 권한을 부여해주기 위해
root@ad73f32c5f1d:/# groupadd -f docker
root@ad73f32c5f1d:/# usermod -aG docker jenkins
root@ad73f32c5f1d:/# chown root:docker /var/run/docker.sock
```

**Docker 버전 확인**

```bash
root@ad73f32c5f1d:/# docker --version
```

**Docker의 OS 정보 확인**

```bash
root@ad73f32c5f1d:/# cat /etc/issue
```