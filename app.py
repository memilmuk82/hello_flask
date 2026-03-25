# Flask 라이브러리에서 필요한 기능 가져오기
from flask import Flask

# Flask 앱 생성
app = Flask(__name__)

# '/' 주소로 접속하면 실행되는 함수
@app.route('/')
def my_profile():
    # 파이썬 딕셔너리를 반환하면 Flask가 알아서 웹 표준인 JSON으로 변환해줍니다!
    return {
        "name": "홍길동",
        "role": "초보 서버 개발자",
        "status": "로컬 환경 통제 완료!",
        "skills": ["Ubuntu", "VS Code", "Python", "Flask"]
    }
    
# 이 파일을 직접 실행했을 때만 서버 실행
if __name__ == '__main__':
    app.run(debug=True)