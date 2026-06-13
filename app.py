from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# messages는 사용자가 입력한 데이터를 저장하는 리스트이다.
# 리스트 안에는 딕셔너리가 들어간다.
messages = []

# next_id는 다음에 추가될 데이터가 사용할 고유 번호이다.
# 처음 추가되는 데이터는 id 1번을 사용한다.
next_id = 1


@app.route('/')
def home():
    # messages 리스트를 index.html로 보낸다.
    return render_template('index.html', messages=messages)


@app.route('/send', methods=['POST'])
def send():
    # next_id는 함수 밖에서 만든 숫자 변수이다.
    # 함수 안에서 next_id 값을 바꾸려면 global이 필요하다.
    global next_id

    # form에서 입력한 값을 가져온다.
    # strip()은 앞뒤 공백을 제거한다.
    skill = request.form.get('skill', '').strip()
    level = request.form.get('level', '').strip()
    status = request.form.get('status', '').strip()

    # 세 값 중 하나라도 비어 있으면 저장하지 않고 메인 화면으로 돌아간다.
    if not skill or not level or not status:
        return redirect('/')

    # 새 데이터를 딕셔너리로 만든다.
    # 이때 id도 함께 저장한다.
    messages.append({
        "id": next_id,
        "skill": skill,
        "level": level,
        "status": status
    })

    # 방금 id를 사용했으므로 다음 데이터는 다음 번호를 사용해야 한다.
    next_id += 1

    return redirect('/')


@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    # messages 리스트 안에 있는 딕셔너리를 하나씩 꺼내 확인한다.
    for item in messages:
        # item["id"]가 주소로 받은 item_id와 같으면 삭제 대상이다.
        if item["id"] == item_id:
            messages.remove(item)
            break

    return redirect('/')


@app.route('/delete_all', methods=['POST'])
def delete_all():
    # messages 리스트 안의 모든 데이터를 삭제한다.
    # 단, next_id는 초기화하지 않는다.
    # id는 한 번 사용한 고유 번호라고 보는 것이 SQLite 전환에 더 적합하다.
    messages.clear()

    return redirect('/')


@app.route('/delete_selected', methods=['POST'])
def delete_selected():
    # 체크된 checkbox들의 value를 리스트로 가져온다.
    # HTML에서 value="{{ item['id'] }}"로 보냈기 때문에 id 목록이 들어온다.
    selected_ids = request.form.getlist('selected_ids')

    # 삭제하지 않고 남길 데이터만 모을 새 리스트이다.
    remaining_messages = []

    # messages 안의 데이터를 하나씩 확인한다.
    for item in messages:
        # request.form.getlist()로 받은 값은 문자열이다.
        # 그래서 item["id"]를 str()로 바꿔 비교한다.
        if str(item["id"]) not in selected_ids:
            remaining_messages.append(item)

    # 기존 messages 리스트를 비운다.
    messages.clear()

    # 남겨야 할 데이터만 다시 messages에 넣는다.
    for item in remaining_messages:
        messages.append(item)

    return redirect('/')


@app.route('/edit/<int:item_id>')
def edit(item_id):
    # 처음에는 수정할 데이터를 찾지 못한 상태이므로 None으로 둔다.
    target_item = None

    # messages 리스트 안에서 id가 item_id와 같은 데이터를 찾는다.
    for item in messages:
        if item["id"] == item_id:
            target_item = item
            break

    # id가 같은 데이터를 찾지 못했다면 메인 화면으로 돌려보낸다.
    if target_item is None:
        return redirect('/')

    # 수정 화면에는 찾은 데이터만 보낸다.
    return render_template('edit.html', item=target_item)


@app.route('/update/<int:item_id>', methods=['POST'])
def update(item_id):
    # 수정할 데이터를 찾기 전 상태이다.
    target_item = None

    # id가 같은 데이터를 찾는다.
    for item in messages:
        if item["id"] == item_id:
            target_item = item
            break

    # 수정할 데이터가 없으면 메인 화면으로 돌아간다.
    if target_item is None:
        return redirect('/')

    # 수정 화면에서 입력한 값을 가져온다.
    skill = request.form.get('skill', '').strip()
    level = request.form.get('level', '').strip()
    status = request.form.get('status', '').strip()

    # 하나라도 비어 있으면 다시 수정 화면으로 돌아간다.
    if not skill or not level or not status:
        return redirect(f'/edit/{item_id}')

    # 기존 딕셔너리의 id는 그대로 둔다.
    # skill, level, status 값만 새 값으로 바꾼다.
    target_item["skill"] = skill
    target_item["level"] = level
    target_item["status"] = status

    return redirect('/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)