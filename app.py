from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    skills = [
        "C", "C++", "C#", "Java", "Kotlin",
        "JavaScript", "TypeScript",
        "Python", "Rust", "Go",
        "Ruby", "PHP",
        "HTML", "CSS", "Markdown",
        "SQL", "R",
        "Bash", "Shell",
        "Dart", "Swift"
    ]
    return render_template('index.html', data=skills)

if __name__ == '__main__':
    app.run(debug=True)