# 오픈소스SW기초 2분반 과제2
### Django와 Docker를 이용하여 Project portfolio를 소개하고 평가하는 웹 사이트 만들기

### 사용자 기능
- 프로젝트 목록 보기
- 프로젝트 상세 페이지에서 평가 점수 등록 (1~5점)

### 관리자 기능
- 프로젝트 추가 / 수정 / 삭제
- 프로젝트 별 평균 점수 및 등위 확인 (관리자 페이지)

## 설치 방법 (Docker)

1. 저장소 클론하기:
   ```bash
   git clone https://github.com/yourusername/portfolio-site.git
   cd portfolio-site

2. Docker 이미지 빌드하기:
   ```bash
   docker build -t portfolio_site .
   
3. Docker 컨테이너 실행하기:
   ```bash
   docker run -p 8000:8000 portfolio_site

4. 웹 애플리케이션에 접속
   http://127.0.0.1:8000
