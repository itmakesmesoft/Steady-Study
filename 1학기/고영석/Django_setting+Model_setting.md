1. 가상 환경 설치
    $ python -m venv venv
    결과 : venv 폴더 생성

2. 가상 환경 활성화 및 확인
    $ source venv/Scripts/activate
   
    확인 명령어 : pip list
    결과 : 기본적으로 설치된 패키지 2개 조회 가능

3. 장고 설치
    $ pip install django==3.2.13
    확인 명령어 : pip list

4. 프로젝트 생성
    $ django-admin startproject firstpjt .
    결과
   
   - 설정한 프로젝트 이름의 폴더 생성
   - 기본적으로 설치되어야할 파일들 확인

5. 앱 생성
    $ python manage.py startapp articles
    결과
   
   - 설정한 앱 이름의 폴더 생성
   - 기본적으로 설치되어야할 파일들 확인

6. 앱 등록
   
   - settings.py 설정

7. 프로젝트 urls 작성
   
   - 바로 include 사용하세요

8. 앱 urls 작성
   
   - views 로 매핑

9. views 작성
   
   - index.html 랜더링

10. templates 작성
    
    - index.html 작성
      폴더 구조 : articles/templates/articles/index.html

------------------

> QuerySet API  
> 
> - 추가 라이브러리 설치 및 설정
>   - pip install ipython + pip install django-extensions
>   - settings.py의 INSTALLED_APPS에 django_extensions 등록
>   - python manage.py shell_plus

> 

1. 청사진 설계 (삭제는 migrations 파일의 init 빼고 삭제)
   
   - python manage.py makemigrations  
   - 명령어 실행 후 migrations/0001_initial.py 생성

2. 설계도를 실제 db.sqlite3 DB파일에 반영하는 과정
   
   - python manage.py migrate
   - 모델에서의 변경사항들과 DB의 스키마가 동기화를 이룸

> 기타 명령어

- python manage.py showmigrations
  
  - migrations 파일들이 migrate 됐는지 안 됐는지 여부를 확인하는 용도
  - [x]표시가 있으면 migrate가 완료되었음을 의미

- sqlmigrate
  
  - python manage.py sqlmigrate articles 0001
    - 해당 migrations 파일이 SQL문으로 어떻게 해석 될지 미리 확인 할 수 있음

---

### 데이터 객체를 만드는 (생성하는) 3가지 방법

> 첫번쨰 방법  

    1. article = Article()  
       - 클래스를 통한 인스턴스 생성      
    2. article.title = 'first'  / article.content = 'django!'
       - 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당  
    3. article.save()  
       - 인스턴스로 save 메서드 호출     

> 두번쨰 방법(인스턴스 생성시 초기 값을 함께 작성하여 생성)

     1. article = Article(title='second', content='pizza')
     2. article.save()
        (여기부터는 확인을 위한 optional)
     3. article
     4. Article.objects.all()

> 세번째 방법(QuerySet API 중 create() 메서드 활용)

    # 위 두가지 방식과는 다르게 바로 생성된 데이터가 반환된다
    1. Article.objects.create(title='third', content='chicken')

---

1. ORM 문법을 사용하여 model의 전체 쿼리셋을 id에 대해 내림차순으로 조회
    Movie.objects.all().order_by("-id")
2. ORM 문법을 사용하여 model의 전체 쿼리셋 중 genre가 action인 것만 조회
    Movie.objects.all().filter(genre="action")
3. ORM 문법을 사용하여 model의 전체 쿼리셋 중 title이 e로 끝나는 것만 조회
    Movie.objects.all().filter(title__endswith("e"))

----

### CSRF(Cross-Site-Request-Forgery)

- "사이트 간 요청 위조"
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만든느 공격 방법
- CSRF 공격 방어 -> "Security Token 사용 방식(CSRF Token)"

### CSRF Token

- 사용자의 데이터에 임의의 난수의 값(token)을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송 시키도록 함
- 이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증
- 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용
- Django는 DTL에서 csrf_token 템플릿 태그를 제공

---

### Admin site

- python manage.py createsuperuser
- ### # articles/admin.py에 등록해야 모델의 record를 볼 수 있다.
  - from django.contrib import admin
  - frim .models import Article  
  - admin.site.register(Article)

---

C(post) R(get) U(post) D(post)
