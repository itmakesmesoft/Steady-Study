# Django 가상환경 설정 및 초기 설정

**1. 프로젝트 할 폴더 생성**

**2. 생성한 프로젝트 폴더 내  Git Bash 실행** (가상환경 설정 및 활성화)

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

**3. Django 설치**

```bash
pip install django==3.2.13
```

**4. 패키지 목록 생성**

```bash
pip freeze > requirements.txt
```

**5. Django project 생성**

```bash
django-admin startproject firstpjt .

```

: firstpjt 라는 프로젝트 생성

* project 이름에는 python이나 Django에서 사용중인 키워드, '-'(하이픈) 사용 불가

* 마지막에 붙은 '.'(dot)을 붙이지 않을 경우 현재 디렉토리에 프로젝트 디렉토리를 새로 생성하게 됨

**6. 서버 실행**

```bash
python manage.py runserver
```

---

추가 - **저장한 requirements.txt로 환경설정하기**

: 다른 곳으로부터 패키지목록을 받아와서 실행할 경우

가상환경설정 및 활성화(위의 2번 항목)를

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

진행한 뒤,

```bash
pip install -r requirements.txt
```

이 코드를 실행하면 된다.

requirements.txt에 있는 패키지 목록을 받아오겠다는 의미이다.