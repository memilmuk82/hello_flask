# Flask 라이브러리에서 필요한 기능 가져오기
from flask import Flask

# Flask 앱 생성
app = Flask(__name__)

# '/' 주소로 접속하면 실행되는 함수
@app.route('/')
def home():
    return "Hello, World!"

# 이 파일을 직접 실행했을 때만 서버 실행
if __name__ == '__main__':
    app.run(debug=True)