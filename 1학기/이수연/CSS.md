# CSS

: cascading style sheets

cascading: 계단식

CSS: ‘스타일을 지정하기 위한 언어’. 선택하고, 스타일을 지정한다.

class(속성) - “article”(별명)

### CSS 구문

h1 {

  color: blue; 

  font-size: 15px; 

}

h1(선택자) {

  color: blue; (선언)

  font-size: 15px; (속성) (값)

}

### CSS 정의 방법

- 인라인
- 내부 참조 - <style>
- 외부 참조 - 분리된 CSS 파일
: 가장 많이 쓰는 방식. 추천

### 선택자 유형

- 기본 선택자 ex) #KOSPI_now
- 결합자
- 의사 클래스 / 요소

### 선택자 설명

- 요소: 서울사람
- 클래스: 최씨, 김씨
- 아이디: 지웅, 길동
- → 손병호 게임처럼: 서울사람 접어, 김씨 접어 등으로 스타일 지정
- 전체선택자
- 요소선택자
- 클래스선택자(.클래스이름)
.green {
color: green;
}
- 아이디선택자(#id이름)
- 자손결합자

lorem : 아무글자나 불러옴. 테스트할 때 사용

### CSS 적용 우선순위

: 범위가 좁을수록 강하다. (+ 같은 범위라면 밑에 있는 게 이김)

1. 중요도 - 사용시 주의 (절대자)
- !important
2. 우선순위
- 인라인 > id > class, 속성, pseudo-class,

### CSS 상속

CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.

- 상속 되는 것 예시
    - text 관련 요소(font, color, text-align), opacity 등
    - 여백 등은 상속되지 않음

### CSS 기본 스타일

- px(픽셀)
고정적인 단위
- %
백분율 단위
가변적인 레이아웃에서 자주 사용
- em
(바로 위, 부모 요소에 대한) 상속의 영향을 받음
배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
ex) 자식 요소는 부모 요소에 비해 2배 - 2em
- rem
(바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
ex) 브라우저마다 기본 글자의 몇 배 / 브라우저가 16px 2rem - 32px

- 크기 단위(vw)
    - px은 브라우저의 크기를 변경해도 그대로
    - vw는 브라우저의 크기에 따라 변한다

### 색상 단위

- 색상 키워드 ex) red
- RGB 색상 : ‘#’ + 16진수 표기법, rgb() 함수형 표기법
- HSL 색상 : 색상, 채도, 명도
- a는 alpha(투명도)

---

# CSS 선택자

### 결합자

1. 자손 결합자(공백 ‘ ‘) a b
    1. 어떤 요소 a 하위에 있는 모든 요소 b
2. 자식 결합자(>)a > b
    1. 어떤 요소 a 바로 밑에있는 요소 b
3. 형제 결합자(~) a ~ b
    1. 어떤 요소 a의 형제 요소중에서 뒤에 위치하는 b요소를 선택
4. 인접 형제 결합자(+) a + b
    1. 어떤 요소 a의 형제요소에 바로 뒤에 위치하는 b 요소를 선택한다.

```html
<div class="parent">
	<div> .parent요소의 자손 요소이자 자식요소이다.
			<div> .parent요소의 자손요소이다.
		</div>
	</div>
	<div class="a"></div> 위에 존재 또는 아래에 있는
	div요소들의 형제요소이다.
	<div></div> .a요소의 인접형제요소(바로 뒤에 있으니까)
	<div></div> .a요소의 일반 형제요소
</div>
```

---

# css box model

html의 모든 요소가 네모(박스모양)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.

### css 원칙1

: 모든 요소는 네모(박스모델)이고,

  위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (좌측 상단에 배치)

### box model 구성

- border: 테두리
- padding: 내용과 border 사이!
- 상하좌우!로 값을 입력
- shorthand를 통해서 표현 가능
    - 값1개: 상하좌우
    - 값2개: 상하, 좌우
    - 값3개: 상, 좌우, 하
    - 값4개: 상, 우, 하, 좌

### box model을 구성하는 영역

- margin : 요소 외부의 간격(border를 기준으로 하는 외부의 간격) / (다른 요소와의 간격)
- border: 요소의 경계선을 정하는 속성
- padding: 요소 내부(border를 기준으로)의 간격
    - 요소 내부의 content를 어디서부터 시작할건지, 얼만큼 공백을 주고 시작할건지를 정하는 속성
- content: 요소 내부에 있는 내용물
    - 이미지나 글자 등등

```html
<style>
  <div> {
	  width: 100px;
	  height: 100px;
	  background-color: blue;
	}
</style>
```

content만 100x100

```html
<style>
  <div> {
	  width: 100px;
	  height: 100px;
	  background-color: blue;
		margin: 50px;
	}
</style>
```

content 100 x 100

margin 50 (상하좌우)

```html
<style>
  <div> {
	  width: 100px;
	  height: 100px;
	  background-color: blue;
		margin-top: 50px;
		margin-left: 50px;
	}
</style>
```

content 100 x 100

margin 50 (상좌)

```html
<style>
<div> {
width: 100px;
height: 100px;
background-color: blue;
margin: 10px 20px 30px 40px;(상부터 시계방향: 상우하좌)
}
</style>
```

---

# box sizing

: 요소의 크기를 정할 때 어떤 방식으로 크기를 정할까?

box-sizing 속성을 변화 시켜 아래 두 개 중 하나를 선택해서 사용

1. content-box: 기본값, width속성을 지정하게 되면 내부에 있는 요소의 쟝소를 지정
2. border-box: 내부 요소(content)너비 + padding +border를 width로 지정

### 기본적으로 모든 요소의 box-sizing은 content-box

padding을 제외한 순수 contents 영역만을 box로 지정

### css 원칙2

: 모든 요소는 네모(박스모델)이고, 좌측상단에 배치

### 대표적으로 활용되는 Display

- display: block
- display: inline

나중에 보여줄일 있다 hidden

나중에 보여줄 일 없다 None

---

 

# css position

: 문서상에서 요소의 위치를 지정한다(웹페이지에서 요소가 나타날 위치)

어떤 방식으로 나타낼지를 정하는 속성

position

- static: 모든 태그의 기본값
    - 일반적인 요소의 배치 순서를 따른다. (위에서 아래, 왼쪽에서 오른쪽)
    - 부모 요소 내에서 배치될 때는 부모 요소의 위치(시작위치, 좌측상단)를 기준으로 배치된다.
- relative: 상대 위치
    - 자기 자신이 원래 존재해야했을 static 위치를 기준으로 이동한다.
    - 요소가 차지하는 공간은 static일때와 같다.
- absolute: 절대 위치
    - 요소를 일반적인 문서 흐름(위에서 아래로, 왼쪽에서 오른쪽으로)에서 제거한다. 흐름에 absolute 요소는 포함되지 않는다.
    - 흐름을 벗어난다. 없는 것처럼
    - static이 아닌 가장 가까이있는 부모 요소
- fixed: 고정 위치
    - 요소를 일반적인 흐름에서 제거한다.
    - 위치를 정할 대 부모 요소를 기준으로 하는 게 아닌 사용자화면(view port)를 기준으로 이동한다.
- sticky: 스크롤에 따라 변하는 속성 static → fixed로 변경
    - 이 속성을 적용한 요소는 평소에 문서 안에서는 position: static인 상태처럼 일반적인 흐름을 따른다
    - 스크롤 위치가 이 속성을 적용한 요소의 위치를 더이상 나타낼 수 없게 됐을 때, 그때부터 화면에 position: fixed 속성을 적용한 것처럼 화면에 고정시키게 된다.