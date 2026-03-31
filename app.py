from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 이제는 JSON이 아니라 HTML 파일을 보냅니다
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)