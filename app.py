from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = []

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    skill = request.form.get('skill', '').strip()
    level = request.form.get('level', '').strip()
    status = request.form.get('status', '').strip()

    if not skill or not level or not status:
        return redirect('/')

    messages.append({
        "skill": skill,
        "level": level,
        "status": status
    })

    return redirect('/')

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(messages):
        messages.pop(index)
        
    return redirect('/')

@app.route('/delete_all', methods=['POST'])
def delete_all():
    messages.clear()
    
    return redirect('/')

@app.route('/delete_selected', methods=['POST'])
def delete_selected():
    selected_indexes = request.form.getlist('selected_indexes')

    remaining_messages = []

    for index, item in enumerate(messages):
        if str(index) not in selected_indexes:
            remaining_messages.append(item)

    messages.clear()

    for item in remaining_messages:
        messages.append(item)

    return redirect('/')

@app.route('/edit/<int:index>')
def edit(index):
    if index < 0 or index >= len(messages):
        return redirect('/')

    item = messages[index]

    return render_template('edit.html', item=item, index=index)

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
    if index < 0 or index >= len(messages):
        return redirect('/')

    skill = request.form.get('skill', '').strip()
    level = request.form.get('level', '').strip()
    status = request.form.get('status', '').strip()

    if not skill or not level or not status:
        return redirect(f'/edit/{index}')

    messages[index] = {
        "skill": skill,
        "level": level,
        "status": status
    }

    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)