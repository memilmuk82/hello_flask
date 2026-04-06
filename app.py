from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    foods = ["치킨", "피자", "햄버거", "떡볶이", "라면", "초밥", "김밥"]
    return render_template('index.html', data=foods)

if __name__ == '__main__':
    app.run(debug=True)