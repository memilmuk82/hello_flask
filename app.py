from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = []

def get_next_id(items):
    ids = [item["id"] for item in items]

    return max(ids, default=0) + 1

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
    
    new_id = get_next_id(messages)

    messages.append({
        "id": new_id,
        "skill": skill,
        "level": level,
        "status": status
    })

    return redirect('/')

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    for item in messages:
        if item["id"] == item_id:
            messages.remove(item)
            break

    return redirect('/')

@app.route('/delete_all', methods=['POST'])
def delete_all():
    messages.clear()
    
    return redirect('/')

@app.route('/delete_selected', methods=['POST'])
def delete_selected():
    selected_indexes = request.form.getlist('selected_ids')

    remaining_messages = []

    for item in messages:
        if str(item["id"]) not in selected_indexes:
            remaining_messages.append(item)

    messages.clear()

    for item in remaining_messages:
        messages.append(item)

    return redirect('/')

@app.route('/edit/<int:item_id>')
def edit(item_id):
    target_item = None

    for item in messages:
        if item["id"] == item_id:
            target_item = item
            break
    
    if target_item is None:
        return redirect('/')

    return render_template('edit.html', item=target_item)

@app.route('/update/<int:item_id>', methods=['POST'])
def update(item_id):
    target_item = None

    for item in messages:
        if item["id"] == item_id:
            target_item = item
            break
    
    if target_item is None:
        return redirect('/')
    
    skill = request.form.get('skill', '').strip()
    level = request.form.get('level', '').strip()
    status = request.form.get('status', '').strip()

    if not skill or not level or not status:
        return redirect(f'/edit/{item_id}')

    target_item["skill"] = skill
    target_item["level"] = level
    target_item["status"] = status

    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)