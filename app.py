from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
		# 여기에 내 데이터를 만든다!
    my_profile = {
        "name": "홍길동", # 내 이름으로
        "age": 18, # 내 나이로
        "school": "종로산업정보학교",   # 추가!
        "hobby": "게임"           # 추가!
    }

    # 이 부분이 바뀌었다!
    return render_template('index.html', data=my_profile)

if __name__ == '__main__':
    app.run(debug=True)