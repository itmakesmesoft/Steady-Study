# [MSA] Window 개발환경 세팅-WSL2, Windows Termial, Docker 설치

## WSL 2 수동 설치 방법

### 1.  ****Linux용 Windows 하위 시스템 사용****

Windows에서 Linux 배포를 설치하려면 먼저 "Linux용 Windows 하위 시스템" 옵션 기능을 사용하도록 설정해야한다. 

- PowerShell을 **관리자 권한(시작 메뉴 > PowerShell >에서 관리자 권한으로 실행 >을 마우스 오른쪽 단추로 클릭)**으로 열고 다음 명령을 입력

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

### 2. ****WSL 2 실행을 위한 요구 사항 확인****

![Untitled](%5BMSA%5D%20Window%20%E1%84%80%E1%85%A2%E1%84%87%E1%85%A1%E1%86%AF%E1%84%92%E1%85%AA%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC%20%E1%84%89%E1%85%A6%E1%84%90%E1%85%B5%E1%86%BC-WSL2,%20Windows%20Termi%2075cd6d05281d49d6a4b845044c394e87/Untitled.png)

- x64 시스템의 경우: **버전 1903** 이상, **빌드 18362** 이상
- ARM64 시스템의 경우: **버전 2004** 이상, **빌드 19041** 이상

### 3. ****Virtual Machine 기능 사용****

WSL 2를 설치하려면 먼저 **Virtual Machine 플랫폼** 옵션 기능을 사용하도록 설정

```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

머신을 **다시 시작하여(재부팅)** WSL 설치를 완료하고 WSL 2로 업데이트

### 4. ****Linux 커널 업데이트 패키지 다운로드****

최신 패키지를 다운로드 후 실행

- [x64 머신용 최신 WSL2 Linux 커널 업데이트 패키지](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

### 5. ****WSL 2를 기본 버전으로 설정****

PowerShell을 열고 이 명령을 실행

```powershell
wsl --set-default-version 2
```

### 6. ****선택한 Linux 배포 설치****

1. [Microsoft Store](https://aka.ms/wslstore)를 열고 즐겨 찾는 Linux 배포를 선택
2. Ubuntu를 설치

![Untitled](%5BMSA%5D%20Window%20%E1%84%80%E1%85%A2%E1%84%87%E1%85%A1%E1%86%AF%E1%84%92%E1%85%AA%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC%20%E1%84%89%E1%85%A6%E1%84%90%E1%85%B5%E1%86%BC-WSL2,%20Windows%20Termi%2075cd6d05281d49d6a4b845044c394e87/Untitled%201.png)

### 7. Windows Termial 설치

Microsoft Store에서 `Windows Termial` 설치

![Untitled](%5BMSA%5D%20Window%20%E1%84%80%E1%85%A2%E1%84%87%E1%85%A1%E1%86%AF%E1%84%92%E1%85%AA%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC%20%E1%84%89%E1%85%A6%E1%84%90%E1%85%B5%E1%86%BC-WSL2,%20Windows%20Termi%2075cd6d05281d49d6a4b845044c394e87/Untitled%202.png)

### 8. ****Linux 사용자 이름 및 암호 설정****

Ubuntu를 열어 **사용자 이름** 및 **암호**를 만들면, 해당 계정이 배포의 기본 사용자가 되고 시작 시 자동으로 로그인 됨

![https://learn.microsoft.com/ko-kr/windows/wsl/media/ubuntuinstall.png](https://learn.microsoft.com/ko-kr/windows/wsl/media/ubuntuinstall.png)

암호를 변경하거나 재설정하려면 Linux 배포를 열고 다음 명령을 `passwd`입력

### 9. ****패키지 업데이트 및 업그레이드****

배포에 기본 설정 패키지 관리자를 사용하여 패키지를 정기적으로 업데이트하고 업그레이드하는 것이 좋다. Ubuntu에 다음 명령어를 실행한다.

```bash
sudo apt update && sudo apt upgrade
```

Windows는 Linux 배포를 자동으로 업데이트하거나 업그레이드하지 않는다. 대부분의 Linux는 사용자가 직접 제어해야 한다.

### 10. Docker 다운로드

[Docker Desktop WSL 2 backend on Windows](https://docs.docker.com/desktop/windows/wsl/)

[Windows용 Docker 데스크톱을](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe) 다운로드

파일을 실행시켜 설치 (wsl2 어쩌고 체크 꼭 하기), 설치 후 윈도우 로그아웃 및 재부팅 실행

### 11. Docker Desktop 실행

Docker Desktop 실행하여 running 확인 후 설정 > 일반 > Use the WSL 2 based engine 선택

Ubuntu에 아래 명령어 쳐서 결과 제대로 나오는지 확인

```bash
docker ps
```

![Untitled](%5BMSA%5D%20Window%20%E1%84%80%E1%85%A2%E1%84%87%E1%85%A1%E1%86%AF%E1%84%92%E1%85%AA%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC%20%E1%84%89%E1%85%A6%E1%84%90%E1%85%B5%E1%86%BC-WSL2,%20Windows%20Termi%2075cd6d05281d49d6a4b845044c394e87/Untitled%203.png)