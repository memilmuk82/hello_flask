from flask import Flask, render_template, request, redirect

app = Flask(__name__)
messages = []

@app.route('/')
def home():
    skills = ["Python", "HTML", "SQL", "Bash"]
    return render_template('index.html', data=skills, messages=messages)

@app.route('/send', methods=['POST'])
def send():
    skill = request.form.get('skill')
    level = request.form.get('level')
    status = request.form.get('status')    
    messages.append(status + " / " + level + " / " + skill)    
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    index = int(request.form['index'])
    messages.pop(index)
    return redirect('/')

@app.route("/delete_all", methods=['POST'])
def delete_all():
    messages.clear()    
    return redirect('/')

@app.route('/delete_selected', methods=['POST'])
def delete_selected():
    indexes = request.form.getlist('delete_indexes')
    indexes = [int(index) for index in indexes]
    indexes.sort(reverse=True)

    for index in indexes:
        messages.pop(index)

    return redirect('/')

@app.route('/edit/<int:index>')
def edit(index):
	return render_template('edit.html', index=index, item=messages[index])

@app.route('/update',methods=['POST'])
def update():
	index = int(request.form['index'])
	value = request.form.get('value')
	messages[index] = value
	return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)