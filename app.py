from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
		# 여기에 내 데이터를 만든다!
    my_profile = {
        "name": "홍길동", # 내 이름으로
        "age": 20, # 내 나이로
        "school": "종로산업정보학교",
        "hobby": "코딩", # 내 취미로
        "email": "test@example.com", # 추가!
        "phone": "010-1234-5678", # 추가!
        "dream": "개발자", # 추가!
        "favorite_food": "치킨" # 추가!
    }
    # 이 부분이 바뀌었다!
    return render_template('index.html', data=my_profile)

if __name__ == '__main__':
    app.run(debug=True)