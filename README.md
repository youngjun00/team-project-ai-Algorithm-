# AI 알고리즘 실습 팀 프로젝트
### TEAM - 라플라스의 개
## 팀원 소개
![zzzz](https://user-images.githubusercontent.com/89188607/141059040-12b4b387-5c34-465b-847c-3564cfa2f547.JPG)


> 김영준(조장, 코딩 담당), 
> 진민규(코딩 담당),
> 이풍규(GUI 담당), 
> 박시언(GUI 담당), 
> 장동현(ReadMe.md 담당),
>
>
> 박창대(ReadMe.md 담당), 
> 황수현(Database 담당), 
> 김도현(Database 담당) 
> 이상 8인 1팀입니다.                     
## 선정한 주제 와 이유
### 주제
> 라플라스 변환 계산기
### 선정이유
> 저희팀이 라플라스 변환 계산기를 AI알고리즘 실습의 팀 프로젝트 과제로 선정하게 된 이유는 이때까지 AI알고리즘과 자동제어 수업에서 배운것중 여러가지를 이용하여 라플라스 변환 계산기를 표현할 수 있고 GUI를 통해 기능을 구현하기에도 가장 적합하다고 판단하여서 입니다.
## 기능
> 우선 기본적인 기능으로 라플라스 변환식중 가장 많이 쓰는 10개와 clear 기능을 사용하고 상수나 변수 등을 따로 지정하여 계산할 수 있게 하는 라플라스 변환 계산기 입니다.
## 시스템의 동작원리, 역할 및 파트분배
### 시스템 동작 원리
>우선 GUI에서 라플라스 변환식을 선택하면 Database에서 라플라스 변환식을 코딩되어 있는 파일로 가져온 후 GUI를 통해 변수를 지정 받으면 라플라스 변환을 한 후 GUI에 결과값을 출력하는 방식입니다.
### 역할 및 파트분배
> GUI : 라플라스 변환 계산기의 기본외형 및 입력을 신호로 전해주는 역할으로 이풍규, 박시언 이상 두명이 담당하게 되었습니다. 기본적으로 생각중인 외형은 다음 사진과 같습니다.


![캡처](https://user-images.githubusercontent.com/89117676/141061140-fc46bf2d-56b8-4dea-8fa9-573153ffee0c.JPG)



> 코딩 : GUI를 통해 받은 데이터를 Database에서 가져와서 라플라스 변환을 한 후 GUI에 다시 출력 해주는 역할으로 김영준, 진민규 이상 두명이 담당하게 되었습니다.


> Database : 다양한 라플라스 변환식을 일일이 쓰지않고 간단하게 만들어 코딩에 도움을 주는 역할으로 김도현, 황수현 이상 두명이 담당하게 되었습니다.


> ReadMe.md :액세스하려는 파일(라플라스 변환 계산기)의 사용 방법에 관한 정보가 들어있는 텍스트 파일 및 발사믹 목업(Balsamiq mockups)을 통해 디자인을 만들어 주는 역할으로 장동현, 박창대 이상 두명이 담당하게 되었습니다.

## 진행상황
> GUI : 현재 버튼 외형은 완성했고 라플라스 변환버튼은 변수지정이 완료된 상태이며 숫자버튼과 변환식에 자연수를 넣는 버튼은 아직 변수 미지정 상태 입니다.(11/17)

> Database: 총 10개 변환식중에 2개 변환식 테스트 완료했고, 변환식에 자연수를 넣는 변수를 코딩 파트와 같이 확인중 입니다.(11/17)

> 코딩: 현재 GUI에서 버튼을 눌렸을때 받는 변수와 데이터베이스 변수를 맞추고있고 변환식에 자연수를 넣는것을 데이터베이스와 같이 확인하는 작업에 있습니다.(11/17)

> GUI : 현재 (진민규)코딩담당 한명이 임시로 GUI 자료수집을 도와주고 있으나 결과값을 출력하거나 입력값을 변수로 주는 부분에 어려움이있고
>       Database 파트와 연동 및 커뮤케이션이 부족한 상태 입니다.(11/24)

> Database: 현재 (김영준)코딩담당 한명이 Database에 자료수집을 도와주고 있으나 Database 파트의 자료가 생각보다 어려워 진행하는데에 까다로운 상태 입니다.(11/24)

> 코딩: 현재 GUI에서 버튼을 눌렸을떄 받는 변수와 Database 변수를 조정중이고 GUI 파트에서 변수를 보내고있는 작업과 Database 파트 구축에 어려움이 생겨
>       각 두개의 파트에 한명씩 임시로 도움을 주고있습니다.(11/24)

> GUI : gui 파트는 현재 코딩파트와 데이터베이스 파트가 마무리되어서 입력값을 코딩파트에 넘겨주는 작업은 완료했지만 결과값을 출력하는 과정에서 결과값의
> 데이터 형태를 파악하는데 어려움을 겪고있습니다.(11/30)

> Database: 저번주 데이터베이스 관련해서 교수님이 알려주신 내용을 바탕으로 database파트는 작업을 완료 했습니다..(11/30)

> 코딩: 저번주에 각 파트로 인원을 분배해서 도와준 결과 database 파트와 코딩파트는 연동이 완료 되었습니다. gui파트는 입력값을 받아오는것까지 완료했고 결과값을 출력하는 과정에서
> 결과값의 데이터 형태를 파악하는 부분이 막히고 있어서 데이터 형태를 파악하면 모든파트가 마무리 될것 같습니다.(11/30)
