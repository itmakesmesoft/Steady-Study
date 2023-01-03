# HTML

# **Hyper Text Markup Language**

웹 페이지를 작성(구조화)하기 위한 언어

**Hyper Text**

참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

**Markup Language**

태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어(ex HTML, Markdown)

# HTML 기본구조

- html : 문서의 최상위(root) 요소
- head : 문서 메타데이터 요소 (문서 제목, 인코딩, 스타일, 외부 파일 로딩 등)
    - <title> : 브라우저 상단 타이틀
    - <meta> : 문서 레벨 메타데이터 요소
        - Open Graph Protocol : thumbnail
    - <link> : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
    - <script> : 스크립트 요소 (JavaScript 파일/코드)
    - <style> : CSS 직접 작성
- body : 문서 본문 요소

```html
<!DOCTYPE html>
<html lang='en'>
<head>
	<title>HTML 수업</title>
	<meta charset="UTF-8">
	<link href="style.css" rel="stylesheet">
	<script src = "javascript.js"></script>
	<style>
		p {
			color: black;
		}
	</style>
</head>
<body>
	<!-- 이것은 주석(ctrl + /)입니다. -->
	<h1>나의 첫번째 HTML</h1>
	<p>이것은 본문입니다.</p>
	<span>이것인 인라인요소</span>
	<a href="https://www.naver.com">네이버로 이동</a>
</body>
</html>
```

## Element

- HTML의 요소는 태그와 내용(contents)으로 구성
    
    <h1>contents</h1>
    

   여는 태그         닫는 태그

- 내용이 없는 태그
    - br, hr, img, input, link, meta
- 요소는 중첩될 수 있음

## Attribute

- 태그별로 사용할 수 있는 속성이 다름
    
    <a href=”https://google.com”></a>
    
       속성명            속성값
    
- 속성 스타일 가이드 : 공백은 No / “” 사용
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음
    - id : 문서 전체에서 유일한 고유 식별자 지정
    - class : 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근)
    - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
    - style : inline 스타일
    - title : 요소에 대한 추가 정보 지정
    - tabindex : 요소의 탭 순서
    

## Semantic Tag

- HTML 태그가 특정 목적, 역할 및 의미적 가치를 가지는 것
    
    ex) h1 태그는 ‘이 페이지에서 최상위 제목’인 텍스트를 감싸는 역할
    
- 검색 엔진 최적화(SEO)를 위해 메타태그, 시멘틱태그 등을 통한 마크업을 효과적으로 활용하기
- Non semantic tag : div(division), span 등
- 대표적인 시맨틱 태그

![Untitled](HTML%20b8dd9538d342471daffab22765c721cc/Untitled.png)

```html
<div>
	<div></div>
</div>
<div>
	<div></div>
	<div></div>
</div>
<div></div>

<!-- sematic tag -->

<header>
	<nav></nav>
</header>
<section>
	<article></article>
	<article></article>
</section>
<footer></footer>
```

## Rendering

- 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정
- DOM(document Object Model) 트리
    - HTML 문서 내의 각 요소에 접근/수정에 필요한 property와 method 제공

![Untitled](HTML%20b8dd9538d342471daffab22765c721cc/Untitled%201.png)

# HTML 문서 구조화

- 인라인 요소 : 글자처럼 취급
- 블록 요소 : 한 줄 모두 사용
- 텍스트 요소

| <a></a> | href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성 |
| --- | --- |
| <strong></strong> | 굵은 글씨 요소 |
| <em></em> = <b></b> | 기울임 글씨 요소 |
| <br> | 텍스트 내에 줄 바꿈 생성 |
| <img> | src 속성을 활용하여 이미지 표현 |
| <span></span> = <i></i> | 의미 없는 인라인 컨테이너 |
|  |  |
| <p></p> | 하나의 문단(paragraph) |
| <hr> | 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨 (A Horizontal Rule) |
| <ol></ol>
<ul></ul> | 순서가 있는 리스트
순서가 없는 리스트 |
| <pre></pre> | HTML에 작성한 내용을 그대로 표현 (글씨체 변환)
보통 고정폭 글꼴이 사용되고 공백문자를 유지 |
| <blockquote></blockquote> | 텍스트가 긴 인용문
주로 들여쓰기를 한 것으로 표현됨 |
| <div></div> | 의미 없는 블록 레벨 컨테이너 |

## form

- 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
- 기본 속성
    - action : form을 처리할 서버의 URL (데이터를 보낼 곳)
    - method : form을 제출할 때 사용할 HTTP 메서드 (GET or POST)
    - enctype : 메서드가 POST인 경우 데이터의 유형
        - application/x-www-form-urlencoded : 기본값
        - multipart/form-data : 파일 전송시 (input type이 file 인 경우)

## input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
- input 요소의 동작은 type에 따라 달라지므로, 각각 내용 숙지 필요
- 대표 속성
    - name : form control에 적용되는 이름 (이름/값 페어로 전송됨)
    - value : form control에 적용되는 값 (이름/값 페어로 전송됨)
    - required, readonly, autofocus, autocomplete, disabled 등
- input label
    - label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
    - <input>에 id 속성을, <label>에는 for 속성을 활용하여 상호 연관을 시킴
- 일반
    - text : 일반 텍스트 입력
    - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
    - email : 이메일 형식이 아닌 경우 form 제출 불가
    - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
    - file : accept 속성을 활용하여 파일 타입 지정 가능
- 항목 중 선택
    - 일반적으로 label 태그와 함께 사용하여 선택항목을 작성
    - checkbox : 다중 선택
    - radio : 단일 선택
- 기타
    - color : color picker
    - date : date picker
    - hidden : 사용자에게 보이지 않는 input
    

```html
<form action="/search" method="GET">
	<input type="text" name="q">
</form>

<lable for="agreetment">개인정보 수집에 동의합니다.</label>
<input type="checkbox" name="agreement" id="agreement">
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Form 활용 실습</h1>
    <form action="">

      <!-- autofocus 및 label 확인 -->
      <div class="input-group">
        <label for="username">아이디</label>
      </div>
      <input type="text" name="username" id="username" autofocus>

      <!-- disabled 및 value 확인 -->
      <div class="input-group">
        <label for="name">이름</label>
      </div>
      <input type="text" name="name" value="홍길동" id="name" disabled>

      <!-- label 확인 -->
      <div class="input-group">
        <label for="agreement">개인정보 수집에 동의합니다</label>
      </div>
      <input type="checkbox" name="agreement" id="agreement">
      <div class="input-group">
        <label>최종 제출을 확인합니다.</label>
      </div>
      <input type="checkbox">
    </form>
    <input type="submit" value="제출">
</body>
</html>
```